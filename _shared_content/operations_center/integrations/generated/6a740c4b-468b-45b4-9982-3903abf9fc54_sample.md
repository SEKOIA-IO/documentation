
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "AuthAccept"

    ```
	AuthAccept HOST_XXX [23/Jul/2025:09:42:41 +0200] "2.2.2.2 uid=toto,ou=Internal,ou=People,o=group" "domain.com GET /affwebservices/redirectjsp/redirect.jsp?RelayState=https%3A%2F%2Fproxy-auth.xxxxgroup.com%2Fmwg-internal%2Fde5fs23hu73ds%2Fplugin%3Ftarget%3DAuth%26reason%3DAuth%26ClientID%3D3664958249%26ttl%3D28800%26url%3DaHR0cHM6Ly9zcHJkYi5lc28taW8uY29tOjQ0Mw%2C%2C%26rnd%3D1753256545.1343803810.NIYDKGKubm1JCVNw4hvLJWZnoE9zPvw2tZ5DCvRz0LA%2C&SAMLRequest=fZLLcpswFIZfxaNFVzYIgQyoxh0CpraD09Zpk7E3HRUrhlZIVBc78dOXkOk0XbTL%2F1z%2FOd%2BZadryjqTW1GLLflqmzeix5UKTIZEAqwSRVDeaCNoyTUxFbtNNSZADSaekkZXkYJRqzZRppMik0LZl6papU1OxL9syAbUxnSau25c%2FPk1ov8oxNeVMH5W0nVPJ1m3Px0kjDFOCcvfA8INGfm1D%2F6DdjttjI94Zqo7MJM9G39C2e6sY1VL80RlvmDCrPPGn0yDGEQriIW4MT1AUQTgoq3hCl1tYLTfT8im%2BVMv1j12DeYUiQ%2B8ju0Ox%2BfD9E9ycx%2BOXNeKQeCH2EZ7iADueH%2FgR9CMPOjerXX79%2Ftp%2Ba711dndzDupTub7fC7mILx9PZ2T2OM9O2wss0zEYFVJVbLhyAh4o1wyMeq%2Fg6yJEMQwL7IfRIvPCqyhOiyDL0ysY5mGBir5Ma8tWQhsqTAIQRHgCwwnyP8OQBIggvAejO6Z0f%2Fw%2B7UAwnz2jI0OfegXz%2Fyzpb4Jg%2Fm9OM%2FfV6PmL%2Bvt55r8A&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso" [idletime=18000;maxtime=18000;authlevel=5;] [0]  [] []
    ```



=== "AuthAttempt"

    ```
	AuthAttempt HOST_XXX [23/Jul/2025:07:01:48 +0200] "10.33.110.2 T0316290@xxxxgroup.com" "domain.com GET /affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=nZJfS8MwFMXf%2FRQl72uzrl23sA7GhlBQmU588C3NblkgTWpuotu3N61%2FmAgTfEtubs65v5MskLeqYyvvDvoBXjygi6JjqzSy4aQk3mpmOEpkmreAzAm2W93esDSmrLPGGWEUuao2JcG0ridZPs%2Fq%2BVhkKWTjWV7TIuXTYp7ls6JIm3AynQpKoiewKI0uSZAhUYXoodLouHahRNN8RItROnmkOaOUZbNnEm3CaFJzN9w6ONchSxJEM5L7LhbGdrE7cAWY8KZ5gxrBvkoRtp2vlRRJT5OGdhJdGytgAC5JwxVC77%2FliPIVvisrDAK919po9C3Y3YdepfdwLMmMLK8WvSQbRrdnkV1OjH%2FpkqU7IJ72XggvWjru4rCKpW4s%2FwRZJGcGn3YduwuS1WZrAtPpPy%2FV47fcXe7uK3I%2FaoZW5izXKEE7Eu22vf%2B950o2EmxJ%2FoIISSpl3tYWuAvpOuuBLD%2FIfrIEwOT3X1y%2BAw%3D%3D&RelayState=s2bb34594b91c42e4185b072a679458772fb9166c0&SMPORTALURL=https%3A%2F%2Fsso-idp.corp.xxxx%2Faffwebservices%2Fpublic%2Fsaml2sso" [] [0]  [] []
    ```



=== "AuthLogout"

    ```
	AuthLogout HOST_XXX [23/Jul/2025:09:41:19 +0200] "2.2.2.2 uid=toto,ou=Internal,ou=People,o=group" "HOST_YYY  " [] [41]  [] []
    ```



=== "AuthReject"

    ```
	AuthReject HOST_XXX [23/Jul/2025:09:36:18 +0200] "3.3.3.3 tata" "domain.com GET /affwebservices/redirectjsp/redirect_unique.jsp?SAMLRequest=fZJRS8MwFIX%2FSsl7mrR1nQtdYWwIBRVR8cG3NL3dAm1Sc1On%2F960RUEGe73ck3O%2Bc1Og7LtB7EZ%2FMs%2FwMQL6qDpsiW5onq%2FyRGYp5Snn9IbzDd20m5Q2G6hXdZ4quc5I9AYOtTVbksacRBXiCJVBL40PI56uKF%2FTNHvla5Hlgt%2FGeZ68k%2BgQfLSRflaevB9QMIZoqW6G2J9kB3h0dhxiZXsm2%2FYMNYL71AqQDWPdacWm4GmQkGhvDcLkNzojrESNwsgeUHglXnYP9yJEE2pZEqPBAZRuNTQkurNOwcy%2BJd6NQKKvvjMo5lKuvzc4662yHSmLGdot0usiiYFigiblL3Rnj9rEgeMSu2mR%2FVGHeOgLtniVxXK2x%2BBQHZ5s6ON7gunllRaSOJkn4bTtvPq%2Fi13X2fPegfTwWwYrC3b5P8of&RelayState=c9fc2739-6a5b-436a-90e4-aca86ee9a636&SMPORTALURL=https%3A%2F%2Fsso-idp.xxxxgroup.com%2Faffwebservices%2Fpublic%2Fsaml2sso&SAMLTRANSACTIONID=529c8b77-146ba9a3-74ecf707-0641d84a-9afd1ab" [] [0] Invalid credentials [] []
    ```



=== "AzAccept"

    ```
	AzAccept HOST_XXX [23/Jul/2025:09:42:49 +0200] "2.2.2.2 uid=toto,ou=Internal,ou=People,o=group"  "domain.com PUT /BFC5SAISIE/api/v1/application/session/renew" [000000000000000000000000339e210a-bd76-68809279-da7f4700-0a1e3005fa49] [0]  [] []
    ```



=== "AzReject"

    ```
	AzReject HOST_XXX [23/Jul/2025:09:41:34 +0200] "2.2.2.2 uid=toto,ou=Internal,ou=People,o=group" "finance.corp.xxxx_agent DELETE /BFC5CONSO/api/v1/user/killsessions" [000000000000000000000000329e210a-cdf8-6880922e-e4ff9700-14d51f4008be] [0]  [] []
    ```



=== "ValidateAccept"

    ```
	ValidateAccept HOST_XXX [23/Jul/2025:09:42:50 +0200] "2.2.2.2 uid=toto,ou=Internal,ou=People,o=group" "domain.com POST /otdsws/rb_dc719c57-85e7-499c-9886-ef5d0d8299d7?type=js3&sn=v_4_srv_10_sn_C6CA31A6988BF09671ADE5FF4D2E1748_perc_100000_ol_0_mul_1_app-3A3b3e336b48aebb25_1&svrid=10&flavor=post&vi=ALLPGLGCBVPLHPHLRUCHHALDSUOFBADW-0&modifiedSince=1753116005271&bp=3&app=3b3e336b48aebb25&crc=3525654176&en=ql84hk9p&end=1" [idletime=18000;maxtime=18000;authlevel=5;] [0]  [] []
    ```



