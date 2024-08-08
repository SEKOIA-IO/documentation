
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



=== "traffic-http-transaction"

    ```
	time=15:01:23 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="traffic" subtype="http-transaction" level="notice" vd="root" eventtime=1631192483 srcip=192.168.1.2 dstip=1.1.1.1 scheme="https" srcport=123456 dstport=443 hostname="example.com" url="https://example.com/foo.html?id=123" policyid=1 reqlength=100 resplength=200 resptype="normal" statuscode=200 reqtime=1631182483 resptime=1631182483 respfinishtime=1631182483 duration=100
    ```



=== "webfilter"

    ```
	time=14:19:19 devname="fortiproxyunit" devid="OIDL03VZRZEDKKD" logid="1000234512" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" vd="root" eventtime=1631179959 policyid=5 sessionid=10000000 user="john" group="groupname" srcip=192.168.1.2 srcport=10000 srcintf="eth" srcintfrole="undefined" dstip=1.1.1.1 dstport=443 dstintf="eth" dstintfrole="undefined" proto=6 service="HTTPS" hostname="example.fr" profile="standard" action="passthrough" reqtype="referral" url="/foo/bar.html?id=1"
    ```



