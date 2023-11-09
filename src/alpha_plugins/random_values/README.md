# Random Values Plugin

The Random Values plugin will enable agi-gpt to generate various random assorted things like numbers and strings.

## Key Features:
- make_uuids generates 1 or more UUIDs (128-bit label)
- generate_string generates 1 or more agi-gptnumeric strings of at least 2 characters in length
- generate_password generates 1 or more passwords of 6 or more characters using letters, numbers and punctuation
- generate_placeholder_text generates 1 or more sentences of lorem ipsum text
- random_number draws 1 or more random numbers between min and max

## Installation:
As part of the agi-gpt plugins package, follow the [installation instructions](https://github.com/coozila/agi-gpt-plugins) on the agi-gpt-plugins GitHub reporistory README page.

## agi-gpt Configuration

Set `ALLOWLISTED_PLUGINS=agi-gpt-random-values,example-plugin1,example-plugin2,etc` in your agi-gpt `.env` file.
