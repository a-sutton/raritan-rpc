import sys
import raritan.rpc as rpc
from raritan.rpc import devsettings, um, usermgmt, pdumodel, radius
import csv

with open('DEVICES.csv', newline='') as rarCSV:
    devices = csv.reader(rarCSV)
    next(devices)
    for row in devices:
        if row[3] == "Raritan":
            user = "admin"
            passw = "raritan"
        elif row[3] == "Server Tech":
            user = "admn"
            passw = "admn"
        elif row[3] == "Not Default User/Pass":
            user = row[4]
            passw = row[5]
        else:
            pass
        print(row)
        agent = rpc.Agent("https", f"{row[2]}", user, passw, disable_certificate_verification=True)
        print('Getting PDU settings...')
        pdu = rpc.pdumodel.Pdu('/model/pdu/0', agent)
        settings = pdu.getSettings()
        print('Successfully retrieved current PDU settings.')
        settings.name = row[0]
        print('Updating PDU settings...')
        ret = pdu.setSettings(settings)
        if ret == 0:
            print('PDU settings successfully updated.')
        else:
            print('Pdu.setSettings() failed: ret = ', ret)
        radius_details = radius.ServerSettings(
            id='',
            server='10.102.87.241',
            sharedSecret='',
            udpAuthPort=1,
            udpAccountPort=1,
            timeout=10,
            retries=3,
            authType=radius.AuthType(0)
        )
        new_user = usermgmt.UserInfo(
            enabled=True,
            locked=False,
            blocked=False,
            needPasswordChange=False,
            auxInfo=usermgmt.AuxInfo(
                fullname='techopsadmn',
                telephone='555-123-1234',
                eMail='fac_tech-svcs@mentor.com'
            ),
            snmpV3Settings=usermgmt.SnmpV3Settings(
                enabled=True,
                secLevel=um.SnmpV3.SecurityLevel(2),
                authProtocol=um.SnmpV3.AuthProtocol(0),
                usePasswordAsAuthPassphrase=False,
                haveAuthPassphrase=True,
                authPassphrase='$iemens5Techops1',
                privProtocol=um.SnmpV3.PrivProtocol(0),
                useAuthPassphraseAsPrivPassphrase=False,
                havePrivPassphrase=True,
                privPassphrase='$iemens5Secur320'
            ),
            sshPublicKey='',
            preferences=usermgmt.Preferences(
                temperatureUnit=usermgmt.TemperatureEnum(0),
                lengthUnit=usermgmt.LengthEnum(0),
                pressureUnit=usermgmt.PressureEnum(0)
            ),
            roleIds=[0]  # role 0 = Administrator
        )
        new_password = "$iemens5Techops1"
        try:
            print('Trying to update existing account ...')
            user_proxy = usermgmt.User('/auth/user/techopsadmn', agent)
            ret = user_proxy.updateAccountFull('', new_user)
            if ret == 0:
                print('Account successfully updated.')
            else:
                print('User.updateAccountFull() failed: ret = ', ret)
                sys.exit(1)
            print('Setting account password ...')
            ret = user_proxy.setAccountPassword(new_password)
            if ret == 0:
                print('Password successfully changed.')
            elif ret == usermgmt.User.ERR_PASSWORD_UNCHANGED:
                print('Password unchanged.')
            else:
                print('User.setAccountPassword() failed: ret = ', ret)
        except rpc.HttpException:
            print('Account not found; creating new one ...')
            usermgr_proxy = usermgmt.UserManager('/auth/user/', agent)
            ret = usermgr_proxy.createAccountFull('techopsadmn', new_password, new_user)
            if ret == 0:
                print('Account successfully created.')
            else:
                print('UserManager.createAccountFull() failed: ret = ', ret)
                sys.exit(1)


