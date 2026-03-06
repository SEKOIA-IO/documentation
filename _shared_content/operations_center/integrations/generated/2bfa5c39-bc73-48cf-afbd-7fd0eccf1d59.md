
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | collect network activities from source |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `['authentication']`, `['web']` |
| Type | `` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "AuthAccept.json"

    ```json
	
    {
        "message": "AuthAccept HOST_XXX [23/Jul/2025:09:42:41 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\" \"domain.com GET /affwebservices/redirectjsp/redirect.jsp?RelayState=https%3A%2F%2Fproxy-auth.xxxxgroup.com%2Fmwg-internal%2Fde5fs23hu73ds%2Fplugin%3Ftarget%3DAuth%26reason%3DAuth%26ClientID%3D3664958249%26ttl%3D28800%26url%3DaHR0cHM6Ly9zcHJkYi5lc28taW8uY29tOjQ0Mw%2C%2C%26rnd%3D1753256545.1343803810.NIYDKGKubm1JCVNw4hvLJWZnoE9zPvw2tZ5DCvRz0LA%2C&SAMLRequest=fZLLcpswFIZfxaNFVzYIgQyoxh0CpraD09Zpk7E3HRUrhlZIVBc78dOXkOk0XbTL%2F1z%2FOd%2BZadryjqTW1GLLflqmzeix5UKTIZEAqwSRVDeaCNoyTUxFbtNNSZADSaekkZXkYJRqzZRppMik0LZl6papU1OxL9syAbUxnSau25c%2FPk1ov8oxNeVMH5W0nVPJ1m3Px0kjDFOCcvfA8INGfm1D%2F6DdjttjI94Zqo7MJM9G39C2e6sY1VL80RlvmDCrPPGn0yDGEQriIW4MT1AUQTgoq3hCl1tYLTfT8im%2BVMv1j12DeYUiQ%2B8ju0Ox%2BfD9E9ycx%2BOXNeKQeCH2EZ7iADueH%2FgR9CMPOjerXX79%2Ftp%2Ba711dndzDupTub7fC7mILx9PZ2T2OM9O2wss0zEYFVJVbLhyAh4o1wyMeq%2Fg6yJEMQwL7IfRIvPCqyhOiyDL0ysY5mGBir5Ma8tWQhsqTAIQRHgCwwnyP8OQBIggvAejO6Z0f%2Fw%2B7UAwnz2jI0OfegXz%2Fyzpb4Jg%2Fm9OM%2FfV6PmL%2Bvt55r8A&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso\" [idletime=18000;maxtime=18000;authlevel=5;] [0]  [] []",
        "event": {
            "action": "AuthAccept",
            "category": [
                "authentication"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "allowed",
                "start"
            ]
        },
        "@timestamp": "2025-07-23T07:42:41Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                },
                "authlevel": "5",
                "idle": "18000",
                "maxtime": "18000",
                "transaction": {
                    "id": "idletime=18000;maxtime=18000;authlevel=5;"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/affwebservices/redirectjsp/redirect.jsp?RelayState=https%3A%2F%2Fproxy-auth.xxxxgroup.com%2Fmwg-internal%2Fde5fs23hu73ds%2Fplugin%3Ftarget%3DAuth%26reason%3DAuth%26ClientID%3D3664958249%26ttl%3D28800%26url%3DaHR0cHM6Ly9zcHJkYi5lc28taW8uY29tOjQ0Mw%2C%2C%26rnd%3D1753256545.1343803810.NIYDKGKubm1JCVNw4hvLJWZnoE9zPvw2tZ5DCvRz0LA%2C&SAMLRequest=fZLLcpswFIZfxaNFVzYIgQyoxh0CpraD09Zpk7E3HRUrhlZIVBc78dOXkOk0XbTL%2F1z%2FOd%2BZadryjqTW1GLLflqmzeix5UKTIZEAqwSRVDeaCNoyTUxFbtNNSZADSaekkZXkYJRqzZRppMik0LZl6papU1OxL9syAbUxnSau25c%2FPk1ov8oxNeVMH5W0nVPJ1m3Px0kjDFOCcvfA8INGfm1D%2F6DdjttjI94Zqo7MJM9G39C2e6sY1VL80RlvmDCrPPGn0yDGEQriIW4MT1AUQTgoq3hCl1tYLTfT8im%2BVMv1j12DeYUiQ%2B8ju0Ox%2BfD9E9ycx%2BOXNeKQeCH2EZ7iADueH%2FgR9CMPOjerXX79%2Ftp%2Ba711dndzDupTub7fC7mILx9PZ2T2OM9O2wss0zEYFVJVbLhyAh4o1wyMeq%2Fg6yJEMQwL7IfRIvPCqyhOiyDL0ysY5mGBir5Ma8tWQhsqTAIQRHgCwwnyP8OQBIggvAejO6Z0f%2Fw%2B7UAwnz2jI0OfegXz%2Fyzpb4Jg%2Fm9OM%2FfV6PmL%2Bvt55r8A&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso"
        }
    }
    	
	```


=== "AuthAttempt.json"

    ```json
	
    {
        "message": "AuthAttempt HOST_XXX [23/Jul/2025:07:01:48 +0200] \"10.33.110.2 T0316290@xxxxgroup.com\" \"domain.com GET /affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=nZJfS8MwFMXf%2FRQl72uzrl23sA7GhlBQmU588C3NblkgTWpuotu3N61%2FmAgTfEtubs65v5MskLeqYyvvDvoBXjygi6JjqzSy4aQk3mpmOEpkmreAzAm2W93esDSmrLPGGWEUuao2JcG0ridZPs%2Fq%2BVhkKWTjWV7TIuXTYp7ls6JIm3AynQpKoiewKI0uSZAhUYXoodLouHahRNN8RItROnmkOaOUZbNnEm3CaFJzN9w6ONchSxJEM5L7LhbGdrE7cAWY8KZ5gxrBvkoRtp2vlRRJT5OGdhJdGytgAC5JwxVC77%2FliPIVvisrDAK919po9C3Y3YdepfdwLMmMLK8WvSQbRrdnkV1OjH%2FpkqU7IJ72XggvWjru4rCKpW4s%2FwRZJGcGn3YduwuS1WZrAtPpPy%2FV47fcXe7uK3I%2FaoZW5izXKEE7Eu22vf%2B950o2EmxJ%2FoIISSpl3tYWuAvpOuuBLD%2FIfrIEwOT3X1y%2BAw%3D%3D&RelayState=s2bb34594b91c42e4185b072a679458772fb9166c0&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso\" [] [0]  [] []",
        "event": {
            "action": "AuthAttempt",
            "category": [
                "authentication"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "unknown",
            "reason": "Sm_Api_Reason_None"
        },
        "@timestamp": "2025-07-23T05:01:48Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                }
            }
        },
        "client": {
            "address": "10.33.110.2",
            "ip": "10.33.110.2",
            "user": {
                "domain": "xxxxgroup.com",
                "name": "T0316290"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "10.33.110.2"
            ],
            "user": [
                "T0316290"
            ]
        },
        "url": {
            "path": "/affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=nZJfS8MwFMXf%2FRQl72uzrl23sA7GhlBQmU588C3NblkgTWpuotu3N61%2FmAgTfEtubs65v5MskLeqYyvvDvoBXjygi6JjqzSy4aQk3mpmOEpkmreAzAm2W93esDSmrLPGGWEUuao2JcG0ridZPs%2Fq%2BVhkKWTjWV7TIuXTYp7ls6JIm3AynQpKoiewKI0uSZAhUYXoodLouHahRNN8RItROnmkOaOUZbNnEm3CaFJzN9w6ONchSxJEM5L7LhbGdrE7cAWY8KZ5gxrBvkoRtp2vlRRJT5OGdhJdGytgAC5JwxVC77%2FliPIVvisrDAK919po9C3Y3YdepfdwLMmMLK8WvSQbRrdnkV1OjH%2FpkqU7IJ72XggvWjru4rCKpW4s%2FwRZJGcGn3YduwuS1WZrAtPpPy%2FV47fcXe7uK3I%2FaoZW5izXKEE7Eu22vf%2B950o2EmxJ%2FoIISSpl3tYWuAvpOuuBLD%2FIfrIEwOT3X1y%2BAw%3D%3D&RelayState=s2bb34594b91c42e4185b072a679458772fb9166c0&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso"
        }
    }
    	
	```


=== "AuthLogout.json"

    ```json
	
    {
        "message": "AuthLogout HOST_XXX [23/Jul/2025:09:41:19 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\" \"HOST_YYY  \" [] [41]  [] []",
        "event": {
            "action": "AuthLogout",
            "category": [
                "authentication"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_UserLogout",
            "type": [
                "end"
            ]
        },
        "@timestamp": "2025-07-23T07:41:19Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "HOST_YYY"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        }
    }
    	
	```


=== "AuthReject.json"

    ```json
	
    {
        "message": "AuthReject HOST_XXX [23/Jul/2025:09:36:18 +0200] \"3.3.3.3 tata\" \"domain.com GET /affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=fZJRS8MwFIX%2FSsl7mrR1nQtdYWwIBRVR8cG3NL3dAm1Sc1On%2F960RUEGe73ck3O%2Bc1Og7LtB7EZ%2FMs%2FwMQL6qDpsiW5onq%2FyRGYp5Snn9IbzDd20m5Q2G6hXdZ4quc5I9AYOtTVbksacRBXiCJVBL40PI56uKF%2FTNHvla5Hlgt%2FGeZ68k%2BgQfLSRflaevB9QMIZoqW6G2J9kB3h0dhxiZXsm2%2FYMNYL71AqQDWPdacWm4GmQkGhvDcLkNzojrESNwsgeUHglXnYP9yJEE2pZEqPBAZRuNTQkurNOwcy%2BJd6NQKKvvjMo5lKuvzc4662yHSmLGdot0usiiYFigiblL3Rnj9rEgeMSu2mR%2FVGHeOgLtniVxXK2x%2BBQHZ5s6ON7gunllRaSOJkn4bTtvPq%2Fi13X2fPegfTwWwYrC3b5P8of&RelayState=c9fc2739-6a5b-436a-90e4-aca86ee9a636&SMPORTALURL=https%3A%2F%2Fsso-idp.xxxxgroup.com%2Faffwebservices%2Fpublic%2Fsaml2sso&SAMLTRANSACTIONID=529c8b77-146ba9a3-74ecf707-0641d84a-9afd1ab\" [] [0] Invalid credentials [] []",
        "event": {
            "action": "AuthReject",
            "category": [
                "authentication"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "message": "Invalid credentials ",
            "outcome": "failure",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-07-23T07:36:18Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                }
            }
        },
        "client": {
            "address": "3.3.3.3",
            "ip": "3.3.3.3",
            "user": {
                "name": "tata"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "3.3.3.3"
            ],
            "user": [
                "tata"
            ]
        },
        "url": {
            "path": "/affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=fZJRS8MwFIX%2FSsl7mrR1nQtdYWwIBRVR8cG3NL3dAm1Sc1On%2F960RUEGe73ck3O%2Bc1Og7LtB7EZ%2FMs%2FwMQL6qDpsiW5onq%2FyRGYp5Snn9IbzDd20m5Q2G6hXdZ4quc5I9AYOtTVbksacRBXiCJVBL40PI56uKF%2FTNHvla5Hlgt%2FGeZ68k%2BgQfLSRflaevB9QMIZoqW6G2J9kB3h0dhxiZXsm2%2FYMNYL71AqQDWPdacWm4GmQkGhvDcLkNzojrESNwsgeUHglXnYP9yJEE2pZEqPBAZRuNTQkurNOwcy%2BJd6NQKKvvjMo5lKuvzc4662yHSmLGdot0usiiYFigiblL3Rnj9rEgeMSu2mR%2FVGHeOgLtniVxXK2x%2BBQHZ5s6ON7gunllRaSOJkn4bTtvPq%2Fi13X2fPegfTwWwYrC3b5P8of&RelayState=c9fc2739-6a5b-436a-90e4-aca86ee9a636&SMPORTALURL=https%3A%2F%2Fsso-idp.xxxxgroup.com%2Faffwebservices%2Fpublic%2Fsaml2sso&SAMLTRANSACTIONID=529c8b77-146ba9a3-74ecf707-0641d84a-9afd1ab"
        }
    }
    	
	```


=== "AzAccept.json"

    ```json
	
    {
        "message": "AzAccept HOST_XXX [23/Jul/2025:09:42:49 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\"  \"domain.com PUT /BFC5SAISIE/api/v1/application/session/renew\" [000000000000000000000000339e210a-bd76-68809279-da7f4700-0a1e3005fa49] [0]  [] []",
        "event": {
            "action": "AzAccept",
            "category": [
                "web"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "allowed",
                "change"
            ]
        },
        "@timestamp": "2025-07-23T07:42:49Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                },
                "transaction": {
                    "id": "000000000000000000000000339e210a-bd76-68809279-da7f4700-0a1e3005fa49"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "http": {
            "request": {
                "method": "PUT"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/BFC5SAISIE/api/v1/application/session/renew"
        }
    }
    	
	```


=== "AzReject.json"

    ```json
	
    {
        "message": "AzReject HOST_XXX [23/Jul/2025:09:41:34 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\" \"finance.corp.xxxx_agent DELETE /BFC5CONSO/api/v1/user/killsessions\" [000000000000000000000000329e210a-cdf8-6880922e-e4ff9700-14d51f4008be] [0]  [] []",
        "event": {
            "action": "AzReject",
            "category": [
                "web"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "failure",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "deletion"
            ]
        },
        "@timestamp": "2025-07-23T07:41:34Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "finance.corp.xxxx_agent"
                },
                "transaction": {
                    "id": "000000000000000000000000329e210a-cdf8-6880922e-e4ff9700-14d51f4008be"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "http": {
            "request": {
                "method": "DELETE"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/BFC5CONSO/api/v1/user/killsessions"
        }
    }
    	
	```


=== "ValidateAccept.json"

    ```json
	
    {
        "message": "ValidateAccept HOST_XXX [23/Jul/2025:09:42:50 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\" \"domain.com POST /otdsws/rb_dc719c57-85e7-499c-9886-ef5d0d8299d7?type=js3&sn=v_4_srv_10_sn_C6CA31A6988BF09671ADE5FF4D2E1748_perc_100000_ol_0_mul_1_app-3A3b3e336b48aebb25_1&svrid=10&flavor=post&vi=ALLPGLGCBVPLHPHLRUCHHALDSUOFBADW-0&modifiedSince=1753116005271&bp=3&app=3b3e336b48aebb25&crc=3525654176&en=ql84hk9p&end=1\" [idletime=18000;maxtime=18000;authlevel=5;] [0]  [] []",
        "event": {
            "action": "ValidateAccept",
            "category": [
                "web"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "allowed",
                "creation"
            ]
        },
        "@timestamp": "2025-07-23T07:42:50Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                },
                "authlevel": "5",
                "idle": "18000",
                "maxtime": "18000",
                "transaction": {
                    "id": "idletime=18000;maxtime=18000;authlevel=5;"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "http": {
            "request": {
                "method": "POST"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/otdsws/rb_dc719c57-85e7-499c-9886-ef5d0d8299d7?type=js3&sn=v_4_srv_10_sn_C6CA31A6988BF09671ADE5FF4D2E1748_perc_100000_ol_0_mul_1_app-3A3b3e336b48aebb25_1&svrid=10&flavor=post&vi=ALLPGLGCBVPLHPHLRUCHHALDSUOFBADW-0&modifiedSince=1753116005271&bp=3&app=3b3e336b48aebb25&crc=3525654176&en=ql84hk9p&end=1"
        }
    }
    	
	```


=== "ressource_filename.json"

    ```json
	
    {
        "message": "ValidateAccept HOST_XXX [23/Jul/2025:09:42:31 +0200] \"2.2.2.2 uid=toto,ou=Internal,ou=People,o=group\" \"domain.com GET /livelink/llisapi.dll/11111111/News_Text_EN.html?func=doc.Fetch&nodeid=1111111\" [idletime=18000;maxtime=18000;authlevel=5;] [0]  [] []",
        "event": {
            "action": "ValidateAccept",
            "category": [
                "web"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "access",
                "allowed"
            ]
        },
        "@timestamp": "2025-07-23T07:42:31Z",
        "broadcom": {
            "siteminder": {
                "agent": {
                    "name": "domain.com"
                },
                "authlevel": "5",
                "function": "doc.Fetch",
                "idle": "18000",
                "maxtime": "18000",
                "node": {
                    "id": "1111111"
                },
                "transaction": {
                    "id": "idletime=18000;maxtime=18000;authlevel=5;"
                }
            }
        },
        "client": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "file": {
            "name": "News_Text_EN.html"
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "hostname": "HOST_XXX",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "HOST_XXX"
            ],
            "ip": [
                "2.2.2.2"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/livelink/llisapi.dll/11111111/News_Text_EN.html?func=doc.Fetch&nodeid=1111111"
        }
    }
    	
	```


=== "ressource_func.json"

    ```json
	
    {
        "message": "AzAccept host_01 [22/Sep/2025:13:29:26 +0200] \"192.168.1.1 uid=toto,ou=Internal,ou=People,o=group\" \"subdomain.corp.xxxxx_agent GET /livelink/livelink.exe?func=multifile.downloadfile&objAction=Browse&objId=1111111111&cacheid=2222222222&nodeid=3333333333\" [000000000000000000000000d111100a-496c-68d11111-111c-01057c71] [0]  [] []",
        "event": {
            "action": "AzAccept",
            "category": [
                "web"
            ],
            "dataset": "smaccess",
            "kind": "event",
            "outcome": "success",
            "reason": "Sm_Api_Reason_None",
            "type": [
                "access",
                "allowed"
            ]
        },
        "@timestamp": "2025-09-22T11:29:26Z",
        "broadcom": {
            "siteminder": {
                "action": "Browse",
                "agent": {
                    "name": "subdomain.corp.xxxxx_agent"
                },
                "cache": {
                    "id": "2222222222"
                },
                "function": "multifile.downloadfile",
                "node": {
                    "id": "3333333333"
                },
                "object": {
                    "id": "1111111111"
                },
                "transaction": {
                    "id": "000000000000000000000000d111100a-496c-68d11111-111c-01057c71"
                }
            }
        },
        "client": {
            "address": "192.168.1.1",
            "ip": "192.168.1.1",
            "user": {
                "domain": "ou=Internal,ou=People,o=group",
                "name": "toto"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "hostname": "host_01",
            "product": "Siteminder",
            "type": "uam",
            "vendor": "Broadcom "
        },
        "related": {
            "hosts": [
                "host_01"
            ],
            "ip": [
                "192.168.1.1"
            ],
            "user": [
                "toto"
            ]
        },
        "url": {
            "path": "/livelink/livelink.exe?func=multifile.downloadfile&objAction=Browse&objId=1111111111&cacheid=2222222222&nodeid=3333333333"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`broadcom.siteminder.action` | `keyword` | Action performed on the resource in Broadcom SiteMinder |
|`broadcom.siteminder.agent.name` | `keyword` | The name of the agent |
|`broadcom.siteminder.authlevel` | `keyword` | Authentication level |
|`broadcom.siteminder.cache.id` | `keyword` | ID of the cache concerned by the action in broadcom siteminder |
|`broadcom.siteminder.function` | `keyword` | Function used on the resource in Broadcom SiteMinder |
|`broadcom.siteminder.idle` | `keyword` | IDLE time in minutes |
|`broadcom.siteminder.maxtime` | `keyword` | Maximum time |
|`broadcom.siteminder.node.id` | `keyword` | ID of the node concerned by the action in broadcom siteminder |
|`broadcom.siteminder.object.id` | `keyword` | ID of the object concerned by the action in broadcom siteminder |
|`broadcom.siteminder.transaction.id` | `keyword` | A string that contains idletime=<value>. |
|`client.ip` | `ip` | IP address of the client. |
|`client.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`client.user.name` | `keyword` | Short name or login of the user. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`http.request.method` | `keyword` | HTTP request method. |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Broadcom/siteminder).