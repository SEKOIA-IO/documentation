# Intelligence Center External Integrations: Cortex Analyzer

SEKOIA is also providing a [Cortex analyzer](https://github.com/TheHive-Project/Cortex-Analyzers/tree/master/analyzers/SEKOIAIntelligenceCenter) to enrich data in [TheHive](https://thehive-project.org/) ecosystem.

To setup the analyzer please [follow this guide](https://github.com/TheHive-Project/CortexDocs/blob/master/analyzer_requirements.md).

In a nutshell:

- Get the SEKOIA.IO API Key
- Install the Analyzer refering to this section of the [TheHive](https://github.com/TheHive-Project/CortexDocs/blob/master/installation/install-guide.md#installation) documentation
- Connect into Cortex with `orgadmin` role
- Select your organization on the top right corner
![!Cortex Organisation Page](/assets/intelligence_center/organization.png){: style="width: 100%; max-width: 100%"}
- Move to `Analyser Config` and search `sekoia`
![!Cortex Analyser Config Page](/assets/intelligence_center/analyzer_config.png){: style="width: 100%; max-width: 100%"}
- Select `SEKOIAIntelligenceCenter`
- Provide simple configurations
![!Cortex Analyser Config API Page](/assets/intelligence_center/sekoia_api.png){: style="width: 100%; max-width: 100%"}
- Enable the Analyzer you would like to use, by clicking on the right side
![!Cortex Analyser Enable Page](/assets/intelligence_center/analyzer_activation.png){: style="width: 100%; max-width: 100%"}
- If wanted, tailor made your Analyzer with additional details
![!Cortex Analyser Enable Context Page](/assets/intelligence_center/enable_context.png){: style="width: 100%; max-width: 100%"}
