---
title: Restart the endpoint agent
---

Use the following command for your operating system.

{% tabs %}
{% tab title="Windows" %}
```powershell
Restart-Service SEKOIAEndpointAgent
```
{% endtab %}

{% tab title="Linux" %}
```shell
sudo systemctl restart SEKOIAEndpointAgent.service
```
{% endtab %}

{% tab title="MacOS" %}
```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent service restart
```
{% endtab %}
{% endtabs %}
