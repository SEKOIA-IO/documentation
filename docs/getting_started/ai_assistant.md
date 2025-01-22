# What is Roy?

Roy Assistant is an **AI-powered companion** designed specifically for the Sekoia platform users. It leverages advanced natural language processing to provide a conversational experience that accelerates workflows and enhances decision-making in security operations. 

With Roy, analysts can quickly access threat intelligence, documentation, and platform data to deepen their investigations, troubleshoot issues, and uncover operational insights.

This revolutionary tool transforms the way analysts interact with security data. Whether you're seeking to explain event fields, obtain a summary of an alert, or dive deeper into specific incidents, Roy simplifies these processes by **reducing the time and effort required**. 

One of the standout features of Roy is its ability to understand and respond in multiple languages, including English, French, and even Polish. This multilingual support empowers analysts to interact with Roy in their native language, making it easier to convey complex security concepts and queries.

Whether you need to analyze alerts, gather contextual information, or create Sigma rules, Roy Assistant is here to help. 

# Where to find Roy?

## Chat with Roy from the Menu

Once ROY is available in your community, you’ll notice a vibrant purple-pink button labeled `Ask Roy` appearing in the menu. This button allows you to access Roy from any page, making its assistance just a click away.

From this panel, you can engage in direct conversations with Roy on a wide range of topics that interest you. Whether you need insights on security alerts, explanations of event fields, or assistance with building complex queries, Roy is equipped to provide the information you need.

To help you get started, the product includes a variety of examples showcasing possible use cases for Roy. These examples serve as a guide to maximize your interaction and leverage Roy's capabilities effectively.

We strongly encourage you to use the thumbs up and down feedback options to rate the answers provided by Roy. This feedback mechanism is crucial for the assistant's learning process and will help us improve its responses over time.

While Roy is designed to assist you, it's important to remember that the AI assistant is not infallible. We recommend double-checking any critical information before acting on it to ensure accuracy and reliability in your security operations.

## Roy can assit with writing Sigma rules

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
