# Use your own CTI

[IOC Collections](../features/detect/ioccollections.md) can be used to use your own CTI inside Sekoia.io's XDR.

This section will show how to programmatically add your CTI inside the platform and how to take profit of it.

## Prerequisites

- A Sekoia.io XDR license
- An API Key with that contains at least the following permissions:
    * INTHREAT_READ_IOC_COLLECTIONS
    * INTHREAT_WRITE_IOC_COLLECTIONS

## Detect threats using your CTI

By creating custom CTI rules for your IOC collections it is possible to detect threats based on your own indicators. To setup this kind of rules follow [the dedicated section in the IOC Collections documentation](../features/detect/ioccollections.md#detect-threats-using-ioc-collections).

## Push CTI

### Python requirements

The code samples provided below need the following python library:

- requests
- websockets

In order to install them the command `pip install requests websockets` can be used. 

### Create an IOC collection

The first step is to create an IOC collection. It can be done manually following [the dedicated documentation](../features/detect/ioccollections.md#create-an-ioc-collection) or automatically relying on the REST endpoint:

```py
import requests

api_key = "{Your API Key}" # (1)!
headers = {
    "authorization": f"Bearer {api_key}"
}
payload = {"name": "My IOC Collection"}
res = requests.post(
    "https://api.sekoia.io/v2/inthreat/ioc-collections",
    headers=headers, 
    json=payload,
)
res.raise_for_status()
print(f"Collection created with id {res.json()['id']}")
```

1. Replace the content of this string with your API Key

!!! tip
    When creating an IOC Collection it is also possible to specify:

    - A description using the `description` field
    - For Multi-tenant users it is possible to specify:
        - For which sub-community the collection must be created for by providing the `community_uuid` attribute
        - If the collection must be made available to sub-communities by  setting `available_for_sub_communities` to  `true`.

### Import indicators from text

The first way to import indicators is to do it providing a raw text format where each line contains one indicator.
The first part of the snippet is about creating the import task, while the second part waits until the import finishes.

```py
import json

import requests
from websockets.sync.client import connect


api_key = "{Your API Key}"  # (1)!
collection_id = "ioc-collection--xxx"  # (2)!

# First we create the import task
headers = {
    "authorization": f"Bearer {api_key}"
}
observables_text = """
microsoftsvc.com
178.236.246.57
d30bb9df615a8d1661f843d426ff40eb,4344e695b5f65917dc68f241ecde4b99cf25d930
"""  # (3)!
payload = {
    "indicators": observables_text,
    "x_ic_related_threat_refs": ["intrusion-set--202fc7e0-1580-4ad1-83d8-5f98be4fe1a2"],  # (4)!
} # (5)!
res = requests.post(
    f"https://api.sekoia.io/v2/inthreat/ioc-collections/{collection_id}/indicators/text",
    headers=headers,
    json=payload
)
res.raise_for_status()
task_id = res.json()["task_id"]

# Then we wait for the import to finish
headers = {"Cookie": f"access_token_cookie={api_key}"}
with connect("wss://app.sekoia.io/live/", additional_headers=headers) as websocket:  # (6)!
    while True:
        raw_message = websocket.recv()
        message = json.loads(raw_message)
        if message.get("type") == "ioc-collection" and message["attributes"].get("task_id") == task_id:  # (7)!
            imported = message["attributes"]["imported"]
            total = message["attributes"]["total"]
            print(f"Imported {imported}/{total}")
            if imported == total:
                break
print("Import finished")
```

1. Replace the content of this string with your API Key
2. Replace the content of this string with the id of the collection the IOC must be added to
3. One IOC per line. Hashes belonging to the same IOC can be added on the same line separated by a comma
4. It is possible to link the created indicators to several threats by providing their ids inside the `x_ic_related_threat_refs` field.
5. When importing indicators various attributes can be provided like the validity dates, a description, the kill chain phases, ... 
To get information about them check [the documentation about this endpoint](https://docs.sekoia.io/cti/develop/rest_api/intelligence/#tag/IOC-Collections/operation/post_collection_indicators_text_resource)
6. Connect to `LiveAPI` using a websocket to be notified in real time of events happening in the community
7. Keep only messages that are about our task


### Import indicators from file

In this sample we will import IOC from a file. The formats currently supported along with their mime types are:

- CSV: `text/csv`, `application/csv` or `text/plain`
- XLS: `application/vnd.ms-excel` or `application/octet-stream`
- XLSX: `application/zip` or `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

The first step consists of uploading the file to obtain a preview. In the response of this requests we will obtain:

- A file handle that must be used to process the file
- A preview of the first lines of the file
- The detected mapping: Which column contains the indicator, the validity dates, the kill chain, the threat, ...
- Whether the first line has been detected to be ignored or not

Once the preview has been generated, if everything seems right the file can be processed.
The last step is to wait for the file to be completely processed. Depending on the number of indicators it can take a bit of time.

```py
import json

import requests
from websockets.sync.client import connect


api_key = "{Your API Key}"  # (1)!
collection_id = "ioc-collection--xxx"  # (2)!

# First we generate a preview of the file
headers = {
    "authorization": f"Bearer {api_key}"
}
files = {"file": ("file", open("path/to/file.csv", "rb"), "text/csv")}  # (3)!
res = requests.post(
    f"https://api.sekoia.io/v2/inthreat/ioc-collections/{collection_id}/indicators/files/preview",
    headers=headers,
    files=files,
)
res.raise_for_status()
content = response.json()

# Then we ask the API to process the file
# The API guessed the mapping and whether the first line must be ignored or not,
# but in this case we assume we know it and provide it manually.
# Update this mapping depending on your files (one type per column).
payload = {
    "file_handle": content["file_handle"],  # (4)!
    "mapping": [
        "observable",  # (5)!
        "valid_from",
        "valid_until",
        null,  # (6)!
        "kill_chain_phases",  # (7)!
        "x_ic_related_threat_refs",  # (8)!
    ],
    "ignore_first_line": True,  # (9)!
}  # (10)!

res = requests.post(
    f"https://api.sekoia.io/v2/inthreat/ioc-collections/{collection_id}/indicators/files/process",
    headers=headers,
    json=payload,
)
res.raise_for_status()
task_id = res.json()["task_id"]

# Then we wait for the import to finish
headers = {"Cookie": f"access_token_cookie={api_key}"}
with connect("wss://app.sekoia.io/live/", additional_headers=headers) as websocket:  # (11)!
    while True:
        raw_message = websocket.recv()
        message = json.loads(raw_message)
        if message.get("type") == "ioc-collection" and message["attributes"].get("task_id") == task_id:  # (12)!
            imported = message["attributes"]["imported"]
            total = message["attributes"]["total"]
            print(f"Imported {imported}/{total}")
            if imported == total:
                break
print("Import finished")
```

1. Replace the content of this string with your API Key
2. Replace the content of this string with the id of the collection the IOC must be added to
3. Update this line with the path to the file to import and the appropriate mime type
4. The file handle must be used to process the file in the next call
5. The column containing the indicator value is named `observable`
6. Columns not linked to any attribute must be set to `null`
7. The kill chain phase names must match a tactic from MITRE ATT&CK or a phase from the cyber kill chain.
Several values can be specified separated by commas.
8. The name of the threats must be known inside the intelligence center. 
Several values can be specified separated by commas. i.e. `Phishing,APT-29`
9.  If the first line contains the columns names we can ignore it when processing the file
10.  When importing indicators various attributes can be provided like the validity dates, a description, the kill chain phases, ... 
To get information about them check [the documentation about this endpoint](https://docs.sekoia.io/cti/develop/rest_api/intelligence/#tag/IOC-Collections/operation/post_collection_indicators_text_resource)
11.   Connect to `LiveAPI` using a websocket to be notified in real time of events happening in the community
12.    Keep only messages that are about our task
