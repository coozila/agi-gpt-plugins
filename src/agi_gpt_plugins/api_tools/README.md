# API Tools Plugin

The API Tools Plugin enables agi-gpt to communicate with APIs.

## Key Features:
- Supports GET, POST, PUT, DELETE, PATCH, HEAD and OPTIONS
- Tries to recover from strange values being used as parameters
- Accepts custom header values

## Installation:
As part of the agi-gpt plugins package, follow the [installation instructions](https://github.com/coozila/agi-gpt-plugins) on the agi-gpt-plugins GitHub reporistory README page.

## agi-gpt Configuration
Set `ALLOWLISTED_PLUGINS=agi-gptApiTools,example-plugin1,example-plugin2,etc` in your agi-gpt `.env` file.
