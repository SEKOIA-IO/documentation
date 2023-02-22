#### Retrieve necessary information

First, you will have to retrieve configuration information.
Connect to [Cloudflare Console](https://dash.cloudflare.com/) to collect the following :

1. **Cloudflare API Token**
    - Go to `My Profile`, then on the left panel, click on `API Tokens`.
    - Click on the `Create Token` button and select the `Create Custom Token` entry.
    - Give a name to your token and set the following permissions:

      |  Scope  |       Group       | Level |
      | ------- | ----------------- | ----- |
      | Account | Account Analytics | Read  |
      | Account | Logs              | Read  |
      | Account | Logs              | Edit  |
      | Zone    | Logs              | Read  |
      | Zone    | Logs              | Edit  |

	[see the Cloudflare documentation](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

2. **Cloudflare Zone ID** :
    - This information is specific to a Website.
    - On the left panel, click on `Websites` and select the Website you want.
    - On the right panel, there is an `API` section where you can retrieve the `Zone ID`.
