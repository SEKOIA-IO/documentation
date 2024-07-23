
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "403"


    ```json
	{
        "Action": "block",
        "ClientIP": "113.206.179.28",
        "ClientRequestHost": "foo-bar-baz.xyz",
        "ClientRequestMethod": "GET",
        "ClientRequestPath": "/static/favicon.ico",
        "ClientRequestQuery": "",
        "Datetime": 1657630626219000000,
        "EdgeResponseStatus": 403,
        "RayID": "7299f155dda47d6b"
    }
    ```



=== "block"


    ```json
	{
        "Action": "block",
        "ClientASN": 4562,
        "ClientASNDescription": "PERFORMIVE",
        "ClientCountry": "us",
        "ClientIP": "10.6.12.26",
        "ClientIPClass": "noRecord",
        "ClientRefererHost": "",
        "ClientRefererPath": "",
        "ClientRefererQuery": "",
        "ClientRefererScheme": "",
        "ClientRequestHost": "foo-bar-baz.xyz",
        "ClientRequestMethod": "GET",
        "ClientRequestPath": "/.env",
        "ClientRequestProtocol": "HTTP/1.1",
        "ClientRequestQuery": "",
        "ClientRequestScheme": "http",
        "ClientRequestUserAgent": "Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30",
        "Datetime": 1669858111716000000,
        "EdgeColoCode": "EWR",
        "EdgeResponseStatus": 403,
        "Kind": "firewall",
        "MatchIndex": 0,
        "Metadata": {
            "group": "cloudflare_specials",
            "rule_message": "Version Control - Information Disclosure"
        },
        "OriginResponseStatus": 0,
        "OriginatorRayID": "00",
        "RayID": "77280bee38a6c461",
        "RuleID": "100016",
        "Source": "waf"
    }
    ```



