import raritan.rpc

class Interface(object):
    """IDL interface reference = base class of all proxies
    """
    class Method():
        def __init__(self, parent):
            self.parent = parent

        def __call__(self, *args):
            encArgs = self.encode(*args)
            rsp = self.parent.agent.json_rpc(self.parent.target, self.name, encArgs)
            return self.decode(rsp, self.parent.agent)

    def __init__(self, target, agent):
        self.target = target
        self.agent = agent

    @staticmethod
    def decode(json, agent):
        if (not json):
            return None
        target = json['rid']
        class_ = raritan.rpc.TypeInfo.decode(json['type'])
        obj = class_(target, agent)
        return obj

    def encode(self):
      json = {}
      json['rid'] = self.target
      json['type'] = self.idlType
      return json

    def __str__(self):
        return "%s: %s" % (raritan.rpc.TypeInfo.typeBaseName(self.idlType), self.target)

    def __eq__(self, other):
        return other and self.idlType == other.idlType and self.target == other.target

    def __hash__(self):
        return hash((self.idlType, self.target))
