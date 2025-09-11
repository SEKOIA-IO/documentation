# Graph Explorations

Graph explorations enable analysts to interactively build comprehensive threat intelligence visualizations by selecting objects and relationships from the Sekoia Intelligence knowledge base, creating shareable intelligence products that support strategic threat analysis and reporting initiatives.

**Understanding Graph Investigation Types**

Sekoia's graphical investigation capabilities serve distinct analytical purposes, each optimized for specific intelligence workflows:

- **Explore**: Graph exploration involves discovering and mapping cyber threat intelligence (CTI) by navigating through interconnected threat data. Analysts can initiate explorations from individual intelligence objects or comprehensive threat reports, providing flexible entry points for threat research. These exploration sessions are temporary by default, allowing for experimental analysis and hypothesis testing. However, valuable insights and threat connections can be preserved by saving explorations, enabling knowledge sharing with team members and facilitating continued analysis across multiple sessions.

- **Investigate**: Graph investigations focus on understanding specific security alerts or cases through event-driven analysis. These investigations automatically construct threat visualizations based on security events within alerts or cases, extracting and correlating relevant threat indicators. As new events are incorporated into alerts or cases, the associated graphs dynamically update to reflect emerging threat patterns and expanded attack context.


## Starting Graph Explorations
### From Intelligence Objects

Initiate a graph exploration from any object within the Sekoia app by clicking the New Graph Exploration button located in the top-right corner of an object page. This approach enables focused analysis beginning with a specific threat actor, malware family, attack technique, or other intelligence entity.

### From Threat Reports

Launch explorations directly from existing threat report graphs, leveraging pre-established threat relationships and contexts as starting points for deeper investigative work or customized intelligence products.

## Building Comprehensive Threat Maps

### Adding Relationships

Clicking on any object within the graph reveals related intelligence in the side panel, providing immediate access to contextual threat information. Navigate to the `Relationships` tab to view comprehensive relationship mappings with other intelligence objects. Add any relationship to your exploration by clicking the `Add relationship to graph` button that appears when hovering over relationship entries, enabling systematic expansion of your threat landscape understanding.

### Removing Graph Elements

Maintain graph clarity and focus by removing unnecessary elements:

- **Relationships**: Remove relationship connections directly from the relationship list using the hover button interface
- **Objects**: Delete individual threat objects by clicking the red trash icon adjacent to their names
- **Automatic Cleanup**: Removing objects automatically eliminates associated relationships, maintaining graph integrity

### Advanced Layer Management

**Understanding Layers in CTI Context**

Layers provide sophisticated organizational capabilities for complex threat intelligence explorations. Each layer represents a logical grouping within your analysis that can be independently controlled, enabling analysts to construct multi-dimensional threat narratives while maintaining analytical focus.

#### Default Layer Operations

Every graph exploration automatically establishes a default layer upon initial creation. This foundational layer:

- Captures initial exploration elements and starting intelligence objects
- Maintains exploration continuity across analytical sessions
- Serves as the primary workspace for ongoing threat research

#### Active Layer Control

The layer management interface, positioned in the top-left corner adjacent to the main analysis panel, provides:

- **Layer Panel Access**: Comprehensive layer management controls and visibility options
- **Active Layer Display**: Clear indication of the currently selected layer where new intelligence additions are placed
- **Dynamic Layer Switching**: Seamless transitions between different analytical perspectives and threat domains

### Saving Graph Explorations

Preserve valuable threat intelligence work by clicking the `Save` button in the toolbar inside an Object page. 

When in other contexts (Graph explorations page), changes are saved automatically. 

New explorations require naming for organizational purposes, while updates to existing explorations are saved directly. 

### Graphical Investigations Applications for CTI 

Access your community's complete library of saved threat intelligence explorations through the `Graph Explorations` menu item. This centralized repository enables:

- **Knowledge Sharing**: Team access to collective threat intelligence research and analysis
- **Analytical Continuity**: Resumption of complex investigations across multiple sessions
- **Intelligence Production**: Foundation material for threat reports, briefings, and strategic assessments
- **Collaborative Research**: Shared starting points for team-based threat hunting and attribution analysis

These enhanced capabilities transform graph explorations from simple visualization tools into comprehensive threat intelligence platforms that support sophisticated analytical workflows, collaborative research initiatives, and professional intelligence reporting requirements.

### Why Use Layers in Your Graphs 

Optimize threat intelligence explorations through strategic layer organization:

- **Object-Based Segregation: Create distinct layers for different threat intelligence categories**:

    **Threat Actors**: Separate layers for different APT groups, cybercriminal organizations, or nation-state entities

    **Malware Families**: Organize layers by specific malware types, variants, or campaign-specific tools

    **Attack Techniques**: Group layers by MITRE ATT&CK techniques, tactics, or specific methodologies

    **Infrastructure**: Separate layers for command-and-control infrastructure, delivery mechanisms, or hosting providers

- **Report-Driven Organization: Structure layers based on intelligence reporting requirements**:

    **Campaign Analysis**: Create individual layers for different attack campaigns or operation phases when analyzing comprehensive threat reports

    **Attribution Analysis**: Separate layers for different attribution hypotheses or evidence categories

    **Timeline Analysis**: Organize layers chronologically to understand threat evolution and campaign development

    **Geographic Analysis**: Structure layers by target regions, threat origins, or operational territories


