## Retrieve events linked to a file access

**Can Sekoia.io Endpoint Agent (Windows) retrieve events linked to file accesses such as denied access to file, modification on file, ...?**

Sekoia.io Agent tracks information on file creation / deletion but not for denied / modified access.
However, an event will probably be linked to a process that tries to open a file. 

## Add Windows Event ID to a file the endpoint agent loaded

**Is it possible to add a Windows Event ID to a file that Sekoia.io Agent loaded?**

It is not possible to add an Event ID. 

For each Event ID, we format the event to follow our Taxonomy (ECS norm) so we cannot add them on the fly.

However, we welcome any suggestions of Event IDs to be collected that seems relevant.

## Retrieve events linked to blocked accounts on AD

**Is Sekoia.io Agent allowed to retrieve events linked to blocked accounts on AD?**

It is not possible at the moment.
This subject has been identified for improvement of Sekoia.io Agent integration with AD.

## Sekoia.io Agent version 0.2.8

**What brings the new Sekoia.io Agent version 0.2.8 in comparison to other versions?**
The Agent 0.2.8 will bring the following elements:

   - Automatic update of the Agent
   - Improvement of Integration with rules produced by Sekoia.io analysts
   - Collect new event types

## DNS logs

**Are DNS logs collected by Sekoia.io agent?**

Yes, DNS logs are collected by the Agent in the Windows version through system calls. It's not available in the Linux version at the moment. 

## Sekoia.io Agent and Sysmon

**Will there be any duplicates when using SEKOIA Agent and Sysmon? For instance, what happens if I search for events in my Sysmon configuration that are already sent by the Sekoia.io agent?**

For some events, the Agent will ignore Sysmon events as it will already cover the same scope and in the same way. Here are some examples:

- sysmonProcessCreation
- sysmonNetworkConnection
- sysmonProcessTerminated
- sysmonCreateRemoteThread
- sysmonFileCreate
- sysmonDNSEvent
- sysmonFileDelete
- sysmonFileDeleteDetected

## Sekoia.io Agent and ANSSI recommendations

**Do you confirm that Sekoia.io Agent (without Sysmon) will apply all SEKOIA rules and ANSSI recommendations? Is it an ongoing subject?**

We plan to cover all the ANSSI recommendations and SEKOIA rules to the greatest extent in the next beta.

## Remove Sysmon option 

**Do you plan to remove the possibility to select Sysmon option or will we allow users to add a Sysmon configuration?**

We most probably will support Sysmon for users who wish to continue using it. 

## Is the agent useful for monitoring a Docker or Kubernetes host?

The Sekoia agent, based on Auditd, is designed to effectively monitor system activities across various Linux technologies, including machines hosting Docker or Kubernetes. While this agent focuses on system logs from the host machine, it can observe some data related to executions within containers. However, it is not specifically tailored to manage Docker or Kubernetes technologies directly and won't capture specific application logs. Consequently, it may provide a lower level of detail compared to specialized tools designed for these environments.

For instance, if a Docker container makes a DNS request or accesses a file on the host, these activities will be captured by the agent just as they would for any application executed on the host. 

