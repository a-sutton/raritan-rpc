# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/libidl_client/topofw/emd/idl/Emd.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.emdmodel

import raritan.rpc.event

import raritan.rpc.hmi

import raritan.rpc.pdumodel

import raritan.rpc.peripheral

import raritan.rpc.portsmodel

import raritan.rpc.sensors


# interface
class Emd(Interface):
    idlType = "emdmodel.Emd:2.2.5"

    ERR_INVALID_PARAMS = 1

    # structure
    class MetaData(Structure):
        idlType = "emdmodel.Emd_2_2_5.MetaData:1.0.0"
        elements = ["nameplate", "ctrlBoardSerial", "hwRevision", "fwRevision", "macAddress"]

        def __init__(self, nameplate, ctrlBoardSerial, hwRevision, fwRevision, macAddress):
            typecheck.is_struct(nameplate, raritan.rpc.pdumodel.Nameplate, AssertionError)
            typecheck.is_string(ctrlBoardSerial, AssertionError)
            typecheck.is_string(hwRevision, AssertionError)
            typecheck.is_string(fwRevision, AssertionError)
            typecheck.is_string(macAddress, AssertionError)

            self.nameplate = nameplate
            self.ctrlBoardSerial = ctrlBoardSerial
            self.hwRevision = hwRevision
            self.fwRevision = fwRevision
            self.macAddress = macAddress

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                nameplate = raritan.rpc.pdumodel.Nameplate.decode(json['nameplate'], agent),
                ctrlBoardSerial = json['ctrlBoardSerial'],
                hwRevision = json['hwRevision'],
                fwRevision = json['fwRevision'],
                macAddress = json['macAddress'],
            )
            return obj

        def encode(self):
            json = {}
            json['nameplate'] = raritan.rpc.pdumodel.Nameplate.encode(self.nameplate)
            json['ctrlBoardSerial'] = self.ctrlBoardSerial
            json['hwRevision'] = self.hwRevision
            json['fwRevision'] = self.fwRevision
            json['macAddress'] = self.macAddress
            return json

    # structure
    class Settings(Structure):
        idlType = "emdmodel.Emd_2_2_5.Settings:1.0.0"
        elements = ["name"]

        def __init__(self, name):
            typecheck.is_string(name, AssertionError)

            self.name = name

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                name = json['name'],
            )
            return obj

        def encode(self):
            json = {}
            json['name'] = self.name
            return json

    # value object
    class SettingsChangedEvent(raritan.rpc.event.UserEvent):
        idlType = "emdmodel.Emd_2_2_5.SettingsChangedEvent:1.0.0"

        def __init__(self, oldSettings, newSettings, actUserName, actIpAddr, source):
            super(raritan.rpc.emdmodel.Emd.SettingsChangedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_struct(oldSettings, raritan.rpc.emdmodel.Emd.Settings, AssertionError)
            typecheck.is_struct(newSettings, raritan.rpc.emdmodel.Emd.Settings, AssertionError)

            self.oldSettings = oldSettings
            self.newSettings = newSettings

        def encode(self):
            json = super(raritan.rpc.emdmodel.Emd.SettingsChangedEvent, self).encode()
            json['oldSettings'] = raritan.rpc.emdmodel.Emd.Settings.encode(self.oldSettings)
            json['newSettings'] = raritan.rpc.emdmodel.Emd.Settings.encode(self.newSettings)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                oldSettings = raritan.rpc.emdmodel.Emd.Settings.decode(json['oldSettings'], agent),
                newSettings = raritan.rpc.emdmodel.Emd.Settings.decode(json['newSettings'], agent),
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["oldSettings", "newSettings"]
            elements = elements + super(raritan.rpc.emdmodel.Emd.SettingsChangedEvent, self).listElements()
            return elements

    class _getMetaData(Interface.Method):
        name = 'getMetaData'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.emdmodel.Emd.MetaData.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.emdmodel.Emd.MetaData, DecodeException)
            return _ret_

    class _getPeripheralDeviceManager(Interface.Method):
        name = 'getPeripheralDeviceManager'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = Interface.decode(rsp['_ret_'], agent)
            typecheck.is_interface(_ret_, raritan.rpc.peripheral.DeviceManager, DecodeException)
            return _ret_

    class _getBeeper(Interface.Method):
        name = 'getBeeper'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = Interface.decode(rsp['_ret_'], agent)
            typecheck.is_interface(_ret_, raritan.rpc.hmi.InternalBeeper, DecodeException)
            return _ret_

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.emdmodel.Emd.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.emdmodel.Emd.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.emdmodel.Emd.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.emdmodel.Emd.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getFeaturePorts(Interface.Method):
        name = 'getFeaturePorts'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [Interface.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_interface(x0, raritan.rpc.portsmodel.Port, DecodeException)
            return _ret_

    class _getAuxiliaryPorts(Interface.Method):
        name = 'getAuxiliaryPorts'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [Interface.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_interface(x0, raritan.rpc.portsmodel.Port, DecodeException)
            return _ret_

    class _getSensorLogger(Interface.Method):
        name = 'getSensorLogger'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = Interface.decode(rsp['_ret_'], agent)
            typecheck.is_interface(_ret_, raritan.rpc.sensors.Logger, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(Emd, self).__init__(target, agent)
        self.getMetaData = Emd._getMetaData(self)
        self.getPeripheralDeviceManager = Emd._getPeripheralDeviceManager(self)
        self.getBeeper = Emd._getBeeper(self)
        self.getSettings = Emd._getSettings(self)
        self.setSettings = Emd._setSettings(self)
        self.getFeaturePorts = Emd._getFeaturePorts(self)
        self.getAuxiliaryPorts = Emd._getAuxiliaryPorts(self)
        self.getSensorLogger = Emd._getSensorLogger(self)
