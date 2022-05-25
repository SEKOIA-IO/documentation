# Content Proposals

Content Proposals (CP) allow analysts to produce and capitalize on their own CTI. 

## Listing and filtering

The Content Proposals homepage lists all the contributions and suggestions made to add content to your TIP CTI database. 

### Types of Content Proposals

There are two types of content proposals: 

- CPs that are **manually** made by analysts
- CPs that are **automatically** pushed by playbooks

### Content Proposals statuses

A Content Proposal has three possible statuses. You can filter your CPs by status by clicking on one of the tabs. 

- **Pending**: CPs are still being updated and have not been merged yet
- **Merged**: CPs have been approved and their content is now part of the CTI database
- **Rejected**: CPs have been rejected and their content has not been deployed in the database

### Available filters on Content Proposals

You can also filter your content proposals based on different filters: 

- The source of the CP
- The assigned analyst in charge of the CP
- The reviewed assigned to the CP

Each Content Proposal can be assigned to a member of your team and a reviewer. 

## Create an empty Content Proposal

In the listing page, the Create button allows you to create a new empty Content Proposal.

In the left panel of the layout, you have access to different tabs:

### The Objects tab

The Objects tab allows you to: 

- Add existing objects from the CTI database to your CP
- Create new objects
- Create relationships (one by one or chain)

In this tab, you can display all the objects present in the Content Proposals and filter them by type, review status or whether or not objects have an associated warning. 

A button also allows multiple selection to perform different “bulk” actions such as adding existing relationships, creating new relationships or deleting objects.

### The Observables tab

The Observables tab allows you to:

- Create Observables individually
- Import Observables in bulk
- Assign tags to Observables
- Transform Observables into Indicators

A button also allows multiple selection to perform different “bulk” actions such as creating indicators from Observables, adding one or more tags or deleting Observables.

### The Relationships tab

The Relationships tab gives you the possibility to create relationships between two objects of the CTI database.

This phase of creating Objects and Relations can also be done directly in the Graph view.

## Import content to create a Content Proposal

To create a Content Proposal, you can also import content. 

There are three possible options to import content: 

- From a file
- From a free text
- From a URL

The imported content will be parsed in order to recognize as many Observables as possible (IP, domain names, file hash, e-mail address, URL, etc.) as well as objects already known to the CTI database (malware, intrusion set, attack pattern ATT&CK, location, etc.).

## Comments on CP
To be able to improve the review of a content proposal and allow interactions between the assignee and the reviewer, a comment feature has been recently implemented inside the content proposal page.

### Post a comment
To be able to comment or to see comments on a content proposal, you'll have to: 
1. Go to a Content Proposal 
2. In the Content Proposal's header, a button `Comments` shows next to the graph icon and the `reject` and `merge` buttons
3. Write down your comment and press `Enter` or click on `Comment`

### Edit a comment
To edit a comment, you'll have to: 
1. Click on the comment panel 
2. Hover over the comment you wrote that you want to edit 
3. Click on the `Edit` icon 
4. Edit your comment and `Enter` or click on `Comment` 

### Delete a comment
To delete a comment, you'll have to: 
1. Click on the comment panel 
2. Hover over the comment you wrote that you want to delete 
3. Click on the `Delete` icon 
4. Confirm your choice by clicking on `Delete` in the confirmation modal

!!! note
    If you delete a comment, you will not be able to recover it. 

## Request for Intelligence

In order to enable end users to make direct requests to our analysts to create an intelligence report or take a specific action, we added a new functionality “RFI” - short for Request For Intelligence - that we integrated into the Intelligence Center. 

### Create an RFI
In the Content Proposals listing page, there is a button on the top right of the page called “Request for Intelligence”. 
After clicking on that button, you will have to fill out a form with the following information:

- Type of request: could be a situational awareness report, a request for investigation, a threat assesment or a request for action 
- Assignee: who's in charge of making the Content Proposal
- Summary of your request: the title of the content proposal
- A description of the request
- Priority of the request: `low`, `medium`or `high` 
- Traffic Light Protocol (TLP)

Once you’ve created the request, a new content proposal will be automatically created.

### Filter on RFI
You can filter the RFI Content Proposals using the checkbox: “Show only RFI”.

!!! note
    This feature is available to the TIP users that have the `INTHREAT_WRITE_REQUEST_FOR_INTELLIGENCE` permission. This permission will be delivered to all the SEKOIA.IO TIPs.
