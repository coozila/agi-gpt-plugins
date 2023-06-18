# alpha-plugins

> ⚠️💀 **WARNING** 💀⚠️:
> Always examine the code of any plugin you use thoroughly, as plugins can execute any Python code, leading to potential malicious activities such as stealing your API keys.

> ⚙️ **WORK IN PROGRESS** ⚙️:
> The plugin API is still being refined. If you are developing a plugin, expect changes in the upcoming versions.

## Installation

**_⚠️This is a work in progress⚠️_**

Here are the steps to configure alpha Plugins:

1. **Install alpha**

   If you haven't done so, follow the installation instructions given by [alpha](https://github.com/coozila/alpha) to install it.

1. **Download the plugins folder from the `root` of `alpha` directory**

    To download it directly from your alpha directory, you can run this command on Linux or MacOS:

    ```bash
    curl -L -o ./plugins/alpha-plugins.zip https://github.com/coozila/alpha-plugins/archive/refs/heads/master.zip
    ```

    Or in PowerShell:

    ```pwsh
    Invoke-WebRequest -Uri "https://github.com/coozila/alpha-plugins/archive/refs/heads/master.zip"     -OutFile "./plugins/alpha-plugins.zip"
    ```

1. **Execute the dependency install script for plugins**

    This can be run via:

    Linux or MacOS:

    ```bash
    ./run.sh --install-plugin-deps
    ```

   Windows:

    ```pwsh
   .\run.bat --install-plugin-deps
    ```

    Or directly via the CLI:

    ```bash
    python -m alpha --install-plugin-deps
    ````

## Plugins

> For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

There are two categories of plugins: **first party** and **third party**. First-party plugins are included in this repo and are installed by default when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for widely-used plugins, and third-party for your specific needs. **You can view all the plugins and their contributors on this [directory](https://autoplugins.vercel.app/).**

If you've built a plugin and it's not listed in the directory, you can make a PR to this [repo](https://github.com/dylanintech/autoplugins) by adding your plugin to the `data` array in `plugins.tsx`.

You can also see the plugins here:

| Plugin       | Description     | Location |
|--------------|-----------|--------|
| Astro Info   | This gives alpha info about astronauts.                                                           | [alpha_plugins/astro](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/astro)           |
| API Tools        | This allows alpha to make API calls of various kinds.                                                           | [alpha_plugins/api_tools](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/api_tools)           |
| Baidu Search |  This search plugin integrates Baidu search engines into alpha. | [alpha_plugins/baidu_search](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/baidu_search)|
| Bing Search      | This search plugin integrates Bing search engines into alpha.                                                  | [alpha_plugins/bing_search](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/bing_search)       |
| Bluesky | Enables alpha to retrieve posts from Bluesky and create new posts. | [alpha_plugins/bluesky](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/bluesky)|
| Email            | Revolutionize email management with the alpha Email Plugin, leveraging AI to automate drafting and intelligent replies. | [alpha_plugins/email](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/email)                 |
| News Search      | This search plugin integrates News Articles searches, using the NewsAPI aggregator into alpha.                 | [alpha_plugins/news_search](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/news_search)   |
| Planner          | Simple Task Planner Module for alpha  | [alpha_plugins/planner](https://github.com/coozila/alpha-plugins/blob/master/src/alpha_plugins/planner/) |
| Random Values    | Enable alpha to generate various random numbers and strings.                                                    | [alpha_plugins/random_values](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/random_values) |
| SceneX           | Explore image storytelling beyond pixels with the alpha SceneX Plugin.                                        | [alpha_plugins/scenex](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/scenex)               |
| Telegram |  A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal. | [alpha_plugins/telegram](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/telegram) |
| Twitter          | alpha is capable of retrieving Twitter posts and other related content by accessing the Twitter platform via the v1.1 API using Tweepy.               | [alpha_plugins/twitter](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/twitter)           |
| Wikipedia Search | This allows alpha to use Wikipedia directly.                                                                    | [alpha_plugins/wikipedia_search](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/wikipedia_search) |
| WolframAlpha Search | This allows alpha to use WolframAlpha directly.                                                                                         | [alpha_plugins/wolframalpha_search](https://github.com/coozila/alpha-plugins/tree/master/src/alpha_plugins/wolframalpha_search)|

Some third-party plugins have been created by contributors that are not included in this repository. For more information about these plugins, please visit their respective GitHub pages.

| Plugin       | Description     | Repository |
|--------------|-----------------|-------------|
| Alpaca-Trading | Trade stocks and crypto, paper or live with alpha | [danikhan632/alpha-AlpacaTrader-Plugin](https://github.com/danikhan632/alpha-AlpacaTrader-Plugin)|
| alpha User Input Request | Allow alpha to specifically request user input in continous mode | [HFrovinJensen/alpha-User-Input-Plugin](https://github.com/HFrovinJensen/alpha-User-Input-Plugin)|
| BingAI | Enable alpha to fetch information via BingAI, saving time, API requests while maintaining accuracy. This does not remove the need for OpenAI API keys | [gravelBridge/alpha-BingAI](https://github.com/gravelBridge/alpha-BingAI)|
| Crypto | Trade crypto with alpha | [isaiahbjork/alpha-Crypto-Plugin](https://github.com/isaiahbjork/alpha-Crypto-Plugin)|
| Discord | Interact with your alpha instance through Discord | [gravelBridge/alpha-Discord](https://github.com/gravelBridge/alpha-Discord)|
| Dolly alpha Cloner | A way to compose & run multiple alpha processes that cooperate, till core has multi-agent support | [pr-0f3t/alpha-Dolly-Plugin](https://github.com/pr-0f3t/alpha-Dolly-Plugin)|
| Google Analytics | Connect your Google Analytics Account to alpha. | [isaiahbjork/alpha-Google-Analytics-Plugin](https://github.com/isaiahbjork/alpha-Google-Analytics-Plugin)|
| IFTTT webhooks | This plugin allows you to easily integrate IFTTT connectivity using Maker | [AntonioCiolino/alpha-IFTTT](https://github.com/AntonioCiolino/alpha-IFTTT)|
| iMessage | Send and Get iMessages using alpha | [danikhan632/alpha-Messages-Plugin](https://github.com/danikhan632/alpha-Messages-Plugin)|
| Instagram | Instagram access | [jpetzke/alpha-Instagram](https://github.com/jpetzke/alpha-Instagram)|
| Mastodon  | Simple Mastodon plugin to send toots through a Mastodon account | [ppetermann/AlphaMastodonPlugin](https://github.com/ppetermann/AlphaMastodonPlugin)|
| MetaTrader | Connect your MetaTrader Account to alpha. | [isaiahbjork/alpha-MetaTrader-Plugin](https://github.com/isaiahbjork/alpha-MetaTrader-Plugin) |
| Notion      | Notion plugin for alpha.  | [doutv/alpha-Notion](https://github.com/doutv/alpha-Notion) |
| Slack | This plugin allows to receive commands and send messages to slack channels | [adithya77/alpha-slack-plugin](https://github.com/adithya77/alpha-slack-plugin)
| Spoonacular | Find recipe insiprations using alpha | [minfenglu/alpha-Spoonacular-Plugin](https://github.com/minfenglu/alpha-Spoonacular-Plugin)
| System Information      | This plugin adds an extra line to the prompt, serving as a hint for the AI to use shell commands likely supported by the current system. By incorporating this plugin, you can ensure that the AI model provides more accurate and system-specific shell commands, improving its overall performance and usefulness. | [hdkiller/alpha-SystemInfo](https://github.com/hdkiller/alpha-SystemInfo) |
| TiDB Serverless   | Connect your TiDB Serverless database to alpha, enable get query results from database | [pingcap/alpha-TiDB-Serverless-Plugin](https://github.com/pingcap/alpha-TiDB-Serverless-Plugin)
| Todoist-Plugin | Allow alpha to programatically interact with yor Todoist to create, update, and manage your Todoist | [danikhan632/alpha-Todoist-Plugin](https://github.com/danikhan632/alpha-Todoist-Plugin) |
| Weather | A simple weather plugin wrapping around python-weather | [ppetermann/alpha-WeatherPlugin](https://github.com/ppetermann/alpha-WeatherPlugin) |
| Web-Interaction | Enable alpha to fully interact with websites! Allows alpha to click elements, input text, and scroll | [gravelBridge/alpha-Web-Interaction](https://github.com/gravelBridge/alpha-Web-Interaction)|
| WolframAlpha | Access to WolframAlpha to do math and get accurate information | [gravelBridge/alpha-WolframAlpha](https://github.com/gravelBridge/alpha-WolframAlpha)|
| YouTube   | Various YouTube features including downloading and understanding | [jpetzke/alpha-YouTube](https://github.com/jpetzke/alpha-YouTube) |
| Zapier webhooks | This plugin allows you to easily integrate Zapier connectivity | [AntonioCiolino/alpha-Zapier](https://github.com/AntonioCiolino/alpha-Zapier)|
| Project Management | Streamline your Project Management with ease: Jira, Trello, and Google Calendar Made Effortless| [minfenglu/alpha-PM-Plugin](https://github.com/minfenglu/alpha-PM-Plugin)|

## Configuration

For interactionless use, set:

`ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,etc` in your `.env` file to allow plugins to load without prompting.
`DENYLISTED_PLUGINS=example-plugin1,example-plugin2,etc` in your `.env` file to block plugins from loading without prompting.

## Creating a Plugin

Creating a plugin is a rewarding experience! You can choose between first-party or third-party plugins. First-party plugins are included in this repo and are installed by default along with other plugins when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for plugins you expect others to use and want, and third-party for things specific to you.

### First Party Plugins How-To

1. Clone the plugins repo
1. Follow the structure of the other plugins, implementing the plugin interface as required
1. Write your tests
1. Add your name to the [codeowners](.github/CODEOWNERS) file
1. Add your plugin to the [Readme](README.md)
1. Add your plugin to the [alpha-package](https://github.com/kurtosis-tech/alpha-package/blob/main/plugins.star). You can copy the line of any of the standard plugins and just add another entry in the dictionary. Raise a PR & get it merged
1. Add your plugin to the [plugin installation integration test](.github/workflows/test-plugin-installation.yml)
1. Make a PR back to this repo!

### Third Party Plugins How-To

1. Clone [the third party template](https://github.com/coozila/alpha-Plugin-Template).
1. Follow the instructions in the [third party template readme](https://github.com/coozila/alpha-Plugin-Template).

### Migrating Third Party to First Party

We appreciate your contribution of a plugin to the project!

1. Clone this repository.
1. Make a folder for your plugin under `src/alpha_plugins`. Use a simple descriptive name such as `notion`, `twitter`, or `web_ui`.
1. Add the files from your third-party plugin located at `src/alpha_plugin_template` into the folder you created.
1. Include your README from your third-party plugin in the folder you created.
1. Add your plugin to the root README with a description and a link to your plugin-specific README.
1. Add your plugin's Python package requirements to `requirements.txt`.
1. Add tests to get your plugin to 80% code coverage.
1. Add your name to the [codeowners](.github/CODEOWNERS) file.
1. Add your plugin to the [Readme](README.md).
1. Submit a pull request back to this repository!

## Get Help

For more information, visit the [discord](https://discord.gg/alpha) server.
