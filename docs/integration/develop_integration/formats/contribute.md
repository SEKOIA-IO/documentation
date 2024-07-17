# Contribute to intake formats Github

Thank you for contributing to Sekoia.io intake formats. This document describes how to contribute to this repository.

## Prerequisites

To contribute to this repository, you will need the following development setup:

- Python3: We recommend you to use Python3.12 or higher. To ease python version management, you can use [pyenv](https://github.com/pyenv/pyenv#installation)
- [Poetry](https://python-poetry.org/docs/#installation): To execute helper scripts in the directory `utils/`

## How to contribute

- Follow this [guide](../parser/) to write your parser in Python
- [Test your format](../testing/)

## Contribution checklist

To ensure the quality of contribution, the following points will be reviewed in your changes:

- Have clear descriptions for new modules, new formats and taxonomy
- A logo is provided for any new modules and any new formats
- Tests should cover at least 75% of parsers
- At least one smart-description is provide for any new format

## Homologation request 

Once you are done writing and testing your intake format, the last step is to request an homologation to Sekoia. Once your intake format is homologated, it will appear in the intake catalog of **Sekoia XDR platform**:

- Send an email to [team-integration@sekoia.io](mailto:team-integration@sekoia.io)
- You will get an acknowledgement from Sekoia Integration team
- In the following days (5 days max), you will receive feedbacks in your pull request that you must take into account
- Once all feedbacks are taken into account, Integration team will **validate** your pull request

The homologation process is now finished.