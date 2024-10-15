# OpenAI

![OpenAI](/assets/playbooks/library/openai.png){ align=right width=150 }

The OpenAI API can be applied to virtually any task that involves understanding or generating natural language, code, or images.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | API Key to use to connect to OpenAI API endpoints |

## Actions

### Ask GPT

Use an OpenAI GPT model to provide an answer to any prompt

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `prompt` | `string` |  |
| `temperature` | `number` | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. |
| `model` | `string` | ID of the model to use. See the model endpoint compatibility table (https://platform.openai.com/docs/models/model-endpoint-compatibility) for details on which models work with the Chat API. |
| `max_tokens` | `integer` | The maximum number of tokens to generate in the chat completion. Default is no limit |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response` | `string` |  |


## Extra

Module **`OpenAI` v1.6.0**