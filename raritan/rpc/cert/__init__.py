# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/libisys/src/idl/ServerSSLCert.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.cert


# interface
class ServerSSLCert(Interface):
    idlType = "cert.ServerSSLCert:2.0.0"

    SUCCESS = 0

    ERR_GEN_KEY_LEN_INVALID = 100

    ERR_GEN_CSR_OR_CERT_PENDING = 101

    ERR_GEN_KEY_GEN_FAILED = 102

    ERR_INSTALL_KEY_MISSING = 200

    ERR_INSTALL_CERT_MISSING = 201

    ERR_INSTALL_CERT_FORMAT_INVALID = 202

    ERR_INSTALL_CERT_KEY_MISMATCH = 203

    # structure
    class CommonAttributes(Structure):
        idlType = "cert.ServerSSLCert_2_0_0.CommonAttributes:1.0.0"
        elements = ["country", "stateOrProvince", "locality", "organization", "organizationalUnit", "commonName", "emailAddress"]

        def __init__(self, country, stateOrProvince, locality, organization, organizationalUnit, commonName, emailAddress):
            typecheck.is_string(country, AssertionError)
            typecheck.is_string(stateOrProvince, AssertionError)
            typecheck.is_string(locality, AssertionError)
            typecheck.is_string(organization, AssertionError)
            typecheck.is_string(organizationalUnit, AssertionError)
            typecheck.is_string(commonName, AssertionError)
            typecheck.is_string(emailAddress, AssertionError)

            self.country = country
            self.stateOrProvince = stateOrProvince
            self.locality = locality
            self.organization = organization
            self.organizationalUnit = organizationalUnit
            self.commonName = commonName
            self.emailAddress = emailAddress

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                country = json['country'],
                stateOrProvince = json['stateOrProvince'],
                locality = json['locality'],
                organization = json['organization'],
                organizationalUnit = json['organizationalUnit'],
                commonName = json['commonName'],
                emailAddress = json['emailAddress'],
            )
            return obj

        def encode(self):
            json = {}
            json['country'] = self.country
            json['stateOrProvince'] = self.stateOrProvince
            json['locality'] = self.locality
            json['organization'] = self.organization
            json['organizationalUnit'] = self.organizationalUnit
            json['commonName'] = self.commonName
            json['emailAddress'] = self.emailAddress
            return json

    # structure
    class ReqInfo(Structure):
        idlType = "cert.ServerSSLCert_2_0_0.ReqInfo:1.0.0"
        elements = ["subject", "names", "keyLength"]

        def __init__(self, subject, names, keyLength):
            typecheck.is_struct(subject, raritan.rpc.cert.ServerSSLCert.CommonAttributes, AssertionError)
            for x0 in names:
                typecheck.is_string(x0, AssertionError)
            typecheck.is_int(keyLength, AssertionError)

            self.subject = subject
            self.names = names
            self.keyLength = keyLength

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                subject = raritan.rpc.cert.ServerSSLCert.CommonAttributes.decode(json['subject'], agent),
                names = [x0 for x0 in json['names']],
                keyLength = json['keyLength'],
            )
            return obj

        def encode(self):
            json = {}
            json['subject'] = raritan.rpc.cert.ServerSSLCert.CommonAttributes.encode(self.subject)
            json['names'] = [x0 for x0 in self.names]
            json['keyLength'] = self.keyLength
            return json

    # structure
    class CertInfo(Structure):
        idlType = "cert.ServerSSLCert_2_0_0.CertInfo:1.0.0"
        elements = ["subject", "issuer", "names", "invalidBefore", "invalidAfter", "serialNumber", "keyLength"]

        def __init__(self, subject, issuer, names, invalidBefore, invalidAfter, serialNumber, keyLength):
            typecheck.is_struct(subject, raritan.rpc.cert.ServerSSLCert.CommonAttributes, AssertionError)
            typecheck.is_struct(issuer, raritan.rpc.cert.ServerSSLCert.CommonAttributes, AssertionError)
            for x0 in names:
                typecheck.is_string(x0, AssertionError)
            typecheck.is_string(invalidBefore, AssertionError)
            typecheck.is_string(invalidAfter, AssertionError)
            typecheck.is_string(serialNumber, AssertionError)
            typecheck.is_int(keyLength, AssertionError)

            self.subject = subject
            self.issuer = issuer
            self.names = names
            self.invalidBefore = invalidBefore
            self.invalidAfter = invalidAfter
            self.serialNumber = serialNumber
            self.keyLength = keyLength

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                subject = raritan.rpc.cert.ServerSSLCert.CommonAttributes.decode(json['subject'], agent),
                issuer = raritan.rpc.cert.ServerSSLCert.CommonAttributes.decode(json['issuer'], agent),
                names = [x0 for x0 in json['names']],
                invalidBefore = json['invalidBefore'],
                invalidAfter = json['invalidAfter'],
                serialNumber = json['serialNumber'],
                keyLength = json['keyLength'],
            )
            return obj

        def encode(self):
            json = {}
            json['subject'] = raritan.rpc.cert.ServerSSLCert.CommonAttributes.encode(self.subject)
            json['issuer'] = raritan.rpc.cert.ServerSSLCert.CommonAttributes.encode(self.issuer)
            json['names'] = [x0 for x0 in self.names]
            json['invalidBefore'] = self.invalidBefore
            json['invalidAfter'] = self.invalidAfter
            json['serialNumber'] = self.serialNumber
            json['keyLength'] = self.keyLength
            return json

    # structure
    class Info(Structure):
        idlType = "cert.ServerSSLCert_2_0_0.Info:1.0.0"
        elements = ["havePendingReq", "havePendingCert", "pendingReqInfo", "pendingCertInfo", "activeCertInfo", "maxSignDays"]

        def __init__(self, havePendingReq, havePendingCert, pendingReqInfo, pendingCertInfo, activeCertInfo, maxSignDays):
            typecheck.is_bool(havePendingReq, AssertionError)
            typecheck.is_bool(havePendingCert, AssertionError)
            typecheck.is_struct(pendingReqInfo, raritan.rpc.cert.ServerSSLCert.ReqInfo, AssertionError)
            typecheck.is_struct(pendingCertInfo, raritan.rpc.cert.ServerSSLCert.CertInfo, AssertionError)
            typecheck.is_struct(activeCertInfo, raritan.rpc.cert.ServerSSLCert.CertInfo, AssertionError)
            typecheck.is_int(maxSignDays, AssertionError)

            self.havePendingReq = havePendingReq
            self.havePendingCert = havePendingCert
            self.pendingReqInfo = pendingReqInfo
            self.pendingCertInfo = pendingCertInfo
            self.activeCertInfo = activeCertInfo
            self.maxSignDays = maxSignDays

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                havePendingReq = json['havePendingReq'],
                havePendingCert = json['havePendingCert'],
                pendingReqInfo = raritan.rpc.cert.ServerSSLCert.ReqInfo.decode(json['pendingReqInfo'], agent),
                pendingCertInfo = raritan.rpc.cert.ServerSSLCert.CertInfo.decode(json['pendingCertInfo'], agent),
                activeCertInfo = raritan.rpc.cert.ServerSSLCert.CertInfo.decode(json['activeCertInfo'], agent),
                maxSignDays = json['maxSignDays'],
            )
            return obj

        def encode(self):
            json = {}
            json['havePendingReq'] = self.havePendingReq
            json['havePendingCert'] = self.havePendingCert
            json['pendingReqInfo'] = raritan.rpc.cert.ServerSSLCert.ReqInfo.encode(self.pendingReqInfo)
            json['pendingCertInfo'] = raritan.rpc.cert.ServerSSLCert.CertInfo.encode(self.pendingCertInfo)
            json['activeCertInfo'] = raritan.rpc.cert.ServerSSLCert.CertInfo.encode(self.activeCertInfo)
            json['maxSignDays'] = self.maxSignDays
            return json

    class _generateUnsignedKeyPair(Interface.Method):
        name = 'generateUnsignedKeyPair'

        @staticmethod
        def encode(reqInfo, challenge):
            typecheck.is_struct(reqInfo, raritan.rpc.cert.ServerSSLCert.ReqInfo, AssertionError)
            typecheck.is_string(challenge, AssertionError)
            args = {}
            args['reqInfo'] = raritan.rpc.cert.ServerSSLCert.ReqInfo.encode(reqInfo)
            args['challenge'] = challenge
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _generateSelfSignedKeyPair(Interface.Method):
        name = 'generateSelfSignedKeyPair'

        @staticmethod
        def encode(reqInfo, days):
            typecheck.is_struct(reqInfo, raritan.rpc.cert.ServerSSLCert.ReqInfo, AssertionError)
            typecheck.is_int(days, AssertionError)
            args = {}
            args['reqInfo'] = raritan.rpc.cert.ServerSSLCert.ReqInfo.encode(reqInfo)
            args['days'] = days
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _deletePending(Interface.Method):
        name = 'deletePending'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _getInfo(Interface.Method):
        name = 'getInfo'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            info = raritan.rpc.cert.ServerSSLCert.Info.decode(rsp['info'], agent)
            typecheck.is_struct(info, raritan.rpc.cert.ServerSSLCert.Info, DecodeException)
            return info

    class _installPendingKeyPair(Interface.Method):
        name = 'installPendingKeyPair'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(ServerSSLCert, self).__init__(target, agent)
        self.generateUnsignedKeyPair = ServerSSLCert._generateUnsignedKeyPair(self)
        self.generateSelfSignedKeyPair = ServerSSLCert._generateSelfSignedKeyPair(self)
        self.deletePending = ServerSSLCert._deletePending(self)
        self.getInfo = ServerSSLCert._getInfo(self)
        self.installPendingKeyPair = ServerSSLCert._installPendingKeyPair(self)