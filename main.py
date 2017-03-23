import requests
import hashlib
import json
import yaml
import settings
from os.path import expanduser
config_files="abuseadv.json abusede.json abuseinfo.json abuse.json activeipphonenumber.json addphonebook.json addphonedectemail.json addphonedectonlbuch.json addphonedectrss.json arp.json assistant.json basinfo.json bbb.json capture.json changestatus.json checkfirm.json connect_disable.json connect.json connect_post.json dect.json dectsettings.json dectstation.json dect_voip.json delabuseadv.json deletecalls.json del-ipphonenumber.json delmobil.json delnasuser.json delphonebook.json delphonedectemail.json delphonedectonlbuch.json delphonedectrss.json dhcp_client.json dhcp_server.json dns.json dsl.json dslTool.json dyndns.json dyndnssubmitfail.json dyndnssubmitres.json eastatus.json easysupport_status.json filterandtime.json firmwareupdate.json firstcall.json fondata.json fonradius.json getcurruser.json get_mediareplay.json get_nasbackup.json get_nassync.json get_nasuser.json getversiontype.json heartbeat.json hsdelmobil.json hsfon.json icmp.json igmp_proxy.json igmp_snooping.json inetip.json inetip_ok.json interfaces.json internetconnection.json internetconnections1p1.json internetconnections1p3.json ipphonehandleraddset.json ipphonehandler.json ipphone.json ipphonenumbers.json ipv6.json lanipchange.json lan.json lanreboot.json lansubmit.json loginDelay.json login.json loginLock.json loginOk.json loginOther.json loginReload.json log.json logout.json lsdirectoryentry.json lstopdirectoryentry.json manageddevicedelete.json manageddevice.json memory.json mobilring.json module.json modules.json nasbackupAddSet.json nasbackupDel.json nasbackupentryGet.json nasbackupentry.json nasbackupGet.json nasbackup.json nasdeviceGet.json nasdevice.json nasemailsettingsGet.json nasemailsettingsSet.json nasguestGet.json nasguest.json naslight.json nasmediacenterGet.json nasmediacenter.json nasmediacenterSet.json nasmediareplay.json nassyncAddSet.json nassyncdel.json nassyncGet.json nassync.json nasuserGet.json nasuser.json newdirectoryfail.json newdirectory.json onlinestatus.json otherdevice.json overview.json phoneactiveable.json phonebook.json phonecalls.json phone.json phonelineset.json phonenumberassignment.json phonenumbers.json phoneplugs.json phonewebnwalk.json portforwarding.json port_mapping.json portmapping.json portmappingset.json porttrigeradd.json porttrigerdel.json porttrigerset.json pubinfo.json reboot.json registertimout.json resetallreboot.json router.json routing.json securestatus.json session.json setabuseadv.json setdectenable.json setdectstation.json setnasuser.json setnasworkgroup.json setphonebook.json setphonedectemail.json setphonedectonlbuch.json setphonedectrss.json setphonenumberassignment.json setphoneplugs.json setpin.json speed.json status.json submitfail.json submitres.json submitvoice.json systemmessages.json temp.json timerules.json updateerror.json webnwalk.json wlanaccess.json wlanbasic.json wlanbasics1p3.json wlanbasics1p.json wlan.json wlanssidsec.json".split(' ')
hp=requests.get("http://192.168.2.1/html/login/index.html")
lines=hp.text.split('\r\n')
csrf=lines[11][22:-2]
challenge=lines[12][21:-2]
#print(csrf)
#print(challenge)
x=hashlib.sha256(challenge.encode("UTF-8") + b":"+open(expanduser("~/routerpass.txt"),"rb").read()).hexdigest()
#print(x)
login=requests.post("http://192.168.2.1/data/Login.json", data = {"csrf_token":csrf, "password":x, "showpw":"0", "challengev":challenge})
login_data=eval(login.text)
def getConfig(fname):
#    print("Fetching config "+fname)
    r = requests.get("http://192.168.2.1/data/"+fname, cookies=login.cookies)
    if r.text == "":
        return []
    try:
        return settings.listToDict(eval(r.text))
    except:
#        print("Fuck off")
        return []
#data={"Login.json":login_data}
#for f in config_files:
#    data[f]=settings.listToDict(getConfig(f))
#with open("config.yaml", "w") as f:
#    yaml.dump(data, f)
