
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_event"


    ```json
	{
        "message": "2023-07-20T09:15:02+00:00 localhost ulog[568]: [0000F4E4] qid=aaa1bbb2cc3,ip=1.2.3.4,sender=test@test.com,site=VSC000001,domain=maildomain.com,recipient=demo_1@maildomain.com: action=drop,status=virus,spamlevel=unknwon,tag=[VIRUS],stop=nil,reply=2,subject=\"Some subject\"",
        "site": "VSC000001",
        "from": "test@test.com",
        "to": "demo_1@maildomain.com",
        "subject": "Some subject",
        "date": 1689844502000,
        "operationType": "DROP",
        "messageType": "VIRUS",
        "messageId": "aaa1bbb2cc3",
        "hostname": "localhost",
        "filterType": "UNKNOWN",
        "filterReason": "2",
        "spamLevel": "UNKNWON",
        "domain": "maildomain.com",
        "ip": "1.2.3.4",
        "tag": "[VIRUS]"
    }
    ```



