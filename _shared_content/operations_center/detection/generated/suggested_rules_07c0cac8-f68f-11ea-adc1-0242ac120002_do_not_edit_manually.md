## Suggested Built-in Rules

This integration enables the following built-in detection rules. Use the Rules Catalog to customize and adapt these to your security posture.


??? warning "Fortinet Firewall Login In Failure"
    
    Detects failed login attemps on firewall administration rule. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master

??? warning "Fortinet Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
