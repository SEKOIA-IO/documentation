# External integration: OpenCTI

## Objective

Collect Sekoia.io CTI feed in an existing OpenCTI instance self managed, for any operational purpose such as CTI aggregation, dissemination, hunting...

## Prerequisites for the public documentation:
- An operational OpenCTI instance with administrator privileges
- An active Sekoia.io licence with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key

## Configuration

### 2-1- Feed on Sekoia.io

By default, all Sekoia.io CTI feed will be consumed in OpenCTI

Besides, it is possible to create a custom feed that will also be consumed in OpenCTI

Please refer to this [page]( https://docs.sekoia.io/cti/features/consume/feeds/#create-new-feed) for Custom feed creation

## 2-2- Setup OpenCTI

    !!!note
        This is a summary of the main steps to follow for Setup.
        Please note that the setup might be updated by OpenCTI
        
        Thank you for your understanding.
        
        As a reference, please find the installation guide with docker to Linux on OpenCTI documentation 
        https://docs.opencti.io/5.7.X/deployment/installation/#using-docker

#### 2-2-1. Clone the repository
1. create a repo for your OpenCTI connector
2. clone OpenCTI connector

```
git clone https://github.com/OpenCTI-Platform/docker.git
```

#### 2-2-2. Configure the environment

1. rename the file `.env.sample` to `.env`  (contain environment variables for Docker)
2. Change the following variables value:
- OPENCTI_ADMIN_EMAIL= *to be set by user*
- OPENCTI_ADMIN_PASSWORD= *to be set by user*
- OPENCTI_BASE_URL=http://*your_server_IP*:*port*

#### 2-2-3. Memory management settings

set the `vm.max_map_count` in `systcl` file before running the containers, as mentioned in the [ElasticSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode).

```
sudo sysctl -w vm.max_map_count=1048575
```

#### 2-2-4. Setup Sekoia Docker
1. Create a separate repo for Sekoia Docker and go to this repo

```
mkdir sekoia-docker
cd sekoia-docker
```

3. Setup Docker in this repo by cloning the repo of  the following https://github.com/OpenCTI-Platform/connectors/tree/master/external-import/sekoia

```
git clone https://github.com/OpenCTI-Platform/connectors/tree/master/external-import/sekoia
```

3. Change the following variables value in the docker-compose file :
   - OPENCTI_URL
   - OPENCTI_TOKEN
   - CONNECTOR_ID
   - SEKOIA_API_KEY = <to be created in [Sekoia.io](http://Sekoia.io) with the IC permissions>

Using for example VIM

```
Vim docker-compose
```

For more information, please refer to [OpenCTI documentation on connector setting](https://docs.opencti.io/5.8.X/deployment/connectors/#connector-configuration)
        

#### 2-2-5. Run OpenCTI

After changing your `.env` file (step 2), please run `docker-compose` in detached (-d) mode:

```
sudo systemctl start docker.service
```

Then Run docker-compose in detached

```
Sudo docker-compose up -d
```

#### 2-2-6. Launching OpenCTI services

```
sudo docker stack deploy --compose-file docker-compose.yml opencti
```

You can now go to `http://localhost:<your_server_port>`  (Port is usually `8080`) and log in with the credentials configured in your environment variables.

## 3- Feed consumption
#### Search for an IOC
**- Sekoia.io**

Please refer to this [documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#search-for-objects)

**- OpenCTI**
- Objects and Relations of Sekoia.io CTI will be available in OpenCTI with the tag Sekoia and not 
- Objects and Relations will be displayed in STIX in OpenCTI
    

## 4- Troubleshoot

**Differences between Sekoia.io and OpenCTI ?**

- Check IOCs dates / updates
- Volume
- Latency of Feed updates might happen


## 5- Other resources
- **OpenCTI official documentation**

https://github.com/OpenCTI-Platform/opencti
https://docs.opencti.io/5.7.X/deployment/installation/#using-docker
https://docs.opencti.io/5.8.X/deployment/connectors/#connector-configuration

- **Sekoia docker**

https://github.com/OpenCTI-Platform/connectors/tree/master/external-import/sekoia
