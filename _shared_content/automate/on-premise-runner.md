# On-premise runner

Some action may need to be executed with access to your internal network. For this use case it is possible to setup an on-premise playbook runner that can execute the playbook actions.


!!! INFO
    This feature is currently in private beta.
    If you would like to try it please contact us.

## Pre requisites

### Supported OS versions

Linux distributions based on a kernel version of **3.10** or newer should be supported by the playbook runner.

Here's a non-exhaustive list of supported distributions:

* Ubuntu 14.04 and newer
* Debian 8 and newer
* CentOS 7 and newer
* Redhat 7 and newer

### Docker

The playbook runners rely on `docker` to execute the actions. To install it follow the [official installation instructions](https://docs.docker.com/engine/install/).

#### podman

Some distribution (RHEL, CentOS, ...) may come with `podman` already installed and may prevent `docker` from working.
Podman may even run docker commands if the package `podman-docker` is installed. 
The playbook runner agent needs not only the docker client but also the engine to be installed.

To uninstall `podman` the following instruction can be followed:

```sh
# Remove packages
sudo yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
# Remove any left-over artifacts & files
sudo rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
# Delete any associated container storage
cd ~ && rm -rf /.local/share/containers/
```

### Allowed domains

The agent must be able to communicate with several external domains:

* To pull module images:
    * ghcr.io
    * githubusercontent.com
* To send execution results and store files:
    * sekoia.io
    * app.sekoia.io
    * api.sekoia.io
    * minio-symphony.prod.sekoia.io
    * ...

### Testing the pre requisites

A docker image has been created to validate the everything is ready for the agent to be installed.

In a terminal run the following command:

```sh
docker run ghcr.io/sekoia-io/hello-sekoia:latest
```

It will pull the image, making sure that the host can access the docker registry and check the connectivity with Sekoia.io.

Here's an example of the expected ouput:

```
Checking connectivity with Sekoia.io APIs ...
  - Checking app.sekoia.io ... OK
  - Checking api.sekoia.io ... OK
Checking connectivity with the object storage ... OK
```

## Creating a runner

On the playbooks listing page click on the "Playbook runners" button at the top right of the screen.

Once on the playbook runners listing click on either "+ Set up a playbook runner" or "+ Playbook runner"

![setup playbook runner](/assets/playbooks/setup_playbook_runner.png){: style="max-width:100%"}

Give a name to your playbook runner

![playbook runner name](/assets/playbooks/playbook_runner_name.png){: style="max-width:100%"}

And follow the instructions displayed to install the playbook runner on your machine.

![playbook runner instructions](/assets/playbooks/playbook_runner_instructions.png){: style="max-width:100%"}

Once the playbook runner has been installed you can leave the instructions by clicking on "Back to playbook runners".
The playbook runner should apprear in the list.

## Using a runner

To use a playbook runner for a specific action go to the concerned playbook and click on the action that should be executed on premise.

Open the configuration sidebar for this action and change "How to execute this action" to "On-premise". Under "Which playbook runner" choose the one you would like to use to execute this action.

![playbook runner instructions](/assets/playbooks/playbook_runner_action_on_premise.png){: style="max-width:100%"}


Once the playbook runner has been chosen save the playbook.