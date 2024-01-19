# External integration: OpenCTI

## Objective

Collect Sekoia.io CTI feed in an existing self-managed OpenCTI instance for any operational purpose (such as CTI aggregation, dissemination, hunting...). 

## Prerequisites

- An operational OpenCTI instance with administrator privileges
- An active Sekoia.io licence with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key with  [**all CTI permissions**](https://docs.sekoia.io/getting_started/Permissions/#cti-permissions)

## Configuration

1. Add the following code **to the end** of **docker-compose.yml** file in the OpenCTI docker repository
    
    ```YAML
    connector-sekoia:
        image: opencti/connector-sekoia:latest
        environment:
          - OPENCTI_URL=http://opencti:8080
          - OPENCTI_TOKEN=${OPENCTI_ADMIN_TOKEN}
          - CONNECTOR_ID=<Replace_by_email>
          - CONNECTOR_TYPE=EXTERNAL_IMPORT
          - CONNECTOR_NAME=SEKOIA.IO
          - CONNECTOR_SCOPE=identity,attack-pattern,course-of-action,intrusion-set,malware,tool,report,location,vulnerability,indicator,campaign,infrastructure,relationship
          - CONNECTOR_CONFIDENCE_LEVEL=15 # From 0 (Unknown) to 100 (Fully trusted)
          - CONNECTOR_UPDATE_EXISTING_DATA=false
          - CONNECTOR_LOG_LEVEL=info
          - SEKOIA_API_KEY=<Replace_by_Sekoia_API_key>
          - SEKOIA_COLLECTION=d6092c37-d8d7-45c3-8aff-c4dc26030608
          - SEKOIA_START_DATE=2022-01-01    # Optional, the date to start consuming data from. Maybe in the formats YYYY-MM-DD or YYYY-MM-DDT00:00:00
          - SEKOIA_CREATE_OBSERVABLES=true  # Create observables from indicators
        restart: always
        depends_on:
          - opencti
    
    volumes:
      esdata:
      s3data:
      redisdata:
      amqpdata:
    ```

2. Replace the following parameters:
    - `CONNECTOR_ID`= Replace_by_email or an UUID4
    - `CONNECTOR_SCOPE` = identity,attack-pattern,course-of-action,intrusion-set,malware,tool,report,location,vulnerability,indicator,campaign,infrastructure,relationship => Sekoia Intelligence elements set to be exported in OpenCTI that can be chosen from this list
    - `SEKOIA_API_KEY`= Sekoia API key with CTI_Permissions
    - `SEKOIA_START_DATE`= <start_date_to_retrieve_feed> e.g. 2023-05-01

3. Build and launch Sekoia connector
    - Build    `docker-compose pull connector-sekoia`
    - Run      `docker-compose up -d connector-sekoia`
    
    !!!note
        Sekoia connector should be named **connector-sekoia** as described in the previous section. 
        To check all connectors available and set in the server, type `docker-compose ps`. 

4. Check if Sekoia connector is running
    ```
    docker-compose ps connector-sekoia
    ```

## Connect to OpenCTI

1. In a Web browser, type the following URL and replace `server_IP` and `port` by their values: http://server_ip:port/dashboard
    ![OpenCTI_login](/assets/intelligence_center/opencti_1.png){: style="width: 40%; max-width: 40%"}

2. Enter your login and password set in the **.env** file

## Sekoia Intelligence in OpenCTI

1. First of all, check if the connector is running and up to date. Go to Sekoia connector **Data > Connectors > Sekoia.io**
    ![OpenCTI_Sekoia_connector1](/assets/intelligence_center/opencti_2.png){: style="width: 60%; max-width: 60%"}

    On this page, you can find the following information: 
   
    - `Update date`:  Last update date of the connector in OpenCTI
    - `Status`:   Status of the connector in OpenCTI
    - `Perimeter`:    Sekoia Intelligence feed set for import in `docker-compose.yml` file under **CONNECTOR_SCOPE**
    - `Last cursor`:  **SEKOIA_START_DATE** set in `docker-compose.yml` file in base64 format

    ![OpenCTI_Sekoia_connector2](/assets/intelligence_center/opencti_3.png){: style="width: 80%; max-width: 80%"}

2. Navigate the Sekoia Intelligence Feed
   
Here are the elements of the Sekoia feed that can be found on OpenCTI after export:

|OpenCTI|Sekoia.io|
|--|--|
|Analysis|Threat-reports|
|Observations|Sightings|
|Arsenal|Malwares|
|Techniques|Intrusion-sets|
|Data|Indicators|

3. Find a Sekoia.io Indicator
   
Here is an example with an indicator:
- In **Sekoia.io**, search for the indicator `blog.google` in the Intelligence Page
        ![OpenCTI_search1](/assets/intelligence_center/opencti_indicator_search1.png){: style="width: 100%; max-width: 100%"}
    
- In **OpenCTI**, look for this indicator in the Data page
    ![OpenCTI_search2](/assets/intelligence_center/opencti_indicator_search2.png){: style="width: 100%; max-width: 100%"}
    
- The content of the indicator will look like the one below
    ![OpenCTI_Sekoia_search2](/assets/intelligence_center/sekoia_indicator.png){: style="width: 100%; max-width: 100%"}

## Troubleshoot

|Issue|Action|Linux command|
|--|--|--|
|Space disk full|check the logs|docker logs <container-id>|
|Conflict with containers|list containers on server|docker-compose ps|

## Other resources

[OpenCTI official documentation](https://github.com/OpenCTI-Platform/opencti)

[OpenCTI - Using Docker](https://docs.opencti.io/5.7.X/deployment/installation/#using-docker) 

[OpenCTI - Connector Configuration](https://docs.opencti.io/5.8.X/deployment/connectors/#connector-configuration) 

