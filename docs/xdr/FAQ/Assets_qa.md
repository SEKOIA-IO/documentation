## How to get the source of a discovered asset ?

In the Asset timeline, events that triggered an asset detection will be displayed.

**Steps:** Go to assets page, click on an asset then click on `See trigger event`.
![Assets_timeline](/assets/operation_center/FAQ/Assets_timeline.png){: style="max-width:80%"}

The details of the event will be displayed in the events page.

## Can a same asset be discovered by two different intakes ?

Only `account`, `host` and `network` will be taken into account in asset detection.

However, the information of the intake associated can be found by clicking on an event in the timeline.

!!! note
     For example, a source IP is a field that will be discovered as an atom extracted from an event.
     This atom can be attached to one or several assets (seen in the Atoms tab).
     Please consult [this documentation about atoms](https://docs.sekoia.io/xdr/features/collect/assets/#what-is-an-atom).

## Is there any impact on the assets set as "Reviewed" ?

There is no impact. However, it is useful in order to clearly identify and confirm the assets used.

## Is there any mechanism that automatically delete an asset if no events have been triggered after a given period ?

Asset management is crucial and it is important to manually monitor your assets frequently in order to have a clear view of their activities and validity.

## Are there any assets duplicates ?

It is possible to have asset duplicates originated from two different sources.

For example: 

1. The first asset discovered as **Marcel** is detected from an email.
2. The second asset discovered as **Marcel (Paris)** is detected from another service account.

Therefore, the same user will be displayed in the two assets.

## Can assets be created manually and also discovered automatically ?

It is possible to have assets created both manually and automatically. 

We suggest to users to manage their assets and keep the ones that are relevant.

## How are assets' duplicates managed ?

Assets are being enriched and updated according to detection rules.

Please find more information [here](https://docs.sekoia.io/xdr/features/collect/assets/#asset-discovery-rules).
