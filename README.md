# agi-gpt-plugins

> ⚠️💀 **WARNING** 💀⚠️:
> Always examine the code of any plugin you use thoroughly, as plugins can execute any Python code, leading to potential malicious activities such as stealing your API keys.

> ⚙️ **WORK IN PROGRESS** ⚙️:
> The plugin API is still being refined. If you are developing a plugin, expect changes in the upcoming versions.

## Installation

**_⚠️This is a work in progress⚠️_**

Here are the steps to configure agi-gpt Plugins:

1. **Install agi-gpt**

   If you haven't done so, follow the installation instructions given by [agi-gpt](https://github.com/coozila/agi-gpt) to install it.

1. **Download the plugins folder from the `root` of `agi-gpt` directory**

    To download it directly from your agi-gpt directory, you can run this command on Linux or MacOS:

    ```bash
    curl -L -o ./plugins/agi-gpt-plugins.zip https://github.com/coozila/agi-gpt-plugins/archive/refs/heads/master.zip
    ```

    Or in PowerShell:

    ```pwsh
    Invoke-WebRequest -Uri "https://github.com/coozila/agi-gpt-plugins/archive/refs/heads/master.zip"     -OutFile "./plugins/agi-gpt-plugins.zip"
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
    python -m agi-gpt --install-plugin-deps
    ````

## Plugins

> For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

There are two categories of plugins: **first party** and **third party**. First-party plugins are included in this repo and are installed by default when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for widely-used plugins, and third-party for your specific needs. **You can view all the plugins and their contributors on this [directory](https://autoplugins.vercel.app/).**

If you've built a plugin and it's not listed in the directory, you can make a PR to this [repo](https://github.com/dylanintech/autoplugins) by adding your plugin to the `data` array in `plugins.tsx`.

You can also see the plugins here:

| Plugin       | Description     | Location |
|--------------|-----------|--------|
| Astro Info   | This gives agi-gpt info about astronauts.                                                           | [agi-gpt_plugins/astro](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/astro)           |
| API Tools        | This allows agi-gpt to make API calls of various kinds.                                                           | [agi-gpt_plugins/api_tools](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/api_tools)           |
| Baidu Search |  This search plugin integrates Baidu search engines into agi-gpt. | [agi-gpt_plugins/baidu_search](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/baidu_search)|
| Bing Search      | This search plugin integrates Bing search engines into agi-gpt.                                                  | [agi-gpt_plugins/bing_search](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/bing_search)       |
| Bluesky | Enables agi-gpt to retrieve posts from Bluesky and create new posts. | [agi-gpt_plugins/bluesky](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/bluesky)|
| Email            | Revolutionize email management with the agi-gpt Email Plugin, leveraging AI to automate drafting and intelligent replies. | [agi-gpt_plugins/email](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/email)                 |
| News Search      | This search plugin integrates News Articles searches, using the NewsAPI aggregator into agi-gpt.                 | [agi-gpt_plugins/news_search](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/news_search)   |
| Planner          | Simple Task Planner Module for agi-gpt  | [agi-gpt_plugins/planner](https://github.com/coozila/agi-gpt-plugins/blob/master/src/agi-gpt_plugins/planner/) |
| Random Values    | Enable agi-gpt to generate various random numbers and strings.                                                    | [agi-gpt_plugins/random_values](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/random_values) |
| SceneX           | Explore image storytelling beyond pixels with the agi-gpt SceneX Plugin.                                        | [agi-gpt_plugins/scenex](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/scenex)               |
| Telegram |  A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal. | [agi-gpt_plugins/telegram](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/telegram) |
| Twitter          | agi-gpt is capable of retrieving Twitter posts and other related content by accessing the Twitter platform via the v1.1 API using Tweepy.               | [agi-gpt_plugins/twitter](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/twitter)           |
| Wikipedia Search | This allows agi-gpt to use Wikipedia directly.                                                                    | [agi-gpt_plugins/wikipedia_search](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/wikipedia_search) |
| Wolframagi-gpt Search | This allows agi-gpt to use Wolframagi-gpt directly.                                                                                         | [agi-gpt_plugins/wolframagi-gpt_search](https://github.com/coozila/agi-gpt-plugins/tree/master/src/agi-gpt_plugins/wolframagi-gpt_search)|

Some third-party plugins have been created by contributors that are not included in this repository. For more information about these plugins, please visit their respective GitHub pages.

| Plugin       | Description     | Repository |
|--------------|-----------------|-------------|
| Alpaca-Trading | Trade stocks and crypto, paper or live with agi-gpt | [danikhan632/agi-gpt-AlpacaTrader-Plugin](https://github.com/danikhan632/agi-gpt-AlpacaTrader-Plugin)|
| agi-gpt User Input Request | Allow agi-gpt to specifically request user input in continous mode | [HFrovinJensen/agi-gpt-User-Input-Plugin](https://github.com/HFrovinJensen/agi-gpt-User-Input-Plugin)|
| BingAI | Enable agi-gpt to fetch information via BingAI, saving time, API requests while maintaining accuracy. This does not remove the need for OpenAI API keys | [gravelBridge/agi-gpt-BingAI](https://github.com/gravelBridge/agi-gpt-BingAI)|
| Crypto | Trade crypto with agi-gpt | [isaiahbjork/agi-gpt-Crypto-Plugin](https://github.com/isaiahbjork/agi-gpt-Crypto-Plugin)|
| Discord | Interact with your agi-gpt instance through Discord | [gravelBridge/agi-gpt-Discord](https://github.com/gravelBridge/agi-gpt-Discord)|
| Dolly agi-gpt Cloner | A way to compose & run multiple agi-gpt processes that cooperate, till core has multi-agent support | [pr-0f3t/agi-gpt-Dolly-Plugin](https://github.com/pr-0f3t/agi-gpt-Dolly-Plugin)|
| Google Analytics | Connect your Google Analytics Account to agi-gpt. | [isaiahbjork/agi-gpt-Google-Analytics-Plugin](https://github.com/isaiahbjork/agi-gpt-Google-Analytics-Plugin)|
| IFTTT webhooks | This plugin allows you to easily integrate IFTTT connectivity using Maker | [AntonioCiolino/agi-gpt-IFTTT](https://github.com/AntonioCiolino/agi-gpt-IFTTT)|
| iMessage | Send and Get iMessages using agi-gpt | [danikhan632/agi-gpt-Messages-Plugin](https://github.com/danikhan632/agi-gpt-Messages-Plugin)|
| Instagram | Instagram access | [jpetzke/agi-gpt-Instagram](https://github.com/jpetzke/agi-gpt-Instagram)|
| Mastodon  | Simple Mastodon plugin to send toots through a Mastodon account | [ppetermann/agi-gptMastodonPlugin](https://github.com/ppetermann/agi-gptMastodonPlugin)|
| MetaTrader | Connect your MetaTrader Account to agi-gpt. | [isaiahbjork/agi-gpt-MetaTrader-Plugin](https://github.com/isaiahbjork/agi-gpt-MetaTrader-Plugin) |
| Notion      | Notion plugin for agi-gpt.  | [doutv/agi-gpt-Notion](https://github.com/doutv/agi-gpt-Notion) |
| Slack | This plugin allows to receive commands and send messages to slack channels | [adithya77/agi-gpt-slack-plugin](https://github.com/adithya77/agi-gpt-slack-plugin)
| Spoonacular | Find recipe insiprations using agi-gpt | [minfenglu/agi-gpt-Spoonacular-Plugin](https://github.com/minfenglu/agi-gpt-Spoonacular-Plugin)
| System Information      | This plugin adds an extra line to the prompt, serving as a hint for the AI to use shell commands likely supported by the current system. By incorporating this plugin, you can ensure that the AI model provides more accurate and system-specific shell commands, improving its overall performance and usefulness. | [hdkiller/agi-gpt-SystemInfo](https://github.com/hdkiller/agi-gpt-SystemInfo) |
| TiDB Serverless   | Connect your TiDB Serverless database to agi-gpt, enable get query results from database | [pingcap/agi-gpt-TiDB-Serverless-Plugin](https://github.com/pingcap/agi-gpt-TiDB-Serverless-Plugin)
| Todoist-Plugin | Allow agi-gpt to programatically interact with yor Todoist to create, update, and manage your Todoist | [danikhan632/agi-gpt-Todoist-Plugin](https://github.com/danikhan632/agi-gpt-Todoist-Plugin) |
| Weather | A simple weather plugin wrapping around python-weather | [ppetermann/agi-gpt-WeatherPlugin](https://github.com/ppetermann/agi-gpt-WeatherPlugin) |
| Web-Interaction | Enable agi-gpt to fully interact with websites! Allows agi-gpt to click elements, input text, and scroll | [gravelBridge/agi-gpt-Web-Interaction](https://github.com/gravelBridge/agi-gpt-Web-Interaction)|
| Wolframagi-gpt | Access to Wolframagi-gpt to do math and get accurate information | [gravelBridge/agi-gpt-Wolframagi-gpt](https://github.com/gravelBridge/agi-gpt-Wolframagi-gpt)|
| YouTube   | Various YouTube features including downloading and understanding | [jpetzke/agi-gpt-YouTube](https://github.com/jpetzke/agi-gpt-YouTube) |
| Zapier webhooks | This plugin allows you to easily integrate Zapier connectivity | [AntonioCiolino/agi-gpt-Zapier](https://github.com/AntonioCiolino/agi-gpt-Zapier)|
| Project Management | Streamline your Project Management with ease: Jira, Trello, and Google Calendar Made Effortless| [minfenglu/agi-gpt-PM-Plugin](https://github.com/minfenglu/agi-gpt-PM-Plugin)|

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
1. Add your plugin to the [agi-gpt-package](https://github.com/kurtosis-tech/agi-gpt-package/blob/main/plugins.star). You can copy the line of any of the standard plugins and just add another entry in the dictionary. Raise a PR & get it merged
1. Add your plugin to the [plugin installation integration test](.github/workflows/test-plugin-installation.yml)
1. Make a PR back to this repo!

### Third Party Plugins How-To

1. Clone [the third party template](https://github.com/coozila/agi-gpt-plugin-template).
1. Follow the instructions in the [third party template readme](https://github.com/coozila/agi-gpt-plugin-template).

### Migrating Third Party to First Party

We appreciate your contribution of a plugin to the project!

1. Clone this repository.
1. Make a folder for your plugin under `src/agi-gpt_plugins`. Use a simple descriptive name such as `notion`, `twitter`, or `web_ui`.
1. Add the files from your third-party plugin located at `src/agi-gpt_plugin_template` into the folder you created.
1. Include your README from your third-party plugin in the folder you created.
1. Add your plugin to the root README with a description and a link to your plugin-specific README.
1. Add your plugin's Python package requirements to `requirements.txt`.
1. Add tests to get your plugin to 80% code coverage.
1. Add your name to the [codeowners](.github/CODEOWNERS) file.
1. Add your plugin to the [Readme](README.md).
1. Submit a pull request back to this repository!

## Get Help

For more information, visit the [discord](https://discord.gg/agi-gpt) server.
