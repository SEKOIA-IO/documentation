
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "app-ctrl"

    ```
	time=15:01:22 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="utm" subtype="app-ctrl" eventtype="app-ctrl-all" level="information" vd="root" eventtime=1631192482 appid=65432 user="jean@SEKOIANETWORK.EXAMPLE.FR" group="ADM" srcip=192.168.1.2 dstip=1.2.3.4 srcport=43564 dstport=443 srcintf="port01" srcintfrole="undefined" dstintf="port01" dstintfrole="undefined" proto=6 service="HTTPS" direction="incoming" policyid=01 sessionid=000000001 applist="standard" appcat="Web.Client" app="HTTPS.BROWSER" action="pass" hostname="example.com" incidentserialno=123456789 url="/" msg="Web.Client: HTTPS.BROWSER," apprisk="medium"
    ```



=== "dlp"

    ```
	time=14:29:04 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="utm" subtype="dlp" eventtype="dlp" level="notice" vd="root" eventtime=1631190544 filteridx=0 filtertype="none" filtercat="none" severity="medium" policyid=6 sessionid=000000001 epoch=402874927 eventid=0 user="USERNAME" group="GROUPNAME" srcip=192.168.1.2 srcport=12345 srcintf="eth" srcintfrole="undefined" dstip=2.2.2.2 dstport=443 dstintf="eth" dstintfrole="undefined" proto=6 service="HTTPS" filetype="png" direction="incoming" action="log-only" hostname="example.fr" url="/rmn.png?foo=bar" agent="Custom Useragent" filename="picture.png" filesize=100 profile="profile_name"
    ```



=== "event-system"

    ```
	time=09:44:52 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="event" subtype="system" level="warning" vd="root" eventtime=1631778292 logdesc="File dropped due to poor network connection" count=6 action="transfer" status="drop" reason="poor-network-condition" msg="1 file were dropped by quard to FortiSandbox: 0 reached max retries, 1 reached TTL."
    ```



=== "forward"

    ```
	time=09:40:24 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="traffic" subtype="forward" level="notice" vd="root" eventtime=1631086824 srcip=192.168.1.2 srcport=11111 srcintf="eth" srcintfrole="undefined" dstip=1.2.3.4 dstport=443 dstintf="eth" dstintfrole="undefined" sessionid=000000001 dstcountry="France" srccountry="Reserved" service="HTTPS" wanoptapptype="web" proto=6 action="accept" duration=100 policyid=1 policytype="policy" wanin=01 rcvdbyte=1000 wanout=2000 lanin=3000 sentbyte=4000 lanout=5000 appcat="appcat1" utmaction="allow" countweb=4
    ```



=== "referralurl"

    ```
	time=10:28:09 devname="fortiprxweb02" devid="FPX4HETA21000025" eventtime=1693384088834139124 tz="+0200" logid="0317013312" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" vd="root" policyid=5 poluuid="721cdbfe-f99e-51ed-1e58-8ced3bccf4b9" policytype="policy" sessionid=1822934421 transid=132186705 user="P001834" group="GGA_PROXY_STANDARD" srcip=10.24.20.183 srcport=55464 srccountry="Reserved" srcintf="port1" srcintfrole="undefined" srcuuid="7020872e-f99e-51ed-b1da-cd426e764ff1" dstip=185.86.138.122 dstport=443 dstcountry="France" dstintf="port1" dstintfrole="undefined" proto=6 service="HTTPS" hostname="adapi.smartadserver.com" profile="standard" action="passthrough" reqtype="referral" url="https://adapi.smartadserver.com/h/nshow?siteid=526525&pgid=1640800&fmtid=115018&tag=sas_115018&tmstp=3164739173&visit=S&acd=1693384088720&opid=6ad51551-b841-4005-a201-e725f3a0462b&opdt=1693384088720&ckid=6765086078691789562&cappid=6765086078691789562&async=1&systgt=%24qc%3D1313276323%3B%24ql%3DMedium%3B%24qpc%3D79000%3B%24qt%3D184_442_42565t%3B%24dma%3D0%3B%24b%3D16999%3B%24o%3D11100%3B%24sw%3D1920%3B%24sh%3D1080&tgt=%24dt%3D1t&pgDomain=https://lfna.fff.fr/competitions&noadcbk=sas.noad&gdpr=1&gdpr_consent=" referralurl="https://lfna.fff.fr/" sentbyte=3753 rcvdbyte=512 direction="outgoing" msg="URL belongs to an allowed category in policy" method="domain" cat=17 catdesc="Advertising"
    ```



=== "severity"

    ```
	time=12:05:11 devname=""test_devname"" devid=""FPX4H00000000"" eventtime=1700561112025540398 tz=""+0100"" logid=""0419013452"" type=""utm"" subtype=""ips"" eventtype=""signature"" level=""alert"" vd=""root"" severity=""medium"" srcip=1.2.3.4 srccountry=""Reserved"" dstip=1.2.3.4 dstcountry=""France"" srcintf=""port_test"" srcintfrole=""undefined"" dstintf=""port_test"" dstintfrole=""undefined"" sessionid=123412341234 action=""dropped"" proto=6 service=""HTTPS"" policyid=13 poluuid=""721c4202-0000-51ed-225e-00000000"" policytype=""policy"" attack=""attack_test"" srcport=51234 dstport=123 hostname=""test.net"" url=""test.js"" direction=""incoming"" attackid=43212 profile=""test-client"" ref=""http://www.test.com/id"" user=""00001111"" group=""test_group"" incidentserialno=12341234 msg=""msg_test"" crscore=10 craction=12121 crlevel=""medium""
    ```



=== "test_dlp_1"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443758757741 tz="+0200" logid="1000234512" type="utm" subtype="dlp" eventtype="dlp" level="warning" vd="root" filteridx=2 filtername="block-mime-types" dlpextra="all-executables" filtertype="file-type" filtercat="file" severity="medium" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 epoch=1714264997 eventid=1 user="P000122" group="GGA_PROXY_STANDARD" srcip=1.2.3.4 srcport=52112 srccountry="Reserved" srcintf="port1" srcintfrole="undefined" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" dstip=5.6.7.8 dstport=80 dstcountry="United States" dstintf="port1" dstintfrole="undefined" proto=6 service="HTTP" filetype="zip" direction="incoming" action="block" hostname="example.com" url="https://example.com/some/long/path?query=param" agent="Microsoft-Delivery-Optimization/10.0" filename="Microsoft.VCLibs.140.00_14.0.33519.0_x64__8wekyb3d8bbwe.Appx" filesize=896581 profile="dlp_standard-and-file-filter" infectedfilename="concrt140_app.dll" infectedfilesize=300104 infectedfiletype="unknown" infectedfilelevel=1
    ```



=== "test_forward_1"

    ```
	time=12:17:25 devname="NX-RMV-FW-FTG-01" devid=1111111111111111 eventtime=1744107444847169073 tz="+0200" logid="1000234512" type="traffic" subtype="forward" level="notice" vd="root" srcip=1.2.3.4 srcname="NX-RMV-LAP-0033" srcport=53569 srcintf="VLAN 9" srcintfrole="lan" dstip=5.6.7.8 dstport=53 dstintf="VLAN 10" dstintfrole="lan" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" dstuuid="f908100a-fad6-51ed-1700-4a39249979c6" srccountry="Reserved" dstcountry="Reserved" sessionid=10000000 proto=17 action="accept" policyid=43 policytype="policy" poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policyname="VLAN9 to VLAN10" service="DNS" trandisp="noop" duration=180 sentbyte=78 rcvdbyte=199 sentpkt=1 rcvdpkt=1 appcat="unscanned" osname="Windows" srcswversion="10" unauthuser="lcherel" unauthusersource="kerberos" mastersrcmac="00:50:b6:fe:1c:a3" srcmac="00:50:b6:fe:1c:a3" srcserver=0 dsthwvendor="VMware" dstdevtype="Server" dstfamily="Virtual Machine" dstosname="Windows" dsthwversion="Virtual Machine" dstswversion="10 / 2016" dstunauthuser="admbouillot" dstunauthusersource="kerberos" masterdstmac="00:11:22:33:44:55" dstmac="00:11:22:33:44:55" dstserver=0
    ```



=== "test_forward_2"

    ```
	time=12:17:25 devname="NX-RMV-FW-FTG-01" devid=1111111111111111 eventtime=1744107444862152259 tz="+0200" logid="1000234512" type="traffic" subtype="forward" level="notice" vd="root" srcip=1.2.3.4 srcname="NX-RMV-LAP-0086" srcport=58183 srcintf="VLAN 9" srcintfrole="lan" dstip=5.6.7.8 dstport=443 dstintf="port1" dstintfrole="wan" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" dstuuid="7b99da0e-f93c-51ed-7b07-fa36102b7aff" srccountry="Reserved" dstcountry="United Kingdom" sessionid=10000000 proto=6 action="accept" policyid=7 policytype="policy" poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policyname="VLAN9 to WAN" service="INTERNET-DEFAULT-SERVICES" trandisp="snat" transip=213.144.200.164 transport=58183 appid=41468 app="Microsoft.365.Portal" appcat="Collaboration" apprisk="elevated" applist="Novalix" duration=1569 sentbyte=51914 rcvdbyte=22449 sentpkt=392 rcvdpkt=307 sentdelta=360 rcvddelta=657 durationdelta=142 sentpktdelta=9 rcvdpktdelta=9 srchwvendor="Dell" devtype="Home & Office" srcfamily="Computer" osname="Windows" srcswversion="10" unauthuser="jhuck" unauthusersource="kerberos" mastersrcmac="00:11:22:33:44:55" srcmac="00:11:22:33:44:55" srcserver=0
    ```



=== "test_http_transaction_1"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443758828086 tz="+0200" logid="1000234512" type="traffic" subtype="http-transaction" level="notice" vd="root" srcip=1.2.3.4 dstip=5.6.7.8 clientip=10.24.20.212 scheme="http" srcport=52112 dstport=80 hostname="example.com" url="https://example.com/some/long/path?query=param" prefetch=0 policyid=5 sessionid=10000000 transid=51313645 reqlength=474 resplength=0 rcvdbyte=1932 sentbyte=943 resptype="generated" user="P000122" group="GGA_PROXY_STANDARD" cat=82 catdesc="Content Servers" agent="Microsoft-Delivery-Optimization/10.0" reqtime=1744107443 resptime=0 respfinishtime=1744107443 duration=10 appcat="unscanned" utmaction="block" countdlp=1
    ```



=== "test_http_transaction_2"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443804142320 tz="+0200" logid="1000234512" type="traffic" subtype="http-transaction" level="notice" vd="root" srcip=1.2.3.4 dstip=5.6.7.8 clientip=10.24.22.19 scheme="https" srcport=63642 dstport=443 hostname="example.com" url="https://example.com/some/long/path?query=param" prefetch=0 policyid=20 sessionid=10000000 transid=51313649 reqlength=134 resplength=0 rcvdbyte=0 sentbyte=134 resptype="generated" user="P002188" cat=52 catdesc="Information Technology" agent="S1-WIN/23.4.4.223" reqtime=1744107443 resptime=0 respfinishtime=1744107443 duration=0 appcat="unscanned" utmaction="allow" countweb=1
    ```



=== "test_local_1"

    ```
	time=12:17:22 devname="NX-RMV-FW-FTG-01" devid=1111111111111111 eventtime=1744107442110646245 tz="+0200" logid="1000234512" type="traffic" subtype="local" level="notice" vd="root" srcip=1.2.3.4 srcport=5353 srcintf="VLAN 9" srcintfrole="lan" dstip=5.6.7.8 dstport=5353 dstintf="unknown-0" dstintfrole="undefined" replysrcintf="root" sessionid=10000000 proto=17 action="deny" policyid=0 policytype="local-in-policy6" service="udp/5353" trandisp="noop" app="udp/5353" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 appcat="unscanned" msg="Connection Failed" srchwvendor="Dell" devtype="Computer" osname="Windows" srcswversion="10" mastersrcmac="6c:2b:59:c8:bb:07" srcmac="6c:2b:59:c8:bb:07" srcserver=0
    ```



=== "test_signature_1"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443929175015 tz="+0200" logid="1000234512" type="utm" subtype="app-ctrl" eventtype="signature" level="information" vd="root" appid=16009 user="P000122" group="GGA_PROXY_STANDARD" srcip=1.2.3.4 srccountry="Reserved" dstip=5.6.7.8 dstcountry="United States" srcport=52119 dstport=443 srcintf="port1" srcintfrole="undefined" dstintf="port1" dstintfrole="undefined" proto=6 service="SSL" direction="outgoing" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 applist="standard" action="pass" appcat="Update" app="Microsoft.Windows.Update" hostname="example.com" incidentserialno=123456789 url="/some/long/path?query=param" msg="Update: Microsoft.Windows.Update" apprisk="elevated"
    ```



=== "test_signature_2"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107444187952936 tz="+0200" logid="1000234512" type="utm" subtype="app-ctrl" eventtype="signature" level="information" vd="root" appid=48983 user="p001720" group="GGA_PROXY_AVANCE" srcip=1.2.3.4 srccountry="Reserved" dstip=5.6.7.8 dstcountry="United States" srcport=62075 dstport=443 srcintf="port1" srcintfrole="undefined" dstintf="port1" dstintfrole="undefined" proto=6 service="HTTPS" direction="outgoing" policyid=6 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 applist="advanced" action="pass" appcat="Collaboration" app="Google.Meet" hostname="example.com" incidentserialno=123456789 url="/some/long/path?query=param" msg="Collaboration: Google.Meet" apprisk="low"
    ```



=== "test_ssl_1"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443929226931 tz="+0200" logid="1000234512" type="utm" subtype="ssl" eventtype="ssl-anomaly" level="notice" vd="root" action="resign-as-untrusted" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 service="HTTPS" user="P000122" group="GGA_PROXY_STANDARD" profile="custom-deep-inspection" srcip=1.2.3.4 srcport=52119 srccountry="Reserved" dstip=5.6.7.8 dstport=443 dstcountry="United States" srcintf="port1" srcintfrole="undefined" dstintf="port1" dstintfrole="undefined" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" proto=6 eventsubtype="certificate-anomaly" msg="Server certificate is re-signed as untrusted, certificate-status: untrusted." hostname="example.com"
    ```



=== "test_ssl_2"

    ```
	time=12:17:18 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107437589829761 tz="+0200" logid="1000234512" type="utm" subtype="ssl" eventtype="ssl-anomaly" level="notice" vd="root" action="resign-as-untrusted" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 service="HTTPS" user="P001779" group="GGA_PROXY_STANDARD" profile="custom-deep-inspection" srcip=1.2.3.4 srcport=59800 srccountry="Reserved" dstip=5.6.7.8 dstport=443 dstcountry="United States" srcintf="port1" srcintfrole="undefined" dstintf="port1" dstintfrole="undefined" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" proto=6 eventsubtype="certificate-anomaly" msg="Server certificate is re-signed as untrusted, certificate-status: untrusted." hostname="example.com"
    ```



=== "test_system_1"

    ```
	time=12:13:32 devname="CRYO-FPX" devid=1111111111111111 eventtime=1744107212454219917 tz="+0200" logid="1000234512" type="event" subtype="system" level="notice" vd="root" logdesc="FortiProxy update succeeded" status="update" msg="Fortiproxyupdate now  fsci=yes from 1.2.3.4:443"
    ```



=== "test_system_2"

    ```
	time=12:14:10 devname="NX-RMV-FW-FTG-01" devid=1111111111111111 eventtime=1744107250324991239 tz="+0200" logid="1000234512" type="event" subtype="system" level="notice" vd="root" logdesc="FortiGate update succeeded" status="update" msg="Fortigate scheduled update fcni=yes fdni=yes from 1.2.3.4:443"
    ```



=== "test_user_1"

    ```
	time=12:16:41 devname="CRYO-FPX" devid=1111111111111111 eventtime=1744107401561964879 tz="+0200" logid="1000234512" type="event" subtype="user" level="notice" vd="root" logdesc="Explicit proxy authentication successful" srcip=1.2.3.4 dstip=5.6.7.8 authid="ntlm_rule" user="Testpompes" authproto="HTTP(10.14.161.33)" action="NTLM-auth" status="success" reason="Authentication succeeded" msg="User Testpompes succeeded in authentication"
    ```



=== "test_virus_1"

    ```
	time=12:17:23 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107442997206951 tz="+0200" logid="1000234512" type="utm" subtype="virus" eventtype="scanerror" level="notice" vd="root" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" msg="Corrupted archive." action="passthrough" service="HTTP" sessionid=10000000 srcip=1.2.3.4 dstip=5.6.7.8 srcport=52111 dstport=80 srccountry="Reserved" dstcountry="United States" srcintf="port1" srcintfrole="undefined" dstintf="port1" dstintfrole="undefined" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" proto=6 direction="incoming" filename="Microsoft.VCLibs.140.00_14.0.33519.0_x64__8wekyb3d8bbwe.Appx" quarskip="No-quarantine-for-av-error" url="https://example.com/some/long/path?query=param" profile="default" user="P000122" group="GGA_PROXY_STANDARD" agent="Microsoft-Delivery-Optimization/10.0" analyticscksum="9c17b521f9d690a1f504da5108ed6eec5669eb3a8fd1331eef43e40d84e74283" analyticssubmit="false" crscore=30 craction=2 crlevel="high"
    ```



=== "test_webfilter_1"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107443754179544 tz="+0200" logid="1000234512" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" vd="root" policyid=5 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 transid=51313646 user="P000122" group="GGA_PROXY_STANDARD" srcip=1.2.3.4 srcport=52114 srccountry="Reserved" srcintf="port1" srcintfrole="undefined" srcuuid="fd949b9d-74bc-4147-a614-51a5ea07d961" dstip=5.6.7.8 dstport=80 dstcountry="United States" dstintf="port1" dstintfrole="undefined" proto=6 service="HTTP" hostname="example.com" profile="standard" action="passthrough" reqtype="direct" url="https://example.com/some/long/path?query=param" sentbyte=469 rcvdbyte=0 direction="outgoing" msg="URL belongs to an allowed category in policy" method="ip" cat=82 catdesc="Content Servers"
    ```



=== "test_webfilter_2"

    ```
	time=12:17:24 devname="fortiprxweb02" devid=1111111111111111 eventtime=1744107444009941928 tz="+0200" logid="1000234512" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" vd="root" policyid=20 poluuid="75a3be3e-54d9-498b-9251-d1427fec35dc" policytype="policy" sessionid=10000000 transid=121738738 srcip=1.2.3.4 srcport=52662 srccountry="Reserved" srcintf="port1" srcintfrole="undefined" dstip=5.6.7.8 dstport=443 dstcountry="Germany" dstintf="port1" dstintfrole="undefined" proto=6 service="HTTPS" hostname="example.com" profile="monitor-all" action="passthrough" reqtype="direct" url="https://example.com/some/long/path?query=param" sentbyte=132 rcvdbyte=0 direction="outgoing" msg="URL belongs to an allowed category in policy" method="domain" cat=52 catdesc="Information Technology"
    ```



=== "traffic-http-transaction"

    ```
	time=15:01:23 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="traffic" subtype="http-transaction" level="notice" vd="root" eventtime=1631192483 srcip=192.168.1.2 dstip=1.1.1.1 scheme="https" srcport=123456 dstport=443 hostname="example.com" url="https://example.com/foo.html?id=123" policyid=1 reqlength=100 resplength=200 resptype="normal" statuscode=200 reqtime=1631182483 resptime=1631182483 respfinishtime=1631182483 duration=100
    ```



=== "traffic"

    ```
	devname="fortiproxyunit" devid="1111111111111111" vd="default" itime=123456 fctsn="FCT1234567890" date="2025-03-27" time="09:38:48" logver=1 id=96900 type="traffic" subtype="system" eventtype="traffic" level="info" uid="A94A8FE5CCB19BA61C4C0873D391E987982FBBD3" hostname="Toowoomba" pcdomain="Domain.int" deviceip=1.2.3.4 devicemac="00-11-22-33-44-55" site="default" fctver="7.2.8.1140" fgtserial="N/A" emsserial="1111111111111111" usingpolicy="Default" os="Microsoft Windows 11 Professional Edition, 64-bit (build 22000)" user="johndoe@DOMAIN" msg="Traffic log" sessionid=10000000 srcname="chrome.exe" srcproduct="Google Chrome" srcport=0 direction="outbound" remotename="login.microsoftonline.com" dstport=443 proto=6 rcvdbyte=0 sentbyte=0 utmaction="userbrowsed" utmevent="webfilter" service="https" userinitiated=1 browsetime=7 url="/common/oauth2/v2.0/authorize?client_id=ed98c729-468d-451b-bf07-ad564a64a318" tz="+0100"
    ```



=== "webfilter"

    ```
	time=14:19:19 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" vd="root" eventtime=1631179959 policyid=5 sessionid=10000000 user="john" group="groupname" srcip=192.168.1.2 srcport=10000 srcintf="eth" srcintfrole="undefined" dstip=1.1.1.1 dstport=443 dstintf="eth" dstintfrole="undefined" proto=6 service="HTTPS" hostname="example.fr" profile="standard" action="passthrough" reqtype="referral" url="/foo/bar.html?id=1"
    ```



