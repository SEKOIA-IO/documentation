
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network intrusion detection system` | AIONIQ identify suspicious behaviors |
| `Network protocol analysis` | AIONIQ analyze traffic protocol |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert` |
| Category | `malware`, `network` |
| Type | `info` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "codebreaker.json"

    ```json
	
    {
        "message": "{\"event_type\":\"powershell\",\"scores\":{\"analysis\":1890,\"analysis_detailed\":{\"CharInt\":0,\"InvokeWebRequest\":0,\"FmtStr\":0,\"WebClientInvokation\":0,\"StrReplace\":0,\"StrJoin\":0,\"SetContent\":0,\"StreamWriter\":0,\"SystemIOFile\":0,\"StreamReader\":0,\"InvokeRestMethod\":0,\"AddContent\":0,\"StartBitsTransfer\":0,\"InvokeExpression\":0,\"GetContent\":0,\"StrCat\":370,\"Base64\":1520},\"proba_obfuscated\":1.0},\"timestamp_detected\":\"2023-03-22T10:30:37.145Z\",\"uuid\":\"8906e477-02b5-4ada-abaa-67b2d41f204a\",\"severity\":1,\"type\":\"codebreaker\",\"src_ip\":\"1.1.1.1\",\"state\":\"Exploit\",\"dest_port\":\"35444\",\"dest_ip\":\"2.2.2.2\",\"flow_id\":\"2157601933358692\",\"gcap\":\"gcap-xxxxxxxxxx.domain.local\",\"@timestamp\":\"2023-03-22T10:32:50.269Z\",\"timestamp_analyzed\":\"2023-03-22T10:32:50.269Z\",\"src_port\":\"4242\",\"file_id\":\"03-22-2023T10:32:45_772669089795425e9ad63823ea1e7ac3_gcap-xxxxxxxx.domain.local\",\"sub_type\":\"powershell\",\"SHA256\":\"efc9380fee13f9accf1cbc2f2bb02ae430cf39d4fbfe1d766f65b500b571ca29\",\"MD5\":\"60b656e17bec0a97f5638790c78a3124\",\"@version\":\"1\",\"gcenter\":\"gcenter-xxxxxxxxxx.domain.local\"}",
        "event": {
            "category": [
                "network"
            ],
            "module": "powershell",
            "severity": 1
        },
        "@timestamp": "2023-03-22T10:30:37.145000Z",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 35444
        },
        "gatewatcher": {
            "event_type": "powershell",
            "flow_id": "2157601933358692",
            "gcap": "gcap-xxxxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxxxx.domain.local",
            "sample_id": "03-22-2023T10:32:45_772669089795425e9ad63823ea1e7ac3_gcap-xxxxxxxx.domain.local",
            "scores": {
                "analysis": 1890,
                "analysis_detailed": "{\"AddContent\":0,\"Base64\":1520,\"CharInt\":0,\"FmtStr\":0,\"GetContent\":0,\"InvokeExpression\":0,\"InvokeRestMethod\":0,\"InvokeWebRequest\":0,\"SetContent\":0,\"StartBitsTransfer\":0,\"StrCat\":370,\"StrJoin\":0,\"StrReplace\":0,\"StreamReader\":0,\"StreamWriter\":0,\"SystemIOFile\":0,\"WebClientInvokation\":0}",
                "proba_obfuscated": 1.0
            },
            "state": "Exploit",
            "sub_type": "powershell",
            "timestamp_analyzed": "2023-03-22T10:32:50.269Z",
            "timestamp_detected": "2023-03-22T10:30:37.145Z",
            "type": "codebreaker"
        },
        "observer": {
            "name": "gcap-xxxxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 4242
        }
    }
    	
	```


=== "dga.json"

    ```json
	
    {
        "message": "{\"event_type\":\"dga\",\"domain_name\":\"pgoadcmgqfacj.com\",\"timestamp_detected\":\"2023-03-22T10:25:54.903Z\",\"uuid\":\"4e4b3104-06ba-4277-899e-149a74a0671c\",\"severity\":1,\"type\":\"machine_learning\",\"probability\":0.9999731546766107,\"dest_port\":53,\"gcap\":\"gcap-xxxxxxxx.domain.local\",\"dest_ip\":\"2.2.2.2\",\"flow_id\":729468278572,\"src_ip\":\"1.1.1.1\",\"@timestamp\":\"2023-03-22T10:46:08.487Z\",\"@version\":\"1\",\"matched_event\":\"041b2ed4-a5e0-4814-8bdc-7522b6d5464f\",\"timestamp_analyzed\":\"2023-03-22T10:46:08.487Z\",\"gcenter\":\"gcenter-xxxxxx.domain.local\",\"src_port\":1294}",
        "event": {
            "category": [
                "network"
            ],
            "module": "dga",
            "severity": 1
        },
        "@timestamp": "2023-03-22T10:25:54.903000Z",
        "destination": {
            "address": "pgoadcmgqfacj.com",
            "domain": "pgoadcmgqfacj.com",
            "ip": "2.2.2.2",
            "port": 53,
            "registered_domain": "pgoadcmgqfacj.com",
            "top_level_domain": "com"
        },
        "gatewatcher": {
            "event_type": "dga",
            "flow_id": "729468278572",
            "gcap": "gcap-xxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxx.domain.local",
            "matched_event": "041b2ed4-a5e0-4814-8bdc-7522b6d5464f",
            "probability": 0.9999731546766107,
            "timestamp_analyzed": "2023-03-22T10:46:08.487Z",
            "timestamp_detected": "2023-03-22T10:25:54.903Z",
            "type": "machine_learning"
        },
        "observer": {
            "name": "gcap-xxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "pgoadcmgqfacj.com"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 1294
        }
    }
    	
	```


=== "malcore.json"

    ```json
	
    {
        "message": "{\"timestamp\":\"2023-03-22T10:35:22.615360+0000\",\"analyzed_infected\":10,\"detail_threat_found\":\"Infected : Script.SWF.CVE-2014-0515+.C107 (B), Exp.SWF.Angler.D, Script.SWF.CVE-2014-0515+.C107, SWF/Exploit.ExKit.J trojan, Exploit.SWF.Agent.ja, Exploit.Agent.Script.371, Exploit.Swf.Agent.dvtnkm, Script.SWF.CVE-2014-0515++.C118, EXP/FLASH.Pubenush.E.Gen, Exploit.SWF\",\"timestamp_detected\":\"2023-03-22T10:35:22.615Z\",\"uuid\":\"2103a99c-549e-49b7-bbef-68459e6cc44e\",\"severity\":1,\"dest_port\":19609,\"detail_wait_time\":320265,\"host\":\"gcap-xxxxxxxxx.domain.local\",\"dest_ip\":\"2.2.2.2\",\"timestamp_analyzed\":\"2023-03-22T10:53:13.408Z\",\"@timestamp\":\"2023-03-22T10:53:13.408Z\",\"file_type_description\":\"Macromedia Flash Player\",\"fileinfo\":{\"sha256\":\"350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4\",\"file_id\":379,\"magic\":\"Macromedia Flash data (compressed), version 14\",\"tx_id\":1,\"state\":\"CLOSED\",\"filename\":\"/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust\",\"sid\":[1100020],\"stored\":true,\"md5\":\"67ca9a31f220bc7b68f203c07ad668b9\",\"gaps\":false,\"size\":77068},\"analyzed_suspicious\":0,\"analyzers_up\":16,\"app_proto\":\"http\",\"engines_last_update_date\":\"2023-03-08T19:03:00Z\",\"total_found\":\"10/16\",\"file_type\":\"application/x-shockwave-flash\",\"detail_scan_time\":13425,\"processing_time\":333690,\"SHA256\":\"350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4\",\"gcenter\":\"gcenter-xxxxxxxx.domain.local\",\"analyzed_clean\":5,\"event_type\":\"malware\",\"http\":{\"http_method\":\"GET\",\"http_port\":8080,\"protocol\":\"HTTP/1.1\",\"status\":200,\"hostname\":\"tsevid-synonymi.justdanceatsea.com\",\"url\":\"/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust\",\"length\":77068,\"http_content_type\":\"application/x-shockwave-flash\",\"http_user_agent\":\"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)\",\"http_refer\":\"http://tsevid-synonymi.justdanceatsea.com:8080/ndf4xx22ci.php\"},\"type\":\"malcore\",\"in_iface\":\"monvirt\",\"src_ip\":\"1.1.1.1\",\"state\":\"Infected\",\"gcap\":\"gcap-xxxxxxxx.domain.local\",\"flow_id\":1910314914537014,\"reporting_token\":\"No GBOX\",\"src_port\":8080,\"analyzed_other\":1,\"engine_id\":{\"4\":{\"id\":\"32f2f45e6d9faf46e6954356a710208d412fac5181f6c641e34cb9956a133684\",\"threat_details\":\"SWF/Exploit.ExKit.J trojan\",\"scan_result\":\"INFECTED\"},\"1\":{\"id\":\"054a20c51cbe9d2cc7d6a237d6cd4e08ab1a67e170b371e632995766d3ba81af\",\"threat_details\":\"\",\"scan_result\":\"CLEAN\"},\"9\":{\"id\":\"95603b80d80fa3e98b6faf07418a55ed0b035d19209e3ad4f1858f6b46fa070a\",\"threat_details\":\"Script.SWF.CVE-2014-0515++.C118\",\"scan_result\":\"INFECTED\"},\"14\":{\"id\":\"ecc47e2309be9838d6dc2c5157be1a840950e943f5aaca6637afca11516c3eaf\",\"threat_details\":\"\",\"scan_result\":\"CLEAN\"},\"8\":{\"id\":\"714eca0a6475fe7d2bf9a24bcae343f657b230ff68acd544b019574f1392de77\",\"threat_details\":\"Exploit.Swf.Agent.dvtnkm\",\"scan_result\":\"INFECTED\"},\"7\":{\"id\":\"527db072abcf877d4bdcd0e9e4ce12c5d769621aa65dd2f7697a3d67de6cc737\",\"threat_details\":\"Exploit.Agent.Script.371\",\"scan_result\":\"INFECTED\"},\"2\":{\"id\":\"0ff95ddb1117d8f36124f6eac406dbbf9f17e3dd89f9bb1bd600f6ad834c25db\",\"threat_details\":\"Exp.SWF.Angler.D\",\"scan_result\":\"INFECTED\"},\"11\":{\"id\":\"ad05e0dc742bcd6251af91bd07ef470c699d5aebbb2055520b07021b14d7380c\",\"threat_details\":\"\",\"scan_result\":\"NOT_SCANNED\"},\"12\":{\"id\":\"af6868a2b87b3388a816e09d2b282629ccf883b763b3691368a27fbd6f6cd51a\",\"threat_details\":\"EXP/FLASH.Pubenush.E.Gen\",\"scan_result\":\"INFECTED\"},\"10\":{\"id\":\"a9b912e461cec506780d8ad8e785cca6b233ad7c72335c262b0a4ab189afa713\",\"threat_details\":\"\",\"scan_result\":\"CLEAN\"},\"3\":{\"id\":\"312a189607571ec2c7544636be405f10889e73d061e0ed77ca0eca97a470838d\",\"threat_details\":\"Script.SWF.CVE-2014-0515+.C107\",\"scan_result\":\"INFECTED\"},\"6\":{\"id\":\"4ca73ae4b92fd7ddcda418e6b70ced0481ac2d878c48e61b686d0c9573c331dc\",\"threat_details\":\"\",\"scan_result\":\"CLEAN\"},\"13\":{\"id\":\"b14014e40c0e672e050ad9c210a68a5303ce7facabae9eb2ee07ddf97dc0da0e\",\"threat_details\":\"\",\"scan_result\":\"CLEAN\"},\"0\":{\"id\":\"038e407ba285f0e01dd30c6e4f77ec19bad5ed3dc866a2904ae6bf46baa14b74\",\"threat_details\":\"Script.SWF.CVE-2014-0515+.C107 (B)\",\"scan_result\":\"INFECTED\"},\"5\":{\"id\":\"3bfeb615a695c5ebaac5ade948ffae0c3cfec3787d4625e3abb27fa3c2867f53\",\"threat_details\":\"Exploit.SWF.Agent.ja\",\"scan_result\":\"INFECTED\"},\"15\":{\"id\":\"fe665976a02d03734c321007328109ab66823b260a8eea117d2ab49ee9dfd3f1\",\"threat_details\":\"Exploit.SWF\",\"scan_result\":\"INFECTED\"}},\"proto\":\"TCP\",\"code\":1,\"analyzed_error\":0,\"@version\":\"1\",\"magic_details\":\"Macromedia Flash data (compressed), version 14\"}",
        "event": {
            "category": [
                "malware"
            ],
            "module": "malware",
            "severity": 1,
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-03-22T10:35:22.615000Z",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 19609
        },
        "file": {
            "hash": {
                "md5": "67ca9a31f220bc7b68f203c07ad668b9",
                "sha256": "350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4"
            },
            "name": "/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust",
            "size": 77068
        },
        "gatewatcher": {
            "event_type": "malware",
            "fileinfo": "{\"file_id\":379,\"filename\":\"/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust\",\"gaps\":false,\"magic\":\"Macromedia Flash data (compressed), version 14\",\"md5\":\"67ca9a31f220bc7b68f203c07ad668b9\",\"sha256\":\"350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4\",\"sid\":[1100020],\"size\":77068,\"state\":\"CLOSED\",\"stored\":true,\"tx_id\":1}",
            "filemagic": "Macromedia Flash data (compressed), version 14",
            "flow_id": "1910314914537014",
            "gcap": "gcap-xxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxx.domain.local",
            "malcore": {
                "code": "1",
                "detail_threat_found": "Infected : Script.SWF.CVE-2014-0515+.C107 (B), Exp.SWF.Angler.D, Script.SWF.CVE-2014-0515+.C107, SWF/Exploit.ExKit.J trojan, Exploit.SWF.Agent.ja, Exploit.Agent.Script.371, Exploit.Swf.Agent.dvtnkm, Script.SWF.CVE-2014-0515++.C118, EXP/FLASH.Pubenush.E.Gen, Exploit.SWF"
            },
            "reporting_token": "No GBOX",
            "state": "Infected",
            "timestamp_analyzed": "2023-03-22T10:53:13.408Z",
            "timestamp_detected": "2023-03-22T10:35:22.615Z",
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
            "hostname": "gcap-xxxxxxxxx.domain.local",
            "name": "gcap-xxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hash": [
                "350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4",
                "67ca9a31f220bc7b68f203c07ad668b9"
            ],
            "hosts": [
                "gcap-xxxxxxxxx.domain.local",
                "tsevid-synonymi.justdanceatsea.com"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 8080
        },
        "url": {
            "domain": "tsevid-synonymi.justdanceatsea.com",
            "path": "/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust",
            "registered_domain": "justdanceatsea.com",
            "subdomain": "tsevid-synonymi",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "IE",
            "original": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
            "os": {
                "name": "Windows",
                "version": "7"
            },
            "version": "8.0"
        }
    }
    	
	```


=== "retrohunt.json"

    ```json
	
    {
        "message": "{\"external_links\":[{\"url\":\"https://urlhaus.abuse.ch/url/2269068/\",\"source_name\":\"URLHaus Abuse.ch\"}],\"relations\":[\"0e3cc27b-7999-48ce-8484-dc12b325a355\"],\"description\":\"IOC matching first tests\",\"event_type\":\"retrohunt\",\"kill_chain_phases\":[],\"timestamp_detected\":\"2023-06-09T14:08:46.845Z\",\"ioc_type\":\"Host\",\"severity\":1,\"community_id\":\"1:x0uuTl0mYnN1nwngep7+A4VH38I=\",\"ioc_creation_date\":\"2023-06-12T10:00:35+00:00\",\"targeted_countries\":[],\"ioc_value\":\"im.a.very.bad.doma.in\",\"dest_ip\":\"2.2.2.2\",\"vulnerabilities\":[],\"matched_event\":\"bd7686c8-20db-427e-941d-844a5ecfe559\",\"risk\":\"Suspicious\",\"uuid\":\"416f35ad-b954-4b6a-a886-987b826bb7f4\",\"meta_data\":{\"ssdeep\":\"1536:87vbq1lGAXSEYQjbChaAU2yU23M51DjZgSQAvcYkFtZTjzBht5:8D+CAXFYQChaAUk5ljnQssL\",\"cwe\":[],\"descriptions\":[],\"tslh\":\"T16D7312E017B517CC1371A8353BED205E9128223972AE35302E97528DF957703BAB2DBE\",\"filetype\":\"ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux)\",\"size\":78.3984375,\"usageMode\":\"hunting\"},\"flow_id\":841376349480333,\"matched_event_type\":\"alert\",\"ioc_updated_date\":\"2023-06-12T10:00:35+00:00\",\"targeted_platforms\":[\"linux\"],\"signature\":\"RetroHunt - Host - malware/Unknown - Hajime - GW Lab Test - 00100035-1206-2023-cbf5-08330f0d5bc0\",\"ioc_tags\":[\"trojan.generickd.34055387 (b)\",\"linux/hajime.a trojan\",\"e32/agent.cd\",\"linux.hajime.bc\",\"backdoor.hajime.linux.129\",\"linux/hajime.75930\",\"unix.malware.agent-6626471-0\",\"linux/hajime.nsnlw\",\"hajime\",\"elf.mirai.43048.gc\",\"trojan.elfarm32.hajime.fbhtfi\",\"trojan.linux.hajime\",\"trojan.generickd.34055387\"],\"@version\":\"1\",\"type\":\"cti\",\"targeted_organizations\":[],\"campaigns\":[],\"categories\":[\"malware\"],\"src_port\":55614,\"gcenter\":\"gcenter-xxxxxxxxxxxxxxxxx.domain.local\",\"case_id\":\"00100035-1206-2023-edb6-b38911f8ba0c\",\"dest_port\":80,\"usage_mode\":\"hunting\",\"timestamp_package\":\"2023-06-12T10:00:35.012874+0000\",\"src_ip\":\"1.1.1.1\",\"ttp\":[],\"tlp\":\"green\",\"probability\":0.5,\"gcap\":\"gcap-xxxxxxxxxxxxxxxx.domain.local\",\"@timestamp\":\"2023-06-12T10:12:39.001Z\",\"timestamp_analyzed\":\"2023-06-12T10:12:39.001Z\",\"families\":[\"Hajime\"],\"ioc_id\":\"00100035-1206-2023-cbf5-08330f0d5bc0\",\"targeted_sectors\":[],\"threat_actor\":[\"GW Lab Test\"],\"matched_app_proto\":\"http\"}",
        "event": {
            "category": [
                "network"
            ],
            "module": "retrohunt",
            "severity": 1
        },
        "@timestamp": "2023-06-09T14:08:46.845000Z",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 80
        },
        "gatewatcher": {
            "campaigns": [],
            "case_id": "00100035-1206-2023-edb6-b38911f8ba0c",
            "categories": [
                "malware"
            ],
            "description": "IOC matching first tests",
            "event_type": "retrohunt",
            "external_links": [
                "{\"source_name\":\"URLHaus Abuse.ch\",\"url\":\"https://urlhaus.abuse.ch/url/2269068/\"}"
            ],
            "families": [
                "Hajime"
            ],
            "flow_id": "841376349480333",
            "gcap": "gcap-xxxxxxxxxxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxxxxxxxxxxx.domain.local",
            "ioc_creation_date": "2023-06-12T10:00:35+00:00",
            "ioc_id": "00100035-1206-2023-cbf5-08330f0d5bc0",
            "ioc_tags": [
                "backdoor.hajime.linux.129",
                "e32/agent.cd",
                "elf.mirai.43048.gc",
                "hajime",
                "linux.hajime.bc",
                "linux/hajime.75930",
                "linux/hajime.a trojan",
                "linux/hajime.nsnlw",
                "trojan.elfarm32.hajime.fbhtfi",
                "trojan.generickd.34055387",
                "trojan.generickd.34055387 (b)",
                "trojan.linux.hajime",
                "unix.malware.agent-6626471-0"
            ],
            "ioc_type": "Host",
            "ioc_updated_date": "2023-06-12T10:00:35+00:00",
            "ioc_value": "im.a.very.bad.doma.in",
            "kill_chain_phases": [],
            "matched_event": "bd7686c8-20db-427e-941d-844a5ecfe559",
            "matched_event_type": "alert",
            "meta_data": "{\"cwe\":[],\"descriptions\":[],\"filetype\":\"ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux)\",\"size\":78.3984375,\"ssdeep\":\"1536:87vbq1lGAXSEYQjbChaAU2yU23M51DjZgSQAvcYkFtZTjzBht5:8D+CAXFYQChaAUk5ljnQssL\",\"tslh\":\"T16D7312E017B517CC1371A8353BED205E9128223972AE35302E97528DF957703BAB2DBE\",\"usageMode\":\"hunting\"}",
            "probability": 0.5,
            "relations": [
                "0e3cc27b-7999-48ce-8484-dc12b325a355"
            ],
            "risk": "Suspicious",
            "signature": "RetroHunt - Host - malware/Unknown - Hajime - GW Lab Test - 00100035-1206-2023-cbf5-08330f0d5bc0",
            "targeted_countries": [],
            "targeted_organizations": [],
            "targeted_platforms": [
                "linux"
            ],
            "targeted_sectors": [],
            "threat_actor": [
                "GW Lab Test"
            ],
            "timestamp_analyzed": "2023-06-12T10:12:39.001Z",
            "timestamp_detected": "2023-06-09T14:08:46.845Z",
            "timestamp_package": "2023-06-12T10:00:35.012874+0000",
            "tlp": "green",
            "ttp": [],
            "type": "cti",
            "usage_mode": "hunting",
            "vulnerabilities": []
        },
        "observer": {
            "name": "gcap-xxxxxxxxxxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 55614
        }
    }
    	
	```


=== "sigflow-alert.json"

    ```json
	
    {
        "message": "{\"event_type\":\"alert\",\"http\":{\"url\":\"/bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll\",\"protocol\":\"HTTP/1.1\",\"hostname\":\"www.devyatinskiy.ru\",\"length\":0,\"http_method\":\"GET\"},\"timestamp_detected\":\"2023-03-22T10:25:55.690Z\",\"uuid\":\"fd5ba8ea-e263-426d-b4b2-a16521ae09b1\",\"packet_info\":{\"linktype\":1},\"severity\":1,\"in_iface\":\"monvirt\",\"src_ip\":\"1.1.1.1\",\"host\":\"gcap-xxxxxxxx.domain.local\",\"dest_ip\":\"2.2.2.2\",\"flow_id\":1408237495862400,\"dest_port\":16122,\"@timestamp\":\"2023-03-22T10:44:08.001Z\",\"timestamp_analyzed\":\"2023-03-22T10:44:08.001Z\",\"gcap\":\"gcap-xxxxxxx.domain.local\",\"type\":\"suricata\",\"src_port\":8550,\"metadata\":{\"flowbits\":[\"min.gethttp\",\"ETPROtxtminhead\",\"http.dottedquadhost.dll\"]},\"community_id\":\"1:hEBuGl9msx7YJtg3Tb/+Gf+a1VI=\",\"app_proto\":\"http\",\"packet\":\"kOK6pqSQkOK6pqSRCABFAAC7Uz1AAEAGPT4py4AkHxzgtiFmPvokcIbSnp074oAYAGsSTgAAAQEICmgi0xNoItMTR0VUIC9ic2IvZGVidWdub3Nzby9pbmRleC5waHA/Tj1HTy1HTy1HQURHRVQtUEMtaW5zcGVjdG9yLWdhZGdldCUyMD0lMjAlMjAlMjAlMjBJbmljaWFyJTdCNjklN0QgSFRUUC8xLjENCkhvc3Q6IHd3dy5kZXZ5YXRpbnNraXkucnUNCg0K\",\"proto\":\"TCP\",\"stream\":1,\"flow\":{\"bytes_toclient\":90364,\"bytes_toserver\":3084,\"pkts_toserver\":19,\"pkts_toclient\":66,\"start\":\"2023-03-22T10:25:55.345216+0000\"},\"tx_id\":5,\"ether\":{\"dest_mac\":\"90:e2:ba:a6:a4:90\",\"src_mac\":\"90:e2:ba:a6:a4:91\"},\"payload\":\"R0VUIC9kb3dubG9hZC9RanRHRGx0bWNlLzE2MDgyMDE2dmVjTzdPa0wzeUxQSUNsZW96aWJLRS52YnM/ZHNpZD1ndjVucTMuNDAwYjg2YzcxOTZmOWU4Y2NkZTM1MzcwZWIwYTU0Yjkmc2Jzcj0yZjViMmRmMGFlMGE4Yzc1NTFjN2RmMGJjNDZhOWQ3OTk4MCZsZ2ZwPTMwMDAgSFRUUC8xLjENCkFjY2VwdDogdGV4dC9odG1sLCBhcHBsaWNhdGlvbi94aHRtbCt4bWwsICovKg0KQWNjZXB0LUxhbmd1YWdlOiBlbi1VUw0KVXNlci1BZ2VudDogTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgVHJpZGVudC83LjA7IHJ2OjExLjApIGxpa2UgR2Vja28NCkFjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZQ0KSG9zdDogZGM1MjQuNHNoYXJlZC5jb20NCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkNvb2tpZTogZGF5MWhvc3Q9aA0KDQpHRVQgL3dlYi9jZG4vcG9wdWxhci9kb3dubG9hZC9RanRHRGx0bWNlP2NvbnREaXNwPWF0dGFjaG1lbnQlM0IrZmlsZW5hbWUlM0QlMjIxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMlMjIlM0IrZmlsZW5hbWUqJTNEdXRmLTglMjclMjcxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMmY29udFR5cGU9QVBQTElDQVRJT04lMkZPQ1RFVC1TVFJFQU0mY2RuaD03YTc0NTUzYTA1N2VhNTVmYzU2OGI4MGU2MGNkN2ZhMiZkM2M9ZmRzUWp0R0RsdG1jZSUzRElOSVRJQUxJWkVEJTNCK2RvbWFpbiUzRC40c2hhcmVkLmNvbSUzQitleHBpcmVzJTNEV2VkJTJDKzE3LUF1Zy0yMDE2KzAxJTNBMzYlM0E0NCtHTVQlM0IrcGF0aCUzRCUyRiBIVFRQLzEuMQ0KQWNjZXB0OiB0ZXh0L2h0bWwsIGFwcGxpY2F0aW9uL3hodG1sK3htbCwgKi8qDQpBY2NlcHQtTGFuZ3VhZ2U6IGVuLVVTDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0OyBUcmlkZW50LzcuMDsgcnY6MTEuMCkgbGlrZSBHZWNrbw0KQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlDQpDb29raWU6IGRheTFob3N0PWgNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkhvc3Q6IGNkbmZpbGVzLjRzaGFyZWQuY29tDQoNCkdFVCAvYTM1bmV3L3c3LnR4dCBIVFRQLzEuMQ0KSG9zdDogNjUuMTgxLjEyNS4xOTMNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9hMzVuZXcvYXc3LnRpZmYgSFRUUC8xLjENCkhvc3Q6IDY1LjE4MS4xMjUuMTkzDQoNCkdFVCAvYnNiL2luZmVjdHMvaW5kZXgucGhwP049R08tR08tR0FER0VULVBDLWluc3BlY3Rvci1nYWRnZXQlMjA9JTIwJTIwJTIwJTIwV2luZG93cyUyMDclMjBIb21lJTIwUHJlbWl1bSUyMCUyMCUyMCUyMD0lMjAlMjAlMjAlMjAlMjAlMjAlMjBOL0EgSFRUUC8xLjENCkhvc3Q6IHd3dy5kZXZ5YXRpbnNraXkucnUNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9ic2IvZGVidWdub3Nzby9pbmRleC5waHA/Tj1HTy1HTy1HQURHRVQtUEMtaW5zcGVjdG9yLWdhZGdldCUyMD0lMjAlMjAlMjAlMjBJbmljaW91JTIwbyUyMGV4ZWN1dGFyJTIwJTIwaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy93Ny56aXAlN0NodHRwOi8vNjUuMTgxLjEyNS4xOTMvYTM1bmV3L3c3LnppcCU3QzMyJTdDaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy9kbGwuZGxsIEhUVFAvMS4xDQpIb3N0OiB3d3cuZGV2eWF0aW5za2l5LnJ1DQoNCg==\",\"@version\":\"1\",\"gcenter\":\"gcenter-xxxxxxxx.domain.local\",\"payload_printable\":\"GET /download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000 HTTP/1.1\\r\\nAccept: text/html, application/xhtml+xml, */*\\r\\nAccept-Language: en-US\\r\\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\\r\\nAccept-Encoding: gzip, deflate\\r\\nHost: dc524.4shared.com\\r\\nConnection: Keep-Alive\\r\\nCookie: day1host=h\\r\\n\\r\\nGET /web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F HTTP/1.1\\r\\nAccept: text/html, application/xhtml+xml, */*\\r\\nAccept-Language: en-US\\r\\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\\r\\nAccept-Encoding: gzip, deflate\\r\\nCookie: day1host=h\\r\\nConnection: Keep-Alive\\r\\nHost: cdnfiles.4shared.com\\r\\n\\r\\nGET /a35new/w7.txt HTTP/1.1\\r\\nHost: 65.181.125.193\\r\\nConnection: Keep-Alive\\r\\n\\r\\nGET /a35new/aw7.tiff HTTP/1.1\\r\\nHost: 65.181.125.193\\r\\n\\r\\nGET /bsb/infects/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Windows%207%20Home%20Premium%20%20%20%20=%20%20%20%20%20%20%20N/A HTTP/1.1\\r\\nHost: www.devyatinskiy.ru\\r\\nConnection: Keep-Alive\\r\\n\\r\\nGET /bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll HTTP/1.1\\r\\nHost: www.devyatinskiy.ru\\r\\n\\r\\n\",\"alert\":{\"signature\":\"ETPRO TROJAN MSIL/Bazidow.A HTTP C2\",\"category\":\"A Network Trojan was detected\",\"gid\":1,\"signature_id\":2828821,\"rev\":3,\"severity\":1,\"metadata\":{\"affected_product\":[\"Windows_XP_Vista_7_8_10_Server_32_64_Bit\"],\"performance_impact\":[\"Moderate\"],\"deployment\":[\"Perimeter\"],\"created_at\":[\"2017_12_07\"],\"updated_at\":[\"2022_05_03\"],\"former_category\":[\"MALWARE\"],\"attack_target\":[\"Client_Endpoint\"],\"signature_severity\":[\"Major\"]},\"action\":\"allowed\"}}",
        "event": {
            "action": "allowed",
            "category": [
                "network"
            ],
            "kind": "alert",
            "module": "alert",
            "severity": 1
        },
        "@timestamp": "2023-03-22T10:25:55.690000Z",
        "destination": {
            "address": "2.2.2.2",
            "bytes": 90364,
            "ip": "2.2.2.2",
            "packets": 66,
            "port": 16122
        },
        "gatewatcher": {
            "event_type": "alert",
            "flow_id": "1408237495862400",
            "gcap": "gcap-xxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxx.domain.local",
            "payload": "R0VUIC9kb3dubG9hZC9RanRHRGx0bWNlLzE2MDgyMDE2dmVjTzdPa0wzeUxQSUNsZW96aWJLRS52YnM/ZHNpZD1ndjVucTMuNDAwYjg2YzcxOTZmOWU4Y2NkZTM1MzcwZWIwYTU0Yjkmc2Jzcj0yZjViMmRmMGFlMGE4Yzc1NTFjN2RmMGJjNDZhOWQ3OTk4MCZsZ2ZwPTMwMDAgSFRUUC8xLjENCkFjY2VwdDogdGV4dC9odG1sLCBhcHBsaWNhdGlvbi94aHRtbCt4bWwsICovKg0KQWNjZXB0LUxhbmd1YWdlOiBlbi1VUw0KVXNlci1BZ2VudDogTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgVHJpZGVudC83LjA7IHJ2OjExLjApIGxpa2UgR2Vja28NCkFjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZQ0KSG9zdDogZGM1MjQuNHNoYXJlZC5jb20NCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkNvb2tpZTogZGF5MWhvc3Q9aA0KDQpHRVQgL3dlYi9jZG4vcG9wdWxhci9kb3dubG9hZC9RanRHRGx0bWNlP2NvbnREaXNwPWF0dGFjaG1lbnQlM0IrZmlsZW5hbWUlM0QlMjIxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMlMjIlM0IrZmlsZW5hbWUqJTNEdXRmLTglMjclMjcxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMmY29udFR5cGU9QVBQTElDQVRJT04lMkZPQ1RFVC1TVFJFQU0mY2RuaD03YTc0NTUzYTA1N2VhNTVmYzU2OGI4MGU2MGNkN2ZhMiZkM2M9ZmRzUWp0R0RsdG1jZSUzRElOSVRJQUxJWkVEJTNCK2RvbWFpbiUzRC40c2hhcmVkLmNvbSUzQitleHBpcmVzJTNEV2VkJTJDKzE3LUF1Zy0yMDE2KzAxJTNBMzYlM0E0NCtHTVQlM0IrcGF0aCUzRCUyRiBIVFRQLzEuMQ0KQWNjZXB0OiB0ZXh0L2h0bWwsIGFwcGxpY2F0aW9uL3hodG1sK3htbCwgKi8qDQpBY2NlcHQtTGFuZ3VhZ2U6IGVuLVVTDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0OyBUcmlkZW50LzcuMDsgcnY6MTEuMCkgbGlrZSBHZWNrbw0KQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlDQpDb29raWU6IGRheTFob3N0PWgNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkhvc3Q6IGNkbmZpbGVzLjRzaGFyZWQuY29tDQoNCkdFVCAvYTM1bmV3L3c3LnR4dCBIVFRQLzEuMQ0KSG9zdDogNjUuMTgxLjEyNS4xOTMNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9hMzVuZXcvYXc3LnRpZmYgSFRUUC8xLjENCkhvc3Q6IDY1LjE4MS4xMjUuMTkzDQoNCkdFVCAvYnNiL2luZmVjdHMvaW5kZXgucGhwP049R08tR08tR0FER0VULVBDLWluc3BlY3Rvci1nYWRnZXQlMjA9JTIwJTIwJTIwJTIwV2luZG93cyUyMDclMjBIb21lJTIwUHJlbWl1bSUyMCUyMCUyMCUyMD0lMjAlMjAlMjAlMjAlMjAlMjAlMjBOL0EgSFRUUC8xLjENCkhvc3Q6IHd3dy5kZXZ5YXRpbnNraXkucnUNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9ic2IvZGVidWdub3Nzby9pbmRleC5waHA/Tj1HTy1HTy1HQURHRVQtUEMtaW5zcGVjdG9yLWdhZGdldCUyMD0lMjAlMjAlMjAlMjBJbmljaW91JTIwbyUyMGV4ZWN1dGFyJTIwJTIwaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy93Ny56aXAlN0NodHRwOi8vNjUuMTgxLjEyNS4xOTMvYTM1bmV3L3c3LnppcCU3QzMyJTdDaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy9kbGwuZGxsIEhUVFAvMS4xDQpIb3N0OiB3d3cuZGV2eWF0aW5za2l5LnJ1DQoNCg==",
            "payload_printable": "GET /download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000 HTTP/1.1\r\nAccept: text/html, application/xhtml+xml, */*\r\nAccept-Language: en-US\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\r\nAccept-Encoding: gzip, deflate\r\nHost: dc524.4shared.com\r\nConnection: Keep-Alive\r\nCookie: day1host=h\r\n\r\nGET /web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F HTTP/1.1\r\nAccept: text/html, application/xhtml+xml, */*\r\nAccept-Language: en-US\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\r\nAccept-Encoding: gzip, deflate\r\nCookie: day1host=h\r\nConnection: Keep-Alive\r\nHost: cdnfiles.4shared.com\r\n\r\nGET /a35new/w7.txt HTTP/1.1\r\nHost: 65.181.125.193\r\nConnection: Keep-Alive\r\n\r\nGET /a35new/aw7.tiff HTTP/1.1\r\nHost: 65.181.125.193\r\n\r\nGET /bsb/infects/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Windows%207%20Home%20Premium%20%20%20%20=%20%20%20%20%20%20%20N/A HTTP/1.1\r\nHost: www.devyatinskiy.ru\r\nConnection: Keep-Alive\r\n\r\nGET /bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll HTTP/1.1\r\nHost: www.devyatinskiy.ru\r\n\r\n",
            "timestamp_analyzed": "2023-03-22T10:44:08.001Z",
            "timestamp_detected": "2023-03-22T10:25:55.690Z",
            "type": "suricata"
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "network": {
            "protocol": "http",
            "transport": "TCP"
        },
        "observer": {
            "hostname": "gcap-xxxxxxxx.domain.local",
            "mac": [
                "90:e2:ba:a6:a4:90",
                "90:e2:ba:a6:a4:91"
            ],
            "name": "gcap-xxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "gcap-xxxxxxxx.domain.local",
                "www.devyatinskiy.ru"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "rule": {
            "category": "A Network Trojan was detected",
            "id": "2828821",
            "name": "ETPRO TROJAN MSIL/Bazidow.A HTTP C2"
        },
        "source": {
            "address": "1.1.1.1",
            "bytes": 3084,
            "ip": "1.1.1.1",
            "packets": 19,
            "port": 8550
        },
        "url": {
            "domain": "www.devyatinskiy.ru",
            "path": "/bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll",
            "registered_domain": "devyatinskiy.ru",
            "subdomain": "www",
            "top_level_domain": "ru"
        }
    }
    	
	```


=== "sigflow-file.json"

    ```json
	
    {
        "message": "{\"event_type\":\"fileinfo\",\"proto\":\"TCP\",\"http\":{\"protocol\":\"HTTP/1.1\",\"url\":\"/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F\",\"hostname\":\"cdnfiles.4shared.com\",\"status\":200,\"length\":1088,\"http_content_type\":\"APPLICATION/OCTET-STREAM\",\"http_user_agent\":\"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\",\"http_method\":\"GET\"},\"timestamp_detected\":\"2023-03-22T10:25:55.469Z\",\"uuid\":\"24231245-276c-4509-9437-016b82f88c7c\",\"type\":\"suricata\",\"in_iface\":\"monvirt\",\"src_ip\":\"1.1.1.1\",\"host\":\"gcap-xxxxxxxxx.domain.local\",\"dest_ip\":\"2.2.2.2\",\"flow_id\":1408237495862400,\"@timestamp\":\"2023-03-22T10:44:07.998Z\",\"timestamp_analyzed\":\"2023-03-22T10:44:07.998Z\",\"@version\":\"1\",\"gcap\":\"gcap-xxxxxxxxxx.domain.local\",\"gcenter\":\"gcenter-xxxxxxxx.domain.local\",\"fileinfo\":{\"size\":1088,\"filename\":\"16082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs\",\"state\":\"CLOSED\",\"sha256\":\"f31faae778ecfee8e27041309444468a37ad7681d42d7972faa92fe2056721df\",\"magic\":\"Little-endian UTF-16 Unicode text, with CRLF line terminators\",\"sid\":[],\"stored\":false,\"tx_id\":1,\"gaps\":false,\"md5\":\"d526c8e4ad7ab6d80baeb839976b7c80\"},\"dest_port\":8550,\"src_port\":16122,\"app_proto\":\"http\"}",
        "event": {
            "category": [
                "network"
            ],
            "module": "fileinfo"
        },
        "@timestamp": "2023-03-22T10:25:55.469000Z",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 8550
        },
        "file": {
            "hash": {
                "md5": "d526c8e4ad7ab6d80baeb839976b7c80",
                "sha256": "f31faae778ecfee8e27041309444468a37ad7681d42d7972faa92fe2056721df"
            },
            "name": "16082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs",
            "size": 1088
        },
        "gatewatcher": {
            "event_type": "fileinfo",
            "filemagic": "Little-endian UTF-16 Unicode text, with CRLF line terminators",
            "flow_id": "1408237495862400",
            "gcap": "gcap-xxxxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxx.domain.local",
            "timestamp_analyzed": "2023-03-22T10:44:07.998Z",
            "timestamp_detected": "2023-03-22T10:25:55.469Z",
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
            "hostname": "gcap-xxxxxxxxx.domain.local",
            "name": "gcap-xxxxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hash": [
                "d526c8e4ad7ab6d80baeb839976b7c80",
                "f31faae778ecfee8e27041309444468a37ad7681d42d7972faa92fe2056721df"
            ],
            "hosts": [
                "cdnfiles.4shared.com",
                "gcap-xxxxxxxxx.domain.local"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 16122
        },
        "url": {
            "domain": "cdnfiles.4shared.com",
            "path": "/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F",
            "registered_domain": "4shared.com",
            "subdomain": "cdnfiles",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "IE",
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "os": {
                "name": "Windows",
                "version": "7"
            },
            "version": "11.0"
        }
    }
    	
	```


=== "sigflow-meta.json"

    ```json
	
    {
        "message": "{\"event_type\":\"http\",\"http\":{\"accept_encoding\":\"gzip, deflate\",\"server\":\"524\",\"accept\":\"text/html, application/xhtml+xml, */*\",\"url\":\"/download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000\",\"protocol\":\"HTTP/1.1\",\"hostname\":\"dc524.4shared.com\",\"accept_language\":\"en-US\",\"location\":\"http://cdnfiles.4shared.com/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F\",\"length\":0,\"status\":302,\"http_user_agent\":\"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\",\"date\":\"Wed, 17 Aug 2016 01:34:43 GMT\",\"redirect\":\"http://cdnfiles.4shared.com/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F\",\"content_length\":\"0\",\"cookie\":\"day1host=h\",\"http_method\":\"GET\"},\"timestamp_detected\":\"2023-03-22T10:25:55.377Z\",\"uuid\":\"f8ee6e33-91ef-404f-bad3-a69185416a0d\",\"type\":\"suricata\",\"in_iface\":\"monvirt\",\"src_ip\":\"1.1.1.1\",\"host\":\"gcap-xxxxxxxxx.domain.local\",\"dest_ip\":\"2.2.2.2\",\"flow_id\":1408237495862400,\"@timestamp\":\"2023-03-22T10:44:07.997Z\",\"timestamp_analyzed\":\"2023-03-22T10:44:07.997Z\",\"gcap\":\"gcap-xxxxxxxxx.domain.local\",\"dest_port\":16122,\"src_port\":8550,\"community_id\":\"1:hEBuGl9msx7YJtg3Tb/+Gf+a1VI=\",\"proto\":\"TCP\",\"tx_id\":0,\"ether\":{\"dest_mac\":\"90:e2:ba:a6:a4:90\",\"src_mac\":\"90:e2:ba:a6:a4:91\"},\"@version\":\"1\",\"gcenter\":\"gcenter-xxxxxxxxxx.domain.local\"}",
        "event": {
            "category": [
                "network"
            ],
            "module": "http"
        },
        "@timestamp": "2023-03-22T10:25:55.377000Z",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 16122
        },
        "gatewatcher": {
            "event_type": "http",
            "flow_id": "1408237495862400",
            "gcap": "gcap-xxxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxxxx.domain.local",
            "timestamp_analyzed": "2023-03-22T10:44:07.997Z",
            "timestamp_detected": "2023-03-22T10:25:55.377Z",
            "type": "suricata"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 302
            }
        },
        "network": {
            "transport": "TCP"
        },
        "observer": {
            "hostname": "gcap-xxxxxxxxx.domain.local",
            "mac": [
                "90:e2:ba:a6:a4:90",
                "90:e2:ba:a6:a4:91"
            ],
            "name": "gcap-xxxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "dc524.4shared.com",
                "gcap-xxxxxxxxx.domain.local"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 8550
        },
        "url": {
            "domain": "dc524.4shared.com",
            "path": "/download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000",
            "registered_domain": "4shared.com",
            "subdomain": "dc524",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "IE",
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "os": {
                "name": "Windows",
                "version": "7"
            },
            "version": "11.0"
        }
    }
    	
	```


=== "sigflow-tls.json"

    ```json
	
    {
        "message": "{\"uuid\":\"b96777f9-6409-4864-b8a1-452094a93c5d\",\"host\":\"gcap-xxxxxxxxx.domain.local\",\"ether\":{\"dest_mac\":\"e6:43:7e:91:1b:92\",\"src_mac\":\"82:df:ee:4f:81:af\"},\"type\":\"suricata\",\"dest_ip\":\"5.6.7.8\",\"src_port\":64809,\"flow_id\":1366008699485799,\"timestamp_analyzed\":\"2024-11-21T13:02:44.291Z\",\"timestamp\":\"2024-11-21T13:02:02.870913+0000\",\"gcenter\":\"gcenter-xxxxxxxx.domain.local\",\"event_type\":\"tls\",\"src_ip\":\"1.2.3.4\",\"dest_port\":443,\"in_iface\":\"mon2\",\"tls\":{\"sni\":\"www.microsoft.com\",\"version\":\"TLS 1.3\",\"ja3s\":{\"string\":\"771,4866,43-51\",\"hash\":\"15af977ce25de452b96affa2addb1036\"}},\"@version\":\"1\",\"proto\":\"TCP\",\"gcap\":\"gcap-xxxxxxxxx.domain.local\",\"@timestamp\":\"2024-11-21T13:02:44.291Z\"}\n",
        "event": {
            "category": [
                "network"
            ],
            "module": "tls"
        },
        "destination": {
            "address": "5.6.7.8",
            "ip": "5.6.7.8",
            "port": 443
        },
        "gatewatcher": {
            "event_type": "tls",
            "flow_id": "1366008699485799",
            "gcap": "gcap-xxxxxxxxx.domain.local",
            "gcenter": "gcenter-xxxxxxxx.domain.local",
            "timestamp_analyzed": "2024-11-21T13:02:44.291Z",
            "tls": "{\"ja3s\":{\"hash\":\"15af977ce25de452b96affa2addb1036\",\"string\":\"771,4866,43-51\"},\"sni\":\"www.microsoft.com\",\"version\":\"TLS 1.3\"}",
            "tls_sni": "www.microsoft.com",
            "type": "suricata"
        },
        "network": {
            "transport": "TCP"
        },
        "observer": {
            "hostname": "gcap-xxxxxxxxx.domain.local",
            "mac": [
                "82:df:ee:4f:81:af",
                "e6:43:7e:91:1b:92"
            ],
            "name": "gcap-xxxxxxxxx.domain.local",
            "type": "ids",
            "version": "0.2"
        },
        "related": {
            "hosts": [
                "gcap-xxxxxxxxx.domain.local"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 64809
        },
        "tls": {
            "server": {
                "ja3s": "15af977ce25de452b96affa2addb1036"
            },
            "version": "TLS 1.3"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`dns.id` | `keyword` | The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.question.type` | `keyword` | The type of record being queried. |
|`dns.type` | `keyword` | The type of DNS event captured, query or answer. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.size` | `long` | File size in bytes. |
|`gatewatcher.calls` | `text` | This field represents the list of calls detected in a shellcode |
|`gatewatcher.campaigns` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.case_id` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.categories` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.description` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.dhcp` | `text` | This field represents the dhcp field in a network metadata (used in legacy format log) |
|`gatewatcher.dnp3` | `text` | This field represents the dnp3 field in a suricata alert (used in legacy format log) |
|`gatewatcher.email` | `text` | This field represents the email field |
|`gatewatcher.encodings` | `text` | This field represents the encodings used in the shellcode |
|`gatewatcher.event_type` | `keyword` | Type of event |
|`gatewatcher.external_links` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.families` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.fileinfo` | `text` | This field represents the fileinfo field in a malcore alert (used in legacy format log) |
|`gatewatcher.filemagic` | `text` | This field represents the magic of a file info |
|`gatewatcher.flow_id` | `keyword` | Identifier of the flow |
|`gatewatcher.ftp` | `text` | This field represents the ftp field in a network metadata (used in legacy format log) |
|`gatewatcher.ftp_data` | `text` | This field represents the ftp-data field in a network metadata (used in legacy format log) |
|`gatewatcher.gcap` | `keyword` | Name of the gcap |
|`gatewatcher.gcenter` | `keyword` | Name of the associated gcenter |
|`gatewatcher.http2` | `text` | This field represents the http2 field in a network metadata (used in legacy format log) |
|`gatewatcher.ikev2` | `text` | This field represents the ikev2 field in a network metadata (used in legacy format log) |
|`gatewatcher.ioc_creation_date` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.ioc_id` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.ioc_tags` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.ioc_type` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.ioc_updated_date` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.ioc_value` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.kill_chain_phases` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.krb5` | `text` | This field represents the krb5 field in a network metadata (used in legacy format log) |
|`gatewatcher.malcore.code` | `keyword` | Return code of the malcore analysis |
|`gatewatcher.malcore.detail_threat_found` | `keyword` | Type of the detected threat |
|`gatewatcher.malcore.file` | `keyword` | Identifier of the file |
|`gatewatcher.malcore.magic` | `keyword` | The magic number of the executable of the malware |
|`gatewatcher.malcore.replica` | `keyword` | Analysis is a replica of another previous one |
|`gatewatcher.matched_event` | `text` | This field represents the matched event found in a dga and retrohunt alert |
|`gatewatcher.matched_event_type` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.meta_data` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.mqtt` | `text` | This field represents the mqtt field in a network metadata (used in legacy format log) |
|`gatewatcher.nb_rescans` | `long` | Number of retroact analysis |
|`gatewatcher.nfs` | `text` | This field represents the nfs field in a network metadata (used in legacy format log) |
|`gatewatcher.payload` | `text` | This field represents the payload in a suricata alert |
|`gatewatcher.payload_printable` | `text` | This field represents the human readable payload in a suricata alert |
|`gatewatcher.probability` | `float` | This field represents the probability found in a dga and retrohunt alert |
|`gatewatcher.rdp` | `text` | This field represents the rdp field in a network metadata (used in legacy format log) |
|`gatewatcher.relations` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.reporting_token` | `keyword` | Token used by Gbox |
|`gatewatcher.retroact` | `keyword` | Analysis result per retroact |
|`gatewatcher.rfb` | `text` | This field represents the rfb field in a network metadata (used in legacy format log) |
|`gatewatcher.risk` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.rpc` | `text` | This field represents the rpc field in a network metadata (used in legacy format log) |
|`gatewatcher.sample_id` | `text` | Matching legacy file_id with ECS sample_id |
|`gatewatcher.scores.analysis` | `number` | test-scores |
|`gatewatcher.scores.analysis_detailed` | `text` | test-scores |
|`gatewatcher.scores.proba_obfuscated` | `float` | test-scores |
|`gatewatcher.signature` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.sip` | `text` | This field represents the sip field in a network metadata (used in legacy format log) |
|`gatewatcher.smb` | `text` | This field represents the smb field in a network metadata (used in legacy format log) |
|`gatewatcher.smtp` | `text` | This field represents the smtp field in a network metadata (used in legacy format log) |
|`gatewatcher.snmp` | `text` | This field represents the snmp field in a network metadata (used in legacy format log) |
|`gatewatcher.ssh` | `text` | This field represents the ssh field in a network metadata (used in legacy format log) |
|`gatewatcher.state` | `keyword` | Analysis result |
|`gatewatcher.stats` | `text` | This field represents the metrics stats |
|`gatewatcher.sub_type` | `text` | Sub type of codebreaker exploit |
|`gatewatcher.targeted_countries` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.targeted_organizations` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.targeted_platforms` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.targeted_sectors` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.tftp` | `text` | This field represents the tftp field in a network metadata (used in legacy format log) |
|`gatewatcher.threat_actor` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.timestamp_analyzed` | `keyword` | Timestamp of the alert processing by gcenter |
|`gatewatcher.timestamp_detected` | `keyword` | Timestamp of the file collection by gcap |
|`gatewatcher.timestamp_package` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.tlp` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.tls` | `text` | This field contains all TLS data fields in a TLS metadata |
|`gatewatcher.tls_fingerprint` | `text` | This field represents the TLS server fingerprint field in a TLS metadata |
|`gatewatcher.tls_sni` | `text` | This field represents the TLS SNI field in a TLS metadata |
|`gatewatcher.ttp` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.type` | `keyword` | Type of analysis |
|`gatewatcher.usage_mode` | `text` | This field is used for retrohunt alerts |
|`gatewatcher.vulnerabilities` | `text` | This field is used for retrohunt alerts |
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
|`tls.server.certificate_chain` | `keyword` | Array of PEM-encoded certificates that make up the certificate chain offered by the server. |
|`tls.server.issuer` | `keyword` | Subject of the issuer of the x.509 certificate presented by the server. |
|`tls.server.ja3s` | `keyword` | A hash that identifies servers based on how they perform an SSL/TLS handshake. |
|`tls.server.not_after` | `date` | Timestamp indicating when server certificate is no longer considered valid. |
|`tls.server.not_before` | `date` | Timestamp indicating when server certificate is first considered valid. |
|`tls.server.subject` | `keyword` | Subject of the x.509 certificate presented by the server. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/GateWatcher/aioniq).