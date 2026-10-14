
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "anvil"

    ```
	statistics: max connection count 10 for (smtp:1.2.3.4) at Sep 11 10:47:30
    ```



=== "appname_postfix_error"

    ```
	2298F5F619: to=<admin@corp.com>, relay=none, delay=89758, delays=89758/0.02/0/0, dsn=4.4.1, status=deferred (delivery temporarily suspended: connect to mail.corp.com[1.1.1.1]:25: Connection timed out) 215
    ```



=== "appname_postfix_local"

    ```
	11FDF5F62A: to=<user@example.com>, relay=local, delay=80181, delays=80181/0.02/0/0, dsn=4.0.0, status=deferred (user lookup error)
    ```



=== "bounced"

    ```
	3D770111AF50: to=<username@corp.com>, relay=none, delay=1.2, delays=1.1/0/0.03/0, dsn=5.4.4, status=bounced (Host or domain name not found. Name service error for name=corp.com type=AAAA: Host not found)
    ```



=== "cleanup"

    ```
	77EFFC0015: warning: header Content-Disposition: inline; filename="image003.jpg"; size=26055;??creation-date="Thu, 12 Sep 2019 12:39:01 GMT";??modification-date="Thu, 12 Sep 2019 12:40:01 GMT" from host.example.com[1.1.1.1]; from=<> to=<john.doe@host.example.com> proto=ESMTP helo=<NAM03.outbound.protection.outlook.com>
    ```



=== "cleanup2"

    ```
	3D770111AF50: warning: header Subject: Manquants LASTNAME GB Nouvelle version from unknown[10.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<SUBDOMAIN.CORP.COM>
    ```



=== "cleanup3"

    ```
	2CE6C111AF50: warning: header Subject: =?ISO-8859-1?Q?Pb_FTP_=3A_999_Aucune_action_effectu=E9e?= from unknown[10.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<SUBDOMAIN.CORP.COM> 279
    ```



=== "cleanup4"

    ```
	B4B613F8B7: warning: header Content-Disposition: inline; filename="image001.png"; size=8879;??creation-date="Thu, 14 Mar 2024 10:19:00 GMT";??modification-date="Thu, 14 Mar 2024 10:19:00 GMT" from subdomain.key.corp.com[1.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<subdomain.key.corp.com>
    ```



=== "cleanup5"

    ```
	707A12000A: warning: header Content-Disposition: attachment;??filename="?iso-8859-2?q?representative_on_migration.pdf?="; size=259210;?? from local; from=<user@example.com> to=<user@example.com>
    ```



=== "client"

    ```
	486D13F8B7: client=COMPUTER.sub.corp.com[1.1.1.1]
    ```



=== "client_address_field_with_mask"

    ```
	8116C5F683: action=pass, reason=client whitelist, client_name=host.example.com, client_address=1.1.1.1/32, sender=user@example.com, recipient=user@example.com
    ```



=== "connect"

    ```
	disconnect from unknown[1.1.1.1] ehlo=1 mail=1 rcpt=0/1 quit=1 commands=3/4
    ```



=== "connection_limited"

    ```
	53C2C140E40: host host.example.com[1.1.1.1] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=host.example.com] (in reply to end of DATA command)
    ```



=== "connection_limited_1"

    ```
	53C2C140E40: host host.example.com[198.51.100.123] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=host.example.com] (in reply to end of DATA command)
    ```



=== "counter"

    ```
	disconnect from localhost[127.0.0.1] ehlo=2 starttls=1 mail=1 rcpt=1 data=1 quit=1 commands=7
    ```



=== "counter2"

    ```
	disconnect from localhost[127.0.0.1] ehlo=2 starttls=1 mail=1 rcpt=1 data=1 quit=1 commands=7 93
    ```



=== "counter3"

    ```
	disconnect from unknown[1.1.1.1] ehlo=1 mail=1 rcpt=2 data=1 quit=1 commands=6 137
    ```



=== "delivered_via_spamfilter"

    ```
	EF0B15F675: to=<user@example.com>, relay=spamfilter, delay=4.2, delays=1.6/0/0/2.6, dsn=2.0.0, status=sent (delivered via spamfilter service) 148
    ```



=== "dns"

    ```
	dns: new_dns_packet: domain is utf8 flagged: ns1.example.org
    ```



=== "local1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "local2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "local3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "local4"

    ```
	B84078B26C7: to=<foreman-proxy@example.com>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.02/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "local5"

    ```
	B84078B26C7: to=user@example.com, orig_to=sample.orig.to, relay=local, delay=0.05, delays=0.04/0.02/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "local6"

    ```
	04B953035FC2: to=john.doe@example.org, orig_to=jane.doe@example.com, relay=127.0.0.1:2525, delay=0.44, delays=0.13/0/0.02/0.29, dsn=2.0.0, status=sent (250 Ok)
    ```



=== "message_id"

    ```
	476295F5AD: message-id=<<test-message-id@example.com>>
    ```



=== "message_id2"

    ```
	123456789: message-id=<<test-message-id@example.com>>
    ```



=== "message_id3"

    ```
	ABA141A0109: message-id=<<test-message-id@example.com>>
    ```



=== "noqueue"

    ```
	NOQUEUE: filter: RCPT from foo.key.corp.com[192.168.1.1]: <foo.key.corp.com[192.168.1.1]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<foo.key.corp.com> 294
    ```



=== "noqueue2"

    ```
	NOQUEUE: filter: RCPT from HOSTNAME.key.corp.com[192.168.1.1]: <HOSTNAME.key.corp.com[192.168.1.1]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<HOSTNAME.key.corp.com> 299
    ```



=== "nospam"

    ```
	Anonymous TLS connection established to example.org[1.2.3.4]:25: TLSv1.2 with cipher ADH-AES256-GCM-SHA384 (256/256 bits)
    ```



=== "opendkim"

    ```
	host01 opendkim[778]: 720B91122280: DKIM-Signature field added (s=test01, d=something-group.com)
    ```



=== "pass"

    ```
	action=pass, reason=triplet found, delay=2400, client_name=host.example.com, client_address=1.1.1.1, sender=user@example.com, recipient=user@example.com
    ```



=== "pass2"

    ```
	action=pass, reason=client AAA, client_name=example.com, client_address=1.2.3.4, sender=user@example.com, recipient=user@example.com
    ```



=== "pickup1"

    ```
	E43D43F838: uid=117 from=<no-reply@example.org>
    ```



=== "pipe1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "pipe2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "pipe3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "policydspf1"

    ```
	Action: prepend: Text: Received-SPF: Permerror (mailfrom) identity=mailfrom; client-ip=1.1.1.1; helo=corp.com; envelope-from=user@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23 210
    ```



=== "policydspf10"

    ```
	Action: prepend: Text: Received-SPF: Pass (sender SPF authorized) identity=helo; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=<>; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "policydspf11"

    ```
	Action: prepend: Text: Received-SPF: Softfail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=noreply@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "policydspf12"

    ```
	Neutral; identity=mailfrom; client-ip=1.2.3.4; helo=example.mail.protection.outlook.com; envelope-from=john.doem@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf13"

    ```
	None; identity=helo; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf14"

    ```
	Pass; identity=helo; client-ip=1.2.3.4; helo=mail.example.org; envelope-from=<>; receiver=<UNKNOWN>
    ```



=== "policydspf15"

    ```
	Pass; identity=mailfrom; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf16"

    ```
	Permerror; identity=helo; client-ip=1.2.3.4; helo=example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf17"

    ```
	Permerror; identity=mailfrom; client-ip=1.2.3.4; helo=example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf18"

    ```
	Permerror; identity=mailfrom; client-ip=1.2.3.4; helo=example.org; envelope-from=no-reply@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf19"

    ```
	Softfail; identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=noreply@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf2"

    ```
	Action: prepend: Text: Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=mx.example.com; envelope-from=prvs=30447fe13=no-reply@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "policydspf20"

    ```
	prepend Received-SPF: Fail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf21"

    ```
	prepend Received-SPF: Neutral (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf22"

    ```
	prepend Received-SPF: None (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf23"

    ```
	prepend Received-SPF: None (no SPF record) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf24"

    ```
	prepend Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf25"

    ```
	prepend Received-SPF: Pass (sender SPF authorized) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf26"

    ```
	prepend Received-SPF: Permerror (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf27"

    ```
	prepend Received-SPF: Softfail (domain owner discourages use of this host) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf28"

    ```
	prepend Received-SPF: Softfail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "policydspf3"

    ```
	Action: prepend Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=198.51.100.51; helo=mta-11-22-33-44.example.or; envelope-from=doe@newsletter.example.org; receiver=<UNKNOWN>
    ```



=== "policydspf4"

    ```
	Pass; identity=mailfrom; client-ip=1.1.1.1; helo=mail.corp.com; envelope-from=username@corp.com; receiver=<UNKNOWN> 131
    ```



=== "policydspf5"

    ```
	None; identity=helo; client-ip=1.1.1.1; helo=sub.corp.com; envelope-from=user@example.com; receiver=<UNKNOWN> 128
    ```



=== "policydspf6"

    ```
	Softfail; identity=mailfrom; client-ip=1.1.1.1; helo=corp.com; envelope-from=username@corp.com; receiver=<UNKNOWN> 120
    ```



=== "policydspf7"

    ```
	Action: prepend: Text: Received-SPF: None (mailfrom) identity=mailfrom; client-ip=198.51.100.3; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "policydspf8"

    ```
	Action: prepend: Text: Received-SPF: None (no SPF record) identity=helo; client-ip=198.51.100.3; helo=posta.example.org; envelope-from=<>; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "policydspf9"

    ```
	Action: prepend: Text: Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=jdoe@example.org; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "postfix1"

    ```
	7B082110A6E0: host host.example.com[198.51.100.122] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=EXAMPLE.PROD.OUTLOOK.COM] (in reply to end of DATA command)
    ```



=== "postfix2"

    ```
	01B3A96050: Used TLS for 198.51.100.121[198.51.100.121]:587
    ```



=== "postfix3"

    ```
	023069605C: Used TLS for smtp.example.org[198.51.100.120]:25
    ```



=== "postfix4"

    ```
	NOQUEUE: client=unknown[10.100.0.3]
    ```



=== "postfix5"

    ```
	warning: read TCP map reply from 198.51.100.119:10030: unexpected EOF (Operation now in progress)
    ```



=== "postfix6"

    ```
	0A90996059: to=<user@example.com>, relay=localhost[127.0.0.1]:10025, conn_use=3, delay=5.2, delays=0/0/0/5.2, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 0BF0C9605C)
    ```



=== "postfix7"

    ```
	proxy-accept: END-OF-MESSAGE: 250 2.0.0 Ok: queued as 7949396087; from=<jdoe@example.org> to=<jane.doe@example.org> proto=ESMTP helo=<mx.example.org>
    ```



=== "postfix8"

    ```
	D2D459605C: Used TLS for smtp-in.example.com[5.6.7.8]:25
    ```



=== "postfix_cleanup1"

    ```
	581B85F5B3: warning: header Content-Disposition: inline; filename=""image018.png""; size=162328;??creation-date=""Thu, 11 Apr 2024 07:53:08 GMT"";??modification-date=""Thu, 11 Apr 2024 07:53:08 GMT"" from local; from=<jdoe@example.org> to=<jane.doe@example.com>
    ```



=== "postfix_cleanup2"

    ```
	59B835F5AD: warning: header Content-Disposition: attachment;??filename=""=?utf-8?B?111111111111111111111111111111111111111111111111111111111111?=? =?utf-8?B?222222222222222222222222222222222222222222222222222222222222?=? =?utf-8? from local; from=<jdoe@example.org> to=<jane.doe@example.com>
    ```



=== "postfix_cleanup3"

    ```
	EBA403F815: message-id=<74c99d8a-eb8b-4045-ae8e-6d3f6d51b41d@example.org>
    ```



=== "postfix_no_spam_cleanup1"

    ```
	000FA5FD8F: prepend: header From: John Doe <jdoe@example.org> from localhost[127.0.0.1]; from=<jdoe@example.org> to=<jane.doe@example.com> proto=ESMTP helo=<smtp.example.org>: X-NMFP-TRUST: TRUE
    ```



=== "postfix_no_spam_cleanup2"

    ```
	008BB5FD76: prepend: header From: =?UTF-8?q?Cellier_du_P=C3=A9rigord?=??<user@example.com> from localhost[127.0.0.1]; from=<user@example.com> to=<jdoe@example.org> proto=ESMTP helo=<smtp.example.org>: X-NMFP-TRUST: FALSE
    ```



=== "postgrey1"

    ```
	action=greylist, reason=early-retry (10s missing), client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey2"

    ```
	action=greylist, reason=new, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey3"

    ```
	action=greylist, reason=new, client_name=unknown, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey4"

    ```
	action=pass, reason=client AWL, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey5"

    ```
	action=pass, reason=client whitelist, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey6"

    ```
	action=pass, reason=triplet found, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "postgrey7"

    ```
	whitelisted: mx.example.org[1.2.3.4/32]
    ```



=== "postgrey8"

    ```
	whitelisted: unknown[1.2.3.4/32]
    ```



=== "qmgr"

    ```
	89BE920002: from=<user@example.com>, size=152518, nrcpt=1 (queue active)
    ```



=== "qmgr2"

    ```
	074955F67C: from=<user@example.com>, size=4303, nrcpt=1 (queue active)
    ```



=== "queued"

    ```
	CA9311112C08: to=<user@example.com>, relay=srv.corp.com[1.1.1.1]:25, delay=8.4, delays=7.6/0/0.31/0.47, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 4TwNdH5zwCz7fxV) 257
    ```



=== "relay"

    ```
	56E28C0007: to=<user@example.com>, relay=1.1.1.1[1.1.1.1]:10025, delay=0.63, delays=0.57/0/0.05/0.01, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as DF82A21108)
    ```



=== "replace_header"

    ```
	95BCC140E40: replace: header From: EXAMPLE <[hola@example.org](mailto:hola@example.org)>: From: [noreply@example.org](mailto:noreply@example.org)
    ```



=== "replace_header_1"

    ```
	95BCC140E40: replace: header From: Example Mailbox <[test@example.org](mailto:test@example.org)>: From: [noreply@example.org](mailto:noreply@example.org)
    ```



=== "replace_header_2"

    ```
	2F46A140256: replace: header From: "Example Help" <help@example.org: From: [help@example.org](mailto:help@example.org)
    ```



=== "sasl_login"

    ```
	warning: unknown[198.51.100.51]: SASL LOGIN authentication failed: authentication failure
    ```



=== "smtp1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "smtp2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "smtp3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "smtp4"

    ```
	05BC43F81E: host mx.example.org[5.6.7.8] said: 421 4.3.0 Upstream error, please check https://example.com/email-routing/postmaster for possible reasons why. yrtPbwx4hZz2 (in reply to end of DATA command)
    ```



=== "smtp5"

    ```
	30D713F81F: host mx.example.org[5.6.7.8] said: 450 4.1.1 <abuse@example.com>: Recipient address rejected: unverified address: Mailbox might be disabled, full, or may not exist on the server. Reason: JFE030050 (in reply to RCPT TO command)
    ```



=== "smtp6"

    ```
	connect to mx.example.org[5.6.7.8]:25: No route to host
    ```



=== "smtp7"

    ```
	ABA141A0109: to=<user@example.com>, orig_to=<john.doe@host.example.com>, relay=1.2.3.4[1.2.3.4]:10024, delay=1.6, delays=1.2/0.03/0.03/0.28, dsn=2.0.0, status=sent (250 2.0.0 from MTA(smtp:[1.2.3.4]:10025): 250 2.0.0 Ok: queued as 300581A89B8)
    ```



=== "smtp_connection3_timed_out"

    ```
	connect to mail.corp.com[1.1.1.1]:25: Connection timed out 125
    ```



=== "smtp_relay"

    ```
	96887C0006: to=<user@example.com>, relay=host.example.com[1.1.1.1]:25, delay=354776, delays=354775/0/0.9/0.16, dsn=4.3.1, status=deferred (host host.example.com[1.1.1.1] said: 452 4.3.1 Insufficient system storage (in reply to MAIL FROM command))
    ```



=== "smtpd1"

    ```
	021C03F820: filter: RCPT from mx.example.org[192.168.100.124]: <mx.example.org[192.168.100.124]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<jdoe@example.org> to=<jane.doe@example.com> proto=ESMTP helo=<mx.example.com>
    ```



=== "smtpd2"

    ```
	lost connection after BDAT from mx.example.org[192.168.100.124]
    ```



=== "smtpd3"

    ```
	warning: hostname mx.example.org does not resolve to address 5.6.7.8: Name or service not known
    ```



=== "smtpd4"

    ```
	warning: mx.example.org[192.168.100.132]: SASL LOGIN authentication failed: authentication failure, sasl_username=john.doe@exmaple.org
    ```



=== "smtpd_connection"

    ```
	lost connection after AUTH from unknown[1.1.1.1]
    ```



=== "smtpd_connection2"

    ```
	connect from unknown[10.1.1.1] 88
    ```



=== "smtpd_tls"

    ```
	Trusted TLS connection established from host.example.com[1.1.1.1]: TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits)
    ```



=== "smtpd_tls2"

    ```
	Trusted TLS connection established to mx.corp.com[1.1.1.1]:25: TLSv1.3 with cipher TLS_AES_128_GCM_SHA256 (128/128 bits) key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256
    ```



=== "smtpd_tls3"

    ```
	Trusted TLS connection established to 198.51.100.119[198.51.100.119]:10025: TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits) key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256 201
    ```



=== "spamd1"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,HEADER_FROM_DIFFERENT_DOMAINS,HTML_MESSAGE,SPF_HELO_NONE,SPF_PASS,T_KAM_HTML_FONT_INVALID scantime=3.4,size=120289,user=User1,uid=119,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=44944,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd10"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,FORGED_HOTMAIL_RCVD2,FREEMAIL_FROM,HTML_IMAGE_RATIO_04,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=2.7,size=102578,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45880,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd11"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,FREEMAIL_ENVFROM_END_DIGIT,FREEMAIL_FROM,FREEMAIL_REPLYTO_END_DIGIT,HTML_MESSAGE,MIME_HTML_ONLY,RCVD_IN_DNSWL_NONE,SPF_HELO_PASS,SPF_PASS,T_FREEMAIL_DOC_PDF scantime=4.7,size=2252595,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=49594,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd12"

    ```
	spamd: result: . -1 - DMARC_PASS,MIME_HEADER_CTYPE_ONLY,MISSING_DATE,MISSING_MID,SPF_HELO_NONE,SPF_PASS scantime=3.3,size=4260,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=46436,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd13"

    ```
	spamd: result: . -1 - FREEMAIL_ENVFROM_END_DIGIT,FREEMAIL_FROM,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=2.6,size=8094,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=39504,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd14"

    ```
	spamd: result: . -1 - FREEMAIL_FORGED_FROMDOMAIN,FREEMAIL_FROM,HEADER_FROM_DIFFERENT_DOMAINS,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_NONE,SPF_PASS scantime=2.8,size=61589,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=37172,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd15"

    ```
	spamd: result: . -1 - HTML_FONT_LOW_CONTRAST,HTML_IMAGE_RATIO_08,HTML_MESSAGE,LOTS_OF_MONEY,MIME_HTML_MOSTLY,MPART_ALT_DIFF,RCVD_IN_MSPIKE_H4,RCVD_IN_MSPIKE_WL,SPF_HELO_NONE,SPF_PASS scantime=3.3,size=164381,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=56082,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd16"

    ```
	spamd: result: . -1 - HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,HTML_OBFUSCATE_05_10,MIME_HTML_ONLY,SPF_HELO_PASS,SPF_PASS scantime=2.5,size=1572,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=51336,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd17"

    ```
	spamd: result: . -6 - DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_MESSAGE,RCVD_IN_DNSWL_MED,SPF_HELO_PASS,SPF_PASS scantime=2.6,size=7882,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=33278,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd18"

    ```
	spamd: connection from test.com [127.0.0.1]:33620 to port 783, fd 5
    ```



=== "spamd19"

    ```
	spamd: connection from mx.example.org [127.0.0.1]:33620 to port 783, fd 5
    ```



=== "spamd2"

    ```
	spamd: connection from example.org [127.0.0.1]:53684 to port 783, fd 5
    ```



=== "spamd20"

    ```
	spamd: processing message <!&!AAAAAAAAAAAYAAAAAAAAA111111111111111111111111111111111/22222222222222/u47tEBAAAAAA==@example.org> for debian-spamd:118
    ```



=== "spamd21"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:117
    ```



=== "spamd22"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:118
    ```



=== "spamd23"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:118
    ```



=== "spamd24"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:117
    ```



=== "spamd3"

    ```
	spamd: result: . -1 - AC_DIV_BONANZA,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H3,RCVD_IN_MSPIKE_WL,SPF_HELO_NONE,SPF_PASS,URI_NOVOWEL scantime=3.2,size=209868,user=User1,uid=117,required_score=5.0,rhost=host.example.com,raddr=127.0.0.1,rport=44702,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd4"

    ```
	spamd: result: . -1 - ANY_BOUNCE_MESSAGE,DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,FORGED_SPF_HELO,HTML_MESSAGE,OOOBOUNCE_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_NONE scantime=2.7,size=14228,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=36236,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd5"

    ```
	spamd: result: . -1 - APOSTROPHE_FROM,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_FONT_LOW_CONTRAST,HTML_MESSAGE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=4.9,size=575869,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=41352,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd6"

    ```
	spamd: result: . -1 - DEAR_SOMETHING,DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,HTML_MESSAGE,PDS_BTC_ID,RCVD_IN_DNSWL_LOW,SPF_HELO_NONE,SPF_NONE scantime=5.3,size=468649,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=42678,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd7"

    ```
	spamd: result: . -1 - DEAR_SOMETHING,DMARC_PASS,HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,MIME_HTML_ONLY,RCVD_IN_DNSWL_LOW,SPF_HELO_NONE,SPF_PASS scantime=2.8,size=3254,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45060,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd8"

    ```
	spamd: result: . -1 - DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,FORGED_SPF_HELO,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_NONE scantime=2.3,size=10467,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45920,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "spamd9"

    ```
	spamd: result: . -1 - DKIM_INVALID,DKIM_SIGNED,HEADER_FROM_DIFFERENT_DOMAINS,HTML_FONT_LOW_CONTRAST,HTML_MESSAGE,MIME_HTML_ONLY,RCVD_IN_MSPIKE_H2,SPF_HELO_NONE,SPF_PASS,T_REMOTE_IMAGE scantime=2.9,size=65264,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=33254,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "test_disconnect_with_helo"

    ```
	disconnect from mail-gateway.example.com[1.2.3.4] helo=1 mail=1 rcpt=1 data=1 quit=1 commands=5
    ```



=== "wo_appname_anvil"

    ```
	statistics: max connection count 10 for (smtp:1.2.3.4) at Sep 11 10:47:30
    ```



=== "wo_appname_appname_postfix_error"

    ```
	2298F5F619: to=<admin@corp.com>, relay=none, delay=89758, delays=89758/0.02/0/0, dsn=4.4.1, status=deferred (delivery temporarily suspended: connect to mail.corp.com[1.1.1.1]:25: Connection timed out) 215
    ```



=== "wo_appname_appname_postfix_local"

    ```
	11FDF5F62A: to=<user@example.com>, relay=local, delay=80181, delays=80181/0.02/0/0, dsn=4.0.0, status=deferred (user lookup error)
    ```



=== "wo_appname_bounced"

    ```
	3D770111AF50: to=<username@corp.com>, relay=none, delay=1.2, delays=1.1/0/0.03/0, dsn=5.4.4, status=bounced (Host or domain name not found. Name service error for name=corp.com type=AAAA: Host not found)
    ```



=== "wo_appname_cleanup"

    ```
	77EFFC0015: warning: header Content-Disposition: inline; filename="image003.jpg"; size=26055;??creation-date="Thu, 12 Sep 2019 12:39:01 GMT";??modification-date="Thu, 12 Sep 2019 12:40:01 GMT" from host.example.com[1.1.1.1]; from=<> to=<john.doe@host.example.com> proto=ESMTP helo=<NAM03.outbound.protection.outlook.com>
    ```



=== "wo_appname_cleanup2"

    ```
	3D770111AF50: warning: header Subject: Manquants LASTNAME GB Nouvelle version from unknown[10.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<SUBDOMAIN.CORP.COM>
    ```



=== "wo_appname_cleanup3"

    ```
	2CE6C111AF50: warning: header Subject: =?ISO-8859-1?Q?Pb_FTP_=3A_999_Aucune_action_effectu=E9e?= from unknown[10.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<SUBDOMAIN.CORP.COM> 279
    ```



=== "wo_appname_cleanup4"

    ```
	B4B613F8B7: warning: header Content-Disposition: inline; filename="image001.png"; size=8879;??creation-date="Thu, 14 Mar 2024 10:19:00 GMT";??modification-date="Thu, 14 Mar 2024 10:19:00 GMT" from subdomain.key.corp.com[1.1.1.1]; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<subdomain.key.corp.com>
    ```



=== "wo_appname_cleanup5"

    ```
	707A12000A: warning: header Content-Disposition: attachment;??filename="?iso-8859-2?q?representative_on_migration.pdf?="; size=259210;?? from local; from=<user@example.com> to=<user@example.com>
    ```



=== "wo_appname_client"

    ```
	486D13F8B7: client=COMPUTER.sub.corp.com[1.1.1.1]
    ```



=== "wo_appname_client_address_field_with_mask"

    ```
	8116C5F683: action=pass, reason=client whitelist, client_name=host.example.com, client_address=1.1.1.1/32, sender=user@example.com, recipient=user@example.com
    ```



=== "wo_appname_connect"

    ```
	disconnect from unknown[1.1.1.1] ehlo=1 mail=1 rcpt=0/1 quit=1 commands=3/4
    ```



=== "wo_appname_connection_limited"

    ```
	53C2C140E40: host host.example.com[1.1.1.1] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=host.example.com] (in reply to end of DATA command)
    ```



=== "wo_appname_connection_limited_1"

    ```
	53C2C140E40: host host.example.com[198.51.100.123] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=host.example.com] (in reply to end of DATA command)
    ```



=== "wo_appname_counter"

    ```
	disconnect from localhost[127.0.0.1] ehlo=2 starttls=1 mail=1 rcpt=1 data=1 quit=1 commands=7
    ```



=== "wo_appname_counter2"

    ```
	disconnect from localhost[127.0.0.1] ehlo=2 starttls=1 mail=1 rcpt=1 data=1 quit=1 commands=7 93
    ```



=== "wo_appname_counter3"

    ```
	disconnect from unknown[1.1.1.1] ehlo=1 mail=1 rcpt=2 data=1 quit=1 commands=6 137
    ```



=== "wo_appname_delivered_via_spamfilter"

    ```
	EF0B15F675: to=<user@example.com>, relay=spamfilter, delay=4.2, delays=1.6/0/0/2.6, dsn=2.0.0, status=sent (delivered via spamfilter service) 148
    ```



=== "wo_appname_dns"

    ```
	dns: new_dns_packet: domain is utf8 flagged: ns1.example.org
    ```



=== "wo_appname_local1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "wo_appname_local2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "wo_appname_local3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "wo_appname_local4"

    ```
	B84078B26C7: to=<foreman-proxy@example.com>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.02/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "wo_appname_local5"

    ```
	B84078B26C7: to=user@example.com, orig_to=sample.orig.to, relay=local, delay=0.05, delays=0.04/0.02/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "wo_appname_local6"

    ```
	04B953035FC2: to=john.doe@example.org, orig_to=jane.doe@example.com, relay=127.0.0.1:2525, delay=0.44, delays=0.13/0/0.02/0.29, dsn=2.0.0, status=sent (250 Ok)
    ```



=== "wo_appname_message_id"

    ```
	476295F5AD: message-id=<<test-message-id@example.com>>
    ```



=== "wo_appname_message_id2"

    ```
	123456789: message-id=<<test-message-id@example.com>>
    ```



=== "wo_appname_noqueue"

    ```
	NOQUEUE: filter: RCPT from foo.key.corp.com[192.168.1.1]: <foo.key.corp.com[192.168.1.1]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<foo.key.corp.com> 294
    ```



=== "wo_appname_noqueue2"

    ```
	NOQUEUE: filter: RCPT from HOSTNAME.key.corp.com[192.168.1.1]: <HOSTNAME.key.corp.com[192.168.1.1]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<user@example.com> to=<user@example.com> proto=ESMTP helo=<HOSTNAME.key.corp.com> 299
    ```



=== "wo_appname_nospam"

    ```
	Anonymous TLS connection established to example.org[1.2.3.4]:25: TLSv1.2 with cipher ADH-AES256-GCM-SHA384 (256/256 bits)
    ```



=== "wo_appname_pass"

    ```
	action=pass, reason=triplet found, delay=2400, client_name=host.example.com, client_address=1.1.1.1, sender=user@example.com, recipient=user@example.com
    ```



=== "wo_appname_pass2"

    ```
	action=pass, reason=client AAA, client_name=example.com, client_address=1.2.3.4, sender=user@example.com, recipient=user@example.com
    ```



=== "wo_appname_pickup1"

    ```
	E43D43F838: uid=117 from=<no-reply@example.org>
    ```



=== "wo_appname_pipe1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "wo_appname_pipe2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "wo_appname_pipe3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "wo_appname_policydspf1"

    ```
	Action: prepend: Text: Received-SPF: Permerror (mailfrom) identity=mailfrom; client-ip=1.1.1.1; helo=corp.com; envelope-from=user@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23 210
    ```



=== "wo_appname_policydspf10"

    ```
	Action: prepend: Text: Received-SPF: Pass (sender SPF authorized) identity=helo; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=<>; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_policydspf11"

    ```
	Action: prepend: Text: Received-SPF: Softfail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=noreply@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_policydspf12"

    ```
	Neutral; identity=mailfrom; client-ip=1.2.3.4; helo=example.mail.protection.outlook.com; envelope-from=john.doem@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf13"

    ```
	None; identity=helo; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf14"

    ```
	Pass; identity=helo; client-ip=1.2.3.4; helo=mail.example.org; envelope-from=<>; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf15"

    ```
	Pass; identity=mailfrom; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf16"

    ```
	Permerror; identity=helo; client-ip=1.2.3.4; helo=example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf17"

    ```
	Permerror; identity=mailfrom; client-ip=1.2.3.4; helo=example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf18"

    ```
	Permerror; identity=mailfrom; client-ip=1.2.3.4; helo=example.org; envelope-from=no-reply@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf19"

    ```
	Softfail; identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=noreply@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf2"

    ```
	Action: prepend: Text: Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=mx.example.com; envelope-from=prvs=30447fe13=no-reply@example.com; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_policydspf20"

    ```
	prepend Received-SPF: Fail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf21"

    ```
	prepend Received-SPF: Neutral (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf22"

    ```
	prepend Received-SPF: None (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf23"

    ```
	prepend Received-SPF: None (no SPF record) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf24"

    ```
	prepend Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf25"

    ```
	prepend Received-SPF: Pass (sender SPF authorized) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf26"

    ```
	prepend Received-SPF: Permerror (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf27"

    ```
	prepend Received-SPF: Softfail (domain owner discourages use of this host) identity=helo; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf28"

    ```
	prepend Received-SPF: Softfail (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=smtp.example.org; envelope-from=jdoe@example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf3"

    ```
	Action: prepend Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=198.51.100.51; helo=mta-11-22-33-44.example.or; envelope-from=doe@newsletter.example.org; receiver=<UNKNOWN>
    ```



=== "wo_appname_policydspf4"

    ```
	Pass; identity=mailfrom; client-ip=1.1.1.1; helo=mail.corp.com; envelope-from=username@corp.com; receiver=<UNKNOWN> 131
    ```



=== "wo_appname_policydspf5"

    ```
	None; identity=helo; client-ip=1.1.1.1; helo=sub.corp.com; envelope-from=user@example.com; receiver=<UNKNOWN> 128
    ```



=== "wo_appname_policydspf6"

    ```
	Softfail; identity=mailfrom; client-ip=1.1.1.1; helo=corp.com; envelope-from=username@corp.com; receiver=<UNKNOWN> 120
    ```



=== "wo_appname_policydspf7"

    ```
	Action: prepend: Text: Received-SPF: None (mailfrom) identity=mailfrom; client-ip=198.51.100.3; helo=[1.2.3.4]; envelope-from=jdoe@example.org; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_policydspf8"

    ```
	Action: prepend: Text: Received-SPF: None (no SPF record) identity=helo; client-ip=198.51.100.3; helo=posta.example.org; envelope-from=<>; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_policydspf9"

    ```
	Action: prepend: Text: Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=1.2.3.4; helo=example.outbound.protection.outlook.com; envelope-from=jdoe@example.org; receiver=<UNKNOWN>  Reject action: 550 5.7.23
    ```



=== "wo_appname_postfix1"

    ```
	7B082110A6E0: host host.example.com[198.51.100.122] said: 432 4.3.2 Concurrent connections limit exceeded. Visit https://aka.ms/concurrent_sending for more information. [Hostname=EXAMPLE.PROD.OUTLOOK.COM] (in reply to end of DATA command)
    ```



=== "wo_appname_postfix2"

    ```
	01B3A96050: Used TLS for 198.51.100.121[198.51.100.121]:587
    ```



=== "wo_appname_postfix3"

    ```
	023069605C: Used TLS for smtp.example.org[198.51.100.120]:25
    ```



=== "wo_appname_postfix4"

    ```
	NOQUEUE: client=unknown[10.100.0.3]
    ```



=== "wo_appname_postfix5"

    ```
	warning: read TCP map reply from 198.51.100.119:10030: unexpected EOF (Operation now in progress)
    ```



=== "wo_appname_postfix6"

    ```
	0A90996059: to=<user@example.com>, relay=localhost[127.0.0.1]:10025, conn_use=3, delay=5.2, delays=0/0/0/5.2, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 0BF0C9605C)
    ```



=== "wo_appname_postfix7"

    ```
	proxy-accept: END-OF-MESSAGE: 250 2.0.0 Ok: queued as 7949396087; from=<jdoe@example.org> to=<jane.doe@example.org> proto=ESMTP helo=<mx.example.org>
    ```



=== "wo_appname_postfix8"

    ```
	D2D459605C: Used TLS for smtp-in.example.com[5.6.7.8]:25
    ```



=== "wo_appname_postfix_cleanup1"

    ```
	581B85F5B3: warning: header Content-Disposition: inline; filename=""image018.png""; size=162328;??creation-date=""Thu, 11 Apr 2024 07:53:08 GMT"";??modification-date=""Thu, 11 Apr 2024 07:53:08 GMT"" from local; from=<jdoe@example.org> to=<jane.doe@example.com>
    ```



=== "wo_appname_postfix_cleanup2"

    ```
	59B835F5AD: warning: header Content-Disposition: attachment;??filename=""=?utf-8?B?111111111111111111111111111111111111111111111111111111111111?=? =?utf-8?B?222222222222222222222222222222222222222222222222222222222222?=? =?utf-8? from local; from=<jdoe@example.org> to=<jane.doe@example.com>
    ```



=== "wo_appname_postfix_cleanup3"

    ```
	EBA403F815: message-id=<74c99d8a-eb8b-4045-ae8e-6d3f6d51b41d@example.org>
    ```



=== "wo_appname_postfix_no_spam_cleanup1"

    ```
	000FA5FD8F: prepend: header From: John Doe <jdoe@example.org> from localhost[127.0.0.1]; from=<jdoe@example.org> to=<jane.doe@example.com> proto=ESMTP helo=<smtp.example.org>: X-NMFP-TRUST: TRUE
    ```



=== "wo_appname_postfix_no_spam_cleanup2"

    ```
	008BB5FD76: prepend: header From: =?UTF-8?q?Cellier_du_P=C3=A9rigord?=??<user@example.com> from localhost[127.0.0.1]; from=<user@example.com> to=<jdoe@example.org> proto=ESMTP helo=<smtp.example.org>: X-NMFP-TRUST: FALSE
    ```



=== "wo_appname_postgrey1"

    ```
	action=greylist, reason=early-retry (10s missing), client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey2"

    ```
	action=greylist, reason=new, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey3"

    ```
	action=greylist, reason=new, client_name=unknown, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey4"

    ```
	action=pass, reason=client AWL, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey5"

    ```
	action=pass, reason=client whitelist, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey6"

    ```
	action=pass, reason=triplet found, client_name=mx.example.org, client_address=1.2.3.4/32, sender=jdoe@example.org, recipient=jane.doe@example.com
    ```



=== "wo_appname_postgrey7"

    ```
	whitelisted: mx.example.org[1.2.3.4/32]
    ```



=== "wo_appname_postgrey8"

    ```
	whitelisted: unknown[1.2.3.4/32]
    ```



=== "wo_appname_qmgr"

    ```
	89BE920002: from=<user@example.com>, size=152518, nrcpt=1 (queue active)
    ```



=== "wo_appname_qmgr2"

    ```
	074955F67C: from=<user@example.com>, size=4303, nrcpt=1 (queue active)
    ```



=== "wo_appname_queued"

    ```
	CA9311112C08: to=<user@example.com>, relay=srv.corp.com[1.1.1.1]:25, delay=8.4, delays=7.6/0/0.31/0.47, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 4TwNdH5zwCz7fxV) 257
    ```



=== "wo_appname_relay"

    ```
	56E28C0007: to=<user@example.com>, relay=1.1.1.1[1.1.1.1]:10025, delay=0.63, delays=0.57/0/0.05/0.01, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as DF82A21108)
    ```



=== "wo_appname_replace_header"

    ```
	95BCC140E40: replace: header From: EXAMPLE <[hola@example.org](mailto:hola@example.org)>: From: [noreply@example.org](mailto:noreply@example.org)
    ```



=== "wo_appname_replace_header_1"

    ```
	95BCC140E40: replace: header From: Example Mailbox <[test@example.org](mailto:test@example.org)>: From: [noreply@example.org](mailto:noreply@example.org)
    ```



=== "wo_appname_replace_header_2"

    ```
	2F46A140256: replace: header From: "Example Help" <help@example.org: From: [help@example.org](mailto:help@example.org)
    ```



=== "wo_appname_sasl_login"

    ```
	warning: unknown[198.51.100.51]: SASL LOGIN authentication failed: authentication failure
    ```



=== "wo_appname_smtp1"

    ```
	175127B26C7: to=<jdoe@example.org>, orig_to=<foreman-proxy>, relay=local, delay=0.05, delays=0.04/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
    ```



=== "wo_appname_smtp2"

    ```
	1176E3F820: to=<jdoe@example.org>, orig_to=<dmarc@example.org>, relay=spamfilter, delay=3.3, delays=0.78/0/0/2.5, dsn=2.0.0, status=sent (delivered via spamfilter service)
    ```



=== "wo_appname_smtp3"

    ```
	7B3643F820: to=<jdoe@example.org>, relay=198.51.100.119[198.51.100.119]:10025, delay=0.08, delays=0.03/0/0.01/0.05, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as 837B35FD17)
    ```



=== "wo_appname_smtp4"

    ```
	05BC43F81E: host mx.example.org[5.6.7.8] said: 421 4.3.0 Upstream error, please check https://example.com/email-routing/postmaster for possible reasons why. yrtPbwx4hZz2 (in reply to end of DATA command)
    ```



=== "wo_appname_smtp5"

    ```
	30D713F81F: host mx.example.org[5.6.7.8] said: 450 4.1.1 <abuse@example.com>: Recipient address rejected: unverified address: Mailbox might be disabled, full, or may not exist on the server. Reason: JFE030050 (in reply to RCPT TO command)
    ```



=== "wo_appname_smtp6"

    ```
	connect to mx.example.org[5.6.7.8]:25: No route to host
    ```



=== "wo_appname_smtp_connection3_timed_out"

    ```
	connect to mail.corp.com[1.1.1.1]:25: Connection timed out 125
    ```



=== "wo_appname_smtp_relay"

    ```
	96887C0006: to=<user@example.com>, relay=host.example.com[1.1.1.1]:25, delay=354776, delays=354775/0/0.9/0.16, dsn=4.3.1, status=deferred (host host.example.com[1.1.1.1] said: 452 4.3.1 Insufficient system storage (in reply to MAIL FROM command))
    ```



=== "wo_appname_smtpd1"

    ```
	021C03F820: filter: RCPT from mx.example.org[192.168.100.124]: <mx.example.org[192.168.100.124]>: Client host triggers FILTER smtp:[127.0.0.1]:10025; from=<jdoe@example.org> to=<jane.doe@example.com> proto=ESMTP helo=<mx.example.com>
    ```



=== "wo_appname_smtpd2"

    ```
	lost connection after BDAT from mx.example.org[192.168.100.124]
    ```



=== "wo_appname_smtpd3"

    ```
	warning: hostname mx.example.org does not resolve to address 5.6.7.8: Name or service not known
    ```



=== "wo_appname_smtpd4"

    ```
	warning: mx.example.org[192.168.100.132]: SASL LOGIN authentication failed: authentication failure, sasl_username=john.doe@exmaple.org
    ```



=== "wo_appname_smtpd_connection"

    ```
	lost connection after AUTH from unknown[1.1.1.1]
    ```



=== "wo_appname_smtpd_connection2"

    ```
	connect from unknown[10.1.1.1] 88
    ```



=== "wo_appname_smtpd_tls"

    ```
	Trusted TLS connection established from host.example.com[1.1.1.1]: TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits)
    ```



=== "wo_appname_smtpd_tls2"

    ```
	Trusted TLS connection established to mx.corp.com[1.1.1.1]:25: TLSv1.3 with cipher TLS_AES_128_GCM_SHA256 (128/128 bits) key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256
    ```



=== "wo_appname_smtpd_tls3"

    ```
	Trusted TLS connection established to 198.51.100.119[198.51.100.119]:10025: TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits) key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256 201
    ```



=== "wo_appname_spamd1"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,HEADER_FROM_DIFFERENT_DOMAINS,HTML_MESSAGE,SPF_HELO_NONE,SPF_PASS,T_KAM_HTML_FONT_INVALID scantime=3.4,size=120289,user=User1,uid=119,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=44944,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd10"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,FORGED_HOTMAIL_RCVD2,FREEMAIL_FROM,HTML_IMAGE_RATIO_04,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=2.7,size=102578,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45880,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd11"

    ```
	spamd: result: . -1 - DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,FREEMAIL_ENVFROM_END_DIGIT,FREEMAIL_FROM,FREEMAIL_REPLYTO_END_DIGIT,HTML_MESSAGE,MIME_HTML_ONLY,RCVD_IN_DNSWL_NONE,SPF_HELO_PASS,SPF_PASS,T_FREEMAIL_DOC_PDF scantime=4.7,size=2252595,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=49594,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd12"

    ```
	spamd: result: . -1 - DMARC_PASS,MIME_HEADER_CTYPE_ONLY,MISSING_DATE,MISSING_MID,SPF_HELO_NONE,SPF_PASS scantime=3.3,size=4260,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=46436,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd13"

    ```
	spamd: result: . -1 - FREEMAIL_ENVFROM_END_DIGIT,FREEMAIL_FROM,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=2.6,size=8094,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=39504,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd14"

    ```
	spamd: result: . -1 - FREEMAIL_FORGED_FROMDOMAIN,FREEMAIL_FROM,HEADER_FROM_DIFFERENT_DOMAINS,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_NONE,SPF_PASS scantime=2.8,size=61589,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=37172,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd15"

    ```
	spamd: result: . -1 - HTML_FONT_LOW_CONTRAST,HTML_IMAGE_RATIO_08,HTML_MESSAGE,LOTS_OF_MONEY,MIME_HTML_MOSTLY,MPART_ALT_DIFF,RCVD_IN_MSPIKE_H4,RCVD_IN_MSPIKE_WL,SPF_HELO_NONE,SPF_PASS scantime=3.3,size=164381,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=56082,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd16"

    ```
	spamd: result: . -1 - HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,HTML_OBFUSCATE_05_10,MIME_HTML_ONLY,SPF_HELO_PASS,SPF_PASS scantime=2.5,size=1572,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=51336,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd17"

    ```
	spamd: result: . -6 - DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_MESSAGE,RCVD_IN_DNSWL_MED,SPF_HELO_PASS,SPF_PASS scantime=2.6,size=7882,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=33278,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd18"

    ```
	spamd: connection from test.com [127.0.0.1]:33620 to port 783, fd 5
    ```



=== "wo_appname_spamd19"

    ```
	spamd: connection from mx.example.org [127.0.0.1]:33620 to port 783, fd 5
    ```



=== "wo_appname_spamd2"

    ```
	spamd: connection from example.org [127.0.0.1]:53684 to port 783, fd 5
    ```



=== "wo_appname_spamd20"

    ```
	spamd: processing message <!&!AAAAAAAAAAAYAAAAAAAAA111111111111111111111111111111111/22222222222222/u47tEBAAAAAA==@example.org> for debian-spamd:118
    ```



=== "wo_appname_spamd21"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:117
    ```



=== "wo_appname_spamd22"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:118
    ```



=== "wo_appname_spamd23"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:118
    ```



=== "wo_appname_spamd24"

    ```
	spamd: processing message <<test-message-id@example.com>> for debian-spamd:117
    ```



=== "wo_appname_spamd3"

    ```
	spamd: result: . -1 - AC_DIV_BONANZA,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H3,RCVD_IN_MSPIKE_WL,SPF_HELO_NONE,SPF_PASS,URI_NOVOWEL scantime=3.2,size=209868,user=User1,uid=117,required_score=5.0,rhost=host.example.com,raddr=127.0.0.1,rport=44702,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd4"

    ```
	spamd: result: . -1 - ANY_BOUNCE_MESSAGE,DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,FORGED_SPF_HELO,HTML_MESSAGE,OOOBOUNCE_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_NONE scantime=2.7,size=14228,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=36236,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd5"

    ```
	spamd: result: . -1 - APOSTROPHE_FROM,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,DKIM_VALID_EF,HTML_FONT_LOW_CONTRAST,HTML_MESSAGE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_PASS scantime=4.9,size=575869,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=41352,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd6"

    ```
	spamd: result: . -1 - DEAR_SOMETHING,DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,HTML_MESSAGE,PDS_BTC_ID,RCVD_IN_DNSWL_LOW,SPF_HELO_NONE,SPF_NONE scantime=5.3,size=468649,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=42678,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd7"

    ```
	spamd: result: . -1 - DEAR_SOMETHING,DMARC_PASS,HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,MIME_HTML_ONLY,RCVD_IN_DNSWL_LOW,SPF_HELO_NONE,SPF_PASS scantime=2.8,size=3254,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45060,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd8"

    ```
	spamd: result: . -1 - DKIMWL_WL_HIGH,DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,FORGED_SPF_HELO,HTML_MESSAGE,RCVD_IN_DNSWL_NONE,RCVD_IN_MSPIKE_H2,SPF_HELO_PASS,SPF_NONE scantime=2.3,size=10467,user=User1,uid=118,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=45920,mid=<test-message-id@example.com>,autolearn=disabled
    ```



=== "wo_appname_spamd9"

    ```
	spamd: result: . -1 - DKIM_INVALID,DKIM_SIGNED,HEADER_FROM_DIFFERENT_DOMAINS,HTML_FONT_LOW_CONTRAST,HTML_MESSAGE,MIME_HTML_ONLY,RCVD_IN_MSPIKE_H2,SPF_HELO_NONE,SPF_PASS,T_REMOTE_IMAGE scantime=2.9,size=65264,user=User1,uid=117,required_score=5.0,rhost=198.51.100.119,raddr=198.51.100.119,rport=33254,mid=<test-message-id@example.com>,autolearn=disabled
    ```



