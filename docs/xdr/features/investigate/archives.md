## Overview

On SEKOIA.IO, events are usually stored 30 days on the platform. If there is a need to keep your logs stored for a longer period of time (to do an ad hoc investigation for example), you can now use the feature Archives to go through your past events and perform various searches on them.  

This feature allows to keep your events stored and archived by using a cloud storage like Amazon S3 pr OVHCloud. 

!!! note 
    To use the Archives feature, you must have the necessary permissions. For more information, contact our support. 

!!! info 
    You must subscribe to Amazon S3 or OVHCloud cloud storage features to be able to configure Archives. The pricing depends on the volume of data you want to archive. SEKOIA.IO support team can help you estimate the costs.

## The Archives page

The Archives feature is accessible on the `Archives page` in the Operations Center menu. 

On this page, a table lists all archives created by the user. 

| Column | Description |
| --- | --- |
| Name | Name of the archive |
| Provider | Where the archive is stored |
| Number of snapshots | How many snapshots were made since the archive was first created   |
| Created at | Creation date |
| Status  | Could be `success` or `error` |

### Views from archive tab

The archives tab lists all the different restorations that have been realized on this community. This view is only accessible internally for now.

## Create an archive

To create an archive, follow these instructions:

=== "Amazon S3"

    1. **Choose your archive destination**: it can be Amazon S3 storage or OVHcloud Object storage
    2. **Configure your bucket** (the data associated with the storage space) by providing the following information
        
        | Name | Description |
        | --- | --- |
        | Container/Bucket | Name of the bucket |
        | Region | The region associated with the bucket |
        | Access Key ID | ? |
        | Access Key Secret | ? |

    3. **Describe your archive**
    4. **Add GPK Key to access your events (optional)**: Archives are stored as GPG encrypted files so that the selected cloud provider does not have access to your events. You will always be able to load your archives inside SEKOIA.IO but if you want to access your events outside of the app, you can add your own public key.

=== "OVHCloud"

    1. **Choose your archive destination**: it can be Amazon S3 storage or OVHcloud Object storage
    2. **Configure your bucket** (the data associated with the storage space) by providing the following information
        
        | Name | Description |
        | --- | --- |
        | User name |  |
        | Password |  |
        | Tenant name |  |
        | Container name |  |

    3. **Describe your archive**
    4. **Add GPK Key to access your events (optional)**: Archives are stored as GPG encrypted files so that the selected cloud provider does not have access to your events. You will always be able to load your archives inside SEKOIA.IO but if you want to access your events outside of the app, you can add your own public key.

!!! info
    The format used in archives are logs compressed in JSON format with enrichments made by SEKOIA.IO. Since we keep the original logs and message fields, the volumes are therefore larger in the archives compared to the originals.

## How to access saved archives and re-hydrated events

When the archives feature is made available in a community, the Events page shows a new filter to list re-hydrated events. 

1. Click on `Search history` next to the search bar and select Re-hydrated events
2. Select which archive you want to upload 
3. Click on `Search` and wait for your re-hydrated logs to appear on the Events page 

!!! tip 
    If you can't find events you're searching for, try changing the date range.

!!! warning
    Detection rules and capabilities do not work on rehydrated events, which means that these events will not generate alerts. This feature only allows analysts to go through events and perform the usual searches enabled by the Events page.