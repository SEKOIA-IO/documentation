# How to forward logs to Sekoia.io using HTTPS

## Overview

To push your events to Sekoia.io, you can use the HTTPS procotol. It's the simpler way to send us your logs, especially for non-syslog system.

Before processing, you have to:

- Connect to [Sekoia.io SOC Platform with a Defend Plan](https://app.sekoia.io/intakes)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

To forward events using HTTPS to Sekoia.io, you have to send a `POST` request to `https://intake.sekoia.io` and to supply your intake key as header. Many formats are available, check the [Formatting options page](./format.md) to have more details

You can choose many option to forward logs:

- Manually, either by utilizing the documented endpoints or through the use of custom scripts.
- Many technologies support forwarding logs directly from your equipment through HTTPS. Be sure to respect the Sekoia collection endpoint expected format (e.g., using the intake key as a header).
- Utilize a [Third-party technology](third_part.md) responsible for collecting data from your equipment and forwarding events to Sekoia.io.

