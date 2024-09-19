
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "encrypt"

    ```
	time=10:45:27 device_id=123 log_id=000000 type=encrypt pri=information session_id="ziuhiohzf" msg="User user1@1.ca read secure message, id:'ziuhiohzf', sent from: 'user2@2.ca', subject: 'ppt file'"
    ```



=== "esmtp"

    ```
	to=<jdoe@example.com> delay=00:00:06 xdelay=00:00:06 mailer=esmtp pri=165917 relay= [3.4.5.6] dsn=2.0.0 stat=Sent (Ok: queued as 4T9pxY2qZtz2XPBPX)
    ```



=== "event"

    ```
	time=17:07:46.124 device_id=FEVM020000087260 log_id=00000 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="1Z11R1T1" msg="from=person.fr, size=26135, class=0, nrcpts=1, msgid=something.com, proto=ESMTP, daemon=SMTP_MTA, relay=notifications [1.1.1.1]"
    ```



=== "event_smpt_to_1"

    ```
	time=18:33:35.615 device_id=xcvfg log_id=0003007072 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="13KGXMHI007058-13KGXMHK007058" msg="to=<contact@example.com>, delay=00:00:06, xdelay=00:00:06, mailer=esmtp, pri=165917, relay= [188.165.36.237], dsn=2.0.0, stat=Sent (Ok: queued as 4T9pxY2qZtz2XPBPX)"
    ```



=== "event_smpt_to_2"

    ```
	time=18:33:35.615 device_id=xcvfg log_id=0003007072 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="13KGXMHI007058-13KGXMHK007058" msg="to=<contact@example.com>, delay=00:00:06, xdelay=00:00:06, mailer=esmtp, pri=165917, relay=smtp.example.org [188.165.36.237], dsn=2.0.0, stat=Sent (Ok: queued as 4T9pxY2qZtz2XPBPX)"
    ```



=== "event_smtp_STARTTLS"

    ```
	time=18:33:36.601 device_id=123456 log_id=0003007110 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="12345" msg="STARTTLS=server, relay=something.com [1.1.1.1], version=TLSv1.2, verify=NO, cipher=ECDHE-RSA-something, bits=256/256"
    ```



=== "event_smtp_to"

    ```
	time=18:33:35.615 device_id=xcvfg log_id=0003007072 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="13KGXMHI007058-13KGXMHK007058" msg="to=<mh.fr>, delay=00:00:13, xdelay=00:00:12, mailer=esmtp, pri=50733, relay=email.fr. [1.1.1.1], dsn=2.0.0, stat=Sent (Ok: queued as C41457FCE6)"
    ```



=== "event_smtp_to_bis"

    ```
	time=15:12:29.013 device_id=FEVM020000087260 log_id=0003014581 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="13RDCREi014579-13RDCREj014579" msg="to=<sjira.eu>, delay=00:00:02, xdelay=00:00:01, mailer=esmtp, pri=40733, relay=mail.eu. [1.1.1.1], dsn=2.0.0, stat=Sent (<email.fr> [InternalId=96830037688413, Hostname=sphinx] 12426 bytes in 0.118, 102,604 KB/sec Queued mail for delivery)"
    ```



=== "kevent"

    ```
	time=17:34:06.188 device_id=0000 log_id=123 type=kevent subtype=dns pri=information  msg="UDP DNS response is truncated, try DNS query in TCP (happened 385350 time(s)), DNS question section:{name=something.com, qtype=16, class=1}"
    ```



=== "kevent_1"

    ```
	time=11:19:15.002 device_id=123 log_id=0701031743 type=kevent subtype=admin pri=information scope=o365 user=j.doe ui=GUI(1.2.3.4) action=login status=success reason=none msg="User j.doe login successfully from GUI(1.2.3.4)"
    ```



=== "relay_ip_only"

    ```
	time=15:03:24.344 device_id=FFFF log_id=YY type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="AAA-BBB" msg="to=<johndoe>, delay=00:00:01, xdelay=00:00:01, mailer=esmtp, pri=2290731, relay= [1.2.3.4], dsn=2.0.0, stat=Sent (ok:  Message 88943067 accepted)"
    ```



=== "smtp_event_STARTTLS_client_local_certificate"

    ```
	time=14:35:47.153 device_id=123 log_id=0000 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="14SCZkrD013672-14SCZkrF013672" msg="STARTTLS=client, cert-subject=/CN=EX-01, cert-issuer=/CN=EX-01, verifymsg=unable to get local issuer certificate"
    ```



=== "smtp_event_STARTTLS_server_local_certificate"

    ```
	time=16:10:33.138 device_id=123 log_id=123 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="000" msg="STARTTLS=server, cert-subject=/C=US/ST=California/L=Mountain View/O=Google LLC/CN=something.com, cert-issuer=issuer, verifymsg=unable to get local issuer certificate"
    ```



=== "smtp_event_STARTTLS_server_signed_certificate"

    ```
	time=14:25:48.564 device_id=123 log_id=0000 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="0000" msg="STARTTLS=server, cert-subject=/something.fr, cert-issuer=issuer name, verifymsg=self signed certificate in certificate chain"
    ```



=== "smtp_event_to_user_unknown"

    ```
	time=10:50:36.931 device_id=FEVM020000087260 log_id=0003008733 type=event subtype=smtp pri=information  user=mail ui=mail action=NONE status=N/A session_id="1548fVq5008733-1548fVq5008733" msg="to=postmaster, delay=00:00:50, mailer=local, pri=58900, dsn=5.1.1, stat=User unknown(Reason from remote:550 5.1.1 User unknown)"
    ```



=== "spam"

    ```
	time=16:01:46.183 device_id=123 log_id=123 type=spam subtype=default pri=information  session_id="00000" client_name="mail.outlook.com" client_ip="2.2.2.2" dst_ip="1.1.1.1" from="" to="mail.fr" subject="Détail de votre quarantaine: [ 1 message(s) en quarantaine entre le jeu. 15 avr. 2021 14 h 00 +0200 et le jeu. 15 avr. 2021 16 h 00 +0200 ]" msg="File name: icon_deleteall.png, scanned by Antivirus Scanner(clean)"
    ```



=== "spam_antispam_url"

    ```
	time=15:08:03.466 device_id=device log_id=121416 type=spam subtype=default pri=information  session_id="123456" client_name="client" client_ip="2.2.2.2" dst_ip="1.1.1.1" from="whatever.com" to="something.com" subject="définitivement aimé cette idée et a pris la décision de vous la montrer" msg="FortiGuard-AntiSpam identified spam URL: http://something.something.photos/apmix"
    ```



=== "spam_antivirus"

    ```
	time=10:00:08.543 device_id=abc log_id=0300025551 type=spam subtype=default pri=information  session_id="123456" client_name="something.live" client_ip="2.2.2.2" dst_ip="1.1.1.1" from="nereply.live" to="info@pms-becus.com" subject="new order to UK" msg="File name: file.ppt(checksum:122452), scanned by Antivirus Scanner(detected)"
    ```



=== "spam_webfilter_url"

    ```
	time=09:59:32.943 device_id=FEVM020000087260 log_id=0300025171 type=spam subtype=default pri=information  session_id="15N7xWCW025167-15N7xWCX025167" client_name="mail@sth.com" client_ip="2.2.2.2" dst_ip="1.1.1.1" from="target.fr" to="source.com" subject="Vos impressions de documents au meilleur prix !" msg="FortiGuard-WebFilter identified URL: url.fr, category: Spam URLs, id: 86."
    ```



=== "spam_webfilter_url_1"

    ```
	time=14:16:45.427 device_id=123 log_id=0300017253 type=spam subtype=default pri=information  session_id="15N7xWCW025167-15N7xWCX025167" client_name="mail.example.org" client_ip="1.2.3.4" dst_ip="5.6.7.8" from="johndoe@example.org" to="jane.doe@example.org" subject="Ring phone promotion" msg="FortiGuard-WebFilter identified URL(category: Phishing, id: 61): https://www.example.org/emailing/promotion.html"
    ```



=== "statistics"

    ```
	time=11:37:27.544 device_id=ABC log_id=0200017947 type=statistics pri=information  session_id="123" client_name="Address.com" client_ip="2.2.2.2" client_cc="FR" dst_ip="1.1.1.1" from="something.fr" hfrom="something.fr" to="something.fr" polid="0:1:1" domain="host.com" mailer="mta" resolved="OK" src_type="int" direction="in" virus="" disposition="Accept" classifier="Domain Safe" message_length="112389" subject=confidential subject
    ```



=== "virus"

    ```
	time=16:17:10.683 device_id=ABC log_id=1234271 type=virus subtype=fortisandbox pri=information  from="" to="" client_name="" client_ip="" session_id="123456789" msg="File file.pdf (checksum: 1234271) has been scanned by FortiSandbox. Scan result: rating=CLEAN"
    ```



=== "virus_1"

    ```
	time=14:18:20.030 device_id=123 log_id=0103021373 type=virus subtype=fortisandbox pri=information  scope=o365 from="" to="" client_name="" client_ip="" session_id="15N7xWCW025167-15N7xWCX025167" msg="URL https://example.org/path/image.jpg has been scanned by FortiSandbox. Scan result: rating=CLEAN"
    ```



=== "virus_2"

    ```
	time=14:18:14.805 device_id=123 log_id=0103001910 type=virus subtype=fortisandbox pri=information  from="" to="" client_name="" client_ip="" session_id="15N7xWCW025167-15N7xWCX025167" msg="URL https://example.org/path/image.jpg has been scanned by FortiSandbox. Scan result: rating=CLEAN"
    ```



