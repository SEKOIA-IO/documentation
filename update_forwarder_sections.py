from pathlib import Path
import re

files = [
    "docs/integration/categories/network/bind.md",
    "docs/integration/categories/network_security/fortiproxy.md",
    "docs/integration/categories/network_security/akamai_guardicore_onprem.md",
    "docs/integration/categories/endpoint/trellix_atd.md",
    "docs/integration/categories/network_security/gatewatcher_aioniq.md",
    "docs/integration/categories/network/cisco_nx_os.md",
    "docs/integration/categories/network/infoblox_ddi.md",
    "docs/integration/categories/network_security/olfeo_secure_web_gateway.md",
    "docs/integration/categories/network/citrix_netscaler_adc.md",
    "docs/integration/categories/applicative/apache.md",
    "docs/integration/categories/network/nginx.md",
    "docs/integration/categories/endpoint/symantec_epp.md",
    "docs/integration/categories/network_security/gatewatcher_aioniq_ecs.md",
    "docs/integration/categories/endpoint/auditbeat_linux.md",
    "docs/integration/categories/network_security/cisco_wsa.md",
]

replacement = """#### Configure a forwarder

Use the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) to collect syslog events from multiple sources and forward them to their corresponding Sekoia intakes. The forwarder maps each listening port to an intake key, so each source normally requires a dedicated port.

!!! warning "Use the supported forwarder"

    The Sekoia.io Forwarder is the officially supported method for collecting syslog events with Sekoia. Other syslog services are documented for reference purposes and are not officially supported.
"""

section_pattern = re.compile(
    r"^#### Configure a forwarder\n.*?(?=^#{2,3} |\Z)",
    re.MULTILINE | re.DOTALL,
)

for filename in files:
    path = Path(filename)

    if not path.exists():
        print(f"[MISSING] {filename}")
        continue

    content = path.read_text(encoding="utf-8")

    if not section_pattern.search(content):
        print(f"[NOT FOUND] {filename}")
        continue

    updated, count = section_pattern.subn(replacement, content, count=1)

    if count == 1:
        path.write_text(updated, encoding="utf-8")
        print(f"[UPDATED] {filename}")