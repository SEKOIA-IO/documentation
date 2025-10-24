
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_1"

    ```
	2025-05-26,13:41:00,64,1977,651,2628,5.6.7.8,5.6.7.8,john.doe@example.com,POST,https,-,aws-sdk-go/1.55.5 (go1.23.8; windows; amd64) amazon-ssm-agent/3.3.2471.0,application/x-amz-json-1.1,200,application/x-amz-json-1.1,example.eu-north-1.amazonaws.com,example.eu-north-1.amazonaws.com,/,443,-,2222222222222222222,Client,Amazon Systems Manager,SE,59.328700,18.071700,Stockholm,Stockholm County,100 04,SE,59.328700,18.071700,Stockholm,Stockholm County,100 04,Windows 11,Native,-,Windows Device,-,1748266860,111111111111111111111111,5.6.7.8,CloudApp,-,IT Service/Application Management,"IT Service/Application Management, Technology, All Categories",http_transaction,-,-,3333333333333333333,3333333333333333333,example.eu-north-1.amazonaws.com,-,14,"14, 564, 10001",-,-,2d908070f157946cc4ea9dca39dbe374,NotAvailable,No,-,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,No,No,NotChecked,NotChecked,NotChecked,No,Allow,Established,None,NotEstablished,5.6.7.8,5.6.7.8,example.eu-north-1.amazonaws.com,Sni,"Technology, All Categories, IT Service/Application Management",Decrypt,-,TLSv1.3,TLS_AES_256_GCM_SHA384,NotChecked,NotChecked,5.6.7.8,FR-PAR1,5.6.7.8,64362,5.6.7.8,443,-,-,5.6.7.8,790,-,-,-,-,-,https://example.eu-north-1.amazonaws.com/,/,HTTP1.1,200,IT Service/Application Management,92,excellent,"Enterprise,Unsanctioned",Amazon,202533540828,-,Untagged,View,-,-,-,-,-,-,-,-,-,-,-,-,2025-05-26 15:41:00,alert,Web Access Allow,5.6.7.8,5.6.7.8,example.eu-north-1.amazonaws.com,HttpHostHeader,-,-,-
    ```



=== "test_2"

    ```
	2025-05-26,13:41:17,292,731,9567,10298,1.2.3.4,1.2.3.4,john.doe@example.com,GET,https,clientId=1234567890&agents=Edge%2CEdgeConfig%2CEdgeServices%2CEdgeFirstRun%2CEdgeFirstRunConfig&osname=win&client=edge&channel=stable&scpfre=0&osarch=x86_64&osver=10.0.22631&wu=1&devicefamily=desktop&soobedate=1742540504&uma=0&sessionid=1011&mngd=0&installdate=1742540615&edu=0&vm=1&bphint=0&fg=1&lbfgdate=1747398666&lafgdate=0,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.2.3.4 Safari/537.36 Edg/1.2.3.4",-,200,application/json,config.edge.skype.com,config.edge.skype.com,/config/v1/Edge/136.0.3240.92?clientId=1234567890&agents=Edge%2CEdgeConfig%2CEdgeServices%2CEdgeFirstRun%2CEdgeFirstRunConfig&osname=win&client=edge&channel=stable&scpfre=0&osarch=x86_64&osver=10.0.22631&wu=1&devicefamily=desktop&soobedate=1742540504&uma=0&sessionid=1011&mngd=0&installdate=1742540615&edu=0&vm=1&bphint=0&fg=1&lbfgdate=1747398666&lafgdate=0,443,-,2071157430488732926,Client,-,US,47.682220,-122.123009,Redmond,Washington,N/A,SE,59.328700,18.071700,Stockholm,Stockholm County,100 04,Windows 11,Edge,1.2.3.4,Windows Device,skype,1748266877,0,1.2.3.4,Web,-,Technology,"Technology, All Categories",http_transaction,-,-,3333333333333333333,3333333333333333333,config.edge.skype.com,-,564,"564, 10001",-,-,2d908070f157946cc4ea9dca39dbe374,NotAvailable,No,-,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,No,No,NotChecked,NotChecked,NotChecked,No,Allow,Established,None,NotEstablished,1.2.3.4,1.2.3.4,config.edge.skype.com,Sni,"Technology, All Categories",Decrypt,-,TLSv1.3,TLS_AES_256_GCM_SHA384,NotChecked,NotChecked,1.2.3.4,SE-STO1,1.2.3.4,64362,1.2.3.4,443,-,-,1.2.3.4,795,-,-,-,-,-,https://config.edge.skype.com/config/v1/Edge/136.0.3240.92?clientId=1234567890&agents=Edge%2CEdgeConfig%2CEdgeServices%2CEdgeFirstRun%2CEdgeFirstRunConfig&osname=win&client=edge&channel=stable&scpfre=0&osarch=x86_64&osver=10.0.22631&wu=1&devicefamily=desktop&soobedate=1742540504&uma=0&sessionid=1011&mngd=0&installdate=1742540615&edu=0&vm=1&bphint=0&fg=1&lbfgdate=1747398666&lafgdate=0,/config/v1/Edge/136.0.3240.92,HTTP1.1,200,-,-,-,-,-,-,-,-,Browse,-,-,File,-,-,text/plain,Text,-,8715,-,-,-,2025-05-26 15:41:18,alert,Web Access Allow,1.2.3.4,1.2.3.4,config.edge.skype.com,HttpHostHeader,-,-,-
    ```



=== "test_3"

    ```
	2025-05-26,13:41:27,7,872,1075,1947,9.10.11.12,9.10.11.12,john.doe@example.com,GET,https,-,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/9.10.11.12 Safari/537.36 Edg/9.10.11.12",-,304,-,pypi.org,pypi.org,/,443,-,111111111111111111111111,Client,PyNLPl,US,37.764200,-122.399300,San Francisco,California,94107,SE,59.328700,18.071700,Stockholm,Stockholm County,100 04,Windows 11,Edge,9.10.11.12,Windows Device,pypi,1748266887,0,9.10.11.12,CloudApp,-,Development Tools,"Development Tools, All Categories",http_transaction,-,-,2222222222222222222,2222222222222222222,pypi.org,-,29,"29, 10001",-,-,2d908070f157946cc4ea9dca39dbe374,NotAvailable,No,-,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,NotChecked,No,No,NotChecked,NotChecked,NotChecked,No,Allow,Established,None,NotEstablished,9.10.11.12,9.10.11.12,pypi.org,Sni,"All Categories, Development Tools",Decrypt,-,TLSv1.3,TLS_AES_256_GCM_SHA384,NotChecked,NotChecked,9.10.11.12,FR-PAR1,9.10.11.12,64362,9.10.11.12,443,-,-,9.10.11.12,836,-,-,-,-,-,https://pypi.org/,/,HTTP1.1,304,Development Tools,47,poor,"Enterprise,Unsanctioned",-,-,-,-,Browse,-,-,-,-,-,-,-,-,-,-,-,-,2025-05-26 15:41:28,alert,Web Access Allow,9.10.11.12,9.10.11.12,pypi.org,HttpHostHeader,-,-,-
    ```



