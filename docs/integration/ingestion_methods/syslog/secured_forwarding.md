# How to secure data collection to the syslog forwarder

## Overview

Events are forwarded to Sekoia.io through a secured transport layer (with TLS) to `intake.sekoia.io:50514`.

For security reason, you may require to secure the collect of events between our equipments/sources and the syslog forwarder.

## Generate the certificates

### Install OpenSSL and Gnutls-bin

According to your operating system, install `openssl` to generate the certificates.

On Debian-like distributions:
```
$ sudo apt install openssl && sudo apt install gnutls-bin
```

On Redhat-like distributions:
```
$ sudo dnf install openssl && sudo apt install gnutls-bin
```

On Mac OS X (with homebrew):
```
$ brew install openssl
```

### Generate the Certificate Autority (CA)

Create a directory that will contain your certificates.
Open a terminal and type:

```
$ mkdir mycertificates && cd mycertificates
```

#### Generate the private key

In the terminal, create the private key of the CA.

```
$ certtool --generate-privkey --outfile ca-key.pem --sec-param High
Generating a 3072 bit RSA private key…
```

#### Generate the CA certificate

In the terminal, generate the certificate of the CA. Type the name of the authority, define the expiration time and set this certificate as an authority certificate.

```
# Generate the CA certificate
$ certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca.pem
Generating a self signed certificate...
Please enter the details of the certificate's distinguished name. Just press enter to ignore a field.
Common name: logconcentrator.domain.tld
[...]
The certificate will expire in (days): 3650
 
Extensions.
Does the certificate belong to an authority? (y/N): y
[...]
Will the certificate be used to sign other certificates? (y/N): y
[...]
Is the above information ok? (y/N): y
 
Signing certificate…

# Change the permission, on the certificate, to read-only
$ chmod 600 ca.pem
```

Copy this certificate on your equipments/sources, in the registry/directory for Certificate Authority

### Generate the certificate

To secure the incoming events to the syslog forwarder, generate a server certificate.


#### Generate the private key

In the terminal, create the private key.

```
# Generate the server key
$ certtool --generate-privkey --outfile server.pem --sec-param High
Generating a 3072 bit RSA private key…

# Change the permission, on the key, to read-only
$ chmod 600 server.pem
```

#### Generate the Certificate Signing Request (CSR)

In the terminal, generate the CSR:

```
$ certtool --generate-request --load-privkey server.pem --outfile server.csr
Generating a PKCS #10 certificate request...
Common name: logserveur.test.local
[...]
Enter a dnsName of the subject of the certificate: logconcentrator.domain.tld
[...]
Is this a TLS web client certificate? (y/N): y
Is this a TLS web server certificate? (y/N): y
```

#### Generate the certificate for the syslog forwarder

In the terminal, generate the certificate of the syslog forwarder. Define the certificate as a server certificate and type the domain name of the syslog forwarder.

```
# Generate the server certificate
$ certtool --generate-certificate --load-request server.csr --outfile server.crt --load-ca-certificate ca.pem --load-ca-privkey ca-key.pem
Generating a signed certificate...
[...]
Activation/Expiration time.
The certificate will expire in (days): 365
 
 
Extensions.
Does the certificate belong to an authority? (y/N): n
Is this a TLS web client certificate? (y/N): n
Is this a TLS web server certificate? (y/N): y
Enter a dnsName of the subject of the certificate: logconcentrator.domain.tld
[...]
Is the above information ok? (y/N): y
 
Signing certificate…

# Change the permission, on the certificate, to read-only
$ chmod 600 server.crt
```

## Secure the collect of events with stunnel

### Install stunnel

According to your operating system, install `stunnel`.

On Debian-like distributions:
```
$ sudo apt install stunnel
```

On Redhat-like distributions:
```
$ sudo dnf install stunnel
```

### Move the certificates

```
# Create the directory for certificates
$ mkdir -p /etc/stunnel/certificates/

# Copy the certificates
$ cp ca.pem server.pem server.crt /etc/stunnel/certificates/
```

### Configure stunnel

Configure stunnel to accept secured connection and forward the events to the syslog forwarder:

```
# Create the configuration if not exist
$ sudo touch /etc/stunnel/default.conf

# Set the configuration
$ sudo vi /etc/stunnel/default.conf
; It is recommended to drop root privileges if stunnel is started by root
setuid = stunnel4
setgid = stunnel4

; PID file is created inside the chroot jail (if enabled)
pid = /var/run/stunnel4/stunnel.pid

output = /var/log/stunnel4/stunnel.log

[secured_source_tunnel]
client = no
accept = 6514
connect = <address of the syslog forwarder>:<port to forward to>
cert = /etc/stunnel/certificates/server.crt
key = /etc/stunnel/certificates/server.pem
CAfile = /etc/stunnel/certificates/ca.pem
```

### Start stunnel

In the terminal, start stunnel:

```
$ sudo stunnel /etc/stunnel/default.conf
```
