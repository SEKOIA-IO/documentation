
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "event_01"

    ```
	[categoryId=0 instanceId=31000 param1="0" param2="0" param3="0" param4="0" ChangesXML="<changes><object><property internal="SyslogReportingEnabled" type="Boolean"><old>False</old><new>True</new></property><property internal="SyslogReportingHost" type="String"><old /><new>logconcentrator.example.org</new></property><property internal="SyslogReportingPort" type="Integer"><old /><new>20517</new></property><property internal="SyslogReportingProtocol" type="SyslogProtocol"><old /><new>Tcp</new></property><property internal="SyslogReportingCertificateThumbprint" type="String"><old /><new></new></property></object></changes>" UserName="example.com\jdoe" Version="1" Description="Backup server general options have been changed"]
    ```



=== "event_02"

    ```
	[categoryId=0 instanceId=31000 param1="0" param2="0" param3="0" param4="0" ChangesXML="<changes><object /></changes>" UserName="example.com\jdoe" Version="1" Description="Backup server general options have been changed"]
    ```



=== "event_03"

    ```
	[categoryId=0 instanceId=25300 CredentialsId="11111111-2222-4333-4444-555555555555" AccountName="example.com\jdoe" param3="0" param4="0" param5="0" UserName="example.com\jdoe" UserFullInfo="<ModifiedUserInfo fullName="example.com\jdoe" loginType="0" />" Version="1" Description="Credentials example.com\jdoe have been added"]
    ```



=== "event_04"

    ```
	[categoryId=0 instanceId=23010 JobID="11111111-2222-4333-4444-555555555555" JobType="12003" Platform="6" JobName="Agent Backup Job 1" ChangesXML="<changes><object id="11111111-2222-4333-4444-555555555555" /></changes>" param6="MyMachine\jdoe" Version="1" Description="Agent Backup job 'Agent Backup Job 1' has been created."]
    ```



=== "event_05"

    ```
	[categoryId=0 instanceId=23110 JobID="11111111-2222-4333-4444-555555555555" JobType="12003" Platform="N\A" JobName="Agent Backup Job 1" ChangesXML="<changes><object id="11111111-2222-4333-4444-555555555555" /></changes>" UserName="example.com\jdoe" Version="1" Description="'1' objects has been created for 'Agent Backup Job 1'."]
    ```



=== "event_06"

    ```
	[categoryId=0 instanceId=710 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12003" Platform="6" Flags="1" Version="1" Description="Agent Backup job 'Agent Backup Job 1' has been started by user .\SYSTEM."]
    ```



=== "event_07"

    ```
	[categoryId=0 instanceId=810 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12005" Flags="0" Version="1" Description="Rescan job 'Rescan of Agent Backup Job 1' has been started."]
    ```



=== "event_08"

    ```
	[categoryId=0 instanceId=32900 param1="0" HostName="127.0.0.1" ComponentDisplayName="Veeam Agent for Windows" Result="True" IsInstallOrUpgrade="True" Version="1" Description="Component [Veeam Agent for Windows] on the host [127.0.0.1] has been updated"]
    ```



=== "event_09"

    ```
	[categoryId=0 instanceId=23010 JobID="11111111-2222-4333-4444-555555555555" JobType="12000" Platform="6" JobName="Agent Backup Job 1 - 127.0.0.1" ChangesXML="<changes><object id="11111111-2222-4333-4444-555555555555" /></changes>" param6="SYSTEM" Version="1" Description="Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been created."]
    ```



=== "event_10"

    ```
	[categoryId=0 instanceId=110 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12000" Platform="6" Flags="1" Version="1" Description="Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started by user NT AUTHORITY\SYSTEM."]
    ```



=== "event_11"

    ```
	[categoryId=0 instanceId=890 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" Result="0" JobType="12005" WillBeRetried="False" Version="1" Description="The Rescan job 'Rescan of Agent Backup Job 1' has finished with Success state."]
    ```



=== "event_12"

    ```
	[categoryId=0 instanceId=42290 param1="0" param2="0" param3="0" param4="0" ChangesXML="<changes><object><property internal="IsEnabledInlineScanning" type="Boolean"><old>False</old><new>True</new></property><property internal="InlineScanningSensitivity" type="ERansomwareScanningSensitivity"><old /><new>Normal</new></property></object></changes>" UserName="example.com\jdoe" Version="1" Description="Malware detection settings have been changed."]
    ```



=== "event_13"

    ```
	[categoryId=0 instanceId=10010 OibID="11111111-2222-4333-4444-555555555555" OriginalOibID="11111111-2222-4333-4444-555555555555" VmRef="11111111-2222-4333-4444-555555555555" VmName="127.0.0.1" ServerName="This server" DateTime="12/19/2023 10:35:56" IsCorrupted="False" Platform="6" StorageSize="35864576" RepositoryID="11111111-2222-4333-4444-555555555555" IsFull="True" Version="1" Description="VM '127.0.0.1' restore point has been created."]
    ```



=== "event_14"

    ```
	[categoryId=0 instanceId=150 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12000" TaskSessionID="11111111-2222-4333-4444-555555555555" OibID="11111111-2222-4333-4444-555555555555" OriginalOibID="11111111-2222-4333-4444-555555555555" CreationTime="12/19/2023 10:35:56" Status="5" SourceHostName="MyMachine" VmRef="11111111-2222-4333-4444-555555555555" VmName="127.0.0.1" TransferredGb="0.031" Platform="6" IsEntry="False" Version="1" Description="VM 127.0.0.1 task has finished with 'InProgress' state."]
    ```



=== "event_15"

    ```
	[categoryId=0 instanceId=790 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" param3="0" JobType="12003" Platform="6" WillBeRetried="False" Version="1" Description="Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully."]
    ```



=== "event_16"

    ```
	[categoryId=0 instanceId=810 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12005" Flags="0" Version="1" Description="Rescan job 'Rescan of 127.0.0.1' has been started."]
    ```



=== "event_17"

    ```
	[categoryId=0 instanceId=890 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" Result="0" JobType="12005" WillBeRetried="False" Version="1" Description="The Rescan job 'Rescan of 127.0.0.1' has finished with Success state."]
    ```



=== "event_18"

    ```
	[categoryId=0 instanceId=29100 ProtectionGroupID="11111111-2222-4333-4444-555555555555" ProtectionGroupName="Protection Group 1" UserName="example.com\jdoe" Version="1" Description="Protection Group Protection Group 1 has been added."]
    ```



=== "event_19"

    ```
	[categoryId=0 instanceId=810 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12005" Flags="1" Version="1" Description="Rescan job 'Rescan of Protection Group 1' has been started by user MyMachine\jdoe."]
    ```



=== "event_20"

    ```
	[categoryId=0 instanceId=890 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" Result="0" JobType="12005" WillBeRetried="False" Version="1" Description="The Rescan job 'Rescan of Protection Group 1' has finished with Success state."]
    ```



=== "event_21"

    ```
	[categoryId=0 instanceId=710 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12003" Platform="6" Flags="0" Version="1" Description="Agent Backup job 'Agent Backup Job 1' has been started."]
    ```



=== "event_22"

    ```
	[categoryId=0 instanceId=110 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" JobType="12000" Platform="6" Flags="0" Version="1" Description="Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started."]
    ```



=== "event_23"

    ```
	[categoryId=0 instanceId=790 JobSessionID="11111111-2222-4333-4444-555555555555" JobID="11111111-2222-4333-4444-555555555555" param3="0" JobType="12003" Platform="6" WillBeRetried="True" Version="1" Description="Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully."]
    ```



=== "event_24"

    ```
	[categoryId=0 instanceId=10050 OibID="11111111-2222-4333-4444-555555555555" OriginalOibID="11111111-2222-4333-4444-555555555555" VmRef="11111111-2222-4333-4444-555555555555" VmName="127.0.0.1" ServerName="This server" DateTime="12/22/2023 15:27:59" IsCorrupted="False" Platform="6" StorageSize="53710848" RepositoryID="11111111-2222-4333-4444-555555555555" IsFull="False" Version="1" Description="Restore point for VM '127.0.0.1' has been removed by user example.com\jdoe."]
    ```



=== "event_25"

    ```
	[categoryId=0 instanceId=111111 JobID="000000000-0000000000-000000000-000000000" JobType="0" Platform="N\A" JobName="TEST_BACKUP" ChangesXML="11111232323(BDD_TEST_01)" UserName="example.com\Administrator" VbrHostName="example.com" VbrVersion="1.2.3.4" Version="1" Description="'1' objects has been deleted for 'TEST_BACKUP'."]
    ```



