uuid: 40adc8cc-8147-47c5-afdf-dcb9c641e554
name: Splunk
type: intake


## Overview

Splunk is a powerful data platform that enables organizations to search, monitor, and analyze machine-generated data in real-time. It provides a comprehensive and centralized approach to collecting, indexing, and correlating large volumes of log and event data from various sources. Splunk allows users to gain valuable insights, troubleshoot issues, detect anomalies, and generate reports based on the data gathered. It is widely used for security information and event management (SIEM), as well as for monitoring and analyzing the performance of IT systems and applications. Splunk's versatility makes it a valuable tool for organizations seeking to derive actionable intelligence from their data.

## Configure

This setup guide will show you how to forward alerts produced by a Splunk instance to Sekoia.io using a Splunk webhook action. The objective of this integration is to transmit alerts for notification purposes, with the understanding that the investigation will be conducted on the Splunk platform.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Splunk`.

### Configure your Splunk instance

Initially, you should create a Splunk search that aligns with your requirements. Subsequently, save this search as an alert and configure it by following the provided form. Finally, define a Webhook action and include the following URL:: `https://intake.sekoia.io/plain?intake_key=YOUR-INTAKE-KEY` 

The webhook alert action will passes JSON formatted information about the alert to Sekoia.io. You can find more details about this action [here](https://docs.splunk.com/Documentation/Splunk/9.1.3/Alert/Webhooks)
