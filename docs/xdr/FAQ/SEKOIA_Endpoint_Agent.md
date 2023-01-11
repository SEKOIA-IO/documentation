## Retrieve events linked to a file access

**Can SEKOIA.IO Endpoint Agent (Windows) retrieve events linked to file accesses such as denied access to file, modification on file, ...?**

SEKOIA.IO Agent tracks information on file creation / deletion but not for denied / modified access.
However, an event will probably be linked to a process that tries to open a file. 

## Add Windows Event ID to a file the endpoint agent loaded

**Is it possible to add a Windows Event ID to a file that SEKOIA.IO Agent loaded?**

It is not possible to add an Event ID. 

For each Event ID, we format the event to follow our Taxonomy (ECS norm) so we cannot add them on the fly.

However, we welcome any suggestions of Event IDs to be collected that seems relevant.

## Retrive events linked to clocked accounts on AD

**Is SEKOIA.IO Agent allowed to retrieve events linked to blocked accounts on AD?**

It is not possible at the moment.
This subject has been identified for improvement of SEKOIA.IO Agent integration with AD.

## SEKOIA.IO Agent version 0.2.8

**What brings the new SEKOIA.IO Agent version 0.2.8 in comparison to other versions?**
The Agent 0.2.8 will bring the following elements:

   - Automatic update of the Agent
   - Improvement of Integration with rules produced by SEKOIA.IO analysts
   - Collect new event types

## DNS logs

**Are DNS logs collected by SEKOIA.IO agent?**

Yes, DNS logs are collected by the Agent in the Windows version through system calls. It's not available in the Linux version at the moment. 

## SEKOIA.IO Agent and Sysmon

**Will there be any duplicates when using SEKOIA Agent and Sysmon? For instance, what happens if I search for events in my Sysmon configuration that are already sent by the SEKOIA.IO agent?**

For some events, the Agent will ignore Sysmon events as it will already cover the same scope and in the same way. Here are some examples:

- sysmonProcessCreation
- sysmonNetworkConnection
- sysmonProcessTerminated
- sysmonCreateRemoteThread
- sysmonFileCreate
- sysmonDNSEvent
- sysmonFileDelete
- sysmonFileDeleteDetected

## SEKOIA.IO Agent and ANSSI recommendations

**Do you confirm that SEKOIA.IO Agent (without Sysmon) will apply all SEKOIA rules and ANSSI recommendations? Is it an ongoing subject?**

We plan to cover all the ANSSI recommendations and SEKOIA rules to the greatest extent in the next beta.

## Remove Sysmon option 

**Do you plan to remove the possibility to select Sysmon option or will we allow users to add a Sysmon configuration?**

We most probably will support Sysmon for users who wish to continue using it. 
