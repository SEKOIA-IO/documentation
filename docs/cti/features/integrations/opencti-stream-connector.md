# OpenCTI Sekoia.io Intel Stream Connector

## Overview

The OpenCTI Sekoia.io Intel Stream Connector is a real-time integration that allows organizations to automatically feed their Sekoia.io IOC (Indicator of Compromise) collections with threat intelligence from their OpenCTI platform.

This stream connector listens to live data streams from OpenCTI and synchronizes indicators to Sekoia.io IOC collections in real-time, enabling seamless threat intelligence sharing between the two platforms.

## Key Features

- **Real-time Synchronization**: Automatically pushes indicators from OpenCTI to Sekoia.io as they are created or updated
- **Bidirectional Operations**: Supports both creation and deletion of indicators
- **Stream-based Architecture**: Listens to OpenCTI live streams for immediate data transfer
- **Flexible Filtering**: Works with OpenCTI stream filters to control which data is synchronized
- **Multiple Collections**: Supports multiple connector instances for different IOC collections

## How It Works

The connector operates as a stream listener that:

1. Connects to a configured OpenCTI live stream
2. Monitors for indicator creation, update, and deletion events
3. Transforms OpenCTI indicators into Sekoia.io IOC format
4. Pushes the IOCs to the specified Sekoia.io collection via API
5. Handles indicator revocation when indicators are deleted in OpenCTI

## Requirements

- **Python**: 3.11.x (not compatible with 3.12+)
- **OpenCTI Platform**: 6.8.x or higher
- **pycti**: 6.8.x or higher
- **Sekoia.io Account**: With API access and an existing IOC collection

## Configuration Prerequisites

Before setting up the connector, you need:

- A Sekoia.io API key with appropriate permissions (IoC Collections)
- An existing IOC collection in Sekoia.io (the connector does not create collections)
- The UUID of the target IOC collection
- A configured live stream in OpenCTI with appropriate filters

## Limitations

- **Collection Limit**: Each IOC collection is limited to 500,000 indicators
- **Deletion Behavior**: Deleted indicators are revoked (not deleted) in Sekoia.io collections
- **Collection Creation**: IOC collections must be created manually in Sekoia.io before running the connector
- **One-to-One Mapping**: Each connector instance connects to one stream and one collection

## Recommended Architecture

- Create one OpenCTI stream (with appropriate filters) per Sekoia.io collection
- Deploy one connector instance per stream/collection pair
- Use stream filters in OpenCTI to control which indicators are sent to each collection

## For More Information

For detailed installation instructions, configuration parameters, and deployment options, please refer to the official connector repository:

**[OpenCTI Sekoia Intel Stream Connector on GitHub](https://github.com/OpenCTI-Platform/connectors/tree/master/stream/sekoia-intel)**

The repository includes:

- Complete configuration variable documentation
- Docker and manual deployment guides
- Sample configuration files
- Troubleshooting and debugging information
