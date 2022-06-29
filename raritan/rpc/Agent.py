# Avoid name clash with raritan.rpc.sys
from __future__ import absolute_import

import base64, json, ssl, sys
import raritan.rpc

try:
    # Python 3
    import urllib.request as urllib_request
except ImportError:
    # Python 2
    import urllib2 as urllib_request

class Agent(object):
    """Provides transport to one RPC service, e.g. one PX2 device - holds host,
       user name, and password."""
    id = 1

    def __init__(self, proto, host, user = None, passwd = None, token = None,
                 debug = False, disable_certificate_verification = False, timeout = None):
        self.url = "%s://%s" % (proto, host)
        self.user = user
        self.passwd = passwd
        self.token = token # authentication token
        self.debug = debug
        self.timeout = timeout

        context = None
        if disable_certificate_verification:
            import ssl
            if "_create_unverified_context" in ssl.__dict__.keys():
                context = ssl._create_unverified_context()

        self.opener = urllib_request.OpenerDirector()
        self.opener.add_handler(urllib_request.HTTPHandler())
        try:
            self.opener.add_handler(urllib_request.HTTPSHandler(context = context))
        except TypeError:
            # Python < 2.7.9
            self.opener.add_handler(urllib_request.HTTPSHandler())

        Agent.defaultInst = self

    def set_auth_basic(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.token = None

    def set_auth_token(self, token):
        self.user = None
        self.passwd = None
        self.token = token

    def handle_http_redirect(self, rid, response):
        location = response.headers["Location"]
        baselen = len(location) - len(rid)
        if baselen <= 0:
            return False
        elif location[baselen:] != rid:
            return False
        else:
            self.url = location[:baselen]
            if self.debug:
                print("Redirected to: " + self.url)
            return True

    def json_rpc(self, target, method, params = [], redirected = False):
        request_json = json.dumps({"method": method, "params": params, "id": Agent.id})
        if (self.debug):
            print("json_rpc: %s() - %s: , request = %s" % (method, target, request_json))
        Agent.id += 1

        target_url = "%s/%s" % (self.url, target)
        request = urllib_request.Request(target_url, str.encode(request_json))

        if self.token != None:
            request.add_header("X-SessionToken", self.token)
        elif self.user != None and self.passwd != None:
            basic = base64.b64encode(str.encode('%s:%s' % (self.user, self.passwd)))
            request.add_header('Authorization', 'Basic:' + bytes.decode(basic))

        try:
            if (self.timeout):
                response = self.opener.open(request, timeout = self.timeout)
            else:
                response = self.opener.open(request)

        except IOError as e:
            if str(e).find("CERTIFICATE_VERIFY_FAILED") >= 0:
                sys.stderr.write("==================================================================\n")
                sys.stderr.write(" SSL certificate verification failed!\n")
                sys.stderr.write("\n")
                sys.stderr.write(" When connecting to a device without valid SSL certificate, try\n")
                sys.stderr.write(" adding 'disable_certificate_verification=True' when creating the\n")
                sys.stderr.write(" raritan.rpc.Agent instance.\n")
                sys.stderr.write("==================================================================\n")
            raise raritan.rpc.HttpException("Opening URL %s failed: %s" % (target_url, e))

        if response.code == 302 and not redirected:
            # handle HTTP-to-HTTPS redirect and try again
            if self.handle_http_redirect(target, response):
                return self.json_rpc(target, method, params, True)

        # get and process response
        try:
            resp = bytes.decode(response.read())
        except:
            raise raritan.rpc.HttpException("Reading response failed.")

        if response.code != 200:
            raise raritan.rpc.HttpException("HTTP Error %d\nResponse:\n%s" % (response.code, resp))

        if (self.debug):
            print("json_rpc: Response:\n%s" % resp)

        try:
            resp_json = json.loads(resp)
        except ValueError as e:
            raise raritan.rpc.JsonRpcSyntaxException(
                    "Decoding response to JSON failed: %s" % e)

        if "error" in resp_json:
            try:
                code = resp_json["error"]["code"]
                msg = resp_json["error"]["message"]
            except KeyError:
                raise raritan.rpc.JsonRpcSyntaxException(
                        "JSON RPC returned malformed error: %s" % resp_json)
            raise raritan.rpc.JsonRpcErrorException(
                    "JSON RPC returned error: code = %d, msg = %s" % (code, msg))

        try:
            res = resp_json["result"]
        except KeyError:
            raise raritan.rpc.JsonRpcSyntaxException(
                    "Result is missing in JSON RPC response: %s" % resp_json)
            
        return res
