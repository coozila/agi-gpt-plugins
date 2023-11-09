from . import agi-gptWolframagi-gptSearch

plugin = agi-gptWolframagi-gptSearch()


def _wolframagi-gpt_search(query: str) -> str | list[str]:
    res = ""
    try:
        ans = plugin.api.query(query)
        res = next(ans.results).text
    except Exception as e:
        return f"'_wolframagi-gpt_search' on query: '{query}' raised exception: '{e}'"
    return res
