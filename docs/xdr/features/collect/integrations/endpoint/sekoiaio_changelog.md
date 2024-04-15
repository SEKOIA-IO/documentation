## Sekoia.io Endpoint Agent Changelog

This is the changelog for the Sekoia.io Endpoint Agent.

## [1.5.1] - 2024-02-19 (linux only)

### Fixed

- Fixes agent crashing for linux distributions without libpcap.so.0.8 installed

## [1.5.0] - 2024-02-16

### Added

- Add user information for process creation and end (windows)
- Allow to ignore paths when computing hashes
  - Paths specified under the attribute `HashesExcludedPaths` in the config file will be ignored
- DNS resolutions for linux
- Allow to watch files based on patterns instead of only the direct file path

### Changed

- Improve logs consumptions in multicast mode (linux)

### Fixed

- Fix OS info in stats events
- Set timestamp to last aggregated event
- Fixes URLs for newest regions

## [1.4.0] - 2023-12-06

### Added

- Add aggregation capabilities for some specific events
- Add support for regions
- Add support for custom CA certs for HTTP requests

### Fixed

- On linux agent resolve full path for files when possible

## [1.3.0] - 2023-10-16

### Added

- Provide host IPs in events
- Display nice error when agent is started without being installed
- Clean the downloaded binaries on startup

### Changed

- Update linux audit rules
- Retry sending playbook runners results on server error

### Fixed 

- Minor fixes on event files handling
- Fixes the way the user and the effective user are set on privilege changes
- Fix parent process on `process-ended` events

## [1.2.1] - 2023-09-18

### Fixed 

- Fixes agent not having any roles

## [1.2.0] - 2023-09-18

### Added

- Playbook runner capabilties (beta)
- Watch for additional log files (beta)

### Fixed

- Make agent exit quickly on shutdown
- Windows: Provide full path to cmd.exe when restarting the service
- Windows: Fixes wrong executable name on some process-creation/process-end events

## [1.1.0] - 2023-04-21 

### Added

- Add help context for command lines

### Changed

- Agent update: Increase timeout when downloading new binary
- Reduce overall memory usage of the agent
- Change the command line arguments of the binary

### Fixed

- Windows error on network connection events having port set but with nil value
- Linux: Event watcher always triggering the "no events" alert
- Windows: Fixes memory leak

## [1.0.0] - 2023-03-13

## [0.6.2] - 2023-03-02

### Added

- In stats events:
  - Add more information about the host
  - Add information about the heap and stack size 

### Changed

- Reduced level of some logs
- Small performance improvements


## [0.6.1] - 2023-02-15

### Added

- Better handling of panic errors

### Fixed

- Rely on proxy if set to download new versions of the agent
- Windows service restart on failure

## [0.6.0] - 2023-02-09

### Added

- Send Agent logs to  Sekoia.io

### Changed

- Improve RAM usage
- On Windows file creation events now include the user id
- In agent usage statistics RAM is now sent in bytes instead of percents

### Fixed

- Fixes wrong process name for powershell events

## [0.5.1] - 2023-01-19

### Fixed

- Fixes special characters handling in Windows events
- Fixes lost events log in linux agent
- Fixes Wrong process for a specific Windows event

## [0.5.0] - 2022-11-28

### Added

- Agent auto update mechanism
- Add support for multiple new Windows events
- Binary signing for Windows
- Memory improvements
- CPU improvements


## [0.2.0] - 2022-07-25

### Added

- Add supports for linux systems
- On Windows Relies on ETW providers instead of Sysmon when possible

## [0.1.0] - 2022-05-24

### Added

- Collect Windows event logs from ETW (Event Tracing for Windows)
- Normalize the events to the ECS (Elastic Common Schema) format
- Send the ECS events to  Sekoia.io
- Persists events on disk when no network connection is available
- Agent is installed and runs as a Windows service
- Collect metrics about the agent and the host
