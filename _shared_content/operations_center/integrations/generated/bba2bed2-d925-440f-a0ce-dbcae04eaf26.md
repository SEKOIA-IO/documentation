
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network intrusion detection system` | AIONIQ identify suspicious behaviors |
| `Network protocol analysis` | AIONIQ analyze traffic protocol |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `malware`, `network` |
| Type | `info` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/docs/xdr/features/detect/rules_catalog) and hunting activities in the [events page](/docs/xdr/features/investigate/events). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/docs/xdr/features/detect/sigma) and to leverage the full potential of the collected data.

=== "malcore_event.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2022-06-03T15:00:20.531Z\",\"detail_wait_time\":18,\"event_type\":\"malware\",\"total_found\":\"3/16\",\"type\":\"malcore\",\"analyzed_clean\":13,\"analyzed_error\":0,\"SHA256\":\"2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c\",\"dest_port\":49804,\"timestamp\":\"2022-06-03T14:59:08.780474+0000\",\"state\":\"Infected\",\"engine_id\":{\"3\":{\"scan_result\":\"CLEAN\",\"id\":\"312a189607571ec2c7544636be405f10889e73d061e0ed77ca0eca97a470838d\",\"threat_details\":\"\"},\"4\":{\"scan_result\":\"INFECTED\",\"id\":\"32f2f45e6d9faf46e6954356a710208d412fac5181f6c641e34cb9956a133684\",\"threat_details\":\"Win32/Exploit.CVE-2022-30190.A trojan\"},\"6\":{\"scan_result\":\"CLEAN\",\"id\":\"4ca73ae4b92fd7ddcda418e6b70ced0481ac2d878c48e61b686d0c9573c331dc\",\"threat_details\":\"\"},\"10\":{\"scan_result\":\"CLEAN\",\"id\":\"a9b912e461cec506780d8ad8e785cca6b233ad7c72335c262b0a4ab189afa713\",\"threat_details\":\"\"},\"13\":{\"scan_result\":\"CLEAN\",\"id\":\"b14014e40c0e672e050ad9c210a68a5303ce7facabae9eb2ee07ddf97dc0da0e\",\"threat_details\":\"\"},\"2\":{\"scan_result\":\"CLEAN\",\"id\":\"0ff95ddb1117d8f36124f6eac406dbbf9f17e3dd89f9bb1bd600f6ad834c25db\",\"threat_details\":\"\"},\"12\":{\"scan_result\":\"CLEAN\",\"id\":\"af6868a2b87b3388a816e09d2b282629ccf883b763b3691368a27fbd6f6cd51a\",\"threat_details\":\"\"},\"1\":{\"scan_result\":\"INFECTED\",\"id\":\"054a20c51cbe9d2cc7d6a237d6cd4e08ab1a67e170b371e632995766d3ba81af\",\"threat_details\":\"Exploit/HTML.CVE-2022-30190.S1841\"},\"14\":{\"scan_result\":\"CLEAN\",\"id\":\"ecc47e2309be9838d6dc2c5157be1a840950e943f5aaca6637afca11516c3eaf\",\"threat_details\":\"\"},\"9\":{\"scan_result\":\"CLEAN\",\"id\":\"95603b80d80fa3e98b6faf07418a55ed0b035d19209e3ad4f1858f6b46fa070a\",\"threat_details\":\"\"},\"15\":{\"scan_result\":\"CLEAN\",\"id\":\"fe665976a02d03734c321007328109ab66823b260a8eea117d2ab49ee9dfd3f1\",\"threat_details\":\"\"},\"7\":{\"scan_result\":\"CLEAN\",\"id\":\"527db072abcf877d4bdcd0e9e4ce12c5d769621aa65dd2f7697a3d67de6cc737\",\"threat_details\":\"\"},\"5\":{\"scan_result\":\"SUSPICIOUS\",\"id\":\"3bfeb615a695c5ebaac5ade948ffae0c3cfec3787d4625e3abb27fa3c2867f53\",\"threat_details\":\"HEUR:Exploit.Script.Generic\"},\"0\":{\"scan_result\":\"CLEAN\",\"id\":\"038e407ba285f0e01dd30c6e4f77ec19bad5ed3dc866a2904ae6bf46baa14b74\",\"threat_details\":\"\"},\"8\":{\"scan_result\":\"CLEAN\",\"id\":\"714eca0a6475fe7d2bf9a24bcae343f657b230ff68acd544b019574f1392de77\",\"threat_details\":\"\"},\"11\":{\"scan_result\":\"CLEAN\",\"id\":\"ad05e0dc742bcd6251af91bd07ef470c699d5aebbb2055520b07021b14d7380c\",\"threat_details\":\"\"}},\"detail_threat_found\":\"Infected : Exploit/HTML.CVE-2022-30190.S1841, Win32/Exploit.CVE-2022-30190.A trojan, HEUR:Exploit.Script.Generic\",\"analyzed_suspicious\":1,\"fileinfo\":{\"tx_id\":0,\"magic\":\"HTML document, ASCII text, with very long lines\",\"gaps\":false,\"md5\":\"16e3fcee85f81ec9e9c75dd13fb08c01\",\"sha256\":\"2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c\",\"file_id\":1,\"sid\":[1100029],\"state\":\"CLOSED\",\"size\":6105,\"stored\":true,\"filename\":\"/exploit.html\"},\"host\":\"network.internal\",\"src_port\":80,\"flow_id\":1686930575880829,\"processing_time\":359,\"file_type_description\":\"Not available\",\"timestamp_analyzed\":\"2022-06-03T15:00:20.531Z\",\"dest_ip\":\"1.2.3.4\",\"reporting_token\":\"No GBOX\",\"severity\":1,\"gcenter\":[\"gcenter-nti.gatewatcher.com\",\"gcenter-nti.gatewatcher.com\"],\"analyzed_other\":0,\"analyzed_infected\":2,\"app_proto\":\"http\",\"detail_scan_time\":341,\"src_ip\":\"9.8.7.6\",\"magic_details\":\"HTML document, ASCII text, with very long lines\",\"proto\":\"TCP\",\"http\":{\"protocol\":\"HTTP/1.1\",\"hostname\":\"www.xmlformats.com\",\"http_content_type\":\"text/html\",\"length\":2485,\"http_user_agent\":\"Mozilla/4.0 (compatible; ms-office; MSOffice 16)\",\"http_method\":\"GET\",\"url\":\"/exploit.html\",\"status\":200},\"timestamp_detected\":\"2022-06-03T14:59:08.780Z\",\"analyzers_up\":16,\"file_type\":\"Not available\",\"in_iface\":\"monvirt\",\"code\":1,\"engines_last_update_date\":\"2022-06-01T21:22:55Z\",\"gcap\":\"gcap-nti.gatewatcher.com\",\"uuid\":\"73a1884d-94a6-4800-9b08-6daa3281ce8f\"}",
        "event": {
            "category": [
                "malware"
            ],
            "kind": "event",
            "severity": 1,
            "type": [
                "info"
            ]
        },
        "@timestamp": "2022-06-03T15:00:20.531000Z",
        "destination": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 49804
        },
        "file": {
            "hash": {
                "md5": "16e3fcee85f81ec9e9c75dd13fb08c01",
                "sha256": "2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c"
            },
            "name": "/exploit.html",
            "size": 6105
        },
        "gatewatcher": {
            "event_type": "malware",
            "flow_id": "1686930575880829",
            "gcap": "gcap-nti.gatewatcher.com",
            "gcenter": [
                "gcenter-nti.gatewatcher.com",
                "gcenter-nti.gatewatcher.com"
            ],
            "malcore": {
                "code": "1",
                "detail_threat_found": "Infected : Exploit/HTML.CVE-2022-30190.S1841, Win32/Exploit.CVE-2022-30190.A trojan, HEUR:Exploit.Script.Generic"
            },
            "reporting_token": "No GBOX",
            "state": "Infected",
            "timestamp_analyzed": "2022-06-03T15:00:20.531Z",
            "timestamp_detected": "2022-06-03T14:59:08.780Z",
            "type": "malcore"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http",
            "transport": "TCP"
        },
        "observer": {
            "hostname": "network.internal",
            "name": "gcap-nti.gatewatcher.com",
            "type": "firewall",
            "version": "0.2"
        },
        "related": {
            "hash": [
                "16e3fcee85f81ec9e9c75dd13fb08c01",
                "2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c"
            ],
            "hosts": [
                "network.internal",
                "www.xmlformats.com"
            ],
            "ip": [
                "1.2.3.4",
                "9.8.7.6"
            ]
        },
        "source": {
            "address": "9.8.7.6",
            "ip": "9.8.7.6",
            "port": 80
        },
        "url": {
            "domain": "www.xmlformats.com",
            "path": "/exploit.html",
            "registered_domain": "xmlformats.com",
            "subdomain": "www",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Outlook",
            "original": "Mozilla/4.0 (compatible; ms-office; MSOffice 16)",
            "os": {
                "name": "Other"
            },
            "version": "2016"
        }
    }
    	
	```


=== "suricata_alert_event.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2022-06-03T14:59:41.373Z\",\"gcenter\":[\"gcenter-sekoia.gatewatcher.com\",\"gcenter-sekoia.gatewatcher.com\"],\"event_type\":\"alert\",\"payload\":\"SFRUUC8xLjEgMjAwIE9LCkRhdGU6IFRodSwgMDIgSnVuIDIwMjIgMjI6Mzc6MjIgR01UClNlcnZlcjogQXBhY2hlLzIuNC40MSAoVWJ1bnR1KQpMYXN0LU1vZGlmaWVkOiBUaHUsIDAyIEp1biAyMDIyIDIyOjMwOjM0IEdNVApFVGFnOiAiMTdkOS01ZTA3ZThkZGI0NTA4LWd6aXAiCkFjY2VwdC1SYW5nZXM6IGJ5dGVzClZhcnk6IEFjY2VwdC1FbmNvZGluZwpDb250ZW50LUVuY29kaW5nOiBnemlwCkNvbnRlbnQtTGVuZ3RoOiAyNDg1CktlZXAtQWxpdmU6IHRpbWVvdXQ9NSwgbWF4PTEwMApDb25uZWN0aW9uOiBLZWVwLUFsaXZlCkNvbnRlbnQtVHlwZTogdGV4dC9odG1sCgp0ZXN0Cg==\",\"packet\":\"CAAnjitsCAAnk+hwCABFAAAoBRhAAD8GMWkKAQHewKg4yABQwow7Z24SQI3k4FAQAfUWzAAA\",\"type\":\"suricata\",\"community_id\":\"1:dGVzdAo=\",\"app_proto\":\"http\",\"src_ip\":\"9.8.7.6\",\"dest_port\":49804,\"alert\":{\"action\":\"allowed\",\"rev\":2,\"signature\":\"ETPRO INFO Observed Suspicious Base64 Encoded Wide String Inbound (exe)\",\"category\":\"Potentially Bad Traffic\",\"gid\":1,\"metadata\":{\"updated_at\":[\"2020_11_17\"],\"created_at\":[\"2020_04_13\"],\"former_category\":[\"HUNTING\"],\"signature_severity\":[\"Informational\"],\"attack_target\":[\"Client_Endpoint\"],\"deployment\":[\"Perimeter\"],\"affected_product\":[\"Windows_XP_Vista_7_8_10_Server_32_64_Bit\"]},\"signature_id\":2841990,\"severity\":2},\"flow\":{\"pkts_toserver\":5,\"bytes_toserver\":798,\"start\":\"2022-06-03T14:59:08.750205+0000\",\"pkts_toclient\":4,\"bytes_toclient\":3052},\"files\":[{\"filename\":\"/exploit.html\",\"state\":\"CLOSED\",\"tx_id\":0,\"sid\":[1100029],\"magic\":\"HTML document, ASCII text, with very long lines\",\"gaps\":false,\"md5\":\"16e3fcee85f81ec9e9c75dd13fb08c01\",\"sha256\":\"2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c\",\"size\":6105,\"stored\":false}],\"proto\":\"TCP\",\"stream\":1,\"host\":\"network.internal\",\"http\":{\"protocol\":\"HTTP/1.1\",\"hostname\":\"www.xmlformats.com\",\"http_content_type\":\"text/html\",\"length\":2485,\"http_user_agent\":\"Mozilla/4.0 (compatible; ms-office; MSOffice 16)\",\"http_method\":\"GET\",\"url\":\"/exploit.html\",\"status\":200},\"timestamp_detected\":\"2022-06-03T14:59:08.780Z\",\"ether\":{\"src_mac\":\"08:00:27:8e:2b:6c\",\"dest_mac\":\"08:00:27:93:e8:70\"},\"src_port\":80,\"flow_id\":1686930575880829,\"payload_printable\":\"HTTP/1.1 200 OK\\r\\nDate: Thu, 02 Jun 2022 22:37:22 GMT\\r\\nServer: Apache/2.4.41 (Ubuntu)\\r\\nLast-Modified: Thu, 02 Jun 2022 22:30:34 GMT\\r\\nETag: \\\"17d9-5e07e8ddb4508-gzip\\\"\\r\\nAccept-Ranges: bytes\\r\\nVary: Accept-Encoding\\r\\nContent-Encoding: gzip\\r\\nContent-Length: 2485\\r\\nKeep-Alive: timeout=5, max=100\\r\\nConnection: Keep-Alive\\r\\nContent-Type: text/html\\r\\n\\r\\n...........Xko........\\n.F&.$VS..]pmYRa.Vd9q.(.........gW......#7....G....s.=.RO.....q..&n.....0.k...|{D.....!6.....V&nB.6.oVap......}7........l..>..{>{..~k.n..f.5]o.....X..k._G....U.....|...\\\\.a.m.f......._.!...c.8.Z..n.0........i..`.:..c[.a..;......_.........gv}.L.1V.G.......o.2,}..C~..w.(,...[..at+..8.~..'.mh1a..y......hVc0.n.iB.en.Z..O.]...l.b..2.b..{|i|._+...o].3}..Wd....3\\\"...!:.............C./.Z.....\\rP$S,.t<Y..m.E.]5Y-...Sx.A..1...[W.@.......kKlb...m.3..n./......c...\\n..@y0.....5.........$ .#..|\\r.......;.w}....`.)..u....U^.....lD...D.#...&...jaT.........@@..Lf..6l.z........p>.s.k..!..r..UI..g...ji^V...,.k..0i...}.!.=.......2.%.@..=u........{'Y@.k.8!.*`... ..c..z.j.u.D.....*......G.ng.U.....@.3U......\\n...$/..!.c.....T..S..tr.$...h......$(....&R...i.U#PL.J{...\\n!E.-9,w.....$%Xh9.U!...6...S`b...C>.i.cW......H...It\\n...B......q.IR....\\n..P&....i.d... .07.]U$tD.R...J4............^....tIT....UaD....g..k.b.......\\rm.VcK....p:....P.Dj...\\nD*0u*..b..(..P...\\\\S..Q*VT'......m.............7B..D./\\\"...gX..\\\".9W....I.=.9......T.%.U....J{b.l.\\r..Q.X.t9U.i)......R.i..V.g.5c..^.,.....&=r..p0SX..E...S5hsSJt..J...'}#8.........R.H.D.(i.TW...^.&..>@v..+sX\\ra..],>I.!%.`l`..,vDvL.....vDwM....,.I.-[3IP.I..GMi.I.MYa..'Z$U]r...... j3CE).NM!.@.!a......T.S.77....k&...P.........8...$..:.A.....+A........a......Mm..*..\\\\..zZ\\\"\\n...D.I.e.....r..9..JD..8.u`vd{..=.)Y.9...\\\\A'.}J...'.A?....)...........U....M5.`....J.&..e.D....N{1.s...d....cZE....\\nG)..8.nq)..G..`..@.T.rgB..B.9>7.@.\\\\&#'EUT...;Xt?...P.%W'.,@(\\r.+Y...4.y~.{d.&xn\\\"...../].....k.m.ZK`..M.lr.....VK.\\\"z&.R+.V.<-..U.\\\"...IU.h%/9....y....T)].f..._.I.X0K.k...|-t...\\\\.d#7.A..J..I.L.H7:.r..%].Ti......(....V-i....2...:...`J...\\\"S\\\"..?I.......w..E....Q.......B.l$.T.E....-......k.u........BQ.#.Tn@.C..x.7.K/...M...},..-L.......~..E.@..o.7.. .!.t....._q.....\\\\........H...Y...MA...`U.8..O..z.J.l#91..\\\".+...Vi..v..k......%.k...0i..u.T.O#A.[j.M...*G*W..s.......V..+.%.......t:..&<....Uz..2.....{....\\\\.{a.H.-.D.QC..]|>3..t5.........9.._n.U..1Ly.....(v.Fm...agn..zs.s=0..........;..U..\\n.........bs...[={.A....oG...7.../.}...yz.>......7......B;.....m\\r.../....F!../O./.n...~~..u$.~....hz..e..n.@(.=.Ui.../.\\\\_-F{..........W....~...g}......W........uWvm..ve1~n...vo_<.....=.......}e.v..gOl.^D{vJ..k_........>......y|.........k.=..W.?}.s.../^......=.4.#=.~..l?.}.}k._.....K>...k....._...:...N........`}C......w.................:.wW...Z.....~.....}.._..%?.W8.....$.R..y...............sCq.....y.....)^e....gS^<z..G...|.G....\\n)p,.|...v7.............LMY._.o.......y.......\",\"packet_info\":{\"linktype\":1},\"in_iface\":\"monvirt\",\"dest_ip\":\"1.2.3.4\",\"timestamp_analyzed\":\"2022-06-03T14:59:41.373Z\",\"gcap\":\"gcap-sekoia.gatewatcher.com\",\"tx_id\":0,\"uuid\":\"525084c9-9a40-4dc9-81fb-27d5efe6b965\",\"severity\":2}",
        "event": {
            "action": "allowed",
            "category": [
                "network"
            ],
            "kind": "alert",
            "severity": 2,
            "type": [
                "info"
            ]
        },
        "@timestamp": "2022-06-03T14:59:41.373000Z",
        "destination": {
            "address": "1.2.3.4",
            "bytes": 3052,
            "ip": "1.2.3.4",
            "packets": 4,
            "port": 49804
        },
        "gatewatcher": {
            "event_type": "alert",
            "flow_id": "1686930575880829",
            "gcap": "gcap-sekoia.gatewatcher.com",
            "gcenter": [
                "gcenter-sekoia.gatewatcher.com",
                "gcenter-sekoia.gatewatcher.com"
            ],
            "timestamp_analyzed": "2022-06-03T14:59:41.373Z",
            "timestamp_detected": "2022-06-03T14:59:08.780Z",
            "type": "suricata"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http",
            "transport": "TCP"
        },
        "observer": {
            "hostname": "network.internal",
            "mac": [
                "08:00:27:8e:2b:6c",
                "08:00:27:93:e8:70"
            ],
            "name": "gcap-sekoia.gatewatcher.com",
            "type": "firewall",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "network.internal",
                "www.xmlformats.com"
            ],
            "ip": [
                "1.2.3.4",
                "9.8.7.6"
            ]
        },
        "rule": {
            "category": "Potentially Bad Traffic",
            "id": "2841990",
            "name": "ETPRO INFO Observed Suspicious Base64 Encoded Wide String Inbound (exe)"
        },
        "source": {
            "address": "9.8.7.6",
            "bytes": 798,
            "ip": "9.8.7.6",
            "packets": 5,
            "port": 80
        },
        "url": {
            "domain": "www.xmlformats.com",
            "path": "/exploit.html",
            "registered_domain": "xmlformats.com",
            "subdomain": "www",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Outlook",
            "original": "Mozilla/4.0 (compatible; ms-office; MSOffice 16)",
            "os": {
                "name": "Other"
            },
            "version": "2016"
        }
    }
    	
	```


=== "suricata_fileinfo_event.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2022-06-03T14:59:41.374Z\",\"gcenter\":[\"gcenter-sekoia.gatewatcher.com\",\"gcenter-sekoia.gatewatcher.com\"],\"event_type\":\"fileinfo\",\"http\":{\"protocol\":\"HTTP/1.1\",\"hostname\":\"www.xmlformats.com\",\"http_content_type\":\"text/html\",\"length\":2485,\"http_user_agent\":\"Mozilla/4.0 (compatible; ms-office; MSOffice 16)\",\"http_method\":\"GET\",\"url\":\"/exploit.html\",\"status\":200},\"host\":\"gcap-sekoia.gatewatcher.com\",\"type\":\"suricata\",\"timestamp_detected\":\"2022-06-03T14:59:08.780Z\",\"fileinfo\":{\"tx_id\":0,\"magic\":\"HTML document, ASCII text, with very long lines\",\"gaps\":false,\"md5\":\"16e3fcee85f81ec9e9c75dd13fb08c01\",\"sha256\":\"2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c\",\"file_id\":1,\"sid\":[1100029],\"state\":\"CLOSED\",\"size\":6105,\"stored\":true,\"filename\":\"/exploit.html\"},\"src_port\":80,\"flow_id\":1686930575880829,\"app_proto\":\"http\",\"in_iface\":\"monvirt\",\"src_ip\":\"9.8.7.6\",\"dest_port\":49804,\"dest_ip\":\"1.2.3.4\",\"timestamp_analyzed\":\"2022-06-03T14:59:41.374Z\",\"gcap\":\"gcap-sekoia.gatewatcher.com\",\"uuid\":\"a2d71147-3283-4136-9dc1-df9beaffd301\",\"proto\":\"TCP\"}",
        "event": {
            "category": [
                "network"
            ],
            "kind": "event",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2022-06-03T14:59:41.374000Z",
        "destination": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 49804
        },
        "file": {
            "hash": {
                "md5": "16e3fcee85f81ec9e9c75dd13fb08c01",
                "sha256": "2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c"
            },
            "name": "/exploit.html",
            "size": 6105
        },
        "gatewatcher": {
            "event_type": "fileinfo",
            "flow_id": "1686930575880829",
            "gcap": "gcap-sekoia.gatewatcher.com",
            "gcenter": [
                "gcenter-sekoia.gatewatcher.com",
                "gcenter-sekoia.gatewatcher.com"
            ],
            "timestamp_analyzed": "2022-06-03T14:59:41.374Z",
            "timestamp_detected": "2022-06-03T14:59:08.780Z",
            "type": "suricata"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http",
            "transport": "TCP"
        },
        "observer": {
            "hostname": "gcap-sekoia.gatewatcher.com",
            "name": "gcap-sekoia.gatewatcher.com",
            "type": "firewall",
            "version": "0.2"
        },
        "related": {
            "hash": [
                "16e3fcee85f81ec9e9c75dd13fb08c01",
                "2c36fbcbac3e57df410f6613180fe572015adba62d0f1bd98c13a1535d64703c"
            ],
            "hosts": [
                "gcap-sekoia.gatewatcher.com",
                "www.xmlformats.com"
            ],
            "ip": [
                "1.2.3.4",
                "9.8.7.6"
            ]
        },
        "source": {
            "address": "9.8.7.6",
            "ip": "9.8.7.6",
            "port": 80
        },
        "url": {
            "domain": "www.xmlformats.com",
            "path": "/exploit.html",
            "registered_domain": "xmlformats.com",
            "subdomain": "www",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Outlook",
            "original": "Mozilla/4.0 (compatible; ms-office; MSOffice 16)",
            "os": {
                "name": "Other"
            },
            "version": "2016"
        }
    }
    	
	```


=== "suricata_http_event.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2022-06-03T14:59:41.378Z\",\"gcenter\":[\"gcenter-sekoia.gatewatcher.com\",\"gcenter-sekoia.gatewatcher.com\"],\"event_type\":\"http\",\"type\":\"suricata\",\"community_id\":\"1:dGVzdAo=\",\"src_ip\":\"9.8.7.6\",\"dest_port\":80,\"proto\":\"TCP\",\"http\":{\"content_type\":\"text/html\",\"hostname\":\"www.xmlformats.com\",\"http_content_type\":\"text/html\",\"connection\":\"Keep-Alive\",\"authorization\":\"Bearer\",\"length\":0,\"server\":\"Apache/2.4.41 (Ubuntu)\",\"url\":\"/exploit.html\",\"http_user_agent\":\"Microsoft Office Existence Discovery\",\"date\":\"Thu, 02 Jun 2022 22:37:22 GMT\",\"protocol\":\"HTTP/1.1\",\"http_parsed_user_agent\":{\"os_name\":\"Other\",\"os_full\":\"Other\",\"name\":\"Other\",\"device\":\"Other\",\"os\":\"Other\"},\"content_length\":\"6105\",\"last_modified\":\"Thu, 02 Jun 2022 22:30:34 GMT\",\"vary\":\"Accept-Encoding\",\"http_method\":\"HEAD\",\"status\":200},\"host\":\"gcap-sekoia.gatewatcher.com\",\"timestamp_detected\":\"2022-06-03T14:59:08.833Z\",\"ether\":{\"src_mac\":\"00:17:a4:77:09:20\",\"dest_mac\":\"a0:36:9f:0f:b1:70\"},\"src_port\":49804,\"flow_id\":1686930575880829,\"in_iface\":\"monvirt\",\"dest_ip\":\"1.2.3.4\",\"timestamp_analyzed\":\"2022-06-03T14:59:41.378Z\",\"metadata\":{\"flowbits\":[\"Office.UA\"]},\"gcap\":\"gcap-sekoia.gatewatcher.com\",\"tx_id\":4,\"uuid\":\"4f1bd378-9439-4c1c-ab1d-4b3ba6c22b87\"}",
        "event": {
            "category": [
                "network"
            ],
            "kind": "event",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2022-06-03T14:59:41.378000Z",
        "destination": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 80
        },
        "gatewatcher": {
            "event_type": "http",
            "flow_id": "1686930575880829",
            "gcap": "gcap-sekoia.gatewatcher.com",
            "gcenter": [
                "gcenter-sekoia.gatewatcher.com",
                "gcenter-sekoia.gatewatcher.com"
            ],
            "timestamp_analyzed": "2022-06-03T14:59:41.378Z",
            "timestamp_detected": "2022-06-03T14:59:08.833Z",
            "type": "suricata"
        },
        "http": {
            "request": {
                "method": "HEAD"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "transport": "TCP"
        },
        "observer": {
            "hostname": "gcap-sekoia.gatewatcher.com",
            "mac": [
                "00:17:a4:77:09:20",
                "a0:36:9f:0f:b1:70"
            ],
            "name": "gcap-sekoia.gatewatcher.com",
            "type": "firewall",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "gcap-sekoia.gatewatcher.com",
                "www.xmlformats.com"
            ],
            "ip": [
                "1.2.3.4",
                "9.8.7.6"
            ]
        },
        "source": {
            "address": "9.8.7.6",
            "ip": "9.8.7.6",
            "port": 49804
        },
        "url": {
            "domain": "www.xmlformats.com",
            "path": "/exploit.html",
            "registered_domain": "xmlformats.com",
            "subdomain": "www",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Other",
            "original": "Microsoft Office Existence Discovery",
            "os": {
                "name": "Other"
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`dns.id` | `keyword` | The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.question.type` | `keyword` | The type of record being queried. |
|`dns.type` | `keyword` | The type of DNS event captured, query or answer. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.size` | `long` | File size in bytes. |
|`gatewatcher.event_type` | `keyword` | Type of event |
|`gatewatcher.flow_id` | `keyword` | Identifier of the flow |
|`gatewatcher.gcap` | `keyword` | Name of the gcap |
|`gatewatcher.gcenter` | `keyword` | Name of the associated gcenter |
|`gatewatcher.malcore.code` | `keyword` | Return code of the malcore analysis |
|`gatewatcher.malcore.detail_threat_found` | `keyword` | Type of the detected threat |
|`gatewatcher.malcore.file` | `keyword` | Identifier of the file |
|`gatewatcher.malcore.magic` | `keyword` | The magic number of the executable of the malware |
|`gatewatcher.malcore.replica` | `keyword` | Analysis is a replica of another previous one |
|`gatewatcher.nb_rescans` | `long` | Number of retroact analysis |
|`gatewatcher.reporting_token` | `keyword` | Token used by Gbox |
|`gatewatcher.retroact` | `keyword` | Analysis result per retroact |
|`gatewatcher.state` | `keyword` | Analysis result |
|`gatewatcher.timestamp_analyzed` | `keyword` | Timestamp of the alert processing by gcenter |
|`gatewatcher.timestamp_detected` | `keyword` | Timestamp of the file collection by gcap |
|`gatewatcher.type` | `keyword` | Type of analysis |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`http.version` | `keyword` | HTTP version. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.mac` | `keyword` | MAC addresses of the observer. |
|`observer.name` | `keyword` | Custom name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.version` | `keyword` | Observer version. |
|`rule.category` | `keyword` | Rule category |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`rule.version` | `keyword` | Rule version |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.ip` | `ip` | IP address of the source. |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.port` | `long` | Port of the source. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/GateWatcher/aioniq).