# Microsoft Remote Server

## Prerequisites

### Remote server configuration

To enable this module, please make sure you have properly configured WinRM on remote server. You can find more information about WinRM configuration [here](https://docs.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management).

If you are using Azure VM please check this [documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/winrm).

### How to setup and configure WinRM

Before doing any setup please make sure that you are able to access remote server with Administrator privileges ( requires to setup WinRM )
and your server is available to accept remote connections on `5985` and `5986` ports.

If you are using Azure VM you can do this in `Network settings` tab on your machine. Below is an example of security rules for WinRM.

  ![Azure VM WinRM](/assets/instructions/winrm/security-rules.png){ align=center }

* Open a PowerShell console as Administrator on remote server
* Execute command `Enable-PSRemoting -force`

  ![Enable-PSRemoting](/assets/instructions/winrm/1-psremoting.png){ align=center }

* Execute command `winrm quickconfig`

  ![Quick Config](/assets/instructions/winrm/2-winrm-quick-config.png){ align=center }

* Below commands will create new rules for allowing outside traffic to remote server on port `5985` fir WinRM HTTP and `5986` for WinRM HTTPS

   ```powershell
   netsh advfirewall firewall add rule name=”WinRM-HTTP” dir=in localport=5985 protocol=TCP action=allow
   netsh advfirewall firewall add rule name=”WinRM-HTTPS” dir=in localport=5986 protocol=TCP action=allow
   ```

  ![Netsh](/assets/instructions/winrm/3-netsh.png){ align=center }

* Create certificate for WinRM HTTPS and add HTTPS Listener with the certificate thumbprint.

  ```powershell
  $cert = New-SelfSignedCertificate -DnsName “<DNS or IP>” -CertStoreLocation cert:\
  winrm create winrm/config/Listener?Address=*+Transport=HTTPS “@{Hostname=`”<DNS_Name or IP>`”;CertificateThumbprint=`”$($cert.ThumbPrint)`”}”
  ```
  
  ![New-SelfSignedCertificate](/assets/instructions/winrm/4-new-self-signed-certificate.png){ align=center }

* Validate Listeners with `winrm e winrm/config/listener`.

  ![Validate listeners](/assets/instructions/winrm/5-validate-listeners.png){ align=center }

* Enable CredSSP on server with `Enable-WSManCredSSP -Role Server`.

  ![WSManCredSSP](/assets/instructions/winrm/6-wsmancredssp.png){ align=center }

## Configuration

| Name       | Type     | Description                                    |
|------------|----------|------------------------------------------------|
| `username` | `string` | Username to do authentication on remote server |
| `password` | `string` | Password to do authentication on remote server |

## Actions

### Change user password

Change existed user password on remote server

**Arguments**

| Name             | Type     | Description                              |
|------------------|----------|------------------------------------------|
| `user_to_update` | `string` | Username you want to change password for |
| `new_password`   | `string` | New password value                       |
| `server`         | `string` | Remote server dns name or IP address     |

### Disable users

Disable users on remote server

**Arguments**

| Name     | Type     | Description                            |
|----------|----------|----------------------------------------|
| `users`  | `array`  | Array of usernames you want to disable |
| `sids`   | `string` | SID`s of users you want to disable.    |
| `server` | `string` | Remote server dns name or IP address   |

### Enable users

Enable users on remote server

**Arguments**

| Name     | Type     | Description                            |
|----------|----------|----------------------------------------|
| `users`  | `array`  | Array of usernames you want to disable |
| `sids`   | `string` | SID`s of users you want to disable.    |
| `server` | `string` | Remote server dns name or IP address   |
