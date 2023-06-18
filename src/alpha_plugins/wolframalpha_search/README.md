# Wolfram Search Plugin

The Wolfram Search plugin will allow alpha to directly interact with Wolfram.

## Key Features:
- Wolfram Search performs search queries using Wolfram.

## Installation:
1. Download the Wolfram Search Plugin repository as a ZIP file.
2. Copy the ZIP file into the "plugins" folder of your alpha project.
3. Add this chunk of code along with your Wolfram AppID (Token API) information to the `.env` file within alpha:

```
################################################################################
### WOLFRAM API
################################################################################

# Wolfram AppId or API keys can be found here: https://developer.wolframalpha.com/portal/myapps/index.html
# the AppId can be generated once you register in Wolfram Developer portal.

WOLFRAMALPHA_APPID=
```

## alpha Configuration

Set `ALLOWLISTED_PLUGINS=alpha-wolframalpha-search,example-plugin1,example-plugin2,etc` in your alpha `.env` file.
