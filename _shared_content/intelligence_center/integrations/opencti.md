# External integration: OpenCTI

## Objective

Collect Sekoia.io CTI feed in an existing OpenCTI instance self managed, for any operational purpose such as CTI aggregation, dissemination, hunting...

## Prerequisites:
- An operational OpenCTI instance with administrator privileges
- An active Sekoia.io licence with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key with [CTI permissions](https://docs.sekoia.io/getting_started/Permissions/#cti-permissions)

## 1. Configuration

1- Add the following code **to the end** of **docker-compose.yml** file in the OpenCTI docker repository

````
connector-sekoia:
    image: opencti/connector-sekoia:latest
    environment:
      - OPENCTI_URL=http://opencti:8080
      - OPENCTI_TOKEN=${OPENCTI_ADMIN_TOKEN}
      - CONNECTOR_ID=<Replace_by_email>
      - CONNECTOR_TYPE=EXTERNAL_IMPORT
      - CONNECTOR_NAME=SEKOIA.IO
      - CONNECTOR_SCOPE=identity,attack-pattern,course-of-action,intrusion-set,malware,tool,report,location,vulnerability,indicator
      - CONNECTOR_CONFIDENCE_LEVEL=15 # From 0 (Unknown) to 100 (Fully trusted)
      - CONNECTOR_UPDATE_EXISTING_DATA=false
      - CONNECTOR_LOG_LEVEL=info
      - SEKOIA_API_KEY=<Replace_by_Sekoia_API_key>
      - SEKOIA_COLLECTION=d6092c37-d8d7-45c3-8aff-c4dc26030608
      - SEKOIA_START_DATE=2022-01-01    # Optional, the date to start consuming data from. Maybe in the formats YYYY-MM-DD or YYYY-MM-DDT00:00:00
      - SEKOIA_CREATE_OBSERVABLES=true  # Create observables from indicators
    depends_on:
      - opencti

volumes:
  esdata:
  s3data:
  redisdata:
  amqpdata:
````

Replace following parameters:
- `CONNECTOR_ID`=_<Replace_by_email>_
- `CONNECTOR_SCOPE` =_identity,attack-pattern,course-of-action,intrusion-set,malware,tool,report,location,vulnerability,indicator_ => Sekoia intelligence elements set to be exported in OpenCTI that can be chosen in this list
- `SEKOIA_API_KEY`=_<Sekoia_API_key_with_CTI_Permissions>_
- `SEKOIA_START_DATE`=_<start_date_to_retrieve_feed>_ e.g. _2023-05-01_

2- Build and launch Sekoia connector
- Build    `docker-compose pull connector-sekoia`
- Run      `docker-compose up -d connector-sekoia`

!!note
   Sekoia connector should be name **connector-sekoia** as describe on top
   **docker-compose ps**   to check all connectors available and set on the server

3- Check if Sekoia connector is running
`docker-compose ps connector-sekoia`

## 2. Connect to OpenCTI

1-  In a Web browser, type the following	_http://<server_ip>:<port>/dashboard_
![OpenCTI_login](../OpenCTI_images/opencti-login.png)

2- Enter your login and password set in **.env** file

## 3. Sekoia intelligence in OpenCTI

**1- Check if the connector is running and up to date**

Go to Sekoia connector    _Data > Connectors > Sekoia.io >_
![OpenCTI_Sekoia_connector1](../OpenCTI_images/open-cti-connectors.png)

In this page, the interesting information can be found about:

- `Update date` :  Last update date of the connector in OpenCTI
- `Status` :	   Status of the connector in OpenCTI
- `Perimeter` :    Sekoia intelligence feed set for import in _docker-compose.yml_ file under **CONNECTOR_SCOPE**
- `Last cursor` :  **SEKOIA_START_DATE** set in _docker-compose.yml_ file in base64 format

![OpenCTI_Sekoia_connector2](../OpenCTI_images/opencti-sekoia.png)
    
**2- Where to find Sekoia intelligence feed**

Here are the elements of the Sekoia feed that can be found on OpenCTI after export:

|OpenCTI|Sekoia.io|
|--|--|
|Analysis|Threat-reports|
|Observations|Sightings|
|Arsenal|Malwares|
|Techniques|Intrusion-sets|
|Data|Indicators|


## 3- Troubleshoot
|Issue|Action|Linux command|
|--|--|--|
|Space disk full|check the logs|docker logs <container-id>|
|Conflict with containers|list containers on server|docker-compose ps|

## 5- Other resources
- **OpenCTI official documentation**
  
https://github.com/OpenCTI-Platform/opencti

https://docs.opencti.io/5.7.X/deployment/installation/#using-docker

https://docs.opencti.io/5.8.X/deployment/connectors/#connector-configuration
