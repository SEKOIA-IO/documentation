# Roy AI assistant

Roy is Sekoia's built-in AI assistant. It is available across the platform and responds to natural language queries to help analysts work faster without switching context.

Roy can:

- Write and refine Sigma detection rules from a plain-language description
- Explain complex event attribute fields directly in the Events page
- Build Query Builder queries from natural language
- Answer questions about platform features using the live documentation
- Provide context on current threats using the Intelligence database

Roy responds in English, French, and Polish.

!!! note "Availability"
    Roy must be enabled for your community before the **Ask Roy** button appears in the navigation menu. Contact your workspace administrator if Roy is not visible.

!!! warning "Verify critical information"
    Roy's responses are AI-generated. Always verify outputs before acting on them in a production environment, particularly for detection rules and queries.

## Access Roy

Click the **Ask Roy** button in the left-hand navigation menu to open the chat panel. The panel is accessible from any page in the platform.

From the panel, you can type a question or select one of the suggested prompts to get started. Use the thumbs up and down icons to rate Roy's responses; this feedback is used to improve future answers.

## Roy can assist with writing Sigma rules

Need help writing a Sigma rule? Roy can assist you by helping to construct the Sigma pattern of the rule. Simply ask Roy for guidance, and you can receive examples or templates to get started.

For instance, you can request:

- _"Help me create a Sigma rule to detect failed login attempts."_
- _"Can you provide a Sigma pattern for identifying suspicious file modifications?"_

To get Roy's help in the Rules Catalog, follow these steps: 

1. Click on `Add new rule`
2. In the section “Specify your detection patterns”, click on the tab `Sigma`
3. Click on the button icon next to `Pattern` 
4. Explicitly state the Sigma rule you want to create (or what you need to detect) 
5. Click on `Generate` and Roy will generate a pattern for you 

## Roy can explain Event attributes

In the context of Events and logs, Roy can assist you with the explanation of some complex event attributes.

Here is the list of event attributes fields where you can find a “Get help with Roy” button: 

- `url.domain`
- `process.command_line`
- `process.executable`
- `process.parent.command_line`
- `process.parent.executable`
- `sekoiaio.source_process.command_line`
- `sekoiaio.source_process.executable`
- `user_agent.original`
- `auditd.data.syscall`
- `action.properties.syscall`
- `file.path`

To access this button, open the Events page, click on an event to extend the section, and look for the attributes cited above. 

## Roy can help with building queries

The **Query Builder** is a powerful tool integrated into the Sekoia platform that allows users to create structured database queries. Roy Assistant is equipped to help you easily build complex queries and save you from the blank paper frustration. 

By simply asking Roy in natural language, you can request assistance in formulating specific queries tailored to your needs. Whether you need to filter logs, aggregate data, or analyze user behavior, Roy can provide you with the necessary structure and syntax to achieve your objectives.

Some examples of queries could be: 

- _"Can you help me create a query to find all login attempts from a specific IP address over the last week?"_
- _"I need a query that shows all failed login attempts along with the user accounts involved."_
- _"Please generate a query to identify any unusual spikes in network traffic during the last 30 days."_
  
## Roy is continuously updated with the latest documentation

Roy Assistant has an in-depth understanding of the Sekoia platform, which makes it an invaluable resource for users navigating its features. Whenever you encounter uncertainty about how to use a specific feature or need assistance with a particular page, you can turn to Roy for guidance as it is connected to the Product documentation and can provide you with helpful information without the need to change context. 

## Roy is aware of the latest threats

Roy Assistant is continuously updated with the latest threat intelligence coming from the Intelligence database. This allows analysts to inquire about emerging threats, vulnerabilities, and attack vectors relevant to their environment. By providing timely and contextual information on current threats, Roy empowers SOC teams to stay proactive in their defense strategies and respond effectively to potential security incidents.

# The security of your information is our priority

Roy Assistant is designed with user privacy and data security as top priorities. It does not memorize queries or retain any information provided by users. This ensures that **your interactions remain confidential.**

When using the chat feature, messages are sent to Sekoia servers for processing. However, **Roy does not have access to your personal data**; instead, it orchestrates the web interface to assist you.

For use cases that require data processing, such as AI Cases or explaining event attributes, Roy uses models hosted on Sekoia's secure servers.
