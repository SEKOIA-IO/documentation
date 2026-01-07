
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "codebreaker"


    ```json
	{
        "event_type": "powershell",
        "scores": {
            "analysis": 1890,
            "analysis_detailed": {
                "CharInt": 0,
                "InvokeWebRequest": 0,
                "FmtStr": 0,
                "WebClientInvokation": 0,
                "StrReplace": 0,
                "StrJoin": 0,
                "SetContent": 0,
                "StreamWriter": 0,
                "SystemIOFile": 0,
                "StreamReader": 0,
                "InvokeRestMethod": 0,
                "AddContent": 0,
                "StartBitsTransfer": 0,
                "InvokeExpression": 0,
                "GetContent": 0,
                "StrCat": 370,
                "Base64": 1520
            },
            "proba_obfuscated": 1.0
        },
        "timestamp_detected": "2023-03-22T10:30:37.145Z",
        "uuid": "8906e477-02b5-4ada-abaa-67b2d41f204a",
        "severity": 1,
        "type": "codebreaker",
        "src_ip": "1.1.1.1",
        "state": "Exploit",
        "dest_port": "35444",
        "dest_ip": "2.2.2.2",
        "flow_id": "2157601933358692",
        "gcap": "gcap-xxxxxxxxxx.domain.local",
        "@timestamp": "2023-03-22T10:32:50.269Z",
        "timestamp_analyzed": "2023-03-22T10:32:50.269Z",
        "src_port": "4242",
        "file_id": "03-22-2023T10:32:45_772669089795425e9ad63823ea1e7ac3_gcap-xxxxxxxx.domain.local",
        "sub_type": "powershell",
        "SHA256": "efc9380fee13f9accf1cbc2f2bb02ae430cf39d4fbfe1d766f65b500b571ca29",
        "MD5": "60b656e17bec0a97f5638790c78a3124",
        "@version": "1",
        "gcenter": "gcenter-xxxxxxxxxx.domain.local"
    }
    ```



=== "dga"


    ```json
	{
        "event_type": "dga",
        "domain_name": "pgoadcmgqfacj.com",
        "timestamp_detected": "2023-03-22T10:25:54.903Z",
        "uuid": "4e4b3104-06ba-4277-899e-149a74a0671c",
        "severity": 1,
        "type": "machine_learning",
        "probability": 0.9999731546766107,
        "dest_port": 53,
        "gcap": "gcap-xxxxxxxx.domain.local",
        "dest_ip": "2.2.2.2",
        "flow_id": 729468278572,
        "src_ip": "1.1.1.1",
        "@timestamp": "2023-03-22T10:46:08.487Z",
        "@version": "1",
        "matched_event": "041b2ed4-a5e0-4814-8bdc-7522b6d5464f",
        "timestamp_analyzed": "2023-03-22T10:46:08.487Z",
        "gcenter": "gcenter-xxxxxx.domain.local",
        "src_port": 1294
    }
    ```



=== "malcore"


    ```json
	{
        "timestamp": "2023-03-22T10:35:22.615360+0000",
        "analyzed_infected": 10,
        "detail_threat_found": "Infected : Script.SWF.CVE-2014-0515+.C107 (B), Exp.SWF.Angler.D, Script.SWF.CVE-2014-0515+.C107, SWF/Exploit.ExKit.J trojan, Exploit.SWF.Agent.ja, Exploit.Agent.Script.371, Exploit.Swf.Agent.dvtnkm, Script.SWF.CVE-2014-0515++.C118, EXP/FLASH.Pubenush.E.Gen, Exploit.SWF",
        "timestamp_detected": "2023-03-22T10:35:22.615Z",
        "uuid": "2103a99c-549e-49b7-bbef-68459e6cc44e",
        "severity": 1,
        "dest_port": 19609,
        "detail_wait_time": 320265,
        "host": "gcap-xxxxxxxxx.domain.local",
        "dest_ip": "2.2.2.2",
        "timestamp_analyzed": "2023-03-22T10:53:13.408Z",
        "@timestamp": "2023-03-22T10:53:13.408Z",
        "file_type_description": "Macromedia Flash Player",
        "fileinfo": {
            "sha256": "350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4",
            "file_id": 379,
            "magic": "Macromedia Flash data (compressed), version 14",
            "tx_id": 1,
            "state": "CLOSED",
            "filename": "/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust",
            "sid": [
                1100020
            ],
            "stored": true,
            "md5": "67ca9a31f220bc7b68f203c07ad668b9",
            "gaps": false,
            "size": 77068
        },
        "analyzed_suspicious": 0,
        "analyzers_up": 16,
        "app_proto": "http",
        "engines_last_update_date": "2023-03-08T19:03:00Z",
        "total_found": "10/16",
        "file_type": "application/x-shockwave-flash",
        "detail_scan_time": 13425,
        "processing_time": 333690,
        "SHA256": "350836364013549b6a76aab79d57d109df6acc143759e24a952d3ff5d6a76ec4",
        "gcenter": "gcenter-xxxxxxxx.domain.local",
        "analyzed_clean": 5,
        "event_type": "malware",
        "http": {
            "http_method": "GET",
            "http_port": 8080,
            "protocol": "HTTP/1.1",
            "status": 200,
            "hostname": "tsevid-synonymi.justdanceatsea.com",
            "url": "/6SuCHKKkf8Sf1aFXJPqD0R6r3oEDCrbwHFm23EU-Af2zwWdHgpn6mEGu5XlxFust",
            "length": 77068,
            "http_content_type": "application/x-shockwave-flash",
            "http_user_agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
            "http_refer": "http://tsevid-synonymi.justdanceatsea.com:8080/ndf4xx22ci.php"
        },
        "type": "malcore",
        "in_iface": "monvirt",
        "src_ip": "1.1.1.1",
        "state": "Infected",
        "gcap": "gcap-xxxxxxxx.domain.local",
        "flow_id": 1910314914537014,
        "reporting_token": "No GBOX",
        "src_port": 8080,
        "analyzed_other": 1,
        "engine_id": {
            "4": {
                "id": "32f2f45e6d9faf46e6954356a710208d412fac5181f6c641e34cb9956a133684",
                "threat_details": "SWF/Exploit.ExKit.J trojan",
                "scan_result": "INFECTED"
            },
            "1": {
                "id": "054a20c51cbe9d2cc7d6a237d6cd4e08ab1a67e170b371e632995766d3ba81af",
                "threat_details": "",
                "scan_result": "CLEAN"
            },
            "9": {
                "id": "95603b80d80fa3e98b6faf07418a55ed0b035d19209e3ad4f1858f6b46fa070a",
                "threat_details": "Script.SWF.CVE-2014-0515++.C118",
                "scan_result": "INFECTED"
            },
            "14": {
                "id": "ecc47e2309be9838d6dc2c5157be1a840950e943f5aaca6637afca11516c3eaf",
                "threat_details": "",
                "scan_result": "CLEAN"
            },
            "8": {
                "id": "714eca0a6475fe7d2bf9a24bcae343f657b230ff68acd544b019574f1392de77",
                "threat_details": "Exploit.Swf.Agent.dvtnkm",
                "scan_result": "INFECTED"
            },
            "7": {
                "id": "527db072abcf877d4bdcd0e9e4ce12c5d769621aa65dd2f7697a3d67de6cc737",
                "threat_details": "Exploit.Agent.Script.371",
                "scan_result": "INFECTED"
            },
            "2": {
                "id": "0ff95ddb1117d8f36124f6eac406dbbf9f17e3dd89f9bb1bd600f6ad834c25db",
                "threat_details": "Exp.SWF.Angler.D",
                "scan_result": "INFECTED"
            },
            "11": {
                "id": "ad05e0dc742bcd6251af91bd07ef470c699d5aebbb2055520b07021b14d7380c",
                "threat_details": "",
                "scan_result": "NOT_SCANNED"
            },
            "12": {
                "id": "af6868a2b87b3388a816e09d2b282629ccf883b763b3691368a27fbd6f6cd51a",
                "threat_details": "EXP/FLASH.Pubenush.E.Gen",
                "scan_result": "INFECTED"
            },
            "10": {
                "id": "a9b912e461cec506780d8ad8e785cca6b233ad7c72335c262b0a4ab189afa713",
                "threat_details": "",
                "scan_result": "CLEAN"
            },
            "3": {
                "id": "312a189607571ec2c7544636be405f10889e73d061e0ed77ca0eca97a470838d",
                "threat_details": "Script.SWF.CVE-2014-0515+.C107",
                "scan_result": "INFECTED"
            },
            "6": {
                "id": "4ca73ae4b92fd7ddcda418e6b70ced0481ac2d878c48e61b686d0c9573c331dc",
                "threat_details": "",
                "scan_result": "CLEAN"
            },
            "13": {
                "id": "b14014e40c0e672e050ad9c210a68a5303ce7facabae9eb2ee07ddf97dc0da0e",
                "threat_details": "",
                "scan_result": "CLEAN"
            },
            "0": {
                "id": "038e407ba285f0e01dd30c6e4f77ec19bad5ed3dc866a2904ae6bf46baa14b74",
                "threat_details": "Script.SWF.CVE-2014-0515+.C107 (B)",
                "scan_result": "INFECTED"
            },
            "5": {
                "id": "3bfeb615a695c5ebaac5ade948ffae0c3cfec3787d4625e3abb27fa3c2867f53",
                "threat_details": "Exploit.SWF.Agent.ja",
                "scan_result": "INFECTED"
            },
            "15": {
                "id": "fe665976a02d03734c321007328109ab66823b260a8eea117d2ab49ee9dfd3f1",
                "threat_details": "Exploit.SWF",
                "scan_result": "INFECTED"
            }
        },
        "proto": "TCP",
        "code": 1,
        "analyzed_error": 0,
        "@version": "1",
        "magic_details": "Macromedia Flash data (compressed), version 14"
    }
    ```



=== "retrohunt"


    ```json
	{
        "external_links": [
            {
                "url": "https://urlhaus.abuse.ch/url/2269068/",
                "source_name": "URLHaus Abuse.ch"
            }
        ],
        "relations": [
            "0e3cc27b-7999-48ce-8484-dc12b325a355"
        ],
        "description": "IOC matching first tests",
        "event_type": "retrohunt",
        "kill_chain_phases": [],
        "timestamp_detected": "2023-06-09T14:08:46.845Z",
        "ioc_type": "Host",
        "severity": 1,
        "community_id": "1:x0uuTl0mYnN1nwngep7+A4VH38I=",
        "ioc_creation_date": "2023-06-12T10:00:35+00:00",
        "targeted_countries": [],
        "ioc_value": "im.a.very.bad.doma.in",
        "dest_ip": "2.2.2.2",
        "vulnerabilities": [],
        "matched_event": "bd7686c8-20db-427e-941d-844a5ecfe559",
        "risk": "Suspicious",
        "uuid": "416f35ad-b954-4b6a-a886-987b826bb7f4",
        "meta_data": {
            "ssdeep": "1536:87vbq1lGAXSEYQjbChaAU2yU23M51DjZgSQAvcYkFtZTjzBht5:8D+CAXFYQChaAUk5ljnQssL",
            "cwe": [],
            "descriptions": [],
            "tslh": "T16D7312E017B517CC1371A8353BED205E9128223972AE35302E97528DF957703BAB2DBE",
            "filetype": "ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux)",
            "size": 78.3984375,
            "usageMode": "hunting"
        },
        "flow_id": 841376349480333,
        "matched_event_type": "alert",
        "ioc_updated_date": "2023-06-12T10:00:35+00:00",
        "targeted_platforms": [
            "linux"
        ],
        "signature": "RetroHunt - Host - malware/Unknown - Hajime - GW Lab Test - 00100035-1206-2023-cbf5-08330f0d5bc0",
        "ioc_tags": [
            "trojan.generickd.34055387 (b)",
            "linux/hajime.a trojan",
            "e32/agent.cd",
            "linux.hajime.bc",
            "backdoor.hajime.linux.129",
            "linux/hajime.75930",
            "unix.malware.agent-6626471-0",
            "linux/hajime.nsnlw",
            "hajime",
            "elf.mirai.43048.gc",
            "trojan.elfarm32.hajime.fbhtfi",
            "trojan.linux.hajime",
            "trojan.generickd.34055387"
        ],
        "@version": "1",
        "type": "cti",
        "targeted_organizations": [],
        "campaigns": [],
        "categories": [
            "malware"
        ],
        "src_port": 55614,
        "gcenter": "gcenter-xxxxxxxxxxxxxxxxx.domain.local",
        "case_id": "00100035-1206-2023-edb6-b38911f8ba0c",
        "dest_port": 80,
        "usage_mode": "hunting",
        "timestamp_package": "2023-06-12T10:00:35.012874+0000",
        "src_ip": "1.1.1.1",
        "ttp": [],
        "tlp": "green",
        "probability": 0.5,
        "gcap": "gcap-xxxxxxxxxxxxxxxx.domain.local",
        "@timestamp": "2023-06-12T10:12:39.001Z",
        "timestamp_analyzed": "2023-06-12T10:12:39.001Z",
        "families": [
            "Hajime"
        ],
        "ioc_id": "00100035-1206-2023-cbf5-08330f0d5bc0",
        "targeted_sectors": [],
        "threat_actor": [
            "GW Lab Test"
        ],
        "matched_app_proto": "http"
    }
    ```



=== "sigflow-alert"


    ```json
	{
        "event_type": "alert",
        "http": {
            "url": "/bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll",
            "protocol": "HTTP/1.1",
            "hostname": "www.devyatinskiy.ru",
            "length": 0,
            "http_method": "GET"
        },
        "timestamp_detected": "2023-03-22T10:25:55.690Z",
        "uuid": "fd5ba8ea-e263-426d-b4b2-a16521ae09b1",
        "packet_info": {
            "linktype": 1
        },
        "severity": 1,
        "in_iface": "monvirt",
        "src_ip": "1.1.1.1",
        "host": "gcap-xxxxxxxx.domain.local",
        "dest_ip": "2.2.2.2",
        "flow_id": 1408237495862400,
        "dest_port": 16122,
        "@timestamp": "2023-03-22T10:44:08.001Z",
        "timestamp_analyzed": "2023-03-22T10:44:08.001Z",
        "gcap": "gcap-xxxxxxx.domain.local",
        "type": "suricata",
        "src_port": 8550,
        "metadata": {
            "flowbits": [
                "min.gethttp",
                "ETPROtxtminhead",
                "http.dottedquadhost.dll"
            ]
        },
        "community_id": "1:hEBuGl9msx7YJtg3Tb/+Gf+a1VI=",
        "app_proto": "http",
        "packet": "kOK6pqSQkOK6pqSRCABFAAC7Uz1AAEAGPT4py4AkHxzgtiFmPvokcIbSnp074oAYAGsSTgAAAQEICmgi0xNoItMTR0VUIC9ic2IvZGVidWdub3Nzby9pbmRleC5waHA/Tj1HTy1HTy1HQURHRVQtUEMtaW5zcGVjdG9yLWdhZGdldCUyMD0lMjAlMjAlMjAlMjBJbmljaWFyJTdCNjklN0QgSFRUUC8xLjENCkhvc3Q6IHd3dy5kZXZ5YXRpbnNraXkucnUNCg0K",
        "proto": "TCP",
        "stream": 1,
        "flow": {
            "bytes_toclient": 90364,
            "bytes_toserver": 3084,
            "pkts_toserver": 19,
            "pkts_toclient": 66,
            "start": "2023-03-22T10:25:55.345216+0000"
        },
        "tx_id": 5,
        "ether": {
            "dest_mac": "90:e2:ba:a6:a4:90",
            "src_mac": "90:e2:ba:a6:a4:91"
        },
        "payload": "R0VUIC9kb3dubG9hZC9RanRHRGx0bWNlLzE2MDgyMDE2dmVjTzdPa0wzeUxQSUNsZW96aWJLRS52YnM/ZHNpZD1ndjVucTMuNDAwYjg2YzcxOTZmOWU4Y2NkZTM1MzcwZWIwYTU0Yjkmc2Jzcj0yZjViMmRmMGFlMGE4Yzc1NTFjN2RmMGJjNDZhOWQ3OTk4MCZsZ2ZwPTMwMDAgSFRUUC8xLjENCkFjY2VwdDogdGV4dC9odG1sLCBhcHBsaWNhdGlvbi94aHRtbCt4bWwsICovKg0KQWNjZXB0LUxhbmd1YWdlOiBlbi1VUw0KVXNlci1BZ2VudDogTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgVHJpZGVudC83LjA7IHJ2OjExLjApIGxpa2UgR2Vja28NCkFjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZQ0KSG9zdDogZGM1MjQuNHNoYXJlZC5jb20NCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkNvb2tpZTogZGF5MWhvc3Q9aA0KDQpHRVQgL3dlYi9jZG4vcG9wdWxhci9kb3dubG9hZC9RanRHRGx0bWNlP2NvbnREaXNwPWF0dGFjaG1lbnQlM0IrZmlsZW5hbWUlM0QlMjIxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMlMjIlM0IrZmlsZW5hbWUqJTNEdXRmLTglMjclMjcxNjA4MjAxNnZlY083T2tMM3lMUElDbGVvemliS0VIYTg2MUh6aDlHRi52YnMmY29udFR5cGU9QVBQTElDQVRJT04lMkZPQ1RFVC1TVFJFQU0mY2RuaD03YTc0NTUzYTA1N2VhNTVmYzU2OGI4MGU2MGNkN2ZhMiZkM2M9ZmRzUWp0R0RsdG1jZSUzRElOSVRJQUxJWkVEJTNCK2RvbWFpbiUzRC40c2hhcmVkLmNvbSUzQitleHBpcmVzJTNEV2VkJTJDKzE3LUF1Zy0yMDE2KzAxJTNBMzYlM0E0NCtHTVQlM0IrcGF0aCUzRCUyRiBIVFRQLzEuMQ0KQWNjZXB0OiB0ZXh0L2h0bWwsIGFwcGxpY2F0aW9uL3hodG1sK3htbCwgKi8qDQpBY2NlcHQtTGFuZ3VhZ2U6IGVuLVVTDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0OyBUcmlkZW50LzcuMDsgcnY6MTEuMCkgbGlrZSBHZWNrbw0KQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlDQpDb29raWU6IGRheTFob3N0PWgNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkhvc3Q6IGNkbmZpbGVzLjRzaGFyZWQuY29tDQoNCkdFVCAvYTM1bmV3L3c3LnR4dCBIVFRQLzEuMQ0KSG9zdDogNjUuMTgxLjEyNS4xOTMNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9hMzVuZXcvYXc3LnRpZmYgSFRUUC8xLjENCkhvc3Q6IDY1LjE4MS4xMjUuMTkzDQoNCkdFVCAvYnNiL2luZmVjdHMvaW5kZXgucGhwP049R08tR08tR0FER0VULVBDLWluc3BlY3Rvci1nYWRnZXQlMjA9JTIwJTIwJTIwJTIwV2luZG93cyUyMDclMjBIb21lJTIwUHJlbWl1bSUyMCUyMCUyMCUyMD0lMjAlMjAlMjAlMjAlMjAlMjAlMjBOL0EgSFRUUC8xLjENCkhvc3Q6IHd3dy5kZXZ5YXRpbnNraXkucnUNCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCg0KR0VUIC9ic2IvZGVidWdub3Nzby9pbmRleC5waHA/Tj1HTy1HTy1HQURHRVQtUEMtaW5zcGVjdG9yLWdhZGdldCUyMD0lMjAlMjAlMjAlMjBJbmljaW91JTIwbyUyMGV4ZWN1dGFyJTIwJTIwaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy93Ny56aXAlN0NodHRwOi8vNjUuMTgxLjEyNS4xOTMvYTM1bmV3L3c3LnppcCU3QzMyJTdDaHR0cDovLzY1LjE4MS4xMjUuMTkzL2EzNW5ldy9kbGwuZGxsIEhUVFAvMS4xDQpIb3N0OiB3d3cuZGV2eWF0aW5za2l5LnJ1DQoNCg==",
        "@version": "1",
        "gcenter": "gcenter-xxxxxxxx.domain.local",
        "payload_printable": "GET /download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000 HTTP/1.1\r\nAccept: text/html, application/xhtml+xml, */*\r\nAccept-Language: en-US\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\r\nAccept-Encoding: gzip, deflate\r\nHost: dc524.4shared.com\r\nConnection: Keep-Alive\r\nCookie: day1host=h\r\n\r\nGET /web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F HTTP/1.1\r\nAccept: text/html, application/xhtml+xml, */*\r\nAccept-Language: en-US\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\r\nAccept-Encoding: gzip, deflate\r\nCookie: day1host=h\r\nConnection: Keep-Alive\r\nHost: cdnfiles.4shared.com\r\n\r\nGET /a35new/w7.txt HTTP/1.1\r\nHost: 65.181.125.193\r\nConnection: Keep-Alive\r\n\r\nGET /a35new/aw7.tiff HTTP/1.1\r\nHost: 65.181.125.193\r\n\r\nGET /bsb/infects/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Windows%207%20Home%20Premium%20%20%20%20=%20%20%20%20%20%20%20N/A HTTP/1.1\r\nHost: www.devyatinskiy.ru\r\nConnection: Keep-Alive\r\n\r\nGET /bsb/debugnosso/index.php?N=GO-GO-GADGET-PC-inspector-gadget%20=%20%20%20%20Iniciou%20o%20executar%20%20http://65.181.125.193/a35new/w7.zip%7Chttp://65.181.125.193/a35new/w7.zip%7C32%7Chttp://65.181.125.193/a35new/dll.dll HTTP/1.1\r\nHost: www.devyatinskiy.ru\r\n\r\n",
        "alert": {
            "signature": "ETPRO TROJAN MSIL/Bazidow.A HTTP C2",
            "category": "A Network Trojan was detected",
            "gid": 1,
            "signature_id": 2828821,
            "rev": 3,
            "severity": 1,
            "metadata": {
                "affected_product": [
                    "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                ],
                "performance_impact": [
                    "Moderate"
                ],
                "deployment": [
                    "Perimeter"
                ],
                "created_at": [
                    "2017_12_07"
                ],
                "updated_at": [
                    "2022_05_03"
                ],
                "former_category": [
                    "MALWARE"
                ],
                "attack_target": [
                    "Client_Endpoint"
                ],
                "signature_severity": [
                    "Major"
                ]
            },
            "action": "allowed"
        }
    }
    ```



=== "sigflow-file"


    ```json
	{
        "event_type": "fileinfo",
        "proto": "TCP",
        "http": {
            "protocol": "HTTP/1.1",
            "url": "/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F",
            "hostname": "cdnfiles.4shared.com",
            "status": 200,
            "length": 1088,
            "http_content_type": "APPLICATION/OCTET-STREAM",
            "http_user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "http_method": "GET"
        },
        "timestamp_detected": "2023-03-22T10:25:55.469Z",
        "uuid": "24231245-276c-4509-9437-016b82f88c7c",
        "type": "suricata",
        "in_iface": "monvirt",
        "src_ip": "1.1.1.1",
        "host": "gcap-xxxxxxxxx.domain.local",
        "dest_ip": "2.2.2.2",
        "flow_id": 1408237495862400,
        "@timestamp": "2023-03-22T10:44:07.998Z",
        "timestamp_analyzed": "2023-03-22T10:44:07.998Z",
        "@version": "1",
        "gcap": "gcap-xxxxxxxxxx.domain.local",
        "gcenter": "gcenter-xxxxxxxx.domain.local",
        "fileinfo": {
            "size": 1088,
            "filename": "16082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs",
            "state": "CLOSED",
            "sha256": "f31faae778ecfee8e27041309444468a37ad7681d42d7972faa92fe2056721df",
            "magic": "Little-endian UTF-16 Unicode text, with CRLF line terminators",
            "sid": [],
            "stored": false,
            "tx_id": 1,
            "gaps": false,
            "md5": "d526c8e4ad7ab6d80baeb839976b7c80"
        },
        "dest_port": 8550,
        "src_port": 16122,
        "app_proto": "http"
    }
    ```



=== "sigflow-meta"


    ```json
	{
        "event_type": "http",
        "http": {
            "accept_encoding": "gzip, deflate",
            "server": "524",
            "accept": "text/html, application/xhtml+xml, */*",
            "url": "/download/QjtGDltmce/16082016vecO7OkL3yLPICleozibKE.vbs?dsid=gv5nq3.400b86c7196f9e8ccde35370eb0a54b9&sbsr=2f5b2df0ae0a8c7551c7df0bc46a9d79980&lgfp=3000",
            "protocol": "HTTP/1.1",
            "hostname": "dc524.4shared.com",
            "accept_language": "en-US",
            "location": "http://cdnfiles.4shared.com/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F",
            "length": 0,
            "status": 302,
            "http_user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "date": "Wed, 17 Aug 2016 01:34:43 GMT",
            "redirect": "http://cdnfiles.4shared.com/web/cdn/popular/download/QjtGDltmce?contDisp=attachment%3B+filename%3D%2216082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs%22%3B+filename*%3Dutf-8%27%2716082016vecO7OkL3yLPICleozibKEHa861Hzh9GF.vbs&contType=APPLICATION%2FOCTET-STREAM&cdnh=7a74553a057ea55fc568b80e60cd7fa2&d3c=fdsQjtGDltmce%3DINITIALIZED%3B+domain%3D.4shared.com%3B+expires%3DWed%2C+17-Aug-2016+01%3A36%3A44+GMT%3B+path%3D%2F",
            "content_length": "0",
            "cookie": "day1host=h",
            "http_method": "GET"
        },
        "timestamp_detected": "2023-03-22T10:25:55.377Z",
        "uuid": "f8ee6e33-91ef-404f-bad3-a69185416a0d",
        "type": "suricata",
        "in_iface": "monvirt",
        "src_ip": "1.1.1.1",
        "host": "gcap-xxxxxxxxx.domain.local",
        "dest_ip": "2.2.2.2",
        "flow_id": 1408237495862400,
        "@timestamp": "2023-03-22T10:44:07.997Z",
        "timestamp_analyzed": "2023-03-22T10:44:07.997Z",
        "gcap": "gcap-xxxxxxxxx.domain.local",
        "dest_port": 16122,
        "src_port": 8550,
        "community_id": "1:hEBuGl9msx7YJtg3Tb/+Gf+a1VI=",
        "proto": "TCP",
        "tx_id": 0,
        "ether": {
            "dest_mac": "90:e2:ba:a6:a4:90",
            "src_mac": "90:e2:ba:a6:a4:91"
        },
        "@version": "1",
        "gcenter": "gcenter-xxxxxxxxxx.domain.local"
    }
    ```



=== "sigflow-tls"


    ```json
	{
        "uuid": "b96777f9-6409-4864-b8a1-452094a93c5d",
        "host": "gcap-xxxxxxxxx.domain.local",
        "ether": {
            "dest_mac": "e6:43:7e:91:1b:92",
            "src_mac": "82:df:ee:4f:81:af"
        },
        "type": "suricata",
        "dest_ip": "5.6.7.8",
        "src_port": 64809,
        "flow_id": 1366008699485799,
        "timestamp_analyzed": "2024-11-21T13:02:44.291Z",
        "timestamp": "2024-11-21T13:02:02.870913+0000",
        "gcenter": "gcenter-xxxxxxxx.domain.local",
        "event_type": "tls",
        "src_ip": "1.2.3.4",
        "dest_port": 443,
        "in_iface": "mon2",
        "tls": {
            "sni": "www.microsoft.com",
            "version": "TLS 1.3",
            "ja3s": {
                "string": "771,4866,43-51",
                "hash": "15af977ce25de452b96affa2addb1036"
            }
        },
        "@version": "1",
        "proto": "TCP",
        "gcap": "gcap-xxxxxxxxx.domain.local",
        "@timestamp": "2024-11-21T13:02:44.291Z"
    }
    ```



