# Expiration Rules

In SEKOIA.IO each indicator object must have a start and a validity end date.

When producing new intelligence in Content Proposals or via a playbook, analysts can manually define these validity periods on a case-by-case basis. 

The Expiration Rules have been designed to define default validity periods for the Indicators objects according to the type of observable. By default 6 rules exist in SEKOIA.IO:

* File (hash): 12 months
* URL: 6 months
* IPv4: 1 month
* IPv6: 1 month
* Domain name: 6 months
* Other observables: 6 months

<img width="1425" alt="image" src="https://user-images.githubusercontent.com/17184467/155111993-587bda36-277e-4c36-b584-77d95c53815c.png">

For example, when importing an IP address into a Content Proposal and creating a new Indicator object, if the analyst does not modify the fields corresponding to the validity date, it will automatically be set to 1 month once merged in the CTI base.

Each default rule can be modified to adapt the validity dates to your needs.

<img width="783" alt="image" src="https://user-images.githubusercontent.com/17184467/155112139-fb0d0d58-1132-45ef-aba4-9311327331f8.png">

