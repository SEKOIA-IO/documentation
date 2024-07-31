
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_type_1000"


    ```json
	{
        "Version": 1,
        "Type": 1000,
        "TypeComputedMap": "LostBuffers",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0E997D-0D6B-40A9-81F1-7C21E9B8AAD3}",
        "Timestamp": "2023-06-15T06:30:00.0000000+01:00",
        "TimestampRaw": 133232454000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "LostBuffersCount": 35
        }
    }
    ```



=== "test_type_1001"


    ```json
	{
        "Version": 1,
        "Type": 1001,
        "TypeComputedMap": "RulesEngCriticalError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD054D09-4231-4A21-8BA1-440AEBAC0CC9}",
        "Timestamp": "2023-06-15T06:40:00.0000000+01:00",
        "TimestampRaw": 133232460000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_1002"


    ```json
	{
        "Version": 1,
        "Type": 1002,
        "TypeComputedMap": "RulesEngIdentifierCollectionError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD060B75-CD2D-4F29-9E23-8F45C47772BA}",
        "Timestamp": "2023-06-15T06:50:00.0000000+01:00",
        "TimestampRaw": 133232466000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_1003"


    ```json
	{
        "Version": 1,
        "Type": 1003,
        "TypeComputedMap": "RulesEngRulesPackageError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0969EB-BA6D-481A-B96D-730EC18FE560}",
        "Timestamp": "2023-06-15T07:00:00.0000000+01:00",
        "TimestampRaw": 133232472000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "RulesPackageKeyPath": "HKLM\\TestPath\\Here"
        }
    }
    ```



=== "test_type_1004"


    ```json
	{
        "Version": 1,
        "Type": 1004,
        "TypeComputedMap": "RulesEngInvalidParameter",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD075EE1-778C-4E3E-81E5-A565E4A4FF68}",
        "Timestamp": "2023-06-15T07:10:00.0000000+01:00",
        "TimestampRaw": 133232478000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_1006"


    ```json
	{
        "Version": 1,
        "Type": 1006,
        "TypeComputedMap": "TemporaryWebAccessStart",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07FF6B-417C-4249-B1D6-259FEDD9CFF2}",
        "Timestamp": "2023-06-15T07:20:00.0000000+01:00",
        "TimestampRaw": 133232484000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Duration": 50000,
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_1007"


    ```json
	{
        "Version": 1,
        "Type": 1007,
        "TypeComputedMap": "TemporaryWebAccessStartFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD04C4F9-0196-441F-A772-F54FC0793D41}",
        "Timestamp": "2023-06-15T07:30:00.0000000+01:00",
        "TimestampRaw": 133232490000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5,
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_1008"


    ```json
	{
        "Version": 1,
        "Type": 1008,
        "TypeComputedMap": "TemporaryWebAccessStop",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0E045B-4A76-4297-9269-D7DDE4C631FD}",
        "Timestamp": "2023-06-15T07:40:00.0000000+01:00",
        "TimestampRaw": 133232496000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": null,
            "UserDomainLookup": null,
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_1009"


    ```json
	{
        "Version": 1,
        "Type": 1009,
        "TypeComputedMap": "TemporaryWebAccessStopFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD02A68E-3F78-438B-B64B-79112040192E}",
        "Timestamp": "2023-06-15T07:50:00.0000000+01:00",
        "TimestampRaw": 133232502000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5,
            "UserNameLookup": null,
            "UserDomainLookup": null,
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_1010"


    ```json
	{
        "Version": 1,
        "Type": 1010,
        "TypeComputedMap": "AgentInternalLogExceedMaxSize",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F16E5-852C-4686-9979-AA5A859D50F2}",
        "Timestamp": "2023-06-15T08:00:00.0000000+01:00",
        "TimestampRaw": 133232508000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "FaultyLogType": 1010,
            "FaultyLogTypeComputedMap": null
        }
    }
    ```



=== "test_type_1011"


    ```json
	{
        "Version": 1,
        "Type": 1011,
        "TypeComputedMap": "TemporaryWebAccessMaxCountReached",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09731F-F853-4815-9DE3-C4B6991F689E}",
        "Timestamp": "2023-06-15T08:10:00.0000000+01:00",
        "TimestampRaw": 133232514000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_103"


    ```json
	{
        "Version": 1,
        "Type": 103,
        "TypeComputedMap": "RegistryKeyCreate",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD042F09-DB50-4EDB-8370-DB9A3C37A5EF}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T05:23:57.0238678+02:00",
        "TimestampRaw": 133311362370238678,
        "SpecificData": {
            "SourceProcess": {
                "PID": 1832,
                "ProcessGuid": "{E38CB57F-32F0-4AB4-9581-8CDD6B0E95B1}",
                "ProcessImageName": "C:\\Windows\\System32\\svchost.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\WINDOWS\\system32\\svchost.exe-knetsvcs-p-swlidsvc",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-16384",
                "IntegrityLevelNameLookup": "Niveauobligatoiresyst\u00e8me",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 0,
                "HashMd5": "B7F884C1B74A263F746EE12A5F7C9F6A",
                "HashSha1": "1BC5066DDF693FC034D6514618854E26A84FD0D1",
                "HashSha256": "ADD683A6910ABBBF0E28B557FAD0BA998166394932AE2ACA069D9AA19EA8FE88",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindowsPublisher",
                        "SigningTime": "2022-06-18T08:21:06.9540000+02:00",
                        "ValidityStart": "2022-01-27T21:31:19.0000000+02:00",
                        "ValidityEnd": "2023-01-26T21:31:19.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-13T15:17:42.8190445+02:00",
                "ProcessStartTimeRaw": 133311358628190445
            },
            "Action": {
                "PolicyGuid": "{621F7A4B-040E-42C2-9B4F-173BA48E067B}",
                "PolicyVersion": 2,
                "RuleGuid": "{E63B82C5-EC6B-4FBA-B854-94D81A98EAAA}",
                "BaseRuleGuid": "{E63B82C5-EC6B-4FBA-B854-94D81A98EAA9}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Details": {
                "Options": 1,
                "OptionsComputedBitMap": [
                    "REG_OPTION_VOLATILE"
                ],
                "DesiredAccess": 131103,
                "DesiredAccessComputedBitMap": [
                    "KEY_QUERY_VALUE",
                    "KEY_SET_VALUE",
                    "KEY_CREATE_SUB_KEY",
                    "KEY_ENUMERATE_SUB_KEYS",
                    "KEY_NOTIFY",
                    "READ_CONTROL"
                ]
            },
            "DetailsType": 0,
            "DetailsTypeComputedMap": "REGISTRY_KEY_CREATE",
            "Path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\IdentityCRL\\ThrottleCache\\S-1-5-18_{67082621-8D18-4333-9C64-10DE93676363}"
        }
    }
    ```



=== "test_type_104"


    ```json
	{
        "Version": 1,
        "Type": 104,
        "TypeComputedMap": "RegistryKeyRead",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B285F-2E43-4390-823C-73CB7736D0AA}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T05:34:00.8441322+02:00",
        "TimestampRaw": 133311368408441322,
        "SpecificData": {
            "SourceProcess": {
                "PID": 6704,
                "ProcessGuid": "{0E6042A8-0DC3-47A6-9FB4-8936B396C1AC}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\WINDOWS\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "790E65F13ECEB64FE297DF08EB1C953A",
                "HashSha1": "5F04BC4911EEBA35EC294B111C57D90808A4C4BD",
                "HashSha256": "B6F176E86DED71B8494FAD53791367C870318B1E7D9C3E1AEE1B0DAC6CFAC237",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-05-09T10:18:43.9710000+02:00",
                        "ValidityStart": "2023-02-03T02:05:42.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:42.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-13T15:32:52.0646809+02:00",
                "ProcessStartTimeRaw": 133311367720646809
            },
            "Action": {
                "PolicyGuid": "{621F7A4B-040E-42C2-9B4F-173BA48E067B}",
                "PolicyVersion": 4,
                "RuleGuid": "{E63B82C5-EC6B-4FBA-B854-94D81A98EAAA}",
                "BaseRuleGuid": "{E63B82C5-EC6B-4FBA-B854-94D81A98EAA9}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsNT\\CurrentVersion\\TimeZones",
            "InformationClass": 0,
            "InformationClassComputedMap": "KeyBasicInformation"
        }
    }
    ```



=== "test_type_109"


    ```json
	{
        "Version": 1,
        "Type": 109,
        "TypeComputedMap": "RegistryKeyWrite",
        "Category": 1,
        "CategoryComputedMap": "Registry",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0D1A3F-D034-4FE6-BE01-10DB9C0F6C4E}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:07:58.8191262+01:00",
        "TimestampRaw": 133225888788191262,
        "SpecificData": {
            "SourceProcess": {
                "PID": 1196,
                "ProcessGuid": "{B0E2F52D-8C18-4DF8-8E73-470BB4E5D373}",
                "ProcessImageName": "C:\\Windows\\regedit.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\WINDOWS\\regedit.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "999A30979F6195BF562068639FFC4426",
                "HashSha1": "D4F2663AABC03478975382B3C69F24B3C6BD2AA9",
                "HashSha256": "92F24FED2BA2927173AAD58981F6E0643C6B89815B117E8A7C4A0988AC918170",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-18T02:58:33.2360000+01:00",
                        "ValidityStart": "2022-05-05T20:23:14.0000000+01:00",
                        "ValidityEnd": "2023-05-04T20:23:14.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-03-06T16:04:21.8793902+01:00",
                "ProcessStartTimeRaw": 133225886618793902
            },
            "Action": {
                "PolicyGuid": "{BF0D5FEE-FF2A-4E6B-97DA-A1FC246FE845}",
                "PolicyVersion": 3,
                "RuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0C0}",
                "BaseRuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0BF}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Details": {
                "Options": 0,
                "OptionsComputedBitMap": [],
                "DesiredAccess": 33554432,
                "DesiredAccessComputedBitMap": [
                    "MAXIMUM_ALLOWED"
                ],
                "SubkeyName": "NewKey#1"
            },
            "DetailsType": 0,
            "DetailsTypeComputedMap": "REGISTRY_KEY_CREATE_SUBKEY",
            "Path": "HKEY_CURRENT_USER\\SOFTWARE\\TEST_ADE"
        }
    }
    ```



=== "test_type_11"


    ```json
	{
        "Version": 1,
        "Type": 11,
        "TypeComputedMap": "ProcessExecution",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 2,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD066513-E7B5-4F79-AE62-0885C51EA629}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:08:53.7673622+01:00",
        "TimestampRaw": 133209473337673622,
        "SpecificData": {
            "SourceProcess": {
                "PID": 5496,
                "ProcessGuid": "{71D28FEC-F11C-4F18-AE90-441C0C7EDBE3}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "DEEEE5E9267B65A9A82BE24BE2693365",
                "HashSha1": "FC924E1BBEC021CB5685B05728618EB421AD3FBE",
                "HashSha256": "0472C590414103F5F8FB9FB3D710ADC5DFD13539E48B4AAA55CC954203202C13",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-06T12:01:50.2850000+01:00",
                        "ValidityStart": "2022-05-05T20:23:15.0000000+01:00",
                        "ValidityEnd": "2023-05-04T20:23:15.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T11:35:02.4495876+01:00",
                "ProcessStartTimeRaw": 133209309024495876
            },
            "Action": {
                "PolicyGuid": "{C28F5498-FDC3-4E59-A13C-6139CE1FD00C}",
                "PolicyVersion": 3,
                "RuleGuid": "{4DE7AEC5-BACF-46F8-9B78-2203A14D1562}",
                "BaseRuleGuid": "{4DE7AEC5-BACF-46F8-9B78-2203A14D1561}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "CreatedProcess": {
                "PID": 5280,
                "ProcessGuid": "{2E91C661-4ACA-4CDB-84D1-CCD98308B120}",
                "ProcessImageName": "C:\\Windows\\System32\\notepad.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\Windows\\system32\\notepad.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "Test",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "27F71B12CB585541885A31BE22F61C83",
                "HashSha1": "D05DEFE2C8EFEF10ED5F1361760FA0AE41FA79F5",
                "HashSha256": "F9D9B9DED9A67AA3CFDBD5002F3B524B265C4086C188E1BE7C936AB25627BF01",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2022-07-21T02:36:42.3560000+01:00",
                        "ValidityStart": "2021-09-02T19:23:41.0000000+01:00",
                        "ValidityEnd": "2022-09-01T19:23:41.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T16:08:53.7602140+01:00",
                "ProcessStartTimeRaw": 133209473337602140
            },
            "ParentProcess": {
                "PID": 5496,
                "ProcessGuid": "{71D28FEC-F11C-4F18-AE90-441C0C7EDBE3}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "Test",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "DEEEE5E9267B65A9A82BE24BE2693365",
                "HashSha1": "FC924E1BBEC021CB5685B05728618EB421AD3FBE",
                "HashSha256": "0472C590414103F5F8FB9FB3D710ADC5DFD13539E48B4AAA55CC954203202C13",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-06T12:01:50.2850000+01:00",
                        "ValidityStart": "2022-05-05T20:23:15.0000000+01:00",
                        "ValidityEnd": "2023-05-04T20:23:15.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T11:35:02.4495876+01:00",
                "ProcessStartTimeRaw": 133209309024495876
            }
        }
    }
    ```



=== "test_type_112"


    ```json
	{
        "Version": 1,
        "Type": 112,
        "TypeComputedMap": "RegistryKeyDelete",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0DBC09-BED9-4335-B645-643B9CAB885C}",
        "Timestamp": "2023-06-15T02:50:00.0000000+01:00",
        "TimestampRaw": 133232322000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Details": null,
            "Path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Test",
            "SourceProcess": {
                "PID": 8,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "f0fbb584-bc08-41d1-93a2-a04f8fc65c32",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD8FAFB111",
                "HashSha1": "AC9F34399C7C5A9372EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 5,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUntrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_113"


    ```json
	{
        "Version": 1,
        "Type": 113,
        "TypeComputedMap": "RegistryValueCreate",
        "Category": 1,
        "CategoryComputedMap": "Registry",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD003007-3EE1-478E-9D07-A3772739A5E6}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:13:20.2600711+01:00",
        "TimestampRaw": 133225892002600711,
        "SpecificData": {
            "SourceProcess": {
                "PID": 1196,
                "ProcessGuid": "{B0E2F52D-8C18-4DF8-8E73-470BB4E5D373}",
                "ProcessImageName": "C:\\Windows\\regedit.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\WINDOWS\\regedit.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "999A30979F6195BF562068639FFC4426",
                "HashSha1": "D4F2663AABC03478975382B3C69F24B3C6BD2AA9",
                "HashSha256": "92F24FED2BA2927173AAD58981F6E0643C6B89815B117E8A7C4A0988AC918170",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-18T02:58:33.2360000+01:00",
                        "ValidityStart": "2022-05-05T20:23:14.0000000+01:00",
                        "ValidityEnd": "2023-05-04T20:23:14.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-03-06T16:04:21.8793902+01:00",
                "ProcessStartTimeRaw": 133225886618793902
            },
            "Action": {
                "PolicyGuid": "{BF0D5FEE-FF2A-4E6B-97DA-A1FC246FE845}",
                "PolicyVersion": 4,
                "RuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0C0}",
                "BaseRuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0BF}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Path": "HKEY_CURRENT_USER\\SOFTWARE\\TEST_ADE",
            "ValueName": "Valeur_String",
            "ValueDataType": 1,
            "ValueDataTypeComputedMap": "REG_SZ",
            "ValueData": ""
        }
    }
    ```



=== "test_type_114"


    ```json
	{
        "Version": 1,
        "Type": 114,
        "TypeComputedMap": "RegistryValueRead",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F267B-2FBB-4457-99C1-AC4663C7FC93}",
        "Timestamp": "2023-06-15T03:10:00.0000000+01:00",
        "TimestampRaw": 133232334000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ValueName": "Value2",
            "Path": "HKEY_LOCAL_MACHINE\\SOFTWARE",
            "SourceProcess": {
                "PID": 1,
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "UserSID": null,
                "SessionID": 2,
                "ProcessGuid": "92c246ec-0acd-11ea-a38a-00155d099004",
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "HashMd5": "4E196CEA0C9C46A7D656C67E52E8C7C7",
                "HashSha1": "726C9D759C5F02080FA003B50466A3BE0C959865",
                "HashSha256": "ED5F36137D09E1CFC0CCF2675FB5D460E7EED135BA36D3259D2C510592047F28",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SigningTime": "2019-10-20T14:09:02.8886192+01:00",
                        "ValidityEnd": "2020-05-02T22:24:36.0705280+01:00",
                        "ValidityStart": "2019-05-02T22:24:36.7807872+01:00",
                        "SubjectCN": "Microsoft Windows"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_115"


    ```json
	{
        "Version": 1,
        "Type": 115,
        "TypeComputedMap": "RegistryValueWrite",
        "Category": 1,
        "CategoryComputedMap": "Registry",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09D00C-D632-4FB1-9606-AD80E2AB9AF5}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:13:26.1106189+01:00",
        "TimestampRaw": 133225892061106189,
        "SpecificData": {
            "SourceProcess": {
                "PID": 1196,
                "ProcessGuid": "{B0E2F52D-8C18-4DF8-8E73-470BB4E5D373}",
                "ProcessImageName": "C:\\Windows\\regedit.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\WINDOWS\\regedit.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "999A30979F6195BF562068639FFC4426",
                "HashSha1": "D4F2663AABC03478975382B3C69F24B3C6BD2AA9",
                "HashSha256": "92F24FED2BA2927173AAD58981F6E0643C6B89815B117E8A7C4A0988AC918170",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-18T02:58:33.2360000+01:00",
                        "ValidityStart": "2022-05-05T20:23:14.0000000+01:00",
                        "ValidityEnd": "2023-05-04T20:23:14.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-03-06T16:04:21.8793902+01:00",
                "ProcessStartTimeRaw": 133225886618793902
            },
            "Action": {
                "PolicyGuid": "{BF0D5FEE-FF2A-4E6B-97DA-A1FC246FE845}",
                "PolicyVersion": 4,
                "RuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0C0}",
                "BaseRuleGuid": "{4CEEDD7A-875D-4C7E-9ABD-A710BD3DD0BF}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Path": "HKEY_CURRENT_USER\\SOFTWARE\\TEST_ADE",
            "ValueName": "Valeur_String",
            "ValueDataType": 1,
            "ValueDataTypeComputedMap": "REG_SZ",
            "ValueData": "lala"
        }
    }
    ```



=== "test_type_116"


    ```json
	{
        "Version": 1,
        "Type": 116,
        "TypeComputedMap": "RegistryValueDelete",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0503D8-60D7-4B07-B649-6F70DE5A1125}",
        "Timestamp": "2023-06-15T03:30:00.0000000+01:00",
        "TimestampRaw": 133232346000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ValueName": "Value2",
            "Path": "HKEY_LOCAL_MACHINE\\SOFTWARE",
            "SourceProcess": {
                "PID": 6,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e83-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF44D9AFD9FAFB111",
                "HashSha1": "0C9F34399C7C5A9372EFE0F6E6F33DA4116016C6",
                "HashSha256": "2347766F6B5AD11E5C97167B5A452374EFF876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 8,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4765488+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadSignature"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_11_1"


    ```json
	{
        "Version": 1,
        "Type": 11,
        "TypeComputedMap": "ProcessExecution",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{5024762E-73B4-40DC-823A-7B080C82C542}",
        "GenerateIncident": true,
        "Timestamp": "2024-02-01T08:10:33.7922326-08:00",
        "TimestampRaw": 133512774337922326,
        "SpecificData": {
            "SourceProcess": {
                "PID": 7248,
                "ProcessGuid": "{90FC03BE-4FBF-4184-A304-6D4B00AA152B}",
                "ProcessImageName": "C:\\ragnarlocker.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\ragnarlocker.exe\" ",
                "User": "S-1-5-21-1111111111-22222222-3333333333-000",
                "UserNameLookup": "Administrator",
                "UserDomainLookup": "EXAMPLE",
                "IntegrityLevel": "S-1-16-11111",
                "IntegrityLevelNameLookup": "High Mandatory Level",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "SessionID": 1,
                "HashMd5": "68B329DA9893E34099C7D8AD5CB9C940",
                "HashSha1": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
                "HashSha256": "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 2,
                "CertificateSignatureStateComputedMap": "SignatureStateNoSignature",
                "Certificates": [],
                "ProcessStartTime": "2024-02-01T08:10:33.5801449-08:00",
                "ProcessStartTimeRaw": 133512774335801449
            },
            "Action": {
                "PolicyGuid": "{64AA4553-15FC-4188-B4AD-A0BDCFB11ED9}",
                "PolicyVersion": 14,
                "RuleGuid": "{B88B8874-E8E3-4F42-92B8-61D364DB65B9}",
                "BaseRuleGuid": "{0C4D019E-B7D5-4456-909A-C5F4152461AE}",
                "IdentifierGuid": "{BC74B5FB-8880-4A74-8316-FE865F9EA75C}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            },
            "CreatedProcess": {
                "PID": 11308,
                "ProcessGuid": "{24F0AA75-BC26-4245-829E-97087BB07A47}",
                "ProcessImageName": "C:\\Windows\\System32\\cmd.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "cmd.exe /c vssadmin delete shadows /all /quiet",
                "User": "S-1-5-21-1111111111-22222222-3333333333-000",
                "UserNameLookup": "Administrator",
                "UserDomainLookup": "EXAMPLE",
                "IntegrityLevel": "S-1-16-11111",
                "IntegrityLevelNameLookup": "High Mandatory Level",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "SessionID": 1,
                "HashMd5": "68B329DA9893E34099C7D8AD5CB9C940",
                "HashSha1": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
                "HashSha256": "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SubjectCN": "Microsoft Windows",
                        "SigningTime": "2013-08-22T05:07:49.2400000-08:00",
                        "ValidityStart": "2013-06-17T13:43:38.0000000-08:00",
                        "ValidityEnd": "2014-09-17T13:43:38.0000000-08:00"
                    }
                ],
                "ProcessStartTime": "2024-02-01T08:10:33.7833468-08:00",
                "ProcessStartTimeRaw": 133512774337833468
            },
            "ParentProcess": {
                "PID": 7248,
                "ProcessGuid": "{D057290C-D86A-441B-B3CB-C6E54D42EBA5}",
                "ProcessImageName": "C:\\ragnarlocker.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\ragnarlocker.exe\" ",
                "User": "S-1-5-21-1111111111-22222222-3333333333-000",
                "UserNameLookup": "Administrator",
                "UserDomainLookup": "EXAMPLE",
                "IntegrityLevel": "S-1-16-11111",
                "IntegrityLevelNameLookup": "High Mandatory Level",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "SessionID": 1,
                "HashMd5": "68B329DA9893E34099C7D8AD5CB9C940",
                "HashSha1": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
                "HashSha256": "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 2,
                "CertificateSignatureStateComputedMap": "SignatureStateNoSignature",
                "Certificates": [],
                "ProcessStartTime": "2024-02-01T08:10:33.5801449-08:00",
                "ProcessStartTimeRaw": 133512774335801449
            }
        },
        "AdditionalData": {
            "AgentAddresses": [
                "172.24.0.14"
            ],
            "AgentGroupGuid": "{00000000-0000-0000-0000-000000000000}",
            "AgentGroupName": "Default group",
            "AgentGuid": "{074C7CCE-ACF4-4674-9650-4B63B569892F}",
            "AgentName": "WINSERVER2012",
            "CategoryName": "Process",
            "IncidentGuid": "{12CA4135-575E-49DE-89AD-4CD35EE2EB3B}",
            "Message": "The 'ragnarlocker.exe' process attempted to run the 'cmd.exe' process",
            "PolicyName": "Stormshield - Incredible policy (1)",
            "SeverityName": "Emergency"
        }
    }
    ```



=== "test_type_173"


    ```json
	{
        "Version": 1,
        "Type": 173,
        "TypeComputedMap": "FileCreate",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0791A3-DF3A-49CB-922A-38C054779CBC}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:19:30.8012653+02:00",
        "TimestampRaw": 133311395708012653,
        "SpecificData": {
            "SourceProcess": {
                "PID": 4816,
                "ProcessGuid": "{1A83B343-5C5C-4B0E-977A-B20CF86B43A8}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 3,
                "VolumeZoneComputedBitMap": [
                    "Operating system",
                    "Computer Boot"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "81886624735B4F8F019E731A8A2E6E69",
                "HashSha1": "A30E4111E183514DEF89D2BC31071231DEABC4DF",
                "HashSha256": "385DBAD0269CAE83598D6706229324EB3CBDEF00E21A0682161477D762AAF2C1",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-04-15T11:56:31.9920000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-13T14:28:06.6858009+02:00",
                "ProcessStartTimeRaw": 133311328866858009
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 6,
                "RuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F9}",
                "BaseRuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F8}",
                "IdentifierGuid": "{9BB78BCC-E85C-4CB5-A6CC-26E21029385C}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "UsbDeviceInfo": {
                "VendorId": 5118,
                "ProductId": 25344,
                "Class": 0,
                "ClassComputedMap": "UseclassinformationintheInterfaceDescriptors",
                "SubClass": 0,
                "Protocol": 0,
                "SerialNumber": "072117691198E329",
                "VendorName": "",
                "ProductName": "USBDISK3.0",
                "Interfaces": [
                    {
                        "Class": 8,
                        "ClassComputedMap": "MassStorage",
                        "Subclass": 6,
                        "Protocol": 80
                    }
                ]
            },
            "UsbVolumeTrackingData": {
                "EnrollFileState": 0,
                "EnrollFileStateComputedMap": "Noenrollfile",
                "FootprintFileState": 0,
                "FootprintFileStateComputedMap": "Nofootprintfile",
                "VendorId": 0,
                "ProductId": 0,
                "SerialNumberHashSha256": "0000000000000000000000000000000000000000000000000000000000000000",
                "EnrollGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "AccessFromNetwork": {},
            "Details": {
                "SourcePath": "F:\\NewTextDocument.txt",
                "Flags": 0,
                "FlagsComputedBitMap": []
            },
            "DetailsType": 2,
            "DetailsTypeComputedMap": "FILE_RENAME_DESTINATION",
            "Path": "F:\\cxvbcxvbcxv.txt",
            "MatchingPath": "",
            "VolumeZone": 3,
            "VolumeZoneComputedBitMap": [
                "Operating system",
                "Computer Boot"
            ],
            "FileObjectType": 0,
            "FileObjectTypeComputedMap": "FILE",
            "FileOwner": "",
            "FileOwnerNameLookup": "",
            "FileOwnerDomainLookup": ""
        }
    }
    ```



=== "test_type_174"


    ```json
	{
        "Version": 1,
        "Type": 174,
        "TypeComputedMap": "FileExecute",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F62D1-43CA-41DE-838D-B80498CB7369}",
        "Timestamp": "2023-06-15T03:50:00.0000000+01:00",
        "TimestampRaw": 133232358000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "AccessFromNetwork": {
                "ShareName": "\\\\Something",
                "AddressFamily": 2,
                "AddressFamilyComputedMap": "IPv4",
                "Address": "127.0.0.1",
                "Port": 80
            },
            "UsbDeviceInfo": {
                "VendorName": "SanDisk",
                "VendorId": 1921,
                "ProductName": "Ultra",
                "ProductId": 21889,
                "SerialNumber": "4C530001211017121370",
                "Class": 1,
                "SubClass": 220,
                "Interfaces": [
                    {
                        "Class": 254,
                        "SubClass": 254
                    },
                    {
                        "Class": 88,
                        "SubClass": 13
                    },
                    {
                        "Class": 224,
                        "SubClass": 16
                    }
                ]
            },
            "UsbVolumeTrackingData": {
                "EnrollFileState": 5,
                "EnrollGuid": "6b8a636d-a508-442e-835f-0538392c904e",
                "FootprintFileState": 0
            },
            "FileOwner": "S-1-5-21-2222222-33333333-44444444-555",
            "FileObjectType": 1,
            "FileObjectTypeComputedMap": "DIRECTORY",
            "MatchingPath": "c:\\tmp\\file2.txt",
            "VolumeZone": 1024,
            "VolumeZoneComputedBitMap": [
                "Remote Webdav"
            ],
            "Details": null,
            "FileOwnerNameLookup": "User1",
            "FileOwnerDomainLookup": "sshield1",
            "Path": "c:\\test\\toto.txt",
            "SourceProcess": {
                "PID": 9,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "9d367a6c-04e4-491b-baa8-25b674db96d9",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD8FAFB221",
                "HashSha1": "AC9F34399C7C5A9372EFE0FA16F33D12116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E13976136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_175"


    ```json
	{
        "Version": 1,
        "Type": 175,
        "TypeComputedMap": "FileRead",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0AA946-7DCE-4AB0-BA45-706B84C1F3FC}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:45:11.6239189+02:00",
        "TimestampRaw": 133312167116239189,
        "SpecificData": {
            "SourceProcess": {
                "PID": 196,
                "ProcessGuid": "{FE730151-438E-4EEC-A433-47C5D4E3B8F0}",
                "ProcessImageName": "C:\\Windows\\System32\\SearchIndexer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\system32\\SearchIndexer.exe/Embedding",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-16384",
                "IntegrityLevelNameLookup": "SystemMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 0,
                "HashMd5": "38E354B0E48633125C5AE4DF7A86AA27",
                "HashSha1": "E1A0C914D7767BEAE5858E91C2F626DC7F7A48DD",
                "HashSha256": "FAE9406A8A627C12FF9E18FEF4DF3CC91E0A2A766DC7D15BB8F2C3AD70CE95EF",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-03-29T01:48:03.5290000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T11:12:07.0737445+02:00",
                "ProcessStartTimeRaw": 133312075270737445
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 9,
                "RuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F9}",
                "BaseRuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F8}",
                "IdentifierGuid": "{9BB78BCC-E85C-4CB5-A6CC-26E21029385C}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "UsbDeviceInfo": {
                "VendorId": 1921,
                "ProductId": 21889,
                "Class": 0,
                "ClassComputedMap": "UseclassinformationintheInterfaceDescriptors",
                "SubClass": 0,
                "Protocol": 0,
                "SerialNumber": "04012f7f3a01c1ae65cdfeac1c2c89feb540858b0d034bc2c60f7de6edef26d7c8e6000000000000000000003b1bd6130017801881558107caa8e117",
                "VendorName": "USB",
                "ProductName": "SanDisk3.2Gen1",
                "Interfaces": [
                    {
                        "Class": 8,
                        "ClassComputedMap": "MassStorage",
                        "Subclass": 6,
                        "Protocol": 80
                    }
                ]
            },
            "UsbVolumeTrackingData": {
                "EnrollFileState": 5,
                "EnrollFileStateComputedMap": "Enrollfileisvalidanditscontentmatches.",
                "FootprintFileState": 5,
                "FootprintFileStateComputedMap": "Footprintfileisvalidanditscontentmatches",
                "VendorId": 1921,
                "ProductId": 21889,
                "SerialNumberHashSha256": "00A0D7D13C20905778EC71AFA1050B1E14E26C5AAF016496C37EE2E7D0120E98",
                "EnrollGuid": "{2474130E-C1AA-4E37-A63E-88AA950FE3CA}"
            },
            "AccessFromNetwork": {},
            "Details": {},
            "DetailsType": 1,
            "DetailsTypeComputedMap": "FILE_READ_DATA",
            "Path": "E:\\SystemVolumeInformation\\IndexerVolumeGuid",
            "MatchingPath": "",
            "VolumeZone": 32768,
            "VolumeZoneComputedBitMap": [
                "Removableunknown"
            ],
            "FileObjectType": 0,
            "FileObjectTypeComputedMap": "FILE",
            "FileOwner": "",
            "FileOwnerNameLookup": "",
            "FileOwnerDomainLookup": ""
        }
    }
    ```



=== "test_type_176"


    ```json
	{
        "Version": 1,
        "Type": 176,
        "TypeComputedMap": "FileWrite",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C1ABD-CE40-4411-AFCB-FB4B8B330BF1}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:45:11.6219776+02:00",
        "TimestampRaw": 133312167116219776,
        "SpecificData": {
            "SourceProcess": {
                "PID": 196,
                "ProcessGuid": "{FE730151-438E-4EEC-A433-47C5D4E3B8F0}",
                "ProcessImageName": "C:\\Windows\\System32\\SearchIndexer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\system32\\SearchIndexer.exe/Embedding",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-16384",
                "IntegrityLevelNameLookup": "SystemMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 0,
                "HashMd5": "38E354B0E48633125C5AE4DF7A86AA27",
                "HashSha1": "E1A0C914D7767BEAE5858E91C2F626DC7F7A48DD",
                "HashSha256": "FAE9406A8A627C12FF9E18FEF4DF3CC91E0A2A766DC7D15BB8F2C3AD70CE95EF",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-03-29T01:48:03.5290000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T11:12:07.0737445+02:00",
                "ProcessStartTimeRaw": 133312075270737445
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 9,
                "RuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F9}",
                "BaseRuleGuid": "{7294769D-86DB-4448-89CB-80A6CF5CB8F8}",
                "IdentifierGuid": "{9BB78BCC-E85C-4CB5-A6CC-26E21029385C}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "UsbDeviceInfo": {
                "VendorId": 1921,
                "ProductId": 21889,
                "Class": 0,
                "ClassComputedMap": "UseclassinformationintheInterfaceDescriptors",
                "SubClass": 0,
                "Protocol": 0,
                "SerialNumber": "04012f7f3a01c1ae65cdfeac1c2c89feb540858b0d034bc2c60f7de6edef26d7c8e6000000000000000000003b1bd6130017801881558107caa8e117",
                "VendorName": "USB",
                "ProductName": "SanDisk3.2Gen1",
                "Interfaces": [
                    {
                        "Class": 8,
                        "ClassComputedMap": "MassStorage",
                        "Subclass": 6,
                        "Protocol": 80
                    }
                ]
            },
            "UsbVolumeTrackingData": {
                "EnrollFileState": 5,
                "EnrollFileStateComputedMap": "Enrollfileisvalidanditscontentmatches.",
                "FootprintFileState": 5,
                "FootprintFileStateComputedMap": "Footprintfileisvalidanditscontentmatches",
                "VendorId": 1921,
                "ProductId": 21889,
                "SerialNumberHashSha256": "00A0D7D13C20905778EC71AFA1050B1E14E26C5AAF016496C37EE2E7D0120E98",
                "EnrollGuid": "{2474130E-C1AA-4E37-A63E-88AA950FE3CA}"
            },
            "AccessFromNetwork": {},
            "Details": {
                "SecurityInformation": 5,
                "SecurityInformationComputedBitMap": [
                    "OWNER_SECURITY_INFORMATION",
                    "DACL_SECURITY_INFORMATION"
                ]
            },
            "DetailsType": 10,
            "DetailsTypeComputedMap": "FILE_SET_SECURITY",
            "Path": "E:\\SystemVolumeInformation",
            "MatchingPath": "",
            "VolumeZone": 32768,
            "VolumeZoneComputedBitMap": [
                "Removableunknown"
            ],
            "FileObjectType": 0,
            "FileObjectTypeComputedMap": "FILE",
            "FileOwner": "",
            "FileOwnerNameLookup": "",
            "FileOwnerDomainLookup": ""
        }
    }
    ```



=== "test_type_177"


    ```json
	{
        "Version": 1,
        "Type": 177,
        "TypeComputedMap": "FileDelete",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD06EECF-C8D3-4BBE-B98F-A0DC5EDDE0C8}",
        "Timestamp": "2023-06-15T04:20:00.0000000+01:00",
        "TimestampRaw": 133232376000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "DetailsType": 2,
            "DetailsTypeComputedMap": "FILE_RENAME_SOURCE",
            "AccessFromNetwork": {
                "ShareName": "\\\\Something",
                "AddressFamily": 23,
                "AddressFamilyComputedMap": "IPv6",
                "Address": "192.168.128.211",
                "Port": 22
            },
            "UsbDeviceInfo": {
                "VendorName": "SanDisk",
                "VendorId": 1921,
                "ProductName": "Ultra",
                "ProductId": 21889,
                "SerialNumber": "4C530001211017121370",
                "Class": 1,
                "SubClass": 3,
                "Interfaces": [
                    {
                        "Class": 8,
                        "SubClass": 11
                    },
                    {
                        "Class": 18,
                        "SubClass": 9
                    },
                    {
                        "Class": 11,
                        "SubClass": 254
                    }
                ]
            },
            "UsbVolumeTrackingData": {
                "EnrollFileState": 1,
                "EnrollGuid": "bf93de07-e0e0-45c9-bfc1-3dfd4fb68ef2",
                "FootprintFileState": 5
            },
            "FileOwner": "S-1-5-21-2222222-33333333-44444444-555",
            "FileObjectType": 0,
            "FileObjectTypeComputedMap": "FILE",
            "MatchingPath": "c:\\tmp\\file2.txt",
            "VolumeZone": 64,
            "VolumeZoneComputedBitMap": [
                "Floppy"
            ],
            "Details": {
                "DesiredAccess": null,
                "Attributes": null,
                "FileName": null,
                "SourcePath": null,
                "DestinationPath": "c:\\test\\file1.txt",
                "Operation": null,
                "NewFileOwner": null,
                "OldFileOwner": null,
                "InformationClass": null,
                "SecurityInformation": null,
                "PageProtection": null,
                "Address": null,
                "Port": null
            },
            "FileOwnerNameLookup": "User1",
            "FileOwnerDomainLookup": "sshield1",
            "Path": "c:\\tmp\\file2.txt",
            "SourceProcess": {
                "PID": 8,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "f0fbb584-bc08-41d1-93a2-a04f8fc65c32",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD8FAFB111",
                "HashSha1": "AC9F34399C7C5A9372EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 5,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUntrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_20002"


    ```json
	{
        "Version": 1,
        "Type": 20002,
        "TypeComputedMap": "LostBuffers",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD084103-F26D-49EA-8890-70C7DB7A63A6}",
        "Timestamp": "2023-06-15T08:20:00.0000000+01:00",
        "TimestampRaw": 133232520000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "LostBuffersCount": 30
        }
    }
    ```



=== "test_type_20003"


    ```json
	{
        "Version": 1,
        "Type": 20003,
        "TypeComputedMap": "NewPolicyNotification",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 4,
        "AttributesComputedBitMap": [
            "Internal"
        ],
        "EventGuid": "{AD093377-53C4-4595-860F-6CD64A4153FB}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:07:54.2839637+01:00",
        "TimestampRaw": 133225888742839637,
        "SpecificData": {
            "PolicyName": "POL_TEST_ADE",
            "PolicyVersion": 3,
            "PolicyGuid": "{BF0D5FEE-FF2A-4E6B-97DA-A1FC246FE845}",
            "PolicyVersionInternal": 4
        }
    }
    ```



=== "test_type_20004"


    ```json
	{
        "Version": 1,
        "Type": 20004,
        "TypeComputedMap": "ServiceDidNotEndCorrectly",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD021EAE-7C29-4B3F-852E-553B95D26471}",
        "Timestamp": "2023-06-15T08:40:00.0000000+01:00",
        "TimestampRaw": 133232532000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ServiceName": "EsaAppIdSvc"
        }
    }
    ```



=== "test_type_20006"


    ```json
	{
        "Version": 1,
        "Type": 20006,
        "TypeComputedMap": "EndUpgradeAgentSucceeded",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0CD620-F5A8-430B-8FA3-BEC8E204DC74}",
        "Timestamp": "2023-06-15T08:50:00.0000000+01:00",
        "TimestampRaw": 133232538000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20007"


    ```json
	{
        "Version": 1,
        "Type": 20007,
        "TypeComputedMap": "EndUpgradeAgentFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD091E59-399B-4A0B-BB1F-7326C55502ED}",
        "Timestamp": "2023-06-15T09:00:00.0000000+01:00",
        "TimestampRaw": 133232544000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5
        }
    }
    ```



=== "test_type_20008"


    ```json
	{
        "Version": 1,
        "Type": 20008,
        "TypeComputedMap": "NewPolicyErrorNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD025B90-CBE6-4DF3-8F4B-BFD11E38270C}",
        "Timestamp": "2023-06-15T09:10:00.0000000+01:00",
        "TimestampRaw": 133232550000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PolicyName": null
        }
    }
    ```



=== "test_type_20009"


    ```json
	{
        "Version": 1,
        "Type": 20009,
        "TypeComputedMap": "InvalidHivePackage",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0951E4-DF4A-4D4A-A636-ABEB310BB6E0}",
        "Timestamp": "2023-06-15T09:20:00.0000000+01:00",
        "TimestampRaw": 133232556000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "HivePackageFullPath": "C:\\Users\\User1\\Desktop\\maliviousHive.hive",
            "LoadingOperationStatus": 5
        }
    }
    ```



=== "test_type_20010"


    ```json
	{
        "Version": 1,
        "Type": 20010,
        "TypeComputedMap": "StartUninstallAgent",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD042AB6-2DDF-4B8A-A805-9619857ECDFF}",
        "Timestamp": "2023-06-15T09:30:00.0000000+01:00",
        "TimestampRaw": 133232562000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20011"


    ```json
	{
        "Version": 1,
        "Type": 20011,
        "TypeComputedMap": "EndUninstallAgentSucceeded",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0DB33A-2194-4800-AB4E-C2BBCCFDE65D}",
        "Timestamp": "2023-06-15T09:40:00.0000000+01:00",
        "TimestampRaw": 133232568000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20012"


    ```json
	{
        "Version": 1,
        "Type": 20012,
        "TypeComputedMap": "EndUninstallAgentFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD075976-1881-4C1C-AB5F-ABE0E0430C9A}",
        "Timestamp": "2023-06-15T09:50:00.0000000+01:00",
        "TimestampRaw": 133232574000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20013"


    ```json
	{
        "Version": 1,
        "Type": 20013,
        "TypeComputedMap": "InvalidPolicyPackageCab",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B6BB8-6422-478E-93D7-1D9DD7A61EC3}",
        "Timestamp": "2023-06-15T00:00:00.0000000+01:00",
        "TimestampRaw": 133232580000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PolicyPackageCabFullPath": "C:\\Users\\User1\\Desktop\\EsPolicy.hive",
            "LoadingOperationStatus": 5
        }
    }
    ```



=== "test_type_20014"


    ```json
	{
        "Version": 1,
        "Type": 20014,
        "TypeComputedMap": "EsScriptHostCreateFailure",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C4A06-F13C-47F1-BF3C-FD7136C519A4}",
        "Timestamp": "2023-06-15T00:10:00.0000000+01:00",
        "TimestampRaw": 133232586000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ImplementationType": 0,
            "StatusCode": 5
        }
    }
    ```



=== "test_type_20015"


    ```json
	{
        "Version": 1,
        "Type": 20015,
        "TypeComputedMap": "KernelCorruptionBugcheck",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0AA66F-5A03-4CE9-ABCD-86988444224C}",
        "Timestamp": "2023-06-15T00:20:00.0000000+01:00",
        "TimestampRaw": 133232592000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Bugcheck": "0x00000109 (0x00000000, 0x00000000, 0x00000000, 0x00000000)"
        }
    }
    ```



=== "test_type_20016"


    ```json
	{
        "Version": 1,
        "Type": 20016,
        "TypeComputedMap": "InvalidPolicyPackageSignature",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0CDBE2-1FD9-43B4-80A3-219638B5C585}",
        "Timestamp": "2023-06-15T00:30:00.0000000+01:00",
        "TimestampRaw": 133232598000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": 5,
            "PolicyPackageFile": "C:\\Users\\User1\\Desktop\\EsPolicy.hive"
        }
    }
    ```



=== "test_type_20017"


    ```json
	{
        "Version": 1,
        "Type": 20017,
        "TypeComputedMap": "StartAgentUpgrade",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09E443-8DC7-4315-98A7-1C48312B835E}",
        "Timestamp": "2023-06-15T00:40:00.0000000+01:00",
        "TimestampRaw": 133232604000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "VersionFrom": "1.0.0.0",
            "VersionTo": "2.0.0.0"
        }
    }
    ```



=== "test_type_20018"


    ```json
	{
        "Version": 1,
        "Type": 20018,
        "TypeComputedMap": "PolicyPackageSignerExpired",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0FE5D0-593B-41FA-B642-98F1CC214FB8}",
        "Timestamp": "2023-06-15T00:50:00.0000000+01:00",
        "TimestampRaw": 133232610000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PolicyPackageFile": "C:\\Users\\User1\\Desktop\\EsPolicy.hive"
        }
    }
    ```



=== "test_type_20019"


    ```json
	{
        "Version": 1,
        "Type": 20019,
        "TypeComputedMap": "SelfProtectionLrpcFailure",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0A7F5A-905E-4E0B-AE2C-F1DA2D610788}",
        "Timestamp": "2023-06-15T01:00:00.0000000+01:00",
        "TimestampRaw": 133232616000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ServerServiceName": "EsaAppIdSvc",
            "SelfProtectionModuleName": "EsaGuardSvc",
            "StatusCode": 5
        }
    }
    ```



=== "test_type_20020"


    ```json
	{
        "Version": 1,
        "Type": 20020,
        "TypeComputedMap": "NewPolicyFromUpdateErrorNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0167A2-3042-453F-8E0C-F0B8BC76C13B}",
        "Timestamp": "2023-06-15T01:10:00.0000000+01:00",
        "TimestampRaw": 133232622000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PolicyName": null
        }
    }
    ```



=== "test_type_20021"


    ```json
	{
        "Version": 1,
        "Type": 20021,
        "TypeComputedMap": "NewPolicyFromUpdateNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0AEC3D-BAB1-4680-827B-FAB47FF00C8E}",
        "Timestamp": "2023-06-15T01:20:00.0000000+01:00",
        "TimestampRaw": 133232628000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PolicyGuid": "00000000-0000-0000-0000-000000000000",
            "PolicyVersion": 0,
            "PolicyName": null
        }
    }
    ```



=== "test_type_20022"


    ```json
	{
        "Version": 1,
        "Type": 20022,
        "TypeComputedMap": "NewConfigurationNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0533A5-A3D3-4F7E-A7B9-000FF784F592}",
        "Timestamp": "2023-06-15T01:30:00.0000000+01:00",
        "TimestampRaw": 133232634000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20023"


    ```json
	{
        "Version": 1,
        "Type": 20023,
        "TypeComputedMap": "NewConfigurationErrorNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0369FB-ED19-4402-A1E7-900E95350EB8}",
        "Timestamp": "2023-06-15T01:40:00.0000000+01:00",
        "TimestampRaw": 133232640000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": 5
        }
    }
    ```



=== "test_type_20024"


    ```json
	{
        "Version": 1,
        "Type": 20024,
        "TypeComputedMap": "NewConfigurationFromUpdateErrorNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C916A-4D69-416B-8014-BB8C8E461CFB}",
        "Timestamp": "2023-06-15T01:50:00.0000000+01:00",
        "TimestampRaw": 133232646000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20025"


    ```json
	{
        "Version": 1,
        "Type": 20025,
        "TypeComputedMap": "NewConfigurationFromUpdateNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0A125B-DF69-440B-B388-B1A9477E7D92}",
        "Timestamp": "2023-06-15T02:00:00.0000000+01:00",
        "TimestampRaw": 133232652000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20026"


    ```json
	{
        "Version": 1,
        "Type": 20026,
        "TypeComputedMap": "InvalidConfigurationPackageCab",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F5A8B-5487-4B22-981A-885363295252}",
        "Timestamp": "2023-06-15T02:10:00.0000000+01:00",
        "TimestampRaw": 133232658000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PackageCabFullPath": "C:\\Users\\User1\\Desktop\\EsConfig.hive",
            "LoadingOperationStatus": 5
        }
    }
    ```



=== "test_type_20027"


    ```json
	{
        "Version": 1,
        "Type": 20027,
        "TypeComputedMap": "DowngradeIsNotAuthorized",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD010390-5326-4D21-9673-CD1B80EF7562}",
        "Timestamp": "2023-06-15T02:20:00.0000000+01:00",
        "TimestampRaw": 133232664000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20028"


    ```json
	{
        "Version": 1,
        "Type": 20028,
        "TypeComputedMap": "SafeModeSessionNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0EF160-1AE3-47C3-8F2C-BA626C3D04C7}",
        "Timestamp": "2023-06-15T02:30:00.0000000+01:00",
        "TimestampRaw": 133232670000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "LoginName": "User1",
            "Timestamp": "2023-03-13T10:54:24.6100962+01:00"
        }
    }
    ```



=== "test_type_20030"


    ```json
	{
        "Version": 1,
        "Type": 20030,
        "TypeComputedMap": "MaintenanceModeStart",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B53D9-A9FF-4257-8A47-BA73FD9798EE}",
        "Timestamp": "2023-06-15T02:40:00.0000000+01:00",
        "TimestampRaw": 133232676000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20031"


    ```json
	{
        "Version": 1,
        "Type": 20031,
        "TypeComputedMap": "MaintenanceModeStop",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD067EED-CA85-4D98-8C35-8DC58D0943C3}",
        "Timestamp": "2023-06-15T02:50:00.0000000+01:00",
        "TimestampRaw": 133232682000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20032"


    ```json
	{
        "Version": 1,
        "Type": 20032,
        "TypeComputedMap": "MaintenanceModeAgentUpgradePostponed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0871CA-224C-4600-A48A-B562DB058C09}",
        "Timestamp": "2023-06-15T03:00:00.0000000+01:00",
        "TimestampRaw": 133232688000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20033"


    ```json
	{
        "Version": 1,
        "Type": 20033,
        "TypeComputedMap": "BfeIsStoppedNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0E7607-D279-4188-BE30-E2A887B80D32}",
        "Timestamp": "2023-06-15T03:10:00.0000000+01:00",
        "TimestampRaw": 133232694000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20034"


    ```json
	{
        "Version": 1,
        "Type": 20034,
        "TypeComputedMap": "RepairFailureNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0D4655-336D-4DD9-9532-78433F39364A}",
        "Timestamp": "2023-06-15T03:20:00.0000000+01:00",
        "TimestampRaw": 133232700000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555",
            "Result": 5
        }
    }
    ```



=== "test_type_20035"


    ```json
	{
        "Version": 1,
        "Type": 20035,
        "TypeComputedMap": "RepairSuccessNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0BBCE5-0299-4F04-9858-756036BCBFBC}",
        "Timestamp": "2023-06-15T03:30:00.0000000+01:00",
        "TimestampRaw": 133232706000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20036"


    ```json
	{
        "Version": 1,
        "Type": 20036,
        "TypeComputedMap": "EndAgentModularityFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD071DC0-58B6-4166-93AC-5E53F025C724}",
        "Timestamp": "2023-06-15T03:40:00.0000000+01:00",
        "TimestampRaw": 133232712000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5
        }
    }
    ```



=== "test_type_20037"


    ```json
	{
        "Version": 1,
        "Type": 20037,
        "TypeComputedMap": "EndAgentModularitySucceeded",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD016C2D-6BA8-4348-BA6D-92FB1CE190A8}",
        "Timestamp": "2023-06-15T03:50:00.0000000+01:00",
        "TimestampRaw": 133232718000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20038"


    ```json
	{
        "Version": 1,
        "Type": 20038,
        "TypeComputedMap": "CommFinishFailedState",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD05A0F2-7163-4A09-9F2D-AB6EA6171047}",
        "Timestamp": "2023-06-15T04:00:00.0000000+01:00",
        "TimestampRaw": 133232724000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5,
            "State": 8,
            "StateName": "PreviousStateName"
        }
    }
    ```



=== "test_type_20039"


    ```json
	{
        "Version": 1,
        "Type": 20039,
        "TypeComputedMap": "ForcedPatchApplication",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09E4CF-09F4-4E78-A3E9-C4CB48471D46}",
        "Timestamp": "2023-06-15T04:10:00.0000000+01:00",
        "TimestampRaw": 133232730000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20040"


    ```json
	{
        "Version": 1,
        "Type": 20040,
        "TypeComputedMap": "ChallengeStart",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD04C00F-2052-440A-9E43-E685F60E2ACF}",
        "Timestamp": "2023-06-15T04:20:00.0000000+01:00",
        "TimestampRaw": 133232736000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Duration": 0,
            "ChallengeAction": 3
        }
    }
    ```



=== "test_type_20041"


    ```json
	{
        "Version": 1,
        "Type": 20041,
        "TypeComputedMap": "ChallengeStop",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F233B-3CCE-470B-9312-A760E05C5065}",
        "Timestamp": "2023-06-15T04:30:00.0000000+01:00",
        "TimestampRaw": 133232742000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Manual": true,
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555",
            "ChallengeAction": 0
        }
    }
    ```



=== "test_type_20042"


    ```json
	{
        "Version": 1,
        "Type": 20042,
        "TypeComputedMap": "ChallengeStopFailure",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD01D6E5-6517-4E2C-B029-8A4668B9A2BE}",
        "Timestamp": "2023-06-15T04:40:00.0000000+01:00",
        "TimestampRaw": 133232748000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5
        }
    }
    ```



=== "test_type_20043"


    ```json
	{
        "Version": 1,
        "Type": 20043,
        "TypeComputedMap": "WrongCabinetVersion",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD052689-74F5-4E19-A0CE-13246249763C}",
        "Timestamp": "2023-06-15T04:50:00.0000000+01:00",
        "TimestampRaw": 133232754000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20044"


    ```json
	{
        "Version": 1,
        "Type": 20044,
        "TypeComputedMap": "MultipleNetworkInterfacesMatchingTest",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07AF61-2014-44FF-83D1-FAFDEBA00A20}",
        "Timestamp": "2023-06-15T05:00:00.0000000+01:00",
        "TimestampRaw": 133232760000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "InterfaceName": "DEV",
            "InterfaceDescription": "Lorem Iterfacum"
        }
    }
    ```



=== "test_type_20045"


    ```json
	{
        "Version": 1,
        "Type": 20045,
        "TypeComputedMap": "ChallengeStartFailure",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD04CFB2-80E8-4237-9345-B73E76623445}",
        "Timestamp": "2023-06-15T05:10:00.0000000+01:00",
        "TimestampRaw": 133232766000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5
        }
    }
    ```



=== "test_type_20048"


    ```json
	{
        "Version": 1,
        "Type": 20048,
        "TypeComputedMap": "External",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0A2E72-1187-4BF6-8773-235285060E82}",
        "Timestamp": "2023-06-15T05:20:00.0000000+01:00",
        "TimestampRaw": 133232772000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Description": "localized:EventForwarding_WinDefender_MalwareProtectionRealTimeProtectionFeatureConfigured",
            "OriginType": 2,
            "ExtraData": {
                "Message": "This is a message",
                "_OriginalText": "2021 Mar 24 17:54:54 WinEvtLog: Microsoft-Windows-Windows Defender/Operational: INFORMATION(5007): Microsoft-Windows-Windows Defender: SYSTEM: NT AUTHORITY: W102004X64: Microsoft Defender Antivirus Configuration has changed. If this is an unexpected event you should review the settings as this may be the result of malware.\r\n \tOld value: HKLM\\SOFTWARE\\Microsoft\\Windows Defender\\ServiceStartStates = 0x1\r\n \tNew value: Default\\ServiceStartStates = 0x0"
            },
            "Fields": {
                "BaseRuleGuid": "64a298f2-c9e8-451f-9637-84254d2d8332"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_20049"


    ```json
	{
        "Version": 1,
        "Type": 20049,
        "TypeComputedMap": "ChallengeTooManyFailedAttempts",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C6027-57C5-40B8-9A45-34C3259FD352}",
        "Timestamp": "2023-06-15T05:30:00.0000000+01:00",
        "TimestampRaw": 133232778000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20050"


    ```json
	{
        "Version": 1,
        "Type": 20050,
        "TypeComputedMap": "MaintenanceModeAgentModularityPostponed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0BF97F-A000-4C5E-B2FD-A9673DB49C79}",
        "Timestamp": "2023-06-15T05:40:00.0000000+01:00",
        "TimestampRaw": 133232784000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20051"


    ```json
	{
        "Version": 1,
        "Type": 20051,
        "TypeComputedMap": "EndUpgradeAgentNothingToDo",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD077BE1-8717-4796-AA97-4E4684223298}",
        "Timestamp": "2023-06-15T05:50:00.0000000+01:00",
        "TimestampRaw": 133232790000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20052"


    ```json
	{
        "Version": 1,
        "Type": 20052,
        "TypeComputedMap": "EndUpgradeAgentGuidUpdated",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD02DCFD-B400-42C2-BE32-B96BB54D4C10}",
        "Timestamp": "2023-06-15T06:00:00.0000000+01:00",
        "TimestampRaw": 133232796000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20053"


    ```json
	{
        "Version": 1,
        "Type": 20053,
        "TypeComputedMap": "MaintenanceModeStopFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07C559-BEF6-40F8-9624-C716A0F37F67}",
        "Timestamp": "2023-06-15T06:10:00.0000000+01:00",
        "TimestampRaw": 133232802000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 0
        }
    }
    ```



=== "test_type_20054"


    ```json
	{
        "Version": 1,
        "Type": 20054,
        "TypeComputedMap": "KerberosPassTheTicket",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F24A3-2C61-4822-89C7-25C274043270}",
        "Timestamp": "2023-06-15T06:20:00.0000000+01:00",
        "TimestampRaw": 133232808000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "KirbiFileFullPath": "C:\\mimikatz_trunk\\Win32\\MyTicket.kirbi",
            "Correlation": {
                "PackageGuid": "a0ba8928-f715-4d6f-b43e-5d020e67c030",
                "PackageVersion": 42
            },
            "SourceProcess": {
                "PID": 9,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "9d367a6c-04e4-491b-baa8-25b674db96d9",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD8FAFB221",
                "HashSha1": "AC9F34399C7C5A9372EFE0FA16F33D12116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E13976136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_20055"


    ```json
	{
        "Version": 1,
        "Type": 20055,
        "TypeComputedMap": "ArpSpoofing",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD089472-11D1-45E7-859C-2185C0BC56EB}",
        "Timestamp": "2023-06-15T06:30:00.0000000+01:00",
        "TimestampRaw": 133232814000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "IPInterface": "172.30.225.122",
            "SpoofedIP": "172.30.225.121",
            "OldMacAddress": "00-ff-b7-1f-9d-10",
            "SpoofedMacAddress": "00-ff-b7-1f-9d-11",
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_20056"


    ```json
	{
        "Version": 1,
        "Type": 20056,
        "TypeComputedMap": "AgentOperationCertutilDecodeMaliciousUsage",
        "Severity": 2,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD06E6EA-AC58-4B9F-96F2-1B4518003441}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:23:39.9571804+02:00",
        "TimestampRaw": 133311398199571804,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{FEFD7270-4013-94B9-0209-DEB987F40E89}",
                "PolicyVersion": 14,
                "RuleGuid": "{BEA2239E-7249-40A8-90BC-CD2981295600}",
                "BaseRuleGuid": "{BEA2239E-7249-40A8-90BC-CD2981295600}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Correlation": {
                "PackageGuid": "{06F508DA-1AB4-4A01-977D-2FD6E51C7F97}",
                "PackageVersion": 6
            },
            "SourceProcess": {
                "ProcessImageName": "C:\\Windows\\System32\\certutil.exe",
                "VolumeZone": 1,
                "HashSha1": "8564027153DCA487ECA613345AB3B2DE0ADD4F26",
                "ProcessStartTime": "2023-06-13T16:23:39.2631277+02:00",
                "SessionID": 2,
                "UserNameLookup": "JOHNDOE",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "HashMd5": "018796D4670AC12865BE2F00382BBC8E",
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "PID": 4904,
                "CertificateSignatureState": 1,
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "ProcessGuid": "{10C09418-9E9C-40E2-B7F7-20D70068CB34}",
                "ProcessCommandLine": "certutil-decode\"C:\\Users\\Arkoon\\Desktop\\certutil-decode.cmd\"\"C:\\Users\\Arkoon\\AppData\\Local\\Temp\\pwned.exe\"",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "ProcessStartTimeRaw": 133311398192631277,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "SigningTime": "2023-05-18T00:55:31.4620000+02:00",
                        "SubjectCN": "MicrosoftWindows",
                        "ValidityEnd": "2024-02-01T02:05:42.0000000+02:00",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "ValidityStart": "2023-02-03T02:05:42.0000000+02:00",
                        "Algorithm": "SHA256"
                    }
                ],
                "IsProtectedOrCritical": false,
                "HashSha256": "22D1471ED17C681AA5580C59712005E1C70EF9C306CBCAD245A64F7DFAE47847"
            },
            "ParentProcess": {
                "ProcessImageName": "C:\\Windows\\System32\\cmd.exe",
                "VolumeZone": 1,
                "HashSha1": "F1EFB0FDDC156E4C61C5F78A54700E4E7984D55D",
                "ProcessStartTime": "2023-06-13T16:23:39.0311777+02:00",
                "SessionID": 2,
                "UserNameLookup": "JOHNDOE",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "HashMd5": "8A2122E8162DBEF04694B9C3E0B6CDEE",
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "PID": 6808,
                "CertificateSignatureState": 1,
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "ProcessGuid": "{387F337F-56ED-4924-B1CC-96357B1E27B3}",
                "ProcessCommandLine": "C:\\WINDOWS\\system32\\cmd.exe/c\"\"C:\\Users\\Arkoon\\Desktop\\certutil-decode.cmd\"\"",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "ProcessStartTimeRaw": 133311398190311777,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "SigningTime": "2023-04-28T03:05:05.3450000+02:00",
                        "SubjectCN": "MicrosoftWindows",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "Algorithm": "SHA256"
                    }
                ],
                "IsProtectedOrCritical": false,
                "HashSha256": "B99D61D874728EDC0918CA0EB10EAB93D381E7367E377406E65963366C874450"
            },
            "SourceFilePath": "C:\\Users\\Arkoon\\Desktop\\certutil-decode.cmd",
            "DestinationFilePath": "C:\\Users\\Arkoon\\AppData\\Local\\Temp\\pwned.exe",
            "FileContentType": 0,
            "FileContentTypeComputedMap": "Unknown",
            "FileContent": "406563686F206F66660D0A0D0A0D0A6563686F2E4465636F64696E6720656D6265646465642070726F6772616D2E2E2E0D0A7365742022544D505F46494C455F4E414D453D2554454D50255C70776E65"
        }
    }
    ```



=== "test_type_20057"


    ```json
	{
        "Version": 1,
        "Type": 20057,
        "TypeComputedMap": "AgentOperationCertutilDownloadMaliciousUsage",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0CE797-8230-47F1-A98E-2F273D1AF92A}",
        "Timestamp": "2023-06-15T06:50:00.0000000+01:00",
        "TimestampRaw": 133232826000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "DownloadUrl": "http://sample.xyz/malicious.encoded",
            "DestinationFilePath": "c:\\malicious\\malicious.encoded",
            "ParentProcess": {
                "PID": 2,
                "ProcessImageName": "C:\\Windows\\System32\\notepad.exe",
                "UserSID": null,
                "SessionID": 2,
                "ProcessGuid": "92c248f1-0acd-11ea-a38a-00155d099004",
                "ProcessCommandLine": "\"C:\\Windows\\system32\\NOTEPAD.EXE\" C:\\Users\\arkoon\\Desktop\\_test\\test.totot",
                "HashMd5": "F1139811BBF61362915958806AD30211",
                "HashSha1": "D487580502354C61808C7180D1A336BEB7AD4624",
                "HashSha256": "F1D62648EF915D85CB4FC140359E925395D315C70F3566B63BB3E21151CB2CE3",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SigningTime": "2019-11-07T04:32:51.5641056+01:00",
                        "ValidityEnd": "2020-05-02T22:24:36.0705280+01:00",
                        "ValidityStart": "2019-05-02T22:24:36.7807872+01:00",
                        "SubjectCN": "Microsoft Windows"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "Correlation": {
                "PackageGuid": "c0d2b0ff-b222-43bb-b134-50e8f4589806",
                "PackageVersion": 42
            },
            "SourceProcess": {
                "PID": 5,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e79-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe\"",
                "HashMd5": "E6224FC8CF2A26B386934DAC0A3495D0",
                "HashSha1": "CF970FA39BA72CC531133EC327203EAD801DA846",
                "HashSha256": "A6AACEDC3F1E866A4ED815595F8FFA6AD99F6AEA7EC937E6AAA9EB4E68B39737",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 4,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4965475+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateRevoked"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_20059"


    ```json
	{
        "Version": 1,
        "Type": 20059,
        "TypeComputedMap": "AgentInternalScriptRuntimeError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09A421-A13C-49BF-AB67-B48A5884C559}",
        "Timestamp": "2023-06-15T07:00:00.0000000+01:00",
        "TimestampRaw": 133232832000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ExecutionStatus": 0,
            "ScriptGuid": "00000000-0000-0000-0000-000000000000"
        }
    }
    ```



=== "test_type_20060"


    ```json
	{
        "Version": 1,
        "Type": 20060,
        "TypeComputedMap": "WmiPersistence",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0903E9-4EEC-4EE0-9CBF-50E00F367470}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T07:02:14.4361240+02:00",
        "TimestampRaw": 133311421344361240,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{FEFD7270-4013-94B9-0209-DEB987F40E89}",
                "PolicyVersion": 14,
                "RuleGuid": "{D9AC047B-591C-42EA-86AD-0997EE000BEF}",
                "BaseRuleGuid": "{D9AC047B-591C-42EA-86AD-0997EE000BEF}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": true,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Correlation": {
                "PackageGuid": "{B757A1F5-8658-4567-A380-73F189F507E6}",
                "PackageVersion": 2
            },
            "ConsumerType": 0,
            "ConsumerTypeComputedMap": "CommandLineEventConsumer",
            "ExecutedAction": "cmd.exe/cecho%ProcessId%>>c:\\\\\\\\tmp\\\\\\\\log.txt",
            "ActionName": "Log01",
            "Trigger": "Query=\"SELECT*FROMWin32_ProcessStartTraceWHEREProcessName='powershell.exe'\"",
            "Namespace": "root/subscription",
            "ESS": "Log01",
            "Consumer": "CommandLineEventConsumer=\"Log01\"",
            "PossibleCause": "BindingEventFilter:\ninstanceof__EventFilter\n{\n\tCreatorSID={1,5,0,0,0,0,0,5,21,0,0,0,182,250,126,125,203,125,194,67,199,210,196,157,233,3,0,0};\n\tEventNamespace=\"root/cimv2\";\n\tName=\"Log01\";\n\tQuery=\"SELECT*FROMWin32_ProcessStartTraceWHEREProcessName='powershell.exe'\";\n\tQueryLanguage=\"WQL\";\n};\nPerm.Consumer:\ninstanceofCommandLineEventConsumer\n{\n\tCommandLineTemplate=\"cmd.exe/cecho%ProcessId%>>c:\\\\\\\\tmp\\\\\\\\log.txt\";\n\tCreatorSID={1,5,0,0,0,0,0,5,21,0,0,0,182,250,126,125,203,125,194,67,199,210,196,157,233,3,0,0};\n\tName=\"Log01\";\n};\n",
            "TimeCreated": "2023-06-13T15:02:08.6658788Z"
        }
    }
    ```



=== "test_type_20061"


    ```json
	{
        "Version": 1,
        "Type": 20061,
        "TypeComputedMap": "Discovery",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B6953-1407-4F68-B7BB-0540BD9F32B3}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T08:00:22.3680507+01:00",
        "TimestampRaw": 133203492223680517,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{C28F5498-FDC3-4E59-A13C-6139CE1FD00C}",
                "PolicyVersion": 1,
                "RuleGuid": "{468C2651-0EC0-42C5-A1D1-CA89F057DC0A}",
                "BaseRuleGuid": "{468C2651-0EC0-42C5-A1D1-CA89F057DC0A}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            },
            "Correlation": {
                "PackageGuid": "{9D0A8212-4B3F-4ABA-9548-D5AAB6095E19}",
                "PackageVersion": 4
            },
            "SourceProcess": {
                "VolumeZone": 1,
                "IntegrityLevel": "S-1-16-8192",
                "UserNameLookup": "JOHNDOE",
                "HashSha1": "F1EFB0FDDC156E4C61C5F78A54700E4E7984D55D",
                "CertificateSignatureState": 1,
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "ProcessGuid": "{9AC2D00F-F8B3-4917-B750-B3DAC7E6DC81}",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "SigningTime": "2022-06-09T00:22:44.7850000+01:00",
                        "ValidityStart": "2021-09-02T19:23:40.0000000+01:00",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "ValidityEnd": "2022-09-01T19:23:40.0000000+01:00"
                    }
                ],
                "HashSha256": "B99D61D874728EDC0918CA0EB10EAB93D381E7367E377406E65963366C874450",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "ProcessImageName": "C:\\Windows\\System32\\cmd.exe",
                "ProcessStartTimeRaw": 133203492157056139,
                "UserDomainLookup": "TEST",
                "ProcessStartTime": "2023-02-08T18:00:15.7056139+01:00",
                "PID": 5204,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "ProcessCommandLine": "\"C:\\Windows\\system32\\cmd.exe\"",
                "IsProtectedOrCritical": false,
                "HashMd5": "8A2122E8162DBEF04694B9C3E0B6CDEE",
                "SessionID": 2
            },
            "DiscoveryProcess": {
                "VolumeZone": 1,
                "IntegrityLevel": "S-1-16-8192",
                "UserNameLookup": "JOHNDOE",
                "HashSha1": "D9BBB4E4900FF03B0486FAC32768170249DAD82D",
                "CertificateSignatureState": 1,
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "ProcessGuid": "{D7235320-A1CF-4151-9451-1DFE77BC0F89}",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "SigningTime": "2022-06-09T01:51:05.6030000+01:00",
                        "ValidityStart": "2021-09-02T19:23:40.0000000+01:00",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "ValidityEnd": "2022-09-01T19:23:40.0000000+01:00"
                    }
                ],
                "HashSha256": "53E000F5AA9B3A00934319DB8080BB99CB323BF48FC628A64F75D7847C265606",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "ProcessImageName": "C:\\Windows\\System32\\ipconfig.exe",
                "ProcessStartTimeRaw": 133203492215762286,
                "UserDomainLookup": "TEST",
                "ProcessStartTime": "2023-02-08T18:00:21.5762286+01:00",
                "PID": 5364,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "ProcessCommandLine": "ipconfig",
                "IsProtectedOrCritical": false,
                "HashMd5": "62F170FB07FDBB79CEB7147101406EB8",
                "SessionID": 2
            },
            "BeginningTime": "2023-02-08T18:00:15.7184398+01:00",
            "TriggerTime": "2023-02-08T18:00:21.5797212+01:00"
        }
    }
    ```



=== "test_type_20062"


    ```json
	{
        "Version": 1,
        "Type": 20062,
        "TypeComputedMap": "AgentInternalUninstallForbidden",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD04A57F-EE9F-4D86-AAD5-E7FC20313376}",
        "Timestamp": "2023-06-15T07:30:00.0000000+01:00",
        "TimestampRaw": 133232850000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UninstallAttemptDateTime": "2020-07-07T09:29:06.066110400Z",
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20063"


    ```json
	{
        "Version": 1,
        "Type": 20063,
        "TypeComputedMap": "AgentInternalLogExceedMaxSize",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD062E12-865A-4B16-B57B-37205E59277B}",
        "Timestamp": "2023-06-15T07:40:00.0000000+01:00",
        "TimestampRaw": 133232856000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "FaultyLogType": 1010,
            "FaultyLogTypeComputedMap": null
        }
    }
    ```



=== "test_type_20064"


    ```json
	{
        "Version": 1,
        "Type": 20064,
        "TypeComputedMap": "StartModularityAgent",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F3A16-4E4E-4790-B3EB-5558D437C77E}",
        "Timestamp": "2023-06-15T07:50:00.0000000+01:00",
        "TimestampRaw": 133232862000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20065"


    ```json
	{
        "Version": 1,
        "Type": 20065,
        "TypeComputedMap": "StartRepairAgent",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD000F33-953C-49B2-9E91-A9D0D16FABFB}",
        "Timestamp": "2023-06-15T08:00:00.0000000+01:00",
        "TimestampRaw": 133232868000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20066"


    ```json
	{
        "Version": 1,
        "Type": 20066,
        "TypeComputedMap": "AgentInternalVolumeWithoutShadowStorage",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07B4CE-114A-42D1-8080-3E10EAAF1F3A}",
        "Timestamp": "2023-06-15T08:10:00.0000000+01:00",
        "TimestampRaw": 133232874000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "VolumePath": "\\\\?\\Volume{3799cd4d-464b-4908-9537-3984827f7c29}\\",
            "DriveLetter": "C:\\",
            "VolumeLabel": "some label"
        }
    }
    ```



=== "test_type_20067"


    ```json
	{
        "Version": 1,
        "Type": 20067,
        "TypeComputedMap": "AgentInternalShadowCopyCreationFailure",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD04DBA1-AC27-47D4-ABBF-588CD950C127}",
        "Timestamp": "2023-06-15T08:20:00.0000000+01:00",
        "TimestampRaw": 133232880000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "VolumePath": "\\\\?\\Volume{a14d9f90-5db7-4b3c-8cf1-d9bd2f9f1a64}\\",
            "DriveLetter": "C:\\",
            "VolumeLabel": "some label",
            "ErrorCode": 5
        }
    }
    ```



=== "test_type_20068"


    ```json
	{
        "Version": 1,
        "Type": 20068,
        "TypeComputedMap": "Ransomware",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C67CC-83EF-4966-8001-10A3B8B13EAC}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T05:23:07.3454198+01:00",
        "TimestampRaw": 133225861873454198,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{BF0D5FEE-FF2A-4E6B-97DA-A1FC246FE845}",
                "PolicyVersion": 2,
                "RuleGuid": "{158E5AB3-C2D2-4707-A8B0-9CD58950B8E2}",
                "BaseRuleGuid": "{158E5AB3-C2D2-4707-A8B0-9CD58950B8E2}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            },
            "Correlation": {
                "PackageGuid": "{C4E948CC-1082-47B9-BE66-10A1B88A3202}",
                "PackageVersion": 4
            },
            "SourceProcess": {
                "ProcessImageName": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "PID": 5816,
                "VolumeZone": 1,
                "HashMd5": "04029E121A0CFA5991749937DD22A1D9",
                "ProcessStartTimeRaw": 133225860434012095,
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "HighMandatoryLevel",
                "ProcessCommandLine": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\"",
                "ProcessStartTime": "2023-03-06T15:20:43.4012095+01:00",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "CertificateSignatureState": 1,
                "IsProtectedOrCritical": false,
                "SessionID": 2,
                "Certificates": [
                    {
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2022-12-02T00:08:48.1500000+01:00",
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "ValidityEnd": "2023-05-04T20:23:14.0000000+01:00",
                        "ValidityStart": "2022-05-05T20:23:14.0000000+01:00"
                    }
                ],
                "HashSha1": "F43D9BB316E30AE1A3494AC5B0624F6BEA1BF054",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "HashSha256": "9F914D42706FE215501044ACD85A32D58AAEF1419D404FDDFA5D3B48F66CCD9F",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "ProcessGuid": "{70FCCA79-9933-4734-8CD6-28AE2E501771}",
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "UserNameLookup": "JOHNDOE"
            },
            "AlteredFileListFilePath": "C:\\ProgramData\\Stormshield\\SESEvolution\\Agent\\Diagnostics\\RansomwareProtection\\encrypted_files2023-03-0615-23-07.txt",
            "OverallAlteredFilesCount": 10,
            "AlteredFiles": [
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(1).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(1).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(10).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(10).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(11).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(11).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(12).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(12).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(13).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(13).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(14).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(14).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(15).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(15).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(16).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(16).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(17).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(17).txt.jmBrN"
                },
                {
                    "SourceFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(18).txt",
                    "DestinationFilename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(18).txt.jmBrN"
                }
            ]
        }
    }
    ```



=== "test_type_20069"


    ```json
	{
        "Version": 1,
        "Type": 20069,
        "TypeComputedMap": "AgentInternalResourcePackageDownloadFailed",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09591B-3AF8-4605-96DE-64B269B9173E}",
        "Timestamp": "2023-06-15T08:40:00.0000000+01:00",
        "TimestampRaw": 133232892000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": 5,
            "ResourceGuid": "28110024-5807-45eb-9b7b-3aed55cb3f04"
        }
    }
    ```



=== "test_type_20070"


    ```json
	{
        "Version": 1,
        "Type": 20070,
        "TypeComputedMap": "AgentInternalInvalidResourcePackageSignature",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD018FE1-B276-4EB6-9E00-9A1CE516E02E}",
        "Timestamp": "2023-06-15T08:50:00.0000000+01:00",
        "TimestampRaw": 133232898000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": 5,
            "ResourceGuid": "ce78187e-1062-4075-9bce-d8c92ee2b99e",
            "ResourcePackageFile": "C:\\Users\\User1\\Desktop\\EsResource.cab"
        }
    }
    ```



=== "test_type_20071"


    ```json
	{
        "Version": 1,
        "Type": 20071,
        "TypeComputedMap": "AgentInternalSecOpsInvalidPackageSignature",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B84DD-18EA-4C30-8D5B-91D288F9368A}",
        "Timestamp": "2023-06-15T09:00:00.0000000+01:00",
        "TimestampRaw": 133232904000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": 5,
            "SecOpsGuid": "b9092244-2249-44bb-ae2d-f9e50a2b0b10",
            "SecOpsPackageFile": "C:\\Users\\User1\\Desktop\\SecOpsTask.cab"
        }
    }
    ```



=== "test_type_20072"


    ```json
	{
        "Version": 1,
        "Type": 20072,
        "TypeComputedMap": "AgentInternalSecOpsInvalidJsonSize",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0E2013-BED1-4DC5-95FB-A881DB5F386A}",
        "Timestamp": "2023-06-15T09:10:00.0000000+01:00",
        "TimestampRaw": 133232910000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "StatusCode": -1609564141,
            "SecOpsGuid": "fbba1fb1-efda-4bba-9929-2d5eae03344e",
            "SecOpsPackageFile": "C:\\Users\\User1\\Desktop\\SecOpsTask.cab",
            "JsonSize": 10241
        }
    }
    ```



=== "test_type_20073"


    ```json
	{
        "Version": 1,
        "Type": 20073,
        "TypeComputedMap": "AgentInternalDowngradeWithPivotVersion223IsRequired",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD02148D-0FE6-4428-805C-3B1A58BB1E1D}",
        "Timestamp": "2023-06-15T09:20:00.0000000+01:00",
        "TimestampRaw": 133232916000000000,
        "GenerateIncident": false,
        "SpecificData": {}
    }
    ```



=== "test_type_20079"


    ```json
	{
        "Version": 2,
        "Type": 20079,
        "TypeComputedMap": "AgentOperationYaraProcessAnalysisMatch",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0FD776-0C61-4946-BA0C-185518A0361C}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T01:58:14.4201973+02:00",
        "TimestampRaw": 133300870944201973,
        "SpecificData": {
            "SourceProcess": {
                "PID": 5848,
                "ProcessGuid": "{36C8E9F1-41B8-44FF-B482-FD11D323D5C7}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "C6CD12BF63E9B9B4478E6F975E7C293D",
                "HashSha1": "FE02128E2A9AF073DB5D6B3843469CA87391C22A",
                "HashSha256": "E1EA06C6884A2CEB9DD0EFEB788011AB2B17041F1C7438A9555415501E9E374C",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-01-06T12:27:04.6400000+02:00",
                        "ValidityStart": "2022-05-05T21:23:15.0000000+02:00",
                        "ValidityEnd": "2023-05-04T21:23:15.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-05-31T13:05:25.0959518+02:00",
                "ProcessStartTimeRaw": 133300047250959518
            },
            "Action": {
                "PolicyGuid": "{AD3E9A72-739A-4AEF-B62C-DB6A82EB6053}",
                "PolicyVersion": 4,
                "RuleGuid": "{6D01E214-075E-472C-A56D-3C6042DEA832}",
                "BaseRuleGuid": "{CF2EB1A3-0A18-4406-B284-F72A4E21D34F}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{919C4A6A-F381-4D01-A159-34C85152B5DF}",
                "Triggers": 8,
                "TriggersComputedBitMap": [
                    "TRIGGER_RULE_EVENT"
                ],
                "AssociatedEventGuid": "{41FD7022-DCDA-4ECE-983D-C780EC4315CA}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsRequestGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedBaseRuleGuid": "{BD00BBE6-3264-46D6-A010-AF9419FD7243}",
                "AssociatedRuleGuid": "{BD00BBE6-3264-46D6-A010-AF9419FD7245}"
            },
            "SourceProcessImageFileDetails": {
                "FileFullPath": "C:\\Windows\\explorer.exe",
                "FileCreateTime": "2023-01-12T10:52:38.2994281+02:00",
                "LastModified": "2023-01-12T10:52:38.4088025+02:00",
                "Owner": "S-1-5-21-2222222-33333333-44444444-555-2271478464",
                "OwnerNameLookup": "TrustedInstaller",
                "OwnerDomainLookup": "NTSERVICE",
                "HashMd5": "C6CD12BF63E9B9B4478E6F975E7C293D",
                "HashSha1": "FE02128E2A9AF073DB5D6B3843469CA87391C22A",
                "HashSha256": "E1EA06C6884A2CEB9DD0EFEB788011AB2B17041F1C7438A9555415501E9E374C",
                "HashSSDeep": "49152:JFV7+LB3mKxTLHWBwPvfb0xer5TaNFLGO3LL6Y6IEF98C21rf2JGno/n7w8A7/eE:obULwVw8a0cDl"
            },
            "MatchedYaraRules": [
                {
                    "MatchedRule": "test_yaralib_pe_module_is_pe_rule",
                    "Tags": [],
                    "Metadatas": [
                        {
                            "MetadataKey": "description",
                            "MetadataValue": "module_is_pe_rule"
                        },
                        {
                            "MetadataKey": "author",
                            "MetadataValue": "SESQAManuel"
                        }
                    ],
                    "MatchedStrings": []
                },
                {
                    "MatchedRule": "test_yaralib_pe_module_is_x64_rule",
                    "Tags": [],
                    "Metadatas": [
                        {
                            "MetadataKey": "description",
                            "MetadataValue": "module_is_x64_rule"
                        },
                        {
                            "MetadataKey": "author",
                            "MetadataValue": "SESQAManuel"
                        }
                    ],
                    "MatchedStrings": []
                }
            ]
        }
    }
    ```



=== "test_type_20080"


    ```json
	{
        "Version": 2,
        "Type": 20080,
        "TypeComputedMap": "AgentOperationYaraFileAnalysisMatch",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD08DEF4-1B0B-4DA3-8DDE-AAB23C392453}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T01:43:47.9837872+02:00",
        "TimestampRaw": 133300862279837872,
        "SpecificData": {
            "SourceProcess": {
                "PID": 2520,
                "ProcessGuid": "{A9344FD4-981C-4460-84B3-6649405DAF60}",
                "ProcessImageName": "C:\\ProgramFiles\\Notepad++\\notepad++.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\ProgramFiles\\Notepad++\\notepad++.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 2,
                "HashMd5": "B7E5E966EBB9C302155D6B6E0DA21721",
                "HashSha1": "ECA5EA2F815C856C22F8A9BA4C2C4C0713DADED0",
                "HashSha256": "31AC7D30E550EEE5F28E1A04F1E7E9346BA91849B27F24C700F098654C054A8B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1",
                        "SubjectCN": "Notepad++",
                        "SigningTime": "2023-05-15T06:12:16.0000000+02:00",
                        "ValidityStart": "2022-05-13T02:00:00.0000000+02:00",
                        "ValidityEnd": "2025-05-15T01:59:59.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-05-31T13:17:23.8002785+02:00",
                "ProcessStartTimeRaw": 133300054438002785
            },
            "Action": {
                "PolicyGuid": "{AD3E9A72-739A-4AEF-B62C-DB6A82EB6053}",
                "PolicyVersion": 2,
                "RuleGuid": "{41314BB5-45D2-4878-812A-6ED813D00D0B}",
                "BaseRuleGuid": "{5D368004-E074-42FA-8674-B35BA3C1FA89}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{68A0C3B1-05C5-4508-B22C-E87526EB8CB9}",
                "Triggers": 8,
                "TriggersComputedBitMap": [
                    "TRIGGER_RULE_EVENT"
                ],
                "AssociatedEventGuid": "{31BEA723-FB51-4461-A812-F7B379F09E8A}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsRequestGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedBaseRuleGuid": "{BD00BBE6-3264-46D6-A010-AF9419FD7243}",
                "AssociatedRuleGuid": "{BD00BBE6-3264-46D6-A010-AF9419FD7245}"
            },
            "FileDetails": {
                "FileFullPath": "C:\\ProgramFiles\\Notepad++\\notepad++.exe",
                "FileCreateTime": "2023-05-15T06:12:14.0000000+02:00",
                "LastModified": "2023-05-15T06:12:14.0000000+02:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrators",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "B7E5E966EBB9C302155D6B6E0DA21721",
                "HashSha1": "ECA5EA2F815C856C22F8A9BA4C2C4C0713DADED0",
                "HashSha256": "31AC7D30E550EEE5F28E1A04F1E7E9346BA91849B27F24C700F098654C054A8B",
                "HashSSDeep": "49152:5d9VFXdEK1BPN2efc5bjaMOoDsKEj45gvV+/QFw935Gt4/fDT5dOotDVhJJao0gB:p26UcvVUDDxD2MdpU/KGHiLUiRt/moD"
            },
            "SourceProcessImageFileDetails": {
                "FileFullPath": "C:\\ProgramFiles\\Notepad++\\notepad++.exe",
                "FileCreateTime": "2023-05-15T06:12:14.0000000+02:00",
                "LastModified": "2023-05-15T06:12:14.0000000+02:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrators",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "B7E5E966EBB9C302155D6B6E0DA21721",
                "HashSha1": "ECA5EA2F815C856C22F8A9BA4C2C4C0713DADED0",
                "HashSha256": "31AC7D30E550EEE5F28E1A04F1E7E9346BA91849B27F24C700F098654C054A8B",
                "HashSSDeep": "49152:5d9VFXdEK1BPN2efc5bjaMOoDsKEj45gvV+/QFw935Gt4/fDT5dOotDVhJJao0gB:p26UcvVUDDxD2MdpU/KGHiLUiRt/moD"
            },
            "MatchedYaraRules": [
                {
                    "MatchedRule": "test_yaralib_pe_module_is_pe_rule",
                    "Tags": [],
                    "Metadatas": [
                        {
                            "MetadataKey": "description",
                            "MetadataValue": "module_is_pe_rule"
                        },
                        {
                            "MetadataKey": "author",
                            "MetadataValue": "SESQAManuel"
                        }
                    ],
                    "MatchedStrings": []
                },
                {
                    "MatchedRule": "test_yaralib_pe_module_is_x64_rule",
                    "Tags": [],
                    "Metadatas": [
                        {
                            "MetadataKey": "description",
                            "MetadataValue": "module_is_x64_rule"
                        },
                        {
                            "MetadataKey": "author",
                            "MetadataValue": "SESQAManuel"
                        }
                    ],
                    "MatchedStrings": []
                }
            ]
        }
    }
    ```



=== "test_type_20081"


    ```json
	{
        "Version": 1,
        "Type": 20081,
        "TypeComputedMap": "AgentOperationYaraFileAnalysisMatchNoSourceProcess",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD06C8B7-7883-4C8B-862F-D9F67EA08BE7}",
        "Timestamp": "2023-06-15T09:50:00.0000000+01:00",
        "TimestampRaw": 133232934000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "MatchedYaraRules": [
                {
                    "MatchedRule": "First Yara rule",
                    "Tags": null,
                    "Metadatas": [
                        {
                            "MetadataKey": "First metadata key",
                            "MetadataValue": "First metadata value"
                        },
                        {
                            "MetadataKey": "Second metadata key",
                            "MetadataValue": "Second metadata value"
                        }
                    ]
                },
                {
                    "MatchedRule": "Second Yara rule",
                    "Tags": [
                        "First tag",
                        "Second tag",
                        "Third tag"
                    ],
                    "Metadatas": null
                },
                {
                    "MatchedRule": "Third Yara rule",
                    "Tags": [
                        "First tag",
                        "Second tag",
                        "Third tag"
                    ],
                    "Metadatas": [
                        {
                            "MetadataKey": "First metadata key",
                            "MetadataValue": "First metadata value"
                        },
                        {
                            "MetadataKey": "Second metadata key",
                            "MetadataValue": "Second metadata value"
                        }
                    ]
                }
            ],
            "FileDetails": {
                "FileFullPath": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_10.2102.13.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe",
                "FileCreateTime": "2021-06-05T15:33:12.3858496+01:00",
                "LastModified": "2021-06-05T15:33:12.3858496+01:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrators",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "0EB8934F47F01E59CAC3FE0E946EE516",
                "HashSha1": "B4CF1A5A6577BA51971B7B7094F0EED281B29223",
                "HashSha256": "D36B2DC6907940B9FDBDFEFCDCD49C9F1224922E77F1374C807C961E346239C8",
                "HashSSDeep": "384:m7Oi2cWe/2Hnd+GQW6bbA2WinQW6j32UkXLsK6QW6cI2i+eQW6fC26rjNfQW67AV:m7+nSRPXHQS+h9pxvxQfiRW8m1pPBWa"
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "00000000-0000-0000-0000-000000000000",
                "Triggers": 8,
                "AssociatedRuleGuid": "00000000-0000-0000-0000-000000000000",
                "AssociatedBaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "AssociatedEventGuid": "00000000-0000-0000-0000-000000000000",
                "AssociatedScheduledTaskGuid": "00000000-0000-0000-0000-000000000000",
                "AssociatedSecOpsGuid": "00000000-0000-0000-0000-000000000000",
                "AssociatedSecOpsRequestGuid": "00000000-0000-0000-0000-000000000000"
            }
        }
    }
    ```



=== "test_type_20082"


    ```json
	{
        "Version": 1,
        "Type": 20082,
        "TypeComputedMap": "PpidSpoofing",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD073784-5E81-4084-8814-9AC10C3EF1C6}",
        "Timestamp": "2023-06-15T00:00:00.0000000+01:00",
        "TimestampRaw": 133232940000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ParentProcess": {
                "PID": 6,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e83-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF44D9AFD9FAFB111",
                "HashSha1": "0C9F34399C7C5A9372EFE0F6E6F33DA4116016C6",
                "HashSha256": "2347766F6B5AD11E5C97167B5A452374EFF876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 8,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4765488+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadSignature"
            },
            "CreatedProcess": {
                "PID": 3,
                "ProcessImageName": "C:\\Windows\\System32\\services.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e1d-0f85-11ea-a38e-806e6f6e6963",
                "ProcessCommandLine": "C:\\Windows\\system32\\services.exe",
                "HashMd5": "FAE441A6EC7FD8F55A404797A25C8910",
                "HashSha1": "141C964905C4CA2110AD8FBFC3D17C960A9B9A54",
                "HashSha256": "70D7571253E091F646F78A4DD078CE7FE8D796625BFA3C0A466DF03971175FB4",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": null,
                "IntegrityLevelNameLookup": null,
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "Description": "Log Test",
            "Correlation": {
                "PackageGuid": "9172e535-7180-467a-874a-d92eb7a43d28",
                "PackageVersion": 42
            },
            "SourceProcess": {
                "PID": 10,
                "ProcessImageName": "C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "fc36ccb9-c9b6-495e-8ead-26e1536df4ad",
                "ProcessCommandLine": "\"C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF14D91238FAFB111",
                "HashSha1": "AC9F34399C7C5A6324EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7A23F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 7,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadContent"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_20083"


    ```json
	{
        "Version": 1,
        "Type": 20083,
        "TypeComputedMap": "IntegrityStart",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0DDBD7-BAC9-4F75-932D-8B68A34A6A7F}",
        "Timestamp": "2023-06-15T00:10:00.0000000+01:00",
        "TimestampRaw": 133232946000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": null,
            "UserDomainLookup": null,
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20084"


    ```json
	{
        "Version": 1,
        "Type": 20084,
        "TypeComputedMap": "IntegritySuccessNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0ED49D-9AA5-4470-A585-65B8A8DDAF49}",
        "Timestamp": "2023-06-15T00:20:00.0000000+01:00",
        "TimestampRaw": 133232952000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20085"


    ```json
	{
        "Version": 1,
        "Type": 20085,
        "TypeComputedMap": "RepairSuccessWithRebootNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0A53CA-5607-4B5C-A69D-BBE54085E159}",
        "Timestamp": "2023-06-15T00:30:00.0000000+01:00",
        "TimestampRaw": 133232958000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": null,
            "UserDomainLookup": null,
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20086"


    ```json
	{
        "Version": 1,
        "Type": 20086,
        "TypeComputedMap": "RepairSuccessWithoutRebootNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07A96B-A47A-49A7-9430-D87EE24D362B}",
        "Timestamp": "2023-06-15T00:40:00.0000000+01:00",
        "TimestampRaw": 133232964000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555"
        }
    }
    ```



=== "test_type_20087"


    ```json
	{
        "Version": 1,
        "Type": 20087,
        "TypeComputedMap": "IntegrityErrorNotification",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0FEB10-4AEA-4290-B09D-C89FE4025222}",
        "Timestamp": "2023-06-15T00:50:00.0000000+01:00",
        "TimestampRaw": 133232970000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "UserNameLookup": "JOHNDOE",
            "UserDomainLookup": "TEST",
            "User": "S-1-5-21-2222222-33333333-44444444-555",
            "Result": 5
        }
    }
    ```



=== "test_type_20089"


    ```json
	{
        "Version": 1,
        "Type": 20089,
        "TypeComputedMap": "AgentRemediationRemoveFile",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD0EF126-5D36-4566-9A32-8593CC49D14F}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:40:30.8104532+01:00",
        "TimestampRaw": 133222380308104532,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 0,
                "ResultComputedMap": "Success",
                "StatusCode": 0,
                "SecOpsTaskGuid": "{C416DCE5-1A8A-41C1-8011-47BD6B5F3BD1}",
                "SecOpsTaskRequestGuid": "{FB62B75C-EF25-4CD9-96F3-C0739790C932}"
            },
            "TargetResourcePath": "C:\\tmp\\Outils\\SysInternalTools\\AccessEnum.exe"
        }
    }
    ```



=== "test_type_20090"


    ```json
	{
        "Version": 1,
        "Type": 20090,
        "TypeComputedMap": "AgentRemediationKillProcess",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD0EEDAA-A2BD-44D4-8D11-7B04561402E7}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:14:54.4956830+01:00",
        "TimestampRaw": 133222364944956830,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 0,
                "ResultComputedMap": "Success",
                "StatusCode": 0,
                "SecOpsTaskGuid": "{31DB74FB-6E97-4B19-A6A5-5AA89DAE89F3}",
                "SecOpsTaskRequestGuid": "{75F53708-EF88-47A9-97D7-80860E11CE68}"
            },
            "TargetResourcePath": "C:\\ProgramFiles\\WindowsNT\\Accessories\\wordpad.exe",
            "ProcessPID": 6544,
            "KillChildren": true
        }
    }
    ```



=== "test_type_20091"


    ```json
	{
        "Version": 1,
        "Type": 20091,
        "TypeComputedMap": "AgentRemediationRemoveRegistryKey",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD0283A0-17CB-4489-A523-A57F738B0785}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T05:05:45.9777231+01:00",
        "TimestampRaw": 133225851459777231,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 2,
                "ResultComputedMap": "Error",
                "StatusCode": -2147024891,
                "SecOpsTaskGuid": "{B138E2EE-44DF-419F-8DA7-7C545042CD9D}",
                "SecOpsTaskRequestGuid": "{2C524176-967B-48B9-986C-133F8CECA476}"
            },
            "TargetResourcePath": "HKEY_LOCAL_MACHINE\\SOFTWARE"
        }
    }
    ```



=== "test_type_20092"


    ```json
	{
        "Version": 1,
        "Type": 20092,
        "TypeComputedMap": "AgentRemediationRemoveRegistryValue",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD0F8E33-E64C-4F46-BF17-D15ED6293319}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:40:51.1314021+01:00",
        "TimestampRaw": 133225836511314021,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 1,
                "ResultComputedMap": "Ignore",
                "StatusCode": 538247172,
                "SecOpsTaskGuid": "{8AEA4BCA-5605-4647-880F-2CF9349EAA30}",
                "SecOpsTaskRequestGuid": "{B0352589-BF7C-4751-B2BC-02D909FDB5ED}"
            },
            "TargetResourcePath": "HKEY_LOCAL_MACHINE\\SOFTWARE",
            "TargetResourceName": "Value2"
        }
    }
    ```



=== "test_type_20093"


    ```json
	{
        "Version": 1,
        "Type": 20093,
        "TypeComputedMap": "AgentRemediationSetRegistryValue",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD0A780A-CE3F-4AE5-BAB1-12923D5ED0F9}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:19:30.3592781+01:00",
        "TimestampRaw": 133225895703592781,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 0,
                "ResultComputedMap": "Success",
                "StatusCode": 0,
                "SecOpsTaskGuid": "{E1BC8B48-5B05-44D5-9840-FBB32EB9EB03}",
                "SecOpsTaskRequestGuid": "{B1FFCA74-1971-4EAD-9861-5868C699384A}"
            },
            "TargetResourcePath": "HKEY_USERS\\S-1-5-21-2222222-33333333-44444444-555\\SOFTWARE\\TEST_ADE",
            "TargetResourceName": "Valeur_String"
        }
    }
    ```



=== "test_type_20094"


    ```json
	{
        "Version": 1,
        "Type": 20094,
        "TypeComputedMap": "AgentRemediationExecutePowershellScript",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD02781E-45F4-4696-900A-0ACE3D39C133}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:58:15.9040047+01:00",
        "TimestampRaw": 133225846959040047,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 0,
                "ResultComputedMap": "Success",
                "StatusCode": 0,
                "SecOpsTaskGuid": "{0ABBCDE4-EF79-4AB5-A1B9-A2B4E45400DD}",
                "SecOpsTaskRequestGuid": "{B2893A58-3CC4-41D0-B93A-C7F3FE5A8174}"
            },
            "ScriptName": "Sleep.ps1",
            "ScriptGuid": "{2A643516-C835-436C-94BD-9F699819C108}",
            "ScriptExitCode": 0,
            "ScriptOutputFilePath": "C:\\ProgramData\\Stormshield\\SESEvolution\\Agent\\Diagnostics\\ScriptsLog\\Remediation\\script_Sleep_2023-03-06T13_57_44_565.log",
            "ScriptOutput": "DATA_MAPPING_CONTROL"
        }
    }
    ```



=== "test_type_20095"


    ```json
	{
        "Version": 1,
        "Type": 20095,
        "TypeComputedMap": "AgentRemediationExtractFilesFromShadowCopy",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 3,
        "ServerReserved": 2,
        "Attributes": 128,
        "AttributesComputedBitMap": [
            "Remediation"
        ],
        "EventGuid": "{AD076098-8C76-4FE6-A77D-F68AEDE5CF44}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T05:47:08.7369109+01:00",
        "TimestampRaw": 133225876287369109,
        "SpecificData": {
            "RemediationSpecificData": {
                "Result": 0,
                "ResultComputedMap": "Success",
                "StatusCode": 0,
                "SecOpsTaskGuid": "{0BE24A51-3A3E-473A-BE36-D251107D7240}",
                "SecOpsTaskRequestGuid": "{D6648978-E8CA-49E5-A663-D9D1E16ABE4A}"
            },
            "TargetResourcePath": "C:\\ProgramData\\Stormshield\\SESEvolution\\Agent\\Diagnostics\\RansomwareProtection\\Remediation_2023-03-06T14_47_08_321.log",
            "RestoredFilesCount": 10,
            "OverallAlteredFilesCount": 10,
            "RestoredFiles": [
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(1).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(10).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(11).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(12).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(13).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(14).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(15).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(16).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(17).txt"
                },
                {
                    "Filename": "C:\\tmp\\Rans\\TXT\\Fichier-Copie(18).txt"
                }
            ]
        }
    }
    ```



=== "test_type_20097"


    ```json
	{
        "Version": 1,
        "Type": 20097,
        "TypeComputedMap": "AgentOperationIocAnalysisNamedObjectMatch",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD072C3D-AB1C-4368-809E-BF2BFF2EFA27}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:07:53.6558208+01:00",
        "TimestampRaw": 133228372736558208,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{6349DD3C-CE0F-4EC0-B47D-588E0C1E6077}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{E8C67A70-F6C2-4F77-96A9-4FB3835AD7B4}",
                "AssociatedSecOpsRequestGuid": "{6E0C19BA-6A69-4C3D-AC78-ED53CF5DD85D}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "ObjectType": 12,
            "ObjectTypeComputedMap": "Mutant",
            "ObjectFullPath": "\\BaseNamedObjects\\TestMutex",
            "MatchedStrings": [
                "TestMutex"
            ]
        }
    }
    ```



=== "test_type_20098"


    ```json
	{
        "Version": 1,
        "Type": 20098,
        "TypeComputedMap": "AgentOperationIocAnalysisEventLogMatch",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD01BB83-9B82-408C-8939-5F88CF949F3C}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:53:21.4493866+02:00",
        "TimestampRaw": 133294892014493866,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{E9811493-6DC4-48AC-B463-88AD229DEFD3}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{DF270F34-2515-4960-81C1-3A30B5A24F1C}",
                "AssociatedSecOpsRequestGuid": "{11E5EDAA-512B-4D3C-8652-81C94C0DB9D7}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "Channel": "Security",
            "ProviderName": "Microsoft-Windows-Security-Auditing",
            "EventTypeId": 5058,
            "EventTimestamp": "2023-05-25T00:00:15.6197403+02:00",
            "EventXml": "<Eventxmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><ProviderName='Microsoft-Windows-Security-Auditing'Guid='{54849625-5478-4994-a5ba-3e3b0328c30d}'/><EventID>5058</EventID><Version>1</Version><Level>0</Level><Task>12292</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreatedSystemTime='2023-05-24T22:00:15.619740300Z'/><EventRecordID>11610</EventRecordID><Correlation/><ExecutionProcessID='744'ThreadID='2136'/><Channel>Security</Channel><Computer>SLS-AHandlerSES.test.local</Computer><Security/></System><EventData><DataName='SubjectUserSid'>S-1-5-20</Data><DataName='SubjectUserName'>SLS-AHANDLERSES$</Data><DataName='SubjectDomainName'>TEST</Data><DataName='SubjectLogonId'>0x3e4</Data><DataName='ClientProcessId'>2648</Data><DataName='ClientCreationTime'>2023-05-24T13:50:07.933149300Z</Data><DataName='ProviderName'>MicrosoftSoftwareKeyStorageProvider</Data><DataName='AlgorithmName'>UNKNOWN</Data><DataName='KeyName'>{ACBB9007-7D21-4AF1-982E-8A47B0F2BB63}</Data><DataName='KeyType'>%%2500</Data><DataName='KeyFilePath'>C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Roaming\\Microsoft\\Crypto\\Keys\\7a93793b6404c4af5e1f6403f45ed59e_6218503d-90d3-45cc-8364-dfa965c89518</Data><DataName='Operation'>%%2458</Data><DataName='ReturnCode'>0x0</Data></EventData></Event>",
            "EventDetails": "Keyfileoperation.\r\n\r\nSubject:\r\n\tSecurityID:\t\tS-1-5-20\r\n\tAccountName:\t\tSLS-AHANDLERSES$\r\n\tAccountDomain:\t\tTEST\r\n\tLogonID:\t\t0x3E4\r\n\r\nProcessInformation:\r\n\tProcessID:\t\t2648\r\n\tProcessCreationTime:\t\u200e2023\u200e-\u200e05\u200e-\u200e24T13:50:07.933149300Z\r\n\r\nCryptographicParameters:\r\n\tProviderName:\tMicrosoftSoftwareKeyStorageProvider\r\n\tAlgorithmName:\tUNKNOWN\r\n\tKeyName:\t{ACBB9007-7D21-4AF1-982E-8A47B0F2BB63}\r\n\tKeyType:\tUserkey.\r\n\r\nKeyFileOperationInformation:\r\n\tFilePath:\tC:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Roaming\\Microsoft\\Crypto\\Keys\\7a93793b6404c4af5e1f6403f45ed59e_6218503d-90d3-45cc-8364-dfa965c89518\r\n\tOperation:\tReadpersistedkeyfromfile.\r\n\tReturnCode:\t0x0",
            "MatchedStrings": [
                "Ygg9"
            ]
        }
    }
    ```



=== "test_type_20099"


    ```json
	{
        "Version": 1,
        "Type": 20099,
        "TypeComputedMap": "AgentOperationIocAnalysisFilenameMatch",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0DD64D-8F6E-4335-96FA-FBB643DDFEDA}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:30:18.9637194+01:00",
        "TimestampRaw": 133228422189637194,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{C59092CF-D526-4C36-915E-03BE46F2D7C1}",
                "PolicyVersion": 1,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{31B00338-D1AC-4350-97A2-3A2E22B4E985}",
                "Triggers": 8,
                "TriggersComputedBitMap": [
                    "TRIGGER_RULE_EVENT"
                ],
                "AssociatedEventGuid": "{84A64211-111D-4B8D-BB81-056DB6033E1E}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsRequestGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedBaseRuleGuid": "{AB5199CE-8818-48F5-B7B8-F81614B0E159}",
                "AssociatedRuleGuid": "{AB5199CE-8818-48F5-B7B8-F81614B0E15A}"
            },
            "SourceProcess": {
                "PID": 7832,
                "ProcessGuid": "{EDBD8108-81A8-488A-A7AA-9E977FD696CE}",
                "ProcessImageName": "C:\\Python37\\python.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"c:\\python37\\python.exe\"\"C:\\Python37\\Scripts\\robot.exe\"--loglevelTRACE--debugfiledebug.txt--outputdirC:\\frigg_report_level_3\\20230309143015[f49af303-d075-419a-966a-4235bf2fb16f]_[AT-10X64PRO]_[AnalysisOnFileACL]--includeScenarioIOCOnDetectionANDAgentANDAnalysisOnFileACL--variableLVL3_TAGFAMILY:ScenarioIOCOnDetectionANDAgentANDAnalysisOnFileACL--variableLVL3_REPORT_LINK:file://///192.168.131.17/frigg_level_3_for_user/20230309143015[f49af303-d075-419a-966a-4235bf2fb16f]_[AT-10X64PRO]_[AnalysisOnFileACL]/log.html--variableLVL1_UUID:SES_v2.4.0_Evolution__2023-03-09_14-24-40--variableLVL2_UUID:f49af303-d075-419a-966a-4235bf2fb16f--variableFRIGG_COMMIT:8d570fe75a2ae31e1553b4d26c78cdd06b980f12--variableINFRASTRUCTURE:primary--pythonpathC:\\Frigg\\src--suitestatlevel4--variableSECTION_TAG:SECTION_IOCC:\\Frigg\\src\\frigg\\poolsrf\\Scenarios\\IOCOnDetection",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "HighMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "606EA23A6E2CA45D2B601DEE04AA68DB",
                "HashSha1": "56ED184B6865F8137885CD1994D18763E8D22B9F",
                "HashSha256": "07AE6C5FD655FA9F9D86138B7D8FD6361A2418C359BF0CE55DB9A86CE31575E1",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "DigiCertSHA2AssuredIDCodeSigningCA",
                        "SubjectCN": "PythonSoftwareFoundation",
                        "SigningTime": "2019-10-15T01:12:48.0000000+01:00",
                        "ValidityStart": "2018-12-18T01:00:00.0000000+01:00",
                        "ValidityEnd": "2021-12-22T13:00:00.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-03-09T14:30:15.1408260+01:00",
                "ProcessStartTimeRaw": 133228422151408260
            },
            "FullPath": "C:\\tmp\\filecreate.txt",
            "MatchedStrings": [
                "filecreate"
            ]
        }
    }
    ```



=== "test_type_20100"


    ```json
	{
        "Version": 1,
        "Type": 20100,
        "TypeComputedMap": "AgentOperationIocAnalysisFilenameMatchNoSourceProcess",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0359AD-F6F6-4600-83DD-80BD350547CD}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:07:53.7120847+01:00",
        "TimestampRaw": 133228372737120847,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{9A8EE5F9-D1D6-4625-972E-211C4F38530C}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{180E7BA4-0D3B-4A80-92C1-AA923CC259C3}",
                "AssociatedSecOpsRequestGuid": "{6E0C19BA-6A69-4C3D-AC78-ED53CF5DD85D}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "FullPath": "c:\\tmp\\IOC_filename_type_match.txt",
            "MatchedStrings": [
                "IOC_filename_type"
            ]
        }
    }
    ```



=== "test_type_20101"


    ```json
	{
        "Version": 1,
        "Type": 20101,
        "TypeComputedMap": "AgentOperationIocAnalysisDnsRequestMatch",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD01C2C4-99ED-433F-9666-2D26FFE77EE1}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T01:52:00.1047712+01:00",
        "TimestampRaw": 133231783201047712,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{F741792F-CAF9-48AC-B603-E7E85478D1DE}",
                "Triggers": 64,
                "TriggersComputedBitMap": [
                    "TRIGGER_SCHEDULED"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{B9219B67-6D7A-4837-9FBB-AC731993E218}",
                "AssociatedSecOpsGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsRequestGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "DnsRequestTimestamp": "2023-03-09T14:30:36.6393490+01:00",
            "DnsRequest": "LDU-10X64",
            "MatchedStrings": [
                "ldu-10x64"
            ]
        }
    }
    ```



=== "test_type_20105"


    ```json
	{
        "Version": 1,
        "Type": 20105,
        "TypeComputedMap": "AgentOperationIocFileSearchByHashFile",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0FF39E-F163-408E-A79F-154924466C24}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T00:22:46.0645687+01:00",
        "TimestampRaw": 133229137660645687,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{D0F30E76-25C7-4179-B37F-16A6638243ED}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{64E13EFB-DBA5-405E-AA87-52D0E6DC0A8A}",
                "AssociatedSecOpsRequestGuid": "{36C30206-83CB-4B22-A80E-F32F55B1B793}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "FileDetails": {
                "FileFullPath": "C:\\tmp\\Dataset\\IOC_filename_type_match.txt",
                "FileCreateTime": "2023-03-09T14:32:39.0955996+01:00",
                "LastModified": "2023-03-09T14:44:10.9444734+01:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrateurs",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "0369387A3D15EA774708761AC1B15146",
                "HashSha1": "CE2C4F63864E3173A9D4C94A88A5061BE890F3D9",
                "HashSha256": "0E2D8F90D85A86BA544BDC868CD06F90C49CB3227496ABD3ABC52B0AB83680A9",
                "HashSSDeep": "3:S6LnhR:JLnH"
            },
            "SearchMatchInformation": {
                "HashAlgorithm": 1,
                "HashAlgorithmComputedMap": "IOC_ALGORITMH_DIGEST_SHA1",
                "SimilarityRate": 100,
                "MatchedHash": "CE2C4F63864E3173A9D4C94A88A5061BE890F3D9"
            }
        }
    }
    ```



=== "test_type_20106"


    ```json
	{
        "Version": 1,
        "Type": 20106,
        "TypeComputedMap": "AgentOperationIocFileSearchByHashProcess",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0A3870-F4B7-4DB2-BB32-1391F05682E3}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T06:58:31.6633661+01:00",
        "TimestampRaw": 133228511116633661,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{D0F30E76-25C7-4179-B37F-16A6638243ED}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{3D074CE1-6E5D-4EEC-9C54-B0B1CEEBE3DF}",
                "AssociatedSecOpsRequestGuid": "{719C335F-EB0F-4A68-8D1D-9683CFB40D31}",
                "AssociatedBaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedRuleGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "SourceProcessImageFileDetails": {
                "FileFullPath": "C:\\tmp\\qa_custom_dll_caller.exe",
                "FileCreateTime": "2023-03-09T14:43:40.4150413+01:00",
                "LastModified": "2022-11-16T16:51:01.1796489+01:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrateurs",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "4942BD5298DC4E4EFDADC95A46C37B56",
                "HashSha1": "AAFA7B6F88BDB51202DCB161123C0441D40A5A2B",
                "HashSha256": "1C77A55289240221CF110A1AC336D375D4F8E190D6A540F97A610D642CA096DA",
                "HashSSDeep": "48:6Mapd6WlAax/6NMPo5g0xminE+kCtaTzxlkssoFjpfbNtm:yrBro5g0xmSei0zNt"
            },
            "SearchMatchInformation": {
                "HashAlgorithm": 1,
                "HashAlgorithmComputedMap": "IOC_ALGORITMH_DIGEST_SHA1",
                "SimilarityRate": 100,
                "MatchedHash": "AAFA7B6F88BDB51202DCB161123C0441D40A5A2B"
            },
            "SourceProcess": {
                "PID": 2300,
                "ProcessGuid": "{FF3D97B0-8340-4750-BD82-18792EF11A01}",
                "ProcessImageName": "C:\\tmp\\qa_custom_dll_caller.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\tmp\\qa_custom_dll_caller.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "4942BD5298DC4E4EFDADC95A46C37B56",
                "HashSha1": "AAFA7B6F88BDB51202DCB161123C0441D40A5A2B",
                "HashSha256": "1C77A55289240221CF110A1AC336D375D4F8E190D6A540F97A610D642CA096DA",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 2,
                "CertificateSignatureStateComputedMap": "SignatureStateNoSignature",
                "Certificates": [],
                "ProcessStartTime": "2023-03-09T14:51:13.8781511+01:00",
                "ProcessStartTimeRaw": 133228434738781511
            }
        }
    }
    ```



=== "test_type_20107"


    ```json
	{
        "Version": 1,
        "Type": 20107,
        "TypeComputedMap": "AgentOperationIocAnalysisTextualSearchProcessMatch",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD01D628-71C0-4432-A358-142306F65E42}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:49:04.5989765+02:00",
        "TimestampRaw": 133311341445989765,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{C6F96B4B-22E1-4F77-B74B-BBB94E7DCEC5}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{D4782D23-E46A-462E-8934-BFDC32920706}",
                "AssociatedSecOpsRequestGuid": "{F5B8FBB4-9B35-45E7-80B6-2D6B81BDB126}",
                "AssociatedBaseRuleGuid": "{BB1C16CA-8916-4891-9A65-078284B20EA1}",
                "AssociatedRuleGuid": "{8CFC6AE9-E111-403E-90AF-1912774CBEC4}"
            },
            "SourceProcess": {
                "PID": 4032,
                "ProcessGuid": "{358F6CB9-1326-469E-807D-9742D7799F1F}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "AC4C51EB24AA95B77F705AB159189E24",
                "HashSha1": "4583DAF9442880204730FB2C8A060430640494B1",
                "HashSha256": "6A671B92A69755DE6FD063FCBE4BA926D83B49F78C42DBAEED8CDB6BBC57576A",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA1",
                        "IssuerCN": "MicrosoftWindowsVerificationPCA",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2010-11-20T21:37:13.0000000+02:00",
                        "ValidityStart": "2009-12-07T23:57:40.0000000+02:00",
                        "ValidityEnd": "2011-03-07T23:57:40.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-13T14:21:19.3323750+02:00",
                "ProcessStartTimeRaw": 133311324793323750
            },
            "SourceProcessImageFileDetails": {
                "FileFullPath": "C:\\Windows\\explorer.exe",
                "FileCreateTime": "2010-11-21T05:24:35.3136502+02:00",
                "LastModified": "2010-11-21T05:24:35.3448503+02:00",
                "Owner": "S-1-5-21-2222222-33333333-44444444-555-2271478464",
                "OwnerNameLookup": "TrustedInstaller",
                "OwnerDomainLookup": "NTSERVICE",
                "HashMd5": "AC4C51EB24AA95B77F705AB159189E24",
                "HashSha1": "4583DAF9442880204730FB2C8A060430640494B1",
                "HashSha256": "6A671B92A69755DE6FD063FCBE4BA926D83B49F78C42DBAEED8CDB6BBC57576A",
                "HashSSDeep": "49152:jxrceI/lIRYraisQhFCUCAvYYYYYYYYYYYRYYYYYYYYYYE3iA7/eFUJN9ojoso2W:FrcPlIWFvYYYYYYYYYYYRYYYYYYYYYY4"
            },
            "MatchedStrings": [
                "fichiertexte.txt",
                "hello",
                "qa_custom_dll_caller.exe",
                "toto"
            ]
        }
    }
    ```



=== "test_type_20108"


    ```json
	{
        "Version": 1,
        "Type": 20108,
        "TypeComputedMap": "AgentOperationIocAnalysisTextualSearchFileMatch",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0882E8-4A4E-4427-BDF6-F93C68BC2CDB}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T00:31:29.6673890+01:00",
        "TimestampRaw": 133229142896673890,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{ACF0AC80-F5CC-4358-8CF9-3F8656637608}",
                "PolicyVersion": 2,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{4C7AAAF5-7BD4-4390-B43A-482695D9F2C8}",
                "Triggers": 8,
                "TriggersComputedBitMap": [
                    "TRIGGER_RULE_EVENT"
                ],
                "AssociatedEventGuid": "{DCBFD32B-23DA-44DC-A50F-CCC0CFFE36BD}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsRequestGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedBaseRuleGuid": "{488C741A-6311-484B-8B99-2AE642629CA2}",
                "AssociatedRuleGuid": "{3A361A3F-BA50-4C5F-94EC-EF57E5ECF5DD}"
            },
            "SourceProcess": {
                "PID": 1580,
                "ProcessGuid": "{66722ED3-5C92-49CB-919F-F8F710D2A7F6}",
                "ProcessImageName": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "7353F60B1739074EB17C5F4DDDEFE239",
                "HashSha1": "6CBCE4A295C163791B60FC23D285E6D84F28EE4C",
                "HashSha256": "DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2018-09-15T08:03:08.1030000+01:00",
                        "ValidityStart": "2018-07-03T21:45:50.0000000+01:00",
                        "ValidityEnd": "2019-07-26T21:45:50.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-03-10T10:30:15.9993999+01:00",
                "ProcessStartTimeRaw": 133229142159993999
            },
            "SourceProcessImageFileDetails": {
                "FileFullPath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "FileCreateTime": "2018-09-15T08:14:14.4547673+01:00",
                "LastModified": "2018-09-15T08:14:14.4547673+01:00",
                "Owner": "S-1-5-21-2222222-33333333-44444444-555-2271478464",
                "OwnerNameLookup": "TrustedInstaller",
                "OwnerDomainLookup": "NTSERVICE",
                "HashMd5": "7353F60B1739074EB17C5F4DDDEFE239",
                "HashSha1": "6CBCE4A295C163791B60FC23D285E6D84F28EE4C",
                "HashSha256": "DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C",
                "HashSSDeep": "6144:+srKopvMWwO9sV1yZywi/PzNKXzJ7BapCK5d3klRzULOnWyjLsPhAQzqO:BrKopEW2KXzJ4pdd3klnnWosPhnzq"
            },
            "FileDetails": {
                "FileFullPath": "C:\\tmp\\testfile1.txt",
                "FileCreateTime": "2023-03-10T10:31:28.6944664+01:00",
                "LastModified": "2023-03-10T10:31:28.6974654+01:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrateurs",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "F5A4425F79015B506FD72DEC488FECAA",
                "HashSha1": "7AC7F7D77BA681397E6F81E343562F43D315143D",
                "HashSha256": "F7ED90A977D853D055AAED809EAF0733C160E60F27461F04A59CE21B0D996A35",
                "HashSSDeep": "3:QswlSxuQaal:QswlS5j"
            },
            "MatchedStrings": [
                "IOC_event_app"
            ]
        }
    }
    ```



=== "test_type_20109"


    ```json
	{
        "Version": 1,
        "Type": 20109,
        "TypeComputedMap": "AgentOperationIocAnalysisTextualSearchFileMatchNoSourceProcess",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0C7323-D0B6-492F-B6DC-B503DFE65054}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T00:22:46.7229516+01:00",
        "TimestampRaw": 133229137667229516,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{00000000-0000-0000-0000-000000000000}",
                "PolicyVersion": 0,
                "RuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "BaseRuleGuid": "{00000000-0000-0000-0000-000000000000}",
                "IdentifierGuid": "{00000000-0000-0000-0000-000000000000}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "AnalysisProperties": {
                "AnalysisUnitGuid": "{8D1643D7-0358-4D5D-B5DE-2FF3A68AE55D}",
                "Triggers": 128,
                "TriggersComputedBitMap": [
                    "TRIGGER_SECOPS"
                ],
                "AssociatedEventGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedScheduledTaskGuid": "{00000000-0000-0000-0000-000000000000}",
                "AssociatedSecOpsGuid": "{C309C9F5-8BAB-42A0-BBE2-A912143FB308}",
                "AssociatedSecOpsRequestGuid": "{36C30206-83CB-4B22-A80E-F32F55B1B793}",
                "AssociatedBaseRuleGuid": "{73F4E7F0-49CA-42E7-94E7-9CF7B5F07C93}",
                "AssociatedRuleGuid": "{8CFC6AE9-E111-403E-90AF-1912774CBEC4}"
            },
            "FileDetails": {
                "FileFullPath": "C:\\tmp\\Dataset\\IOC_filename_type_match.txt",
                "FileCreateTime": "2023-03-09T14:32:39.0955996+01:00",
                "LastModified": "2023-03-09T14:44:10.9444734+01:00",
                "Owner": "S-1-5-32-544",
                "OwnerNameLookup": "Administrateurs",
                "OwnerDomainLookup": "BUILTIN",
                "HashMd5": "0369387A3D15EA774708761AC1B15146",
                "HashSha1": "CE2C4F63864E3173A9D4C94A88A5061BE890F3D9",
                "HashSha256": "0E2D8F90D85A86BA544BDC868CD06F90C49CB3227496ABD3ABC52B0AB83680A9",
                "HashSSDeep": "3:S6LnhR:JLnH"
            },
            "MatchedStrings": [
                "IOC_event_app"
            ]
        }
    }
    ```



=== "test_type_301"


    ```json
	{
        "Version": 1,
        "Type": 301,
        "TypeComputedMap": "Floppy",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD093442-0673-4288-9682-089F74158DA4}",
        "Timestamp": "2023-06-15T04:30:00.0000000+01:00",
        "TimestampRaw": 133232382000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "PnPDeviceInfo": {
                "DeviceDescription": "This is a disk drive",
                "Manufacturer": "Kingston",
                "ClassName": "DiskDrive",
                "FriendlyName": "SanDisk"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_302"


    ```json
	{
        "Version": 1,
        "Type": 302,
        "TypeComputedMap": "CDRom",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD097A02-082C-44A2-87BB-6D6DC511FC45}",
        "Timestamp": "2023-06-15T04:40:00.0000000+01:00",
        "TimestampRaw": 133232388000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Operation": 0,
            "PnPDeviceInfo": {
                "DeviceDescription": "This is a disk drive",
                "Manufacturer": "Kingston",
                "ClassName": "DiskDrive",
                "FriendlyName": "SanDisk"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_303"


    ```json
	{
        "Version": 1,
        "Type": 303,
        "TypeComputedMap": "ComPort",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD087B9D-25F8-42A4-BA9D-ED3D3A87E3F6}",
        "Timestamp": "2023-06-15T04:50:00.0000000+01:00",
        "TimestampRaw": 133232394000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_305"


    ```json
	{
        "Version": 1,
        "Type": 305,
        "TypeComputedMap": "UsbDevice",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD07AA0D-B844-4707-8E84-ED8B03025B17}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:44:36.7982369+02:00",
        "TimestampRaw": 133311338767982369,
        "SpecificData": {
            "UsbDeviceInfo": {
                "VendorId": 5118,
                "ProductId": 25344,
                "Class": 0,
                "ClassComputedMap": "UseclassinformationintheInterfaceDescriptors",
                "SubClass": 0,
                "Protocol": 0,
                "SerialNumber": "072117691198E329",
                "VendorName": "",
                "ProductName": "USBDISK3.0",
                "Interfaces": [
                    {
                        "Class": 8,
                        "ClassComputedMap": "MassStorage",
                        "Subclass": 6,
                        "Protocol": 80
                    }
                ]
            },
            "PhysicalConsoleSession": {
                "PhysicalConsoleSessionId": 1,
                "LoginUserName": "TEST\\user1"
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 3,
                "RuleGuid": "{15FE2620-5AB1-418E-B390-A8519F21EDA3}",
                "BaseRuleGuid": "{15FE2620-5AB1-418E-B390-A8519F21EDA2}",
                "IdentifierGuid": "{7337F8D7-D797-4A0F-AD46-BF317FFE7900}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "DeviceEventType": 0,
            "DeviceEventTypeComputedMap": "USBdeviceconnection"
        }
    }
    ```



=== "test_type_325"


    ```json
	{
        "Version": 1,
        "Type": 325,
        "TypeComputedMap": "UsbVolumeScanSuccess",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 4,
        "AttributesComputedBitMap": [
            "Internal"
        ],
        "EventGuid": "{AD01376E-B19F-412B-8D84-408FB15947B5}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T01:27:17.7845217+02:00",
        "TimestampRaw": 133312084377845217,
        "SpecificData": {
            "UsbDeviceInfo": {
                "VendorId": 1921,
                "ProductId": 21889,
                "Class": 0,
                "ClassComputedMap": "UseclassinformationintheInterfaceDescriptors",
                "SubClass": 0,
                "Protocol": 0,
                "SerialNumber": "04012f7f3a01c1ae65cdfeac1c2c89feb540858b0d034bc2c60f7de6edef26d7c8e6000000000000000000003b1bd6130017801881558107caa8e117",
                "VendorName": "USB",
                "ProductName": "SanDisk3.2Gen1",
                "Interfaces": [
                    {
                        "Class": 8,
                        "ClassComputedMap": "MassStorage",
                        "Subclass": 6,
                        "Protocol": 80
                    }
                ]
            },
            "TrackingData": {
                "EnrollFileState": 1,
                "EnrollFileStateComputedMap": "Enrollfileisinvalid.",
                "FootprintFileState": 0,
                "FootprintFileStateComputedMap": "Nofootprintfile",
                "VendorId": 0,
                "ProductId": 0,
                "SerialNumberHashSha256": "0000000000000000000000000000000000000000000000000000000000000000",
                "EnrollGuid": "{00000000-0000-0000-0000-000000000000}"
            },
            "ScannedFileCount": 0,
            "QuarantinedFileCount": 0,
            "VolumePath": "E:\\"
        }
    }
    ```



=== "test_type_326"


    ```json
	{
        "Version": 1,
        "Type": 326,
        "TypeComputedMap": "UsbVolumeScanError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09E648-81DB-4F9D-8C4F-A417443FCB63}",
        "Timestamp": "2023-06-15T05:40:00.0000000+01:00",
        "TimestampRaw": 133232424000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5,
            "UsbDeviceInfo": {
                "VendorName": "SanDisk",
                "VendorId": 1921,
                "ProductName": "Ultra",
                "ProductId": 21889,
                "SerialNumber": "4C530001211017121370",
                "Class": 88,
                "SubClass": 9,
                "Interfaces": [
                    {
                        "Class": 9,
                        "SubClass": 255
                    },
                    {
                        "Class": 9,
                        "SubClass": 14
                    },
                    {
                        "Class": 5,
                        "SubClass": 255
                    }
                ]
            },
            "TrackingData": {
                "EnrollFileState": 1,
                "EnrollGuid": "936abb9c-1151-4087-be6f-95b59a432830",
                "FootprintFileState": 0
            },
            "VolumePath": "E:\\\\"
        }
    }
    ```



=== "test_type_327"


    ```json
	{
        "Version": 1,
        "Type": 327,
        "TypeComputedMap": "UsbVolumeFootprintComputationError",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD075EFB-625D-4664-A6EC-DCED30701CDF}",
        "Timestamp": "2023-06-15T05:50:00.0000000+01:00",
        "TimestampRaw": 133232430000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ErrorCode": 5,
            "UsbDeviceInfo": {
                "VendorName": "SanDisk",
                "VendorId": 1921,
                "ProductName": "Ultra",
                "ProductId": 21889,
                "SerialNumber": "4C530001211017121370",
                "Class": 239,
                "SubClass": 224,
                "Interfaces": [
                    {
                        "Class": 17,
                        "SubClass": 17
                    },
                    {
                        "Class": 239,
                        "SubClass": 7
                    },
                    {
                        "Class": 255,
                        "SubClass": 1
                    }
                ]
            },
            "TrackingData": {
                "EnrollFileState": 4,
                "EnrollGuid": "58cb78b6-510a-4144-8ad9-c120b0513ed9",
                "FootprintFileState": 0
            },
            "VolumePath": "E:\\\\"
        }
    }
    ```



=== "test_type_361"


    ```json
	{
        "Version": 1,
        "Type": 361,
        "TypeComputedMap": "BluetoothAccess",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD004BC1-D189-436D-8F8E-848F2E6ADC7A}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:30:40.7191880+02:00",
        "TimestampRaw": 133311330407191880,
        "SpecificData": {
            "ConnectedDeviceInfo": {
                "ClassOfDevice": 5898764,
                "DeviceName": "S22UltradeAur\u00e9lien",
                "MajorServiceClass": 720,
                "MajorServiceClassComputedBitMap": [
                    "Networking(LAN,Adhoc,...)",
                    "Capturing(Scanner,Microphone,...)",
                    "ObjectTransfer(v-Inbox,v-Folder,...)",
                    "Telephony(Cordlesstelephony,Modem,Headsetservice,...)"
                ],
                "MajorDeviceClass": 2,
                "MajorDeviceClassComputedMap": "Phone(cellular,cordless,payphone,modem,...)",
                "MinorDeviceClass": {
                    "Info": 3,
                    "InfoComputedMap": "Smartphone"
                }
            },
            "LocalRadioDeviceInfo": {
                "ClassOfDevice": 2752780,
                "DeviceName": "QA-SES-2",
                "MajorServiceClass": 336,
                "MajorServiceClassComputedBitMap": [
                    "Networking(LAN,Adhoc,...)",
                    "Capturing(Scanner,Microphone,...)",
                    "Audio(Speaker,Microphone,Headsetservice,...)"
                ],
                "MajorDeviceClass": 1,
                "MajorDeviceClassComputedMap": "Computer(desktop,notebook,PDA,organizers,....)",
                "MinorDeviceClass": {
                    "Info": 3,
                    "InfoComputedMap": "Laptop"
                }
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 2,
                "RuleGuid": "{3BF67592-5E87-41C3-8064-ED52A6FD0C9C}",
                "BaseRuleGuid": "{3BF67592-5E87-41C3-8064-ED52A6FD0C9B}",
                "IdentifierGuid": "{DCA4EA7A-F456-483C-BF17-3A9DFBF7B8CF}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_39"


    ```json
	{
        "Version": 1,
        "Type": 39,
        "TypeComputedMap": "RawVolumeAccess",
        "Severity": 3,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD078924-C897-4BF5-9EAC-62F34AAE31EB}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T02:12:28.8623750+02:00",
        "TimestampRaw": 133312975488623750,
        "SpecificData": {
            "SourceProcess": {
                "PID": 3236,
                "ProcessGuid": "{2C8AC69F-A395-4589-9C27-3B1BF5672D71}",
                "ProcessImageName": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operatingsystem"
                ],
                "ProcessCommandLine": "\"powershell.exe\"C:\\Frigg\\src\\frigg\\tools\\PowershellScript\\Protection\\AccessVolumeRaw\\AccessVolumeRaw.ps1C:\\Users\\Public\\20bedfd0-fbde-48e5-ab3b-8e3522b8a61e.jsonC:\\Users\\Public\\8648cd4c-4237-4122-a67e-9216bf42bf62.txt",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "HighMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "A575A7610E5F003CC36DF39E07C4BA7D",
                "HashSha1": "88E7CDC0B75364418E11B2C53F772085F1B61D1E",
                "HashSha256": "006CEF6EF6488721895D93E4CEF7FA0709C2692D74BDE1E22E2A8719B2A86218",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA1",
                        "IssuerCN": "MicrosoftWindowsVerificationPCA",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2016-12-10T13:42:48.0000000+02:00",
                        "ValidityStart": "2016-11-22T20:12:21.0000000+02:00",
                        "ValidityEnd": "2017-05-22T20:12:21.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-15T12:12:25.7998750+02:00",
                "ProcessStartTimeRaw": 133312975457998750
            },
            "Action": {
                "PolicyGuid": "{2AE83DF7-9180-4F10-9AB7-D43801EA60FC}",
                "PolicyVersion": 1,
                "RuleGuid": "{AD8FA125-A849-47E7-B398-6672D5E40E15}",
                "BaseRuleGuid": "{AD8FA125-A849-47E7-B398-6672D5E40E14}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": true,
                "RequestMoveToQuarantine": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Path": "C:",
            "VolumeZone": 1,
            "VolumeZoneComputedBitMap": [
                "Operatingsystem"
            ],
            "AccessType": 2,
            "AccessTypeComputedMap": "Write",
            "DataOffset": 0,
            "DataLength": 512
        }
    }
    ```



=== "test_type_40"


    ```json
	{
        "Version": 1,
        "Type": 40,
        "TypeComputedMap": "NetworkAccessBind",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD01AAFD-F6E1-4434-9048-4119FACE3B20}",
        "Timestamp": "2023-06-15T00:30:00.0000000+01:00",
        "TimestampRaw": 133232238000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Operation": 1,
            "AddressFamily": 0,
            "Protocol": 6,
            "LocalAddress": "1.2.3.4",
            "LocalPort": 21,
            "SourceProcess": {
                "PID": 10,
                "ProcessImageName": "C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "fc36ccb9-c9b6-495e-8ead-26e1536df4ad",
                "ProcessCommandLine": "\"C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF14D91238FAFB111",
                "HashSha1": "AC9F34399C7C5A6324EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7A23F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 7,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadContent"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_400"


    ```json
	{
        "Version": 1,
        "Type": 400,
        "TypeComputedMap": "WifiAccessConnectedNetwork",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 8,
        "AttributesComputedBitMap": [
            "Audit"
        ],
        "EventGuid": "{AD07F7A8-D39A-4AB7-B993-5415D12C1F30}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:59:31.1363444+02:00",
        "TimestampRaw": 133311347711363444,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 6,
                "RuleGuid": "{FCC06F94-0DBD-4DE6-904A-A267486EC5B8}",
                "BaseRuleGuid": "{FCC06F94-0DBD-4DE6-904A-A267486EC5B7}",
                "IdentifierGuid": "{68FB25E1-146B-40C2-876B-D72317D39711}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "ConnectionMode": 1,
            "ConnectionModeComputedBitMap": [
                "Infrastructure"
            ],
            "AuthAlgo": 2,
            "AuthAlgoComputedBitMap": [
                "WPA2personal"
            ],
            "Ssid": "AgentMobileS9P",
            "RemoteMacAddress": "8E9A69150D8F"
        }
    }
    ```



=== "test_type_401"


    ```json
	{
        "Version": 1,
        "Type": 401,
        "TypeComputedMap": "WifiAccessFunctionnality",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0F7AFA-D4BC-45AC-98E2-46FB56EDE7A2}",
        "Timestamp": "2023-06-15T06:20:00.0000000+01:00",
        "TimestampRaw": 133232448000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_41"


    ```json
	{
        "Version": 1,
        "Type": 41,
        "TypeComputedMap": "NetworkAccessAccept",
        "Category": 4,
        "CategoryComputedMap": "Other",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD08384E-F7B1-4E7E-ABFB-3F62FFD20102}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:21:41.0544635+01:00",
        "TimestampRaw": 133219741010544635,
        "SpecificData": {
            "SourceProcess": {
                "PID": 1300,
                "ProcessGuid": "{9BF8BDA3-3BD6-492E-A1AE-AA4ADCCFA899}",
                "ProcessImageName": "C:\\tmp\\2.4.0_Build_797\\SecurityAndTestingTools\\x64\\NetworkTester\\NetworkTesterServer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": ".\\NetworkTesterServer.exe--tcp--port5001--infinite-lc",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "AB1938E5473CE3CFD04FEDC5250953B7",
                "HashSha1": "A37FFBBF38FEB91D98F839F58F17C1420A665D55",
                "HashSha256": "BBB03C3F06A9E6A988DB2376DE191712A8767D245151714C6D45D35811C83FA2",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 2,
                "CertificateSignatureStateComputedMap": "SignatureStateNoSignature",
                "Certificates": [],
                "ProcessStartTime": "2023-02-27T13:21:37.0244871+01:00",
                "ProcessStartTimeRaw": 133219740970244871
            },
            "Action": {
                "PolicyGuid": "{26CE8F68-454A-4A1C-B6C1-18BF591AD255}",
                "PolicyVersion": 7,
                "RuleGuid": "{47CFDDF4-8532-45F1-80E3-46D945386D3E}",
                "BaseRuleGuid": "{47CFDDF4-8532-45F1-80E3-46D945386D3D}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Protocol": 6,
            "ProtocolComputedMap": "TCP",
            "Operation": 2,
            "OperationComputedMap": "Accept",
            "AddressFamily": 2,
            "AddressFamilyComputedMap": "IPv4",
            "LocalAddress": "1.2.3.4",
            "RemoteAddress": "5.6.7.8",
            "LocalPort": 5001,
            "RemotePort": 49726
        }
    }
    ```



=== "test_type_42"


    ```json
	{
        "Version": 1,
        "Type": 42,
        "TypeComputedMap": "NetworkAccessConnect",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0950D9-5F4A-4664-B567-591010BB82B6}",
        "Timestamp": "2023-06-15T00:50:00.0000000+01:00",
        "TimestampRaw": 133232250000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "RemoteAddress": "5.6.7.8",
            "RemotePort": 21,
            "Operation": 1,
            "AddressFamily": 0,
            "Protocol": 0,
            "LocalAddress": "1.2.3.4",
            "LocalPort": 80,
            "SourceProcess": {
                "PID": 7,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "277db927-ab05-43ad-aeca-68e5e8f2b934",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD9FAFB111",
                "HashSha1": "AC9F34399C7C5A9372EFE0F6E6F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374EFF876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_43"


    ```json
	{
        "Version": 1,
        "Type": 43,
        "TypeComputedMap": "ProcessHollowing",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0341EF-79A6-4EBC-9D7F-56F60740D4F4}",
        "Timestamp": "2023-06-15T00:00:00.0000000+01:00",
        "TimestampRaw": 133232220000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Operation": 6,
            "CreatedProcess": {
                "PID": 5,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e79-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe\"",
                "HashMd5": "E6224FC8CF2A26B386934DAC0A3495D0",
                "HashSha1": "CF970FA39BA72CC531133EC327203EAD801DA846",
                "HashSha256": "A6AACEDC3F1E866A4ED815595F8FFA6AD99F6AEA7EC937E6AAA9EB4E68B39737",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 4,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4965475+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateRevoked"
            },
            "SourceProcess": {
                "PID": 5,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e79-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsGuiSrv.exe\"",
                "HashMd5": "E6224FC8CF2A26B386934DAC0A3495D0",
                "HashSha1": "CF970FA39BA72CC531133EC327203EAD801DA846",
                "HashSha256": "A6AACEDC3F1E866A4ED815595F8FFA6AD99F6AEA7EC937E6AAA9EB4E68B39737",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 4,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4965475+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateRevoked"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_44"


    ```json
	{
        "Version": 1,
        "Type": 44,
        "TypeComputedMap": "StackPivot",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09F16B-4399-4542-B80F-F41E374DD031}",
        "Timestamp": "2023-06-15T00:10:00.0000000+01:00",
        "TimestampRaw": 133232226000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "SourceProcess": {
                "PID": 10,
                "ProcessImageName": "C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "fc36ccb9-c9b6-495e-8ead-26e1536df4ad",
                "ProcessCommandLine": "\"C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF14D91238FAFB111",
                "HashSha1": "AC9F34399C7C5A6324EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7A23F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 7,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadContent"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_45"


    ```json
	{
        "Version": 1,
        "Type": 45,
        "TypeComputedMap": "DriverLoading",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD09877A-957B-4A49-9D0D-6ECBD9D39EFD}",
        "Timestamp": "2023-06-15T00:20:00.0000000+01:00",
        "TimestampRaw": 133232232000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "FileOwnerNameLookup": "User1",
            "FileOwnerDomainLookup": "sshield1",
            "FileOwner": "S-1-5-21-2222222-33333333-44444444-555",
            "Path": "C:\\Windows\\malicious.dll",
            "SourceProcess": {
                "PID": 3,
                "ProcessImageName": "C:\\Windows\\System32\\services.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e1d-0f85-11ea-a38e-806e6f6e6963",
                "ProcessCommandLine": "C:\\Windows\\system32\\services.exe",
                "HashMd5": "FAE441A6EC7FD8F55A404797A25C8910",
                "HashSha1": "141C964905C4CA2110AD8FBFC3D17C960A9B9A54",
                "HashSha256": "70D7571253E091F646F78A4DD078CE7FE8D796625BFA3C0A466DF03971175FB4",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": null,
                "IntegrityLevelNameLookup": null,
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_46"


    ```json
	{
        "Version": 1,
        "Type": 46,
        "TypeComputedMap": "DriverGuard",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD091861-7366-47FA-84A0-A332D12C2C94}",
        "Timestamp": "2023-06-15T00:30:00.0000000+01:00",
        "TimestampRaw": 133232238000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "CorruptedDriverName": "CorruptedDriver",
            "CorruptingDriverPath": "CorruptingDriver",
            "FileOwnerNameLookup": "User1",
            "FileOwnerDomainLookup": "sshield1",
            "FileOwner": "S-1-5-21-2222222-33333333-44444444-555",
            "SourceProcess": {
                "PID": 3,
                "ProcessImageName": "C:\\Windows\\System32\\services.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e1d-0f85-11ea-a38e-806e6f6e6963",
                "ProcessCommandLine": "C:\\Windows\\system32\\services.exe",
                "HashMd5": "FAE441A6EC7FD8F55A404797A25C8910",
                "HashSha1": "141C964905C4CA2110AD8FBFC3D17C960A9B9A54",
                "HashSha256": "70D7571253E091F646F78A4DD078CE7FE8D796625BFA3C0A466DF03971175FB4",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": null,
                "IntegrityLevelNameLookup": null,
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_47"


    ```json
	{
        "Version": 1,
        "Type": 47,
        "TypeComputedMap": "HoneyPot",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD00D888-A11D-4C08-91F2-1BAC3808A9B3}",
        "Timestamp": "2023-06-15T00:40:00.0000000+01:00",
        "TimestampRaw": 133232244000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "FunctionName": "MaliciousFunc",
            "CallerModuleFileName": "malicious.dll",
            "ExtraParametersInfo": "Something something.",
            "SourceProcess": {
                "PID": 7,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "277db927-ab05-43ad-aeca-68e5e8f2b934",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD9FAFB111",
                "HashSha1": "AC9F34399C7C5A9372EFE0F6E6F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374EFF876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_50"


    ```json
	{
        "Version": 1,
        "Type": 50,
        "TypeComputedMap": "TokenGuard",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD049A47-6754-4C3C-AF7E-B9A9E5D3A448}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T04:30:44.2577805+02:00",
        "TimestampRaw": 133312194442577805,
        "SpecificData": {
            "SourceProcess": {
                "PID": 6600,
                "ProcessGuid": "{897C964E-15DE-4F9E-B089-DE3A8BB7AD92}",
                "ProcessImageName": "C:\\tmp\\TokenGuardTester\\TokenGuardTester.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": ".\\TokenGuardTester.exetokenmodify",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "HighMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "D23FBD2C75547282289DD9743673ED89",
                "HashSha1": "6182272741CB8BAA6AE60C158ED446717784ADFA",
                "HashSha256": "356C2AF15AA08027B827DF594CF9976C50EF85A744C10552DA451A353D91FC5F",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1",
                        "SubjectCN": "StormshieldSAS",
                        "SigningTime": "2023-04-28T18:23:01.0000000+02:00",
                        "ValidityStart": "2022-10-05T02:00:00.0000000+02:00",
                        "ValidityEnd": "2025-12-07T01:59:59.0000000+02:00"
                    },
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftIDVerifiedCSEOCCA01",
                        "SubjectCN": "StormshieldSAS",
                        "SigningTime": "2023-04-28T18:23:36.7530000+02:00",
                        "ValidityStart": "2023-04-28T17:02:55.0000000+02:00",
                        "ValidityEnd": "2023-05-01T17:02:55.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T14:30:44.2187460+02:00",
                "ProcessStartTimeRaw": 133312194442187460
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 9,
                "RuleGuid": "{3E715FA0-4C90-4D29-9D2F-1DF82A43D2A6}",
                "BaseRuleGuid": "{3E715FA0-4C90-4D29-9D2F-1DF82A43D2A5}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "Details": {
                "PrivilegesLow": 2675965948,
                "PrivilegesLowComputedBitMap": [
                    "SE_CREATE_TOKEN_PRIVILEGE",
                    "SE_ASSIGNPRIMARYTOKEN_PRIVILEGE",
                    "SE_LOCK_MEMORY_PRIVILEGE",
                    "SE_INCREASE_QUOTA_PRIVILEGE",
                    "SE_MACHINE_ACCOUNT_PRIVILEGE",
                    "SE_TCB_PRIVILEGE",
                    "SE_SECURITY_PRIVILEGE",
                    "SE_TAKE_OWNERSHIP_PRIVILEGE",
                    "SE_LOAD_DRIVER_PRIVILEGE",
                    "SE_SYSTEM_PROFILE_PRIVILEGE",
                    "SE_SYSTEMTIME_PRIVILEGE",
                    "SE_PROF_SINGLE_PROCESS_PRIVILEGE",
                    "SE_INC_BASE_PRIORITY_PRIVILEGE",
                    "SE_CREATE_PAGEFILE_PRIVILEGE",
                    "SE_CREATE_PERMANENT_PRIVILEGE",
                    "SE_BACKUP_PRIVILEGE",
                    "SE_RESTORE_PRIVILEGE",
                    "SE_SHUTDOWN_PRIVILEGE",
                    "SE_DEBUG_PRIVILEGE",
                    "SE_AUDIT_PRIVILEGE",
                    "SE_SYSTEM_ENVIRONMENT_PRIVILEGE",
                    "SE_REMOTE_SHUTDOWN_PRIVILEGE",
                    "SE_UNDOCK_PRIVILEGE",
                    "SE_SYNC_AGENT_PRIVILEGE",
                    "SE_ENABLE_DELEGATION_PRIVILEGE",
                    "SE_MANAGE_VOLUME_PRIVILEGE",
                    "SE_TRUSTED_CREDMAN_ACCESS_PRIVILEGE"
                ],
                "PrivilegesHigh": 15,
                "PrivilegesHighComputedBitMap": [
                    "SE_RELABEL_PRIVILEGE",
                    "SE_INC_WORKING_SET_PRIVILEGE",
                    "SE_TIME_ZONE_PRIVILEGE",
                    "SE_CREATE_SYMBOLIC_LINK_PRIVILEGE"
                ]
            },
            "DetailsType": 2,
            "DetailsTypeComputedMap": "Tokenmodificationoperation"
        }
    }
    ```



=== "test_type_51"


    ```json
	{
        "Version": 1,
        "Type": 51,
        "TypeComputedMap": "Keylogging",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 9,
        "AttributesComputedBitMap": [
            "Audit",
            "SelfProtection"
        ],
        "EventGuid": "{AD0C29F8-C747-413F-A084-A5A81196E65A}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T00:28:42.0857990+02:00",
        "TimestampRaw": 133311185220857990,
        "SpecificData": {
            "SourceProcess": {
                "PID": 12096,
                "ProcessGuid": "{45AD34C1-540C-4F7E-B226-B7387FF2AC0E}",
                "ProcessImageName": "C:\\Windows\\System32\\rundll32.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\windows\\system32\\rundll32.exe\"Shell32.dll,Control_RunDLL\"C:\\Windows\\System32\\ncpa.cpl\",",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 1,
                "HashMd5": "EF3179D498793BF4234F708D3BE28633",
                "HashSha1": "DD399AE46303343F9F0DA189AEE11C67BD868222",
                "HashSha256": "B53F3C0CD32D7F20849850768DA6431E5F876B7BFA61DB0AA0700B02873393FA",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2022-03-03T02:02:27.0570000+02:00",
                        "ValidityStart": "2021-09-02T20:23:41.0000000+02:00",
                        "ValidityEnd": "2022-09-01T20:23:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-13T10:28:41.5265454+02:00",
                "ProcessStartTimeRaw": 133311185215265454
            },
            "Action": {
                "PolicyGuid": "{9CFDF881-2372-4084-A5F6-37ECDF1EECC3}",
                "PolicyVersion": 7,
                "RuleGuid": "{C4526DEE-B715-455C-A4E6-DD189B13EE08}",
                "BaseRuleGuid": "{C4526DEE-B715-455C-A4E6-DD189B13EE07}",
                "IdentifierGuid": "{4E509127-2223-4B26-B4EF-076BBC9DCEAC}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "TargetProcess": {
                "PID": 8288,
                "ProcessGuid": "{7062B9CA-32EA-43C7-9346-F40ABBC63AA8}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Niveauobligatoiremoyen",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 1,
                "HashMd5": "81886624735B4F8F019E731A8A2E6E69",
                "HashSha1": "A30E4111E183514DEF89D2BC31071231DEABC4DF",
                "HashSha256": "385DBAD0269CAE83598D6706229324EB3CBDEF00E21A0682161477D762AAF2C1",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-04-15T11:56:31.9920000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-12T08:58:10.5382640+02:00",
                "ProcessStartTimeRaw": 133310266905382640
            },
            "KeyloggingMethod": 1,
            "KeyloggingMethodComputedMap": "GET_ASYNC_KEY_STATE"
        }
    }
    ```



=== "test_type_53"


    ```json
	{
        "Version": 1,
        "Type": 53,
        "TypeComputedMap": "HeapSpray",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0FDAFF-AA1C-4853-9BA1-DF4EE2A9E1CB}",
        "Timestamp": "2023-06-15T01:10:00.0000000+01:00",
        "TimestampRaw": 133232262000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "SourceProcess": {
                "PID": 10,
                "ProcessImageName": "C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "fc36ccb9-c9b6-495e-8ead-26e1536df4ad",
                "ProcessCommandLine": "\"C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF14D91238FAFB111",
                "HashSha1": "AC9F34399C7C5A6324EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7A23F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 7,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadContent"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_54"


    ```json
	{
        "Version": 1,
        "Type": 54,
        "TypeComputedMap": "LrpcAccess",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0929AA-A847-4C48-A82D-458FC89C8742}",
        "Timestamp": "2023-06-15T01:20:00.0000000+01:00",
        "TimestampRaw": 133232268000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "CallerModuleName": "MaliciousModule",
            "SourceProcess": {
                "PID": 2,
                "ProcessImageName": "C:\\Windows\\System32\\notepad.exe",
                "UserSID": null,
                "SessionID": 2,
                "ProcessGuid": "92c248f1-0acd-11ea-a38a-00155d099004",
                "ProcessCommandLine": "\"C:\\Windows\\system32\\NOTEPAD.EXE\" C:\\Users\\arkoon\\Desktop\\_test\\test.totot",
                "HashMd5": "F1139811BBF61362915958806AD30211",
                "HashSha1": "D487580502354C61808C7180D1A336BEB7AD4624",
                "HashSha256": "F1D62648EF915D85CB4FC140359E925395D315C70F3566B63BB3E21151CB2CE3",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SigningTime": "2019-11-07T04:32:51.5641056+01:00",
                        "ValidityEnd": "2020-05-02T22:24:36.0705280+01:00",
                        "ValidityStart": "2019-05-02T22:24:36.7807872+01:00",
                        "SubjectCN": "Microsoft Windows"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_55"


    ```json
	{
        "Version": 1,
        "Type": 55,
        "TypeComputedMap": "CreateRemoteThread",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0CF2B4-3CBE-48F3-BF02-9034793AF5CD}",
        "Timestamp": "2023-06-15T01:30:00.0000000+01:00",
        "TimestampRaw": 133232274000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "TargetProcess": {
                "PID": 3,
                "ProcessImageName": "C:\\Windows\\System32\\services.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e1d-0f85-11ea-a38e-806e6f6e6963",
                "ProcessCommandLine": "C:\\Windows\\system32\\services.exe",
                "HashMd5": "FAE441A6EC7FD8F55A404797A25C8910",
                "HashSha1": "141C964905C4CA2110AD8FBFC3D17C960A9B9A54",
                "HashSha256": "70D7571253E091F646F78A4DD078CE7FE8D796625BFA3C0A466DF03971175FB4",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 0,
                "Certificates": [],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": null,
                "IntegrityLevelNameLookup": null,
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateUnavailable"
            },
            "SourceProcess": {
                "PID": 9,
                "ProcessImageName": "C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "9d367a6c-04e4-491b-baa8-25b674db96d9",
                "ProcessCommandLine": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\Excel.EXE\"",
                "HashMd5": "0470A1A62B3FAA0AF14D9AFD8FAFB221",
                "HashSha1": "AC9F34399C7C5A9372EFE0FA16F33D12116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E13976136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_55_1"


    ```json
	{
        "Version": 1,
        "Type": 55,
        "TypeComputedMap": "CreateRemoteThread",
        "Severity": 1,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{3FC7A46F-A166-4316-B0B0-859DF8E93B98}",
        "GenerateIncident": true,
        "Timestamp": "2024-02-01T08:09:21.8983738-08:00",
        "TimestampRaw": 133512773618983738,
        "SpecificData": {
            "SourceProcess": {
                "PID": 4452,
                "ProcessGuid": "{18561EAB-115D-4B1E-ACF9-E185819BB548}",
                "ProcessImageName": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\system32\\wbem\\wmiprvse.exe -Embedding",
                "User": "S-1-5-18",
                "UserNameLookup": "SYSTEM",
                "UserDomainLookup": "NT AUTHORITY",
                "IntegrityLevel": "S-1-16-11111",
                "IntegrityLevelNameLookup": "System Mandatory Level",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "SessionID": 0,
                "HashMd5": "68B329DA9893E34099C7D8AD5CB9C940",
                "HashSha1": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
                "HashSha256": "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SubjectCN": "Microsoft Windows",
                        "SigningTime": "2016-12-10T03:42:04.9630000-08:00",
                        "ValidityStart": "2016-10-11T12:39:31.0000000-08:00",
                        "ValidityEnd": "2018-01-11T12:39:31.0000000-08:00"
                    }
                ],
                "ProcessStartTime": "2024-02-01T08:04:31.5500341-08:00",
                "ProcessStartTimeRaw": 133512770715500341
            },
            "Action": {
                "PolicyGuid": "{05AB2138-A3DD-46D5-926E-901041D49FD8}",
                "PolicyVersion": 14,
                "RuleGuid": "{6082AB41-5836-4BDD-B479-19DC0ABA4302}",
                "BaseRuleGuid": "{2F13CCB0-21D2-43B0-8D10-D241A6989FBD}",
                "IdentifierGuid": "{94699F8C-0E7A-490E-A3CA-1C851232B577}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "TargetProcess": {
                "PID": 608,
                "ProcessGuid": "{1876D654-057F-4B5D-9D1B-69BA1C74DA4B}",
                "ProcessImageName": "C:\\Windows\\System32\\lsass.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\system32\\lsass.exe",
                "User": "S-1-5-18",
                "UserNameLookup": "SYSTEM",
                "UserDomainLookup": "NT AUTHORITY",
                "IntegrityLevel": "S-1-16-16384",
                "IntegrityLevelNameLookup": "System Mandatory Level",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "SessionID": 0,
                "HashMd5": "68B329DA9893E34099C7D8AD5CB9C940",
                "HashSha1": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
                "HashSha256": "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SubjectCN": "Microsoft Windows Publisher",
                        "SigningTime": "2013-08-22T04:32:54.6290000-08:00",
                        "ValidityStart": "2013-03-13T13:34:10.0000000-08:00",
                        "ValidityEnd": "2014-06-13T13:34:10.0000000-08:00"
                    }
                ],
                "ProcessStartTime": "2024-02-01T08:03:34.5476641-08:00",
                "ProcessStartTimeRaw": 133512770145476641
            }
        },
        "AdditionalData": {
            "AgentAddresses": [
                "172.24.0.14"
            ],
            "AgentGroupGuid": "{00000000-0000-0000-0000-000000000000}",
            "AgentGroupName": "Default group",
            "AgentGuid": "{FD088C3A-30F3-4119-8FC0-7527538EF361}",
            "AgentName": "WINSERVER2012",
            "CategoryName": "Process",
            "IncidentGuid": "{49C0571C-0F35-46E6-A81C-35F8F011D8A5}",
            "Message": "The 'WmiPrvSE.exe' process injected code into the 'lsass.exe' process",
            "PolicyName": "Stormshield - Incredible policy (1)",
            "SeverityName": "Alert"
        }
    }
    ```



=== "test_type_56"


    ```json
	{
        "Version": 1,
        "Type": 56,
        "TypeComputedMap": "ProcessExit",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD0B184E-85BE-48A2-8B4F-C31D5EA86974}",
        "Timestamp": "2023-06-15T01:40:00.0000000+01:00",
        "TimestampRaw": 133232280000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "ExitStatusCode": 5,
            "SourceProcess": {
                "PID": 6,
                "ProcessImageName": "C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "bed63e83-0f85-11ea-a38e-00155d099004",
                "ProcessCommandLine": "\"C:\\Program Files\\Stormshield\\SES Evolution\\Agent\\Bin\\EsScript.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF44D9AFD9FAFB111",
                "HashSha1": "0C9F34399C7C5A9372EFE0F6E6F33DA4116016C6",
                "HashSha256": "2347766F6B5AD11E5C97167B5A452374EFF876136FC7B44F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 8,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Stormshield",
                        "SigningTime": "2019-11-25T14:15:45.4765488+01:00",
                        "ValidityEnd": "2040-01-01T00:59:59.1248256+01:00",
                        "ValidityStart": "2017-04-25T15:21:15.7216000+01:00",
                        "SubjectCN": "Stormshield"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadSignature"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            }
        }
    }
    ```



=== "test_type_57"


    ```json
	{
        "Version": 1,
        "Type": 57,
        "TypeComputedMap": "SetWindowsHookExAll",
        "Severity": 3,
        "ServerReserved": 0,
        "Attributes": 8,
        "AttributesComputedBitMap": [
            "Audit"
        ],
        "EventGuid": "{AD0A8453-EC3D-4CE6-B337-FD3F3BC40310}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T03:52:19.0004158+02:00",
        "TimestampRaw": 133312171390004158,
        "SpecificData": {
            "SourceProcess": {
                "PID": 2948,
                "ProcessGuid": "{6F14D6D8-D8FF-4BEC-BA64-059BBF184A5B}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "81886624735B4F8F019E731A8A2E6E69",
                "HashSha1": "A30E4111E183514DEF89D2BC31071231DEABC4DF",
                "HashSha256": "385DBAD0269CAE83598D6706229324EB3CBDEF00E21A0682161477D762AAF2C1",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-04-15T11:56:31.9920000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T11:25:25.3085133+02:00",
                "ProcessStartTimeRaw": 133312083253085133
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 9,
                "RuleGuid": "{8D2EF1D8-670B-4AE4-ABDC-9316DAD15AAF}",
                "BaseRuleGuid": "{8D2EF1D8-670B-4AE4-ABDC-9316DAD15AAE}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "HookId": 13,
            "HookIdComputedMap": "WH_KEYBOARD_LL",
            "ModuleName": "C:\\Windows\\Explorer.EXE"
        }
    }
    ```



=== "test_type_58"


    ```json
	{
        "Version": 1,
        "Type": 58,
        "TypeComputedMap": "SetWindowsHookEx",
        "Severity": 3,
        "ServerReserved": 0,
        "Attributes": 8,
        "AttributesComputedBitMap": [
            "Audit"
        ],
        "EventGuid": "{AD08E493-2A70-4D6D-AFB5-80240A5E780A}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T01:25:28.8124881+02:00",
        "TimestampRaw": 133312083288124881,
        "SpecificData": {
            "SourceProcess": {
                "PID": 7512,
                "ProcessGuid": "{E321E2D1-260B-4CDE-A41E-0D32BF0DDF58}",
                "ProcessImageName": "C:\\ProgramFiles\\Apoint2K\\Apoint.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\ProgramFiles\\Apoint2K\\Apoint.exe\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "1C51D884DEFB0E948FBA909D730E3D59",
                "HashSha1": "F55CD206D052A2683BAC53F3A3662292B23FE123",
                "HashSha256": "1991F6D0AED0CB298017C2CA7C12DF6C473027FBDB6F9F334C4BDA0E1718AD00",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA1",
                        "IssuerCN": "DigiCertEVCodeSigningCA",
                        "SubjectCN": "ALPSELECTRICCO.,LTD.",
                        "SigningTime": "2019-02-19T11:00:30.0000000+02:00",
                        "ValidityStart": "2018-01-30T02:00:00.0000000+02:00",
                        "ValidityEnd": "2019-03-29T14:00:00.0000000+02:00"
                    },
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsThirdPartyComponentCA2012",
                        "SubjectCN": "MicrosoftWindowsHardwareCompatibilityPublisher",
                        "SigningTime": "2020-03-30T03:34:44.8600000+02:00",
                        "ValidityStart": "2019-06-05T20:06:32.0000000+02:00",
                        "ValidityEnd": "2020-06-03T20:06:32.0000000+02:00"
                    },
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "DigiCertEVCodeSigningCA(SHA2)",
                        "SubjectCN": "ALPSELECTRICCO.,LTD.",
                        "SigningTime": "2019-02-19T11:00:33.0000000+02:00",
                        "ValidityStart": "2018-01-30T02:00:00.0000000+02:00",
                        "ValidityEnd": "2019-03-29T14:00:00.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T11:25:24.4278630+02:00",
                "ProcessStartTimeRaw": 133312083244278630
            },
            "Action": {
                "PolicyGuid": "{0A8FF960-1689-41CF-9D87-A2796B1DE5BF}",
                "PolicyVersion": 8,
                "RuleGuid": "{8D2EF1D8-670B-4AE4-ABDC-9316DAD15AAF}",
                "BaseRuleGuid": "{8D2EF1D8-670B-4AE4-ABDC-9316DAD15AAE}",
                "IdentifierGuid": "{5C079068-7641-4C9A-8600-BBDC93FBBCDD}",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "TargetProcess": {
                "PID": 2948,
                "ProcessGuid": "{6F14D6D8-D8FF-4BEC-BA64-059BBF184A5B}",
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "MediumMandatoryLevel",
                "IntegrityLevelDomainLookup": "MandatoryLabel",
                "SessionID": 1,
                "HashMd5": "81886624735B4F8F019E731A8A2E6E69",
                "HashSha1": "A30E4111E183514DEF89D2BC31071231DEABC4DF",
                "HashSha256": "385DBAD0269CAE83598D6706229324EB3CBDEF00E21A0682161477D762AAF2C1",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2023-04-15T11:56:31.9920000+02:00",
                        "ValidityStart": "2023-02-03T02:05:41.0000000+02:00",
                        "ValidityEnd": "2024-02-01T02:05:41.0000000+02:00"
                    }
                ],
                "ProcessStartTime": "2023-06-14T11:25:25.3085133+02:00",
                "ProcessStartTimeRaw": 133312083253085133
            },
            "HookId": 3,
            "HookIdComputedMap": "WH_GETMESSAGE",
            "ModuleName": "C:\\ProgramFiles\\Apoint2K\\Apoint.DLL"
        }
    }
    ```



=== "test_type_59"


    ```json
	{
        "Version": 1,
        "Type": 59,
        "TypeComputedMap": "ProcessAccessWithPrivilegeEscalation",
        "Severity": 0,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD078DA9-0D79-4995-BD8B-5BA2605C48D1}",
        "Timestamp": "2023-06-15T02:10:00.0000000+01:00",
        "TimestampRaw": 133232298000000000,
        "GenerateIncident": false,
        "SpecificData": {
            "Details": null,
            "ObjectType": 0,
            "TargetProcess": {
                "PID": 1,
                "ProcessImageName": "C:\\Windows\\explorer.exe",
                "UserSID": null,
                "SessionID": 2,
                "ProcessGuid": "92c246ec-0acd-11ea-a38a-00155d099004",
                "ProcessCommandLine": "C:\\Windows\\Explorer.EXE",
                "HashMd5": "4E196CEA0C9C46A7D656C67E52E8C7C7",
                "HashSha1": "726C9D759C5F02080FA003B50466A3BE0C959865",
                "HashSha256": "ED5F36137D09E1CFC0CCF2675FB5D460E7EED135BA36D3259D2C510592047F28",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 1,
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "Microsoft Windows Production PCA 2011",
                        "SigningTime": "2019-10-20T14:09:02.8886192+01:00",
                        "ValidityEnd": "2020-05-02T22:24:36.0705280+01:00",
                        "ValidityStart": "2019-05-02T22:24:36.7807872+01:00",
                        "SubjectCN": "Microsoft Windows"
                    }
                ],
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted"
            },
            "SourceProcess": {
                "PID": 10,
                "ProcessImageName": "C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe",
                "UserSID": null,
                "SessionID": 0,
                "ProcessGuid": "fc36ccb9-c9b6-495e-8ead-26e1536df4ad",
                "ProcessCommandLine": "\"C:\\Program Files (x86)\\Balsamiq Mockups 3\\Balsamiq Mockups 3.exe\"",
                "HashMd5": "0470A1A62B3FAA0AF14D91238FAFB111",
                "HashSha1": "AC9F34399C7C5A6324EFE0FA16F33DA4116016C6",
                "HashSha256": "1247766F6B5AD11E5C97167B5A452374E22876136FC7A23F79BE14AD9A7FA3E7",
                "UserNameLookup": "JOHNDOE",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserDomainLookup": "TEST",
                "CertificateSignatureState": 7,
                "Certificates": null,
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "IntegrityLevel": "S-1-16-8192",
                "IntegrityLevelNameLookup": "Medium",
                "IntegrityLevelDomainLookup": "Mandatory Label",
                "IsProtectedOrCritical": false,
                "ProcessStartTimeRaw": 133204190354018719,
                "ProcessStartTime": "2023-02-09T13:23:55.4018719+01:00",
                "CertificateSignatureStateComputedMap": "SignatureStateBadContent"
            },
            "Action": {
                "PolicyGuid": "00000000-0000-0000-0000-000000000000",
                "PolicyVersion": 0,
                "RuleGuid": "00000000-0000-0000-0000-000000000000",
                "BaseRuleGuid": "00000000-0000-0000-0000-000000000000",
                "IdentifierGuid": "00000000-0000-0000-0000-000000000000",
                "Blocked": false,
                "UserDecision": false,
                "SourceProcessKilled": true
            }
        }
    }
    ```



=== "test_type_7"


    ```json
	{
        "Version": 1,
        "Type": 7,
        "TypeComputedMap": "ProcessAccess",
        "Category": 0,
        "CategoryComputedMap": "ProcessAccess",
        "Severity": 4,
        "ServerReserved": 0,
        "Attributes": 2,
        "AttributesComputedBitMap": [
            "Protection"
        ],
        "EventGuid": "{AD081172-EC3A-4C44-B5BF-81D61A2C8A7F}",
        "GenerateIncident": false,
        "Timestamp": "2023-06-15T07:24:56.3526431+01:00",
        "TimestampRaw": 133209518963526431,
        "SpecificData": {
            "SourceProcess": {
                "PID": 464,
                "ProcessGuid": "{A8E8DCB5-B340-4417-89A6-893B299DD5F1}",
                "ProcessImageName": "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\2\\ps_ReadOnly.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\2\\ps_ReadOnly.exe\"-ExecutionPolicyUnrestricted-File\"C:\\tmp\\ProcessAccess\\Duplicate\\Attacker.ps1\"-OutputFileLog\"c:\\tmp\\a.jsonAttackerReadOnly\"-OutputExr\"c:\\tmp\\a.txtReadOnly\"-TargetProcessHandleValue2388-TargetThreadHandleValue2540-TargetProcessHandle3980-SASAT\"c:\\tmp\\ProcessAccess\\WSASA\\NtObjectManager\\NtObjectManager.psd1\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "7353F60B1739074EB17C5F4DDDEFE239",
                "HashSha1": "6CBCE4A295C163791B60FC23D285E6D84F28EE4C",
                "HashSha256": "DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2018-09-15T08:03:08.1030000+01:00",
                        "ValidityStart": "2018-07-03T21:45:50.0000000+01:00",
                        "ValidityEnd": "2019-07-26T21:45:50.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T17:24:55.4703759+01:00",
                "ProcessStartTimeRaw": 133209518954703759
            },
            "Action": {
                "PolicyGuid": "{DECD92C6-A814-4DD5-8BF1-32022D5EBE58}",
                "PolicyVersion": 3,
                "RuleGuid": "{0BDCB8A4-532E-446A-BD5B-5E163539A529}",
                "BaseRuleGuid": "{0BDCB8A4-532E-446A-BD5B-5E163539A528}",
                "IdentifierGuid": "{E2AA0DB7-90A0-4913-AA1A-F89225A3B197}",
                "Blocked": true,
                "UserDecision": false,
                "SourceProcessKilled": false
            },
            "TargetProcess": {
                "PID": 6032,
                "ProcessGuid": "{45B56BF8-4E3A-41B6-995D-FA6D3480D6A8}",
                "ProcessImageName": "C:\\Windows\\Temp\\ps_Target.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\Windows\\TEMP\\ps_Target.exe\"-ExecutionPolicyUnrestricted-File\"C:\\tmp\\ProcessAccess\\Duplicate\\Target.ps1\"-OutputFileLog\"c:\\tmp\\a.jsonTarget\"-SASAT\"c:\\tmp\\ProcessAccess\\WSASA\\NtObjectManager\\NtObjectManager.psd1\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "7353F60B1739074EB17C5F4DDDEFE239",
                "HashSha1": "6CBCE4A295C163791B60FC23D285E6D84F28EE4C",
                "HashSha256": "DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2018-09-15T08:03:08.1030000+01:00",
                        "ValidityStart": "2018-07-03T21:45:50.0000000+01:00",
                        "ValidityEnd": "2019-07-26T21:45:50.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T17:24:53.2107914+01:00",
                "ProcessStartTimeRaw": 133209518932107914
            },
            "Details": {
                "DesiredAccess": 2097151,
                "DesiredAccessComputedBitMap": [
                    "THREAD_TERMINATE",
                    "THREAD_SUSPEND_RESUME",
                    "THREAD_ALERT",
                    "THREAD_GET_CONTEXT",
                    "THREAD_SET_CONTEXT",
                    "THREAD_SET_INFORMATION",
                    "THREAD_QUERY_INFORMATION",
                    "THREAD_SET_THREAD_TOKEN",
                    "THREAD_IMPERSONATE",
                    "THREAD_DIRECT_IMPERSONATION",
                    "THREAD_SET_LIMITED_INFORMATION",
                    "THREAD_QUERY_LIMITED_INFORMATION",
                    "THREAD_RESUME",
                    "DELETE",
                    "READ_CONTROL",
                    "WRITE_DAC",
                    "WRITE_OWNER",
                    "SYNCHRONIZE"
                ],
                "MatchingAccess": 852915,
                "MatchingAccessComputedBitMap": [
                    "THREAD_TERMINATE",
                    "THREAD_SUSPEND_RESUME",
                    "THREAD_SET_CONTEXT",
                    "THREAD_SET_INFORMATION",
                    "THREAD_SET_THREAD_TOKEN",
                    "THREAD_IMPERSONATE",
                    "THREAD_DIRECT_IMPERSONATION",
                    "DELETE",
                    "WRITE_DAC",
                    "WRITE_OWNER"
                ]
            },
            "ObjectType": 2,
            "ObjectTypeComputedMap": "Thread",
            "Operation": 2,
            "OperationComputedMap": "Duplicate",
            "DuplicatingProcess": {
                "PID": 464,
                "ProcessGuid": "{A8E8DCB5-B340-4417-89A6-893B299DD5F1}",
                "ProcessImageName": "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\2\\ps_ReadOnly.exe",
                "VolumeZone": 1,
                "VolumeZoneComputedBitMap": [
                    "Operating system"
                ],
                "ProcessCommandLine": "\"C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\2\\ps_ReadOnly.exe\"-ExecutionPolicyUnrestricted-File\"C:\\tmp\\ProcessAccess\\Duplicate\\Attacker.ps1\"-OutputFileLog\"c:\\tmp\\a.jsonAttackerReadOnly\"-OutputExr\"c:\\tmp\\a.txtReadOnly\"-TargetProcessHandleValue2388-TargetThreadHandleValue2540-TargetProcessHandle3980-SASAT\"c:\\tmp\\ProcessAccess\\WSASA\\NtObjectManager\\NtObjectManager.psd1\"",
                "User": "S-1-5-21-2222222-33333333-44444444-555",
                "UserNameLookup": "JOHNDOE",
                "UserDomainLookup": "TEST",
                "IntegrityLevel": "S-1-16-12288",
                "IntegrityLevelNameLookup": "Niveauobligatoire\u00e9lev\u00e9",
                "IntegrityLevelDomainLookup": "\u00c9tiquetteobligatoire",
                "SessionID": 2,
                "HashMd5": "7353F60B1739074EB17C5F4DDDEFE239",
                "HashSha1": "6CBCE4A295C163791B60FC23D285E6D84F28EE4C",
                "HashSha256": "DE96A6E69944335375DC1AC238336066889D9FFC7D73628EF4FE1B1B160AB32C",
                "IsProtectedOrCritical": false,
                "CertificateSignatureState": 1,
                "CertificateSignatureStateComputedMap": "SignatureStateTrusted",
                "Certificates": [
                    {
                        "Algorithm": "SHA256",
                        "IssuerCN": "MicrosoftWindowsProductionPCA2011",
                        "SubjectCN": "MicrosoftWindows",
                        "SigningTime": "2018-09-15T08:03:08.1030000+01:00",
                        "ValidityStart": "2018-07-03T21:45:50.0000000+01:00",
                        "ValidityEnd": "2019-07-26T21:45:50.0000000+01:00"
                    }
                ],
                "ProcessStartTime": "2023-02-15T17:24:55.4703759+01:00",
                "ProcessStartTimeRaw": 133209518954703759
            }
        }
    }
    ```



