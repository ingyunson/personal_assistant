from lib.google_search_results import GoogleSearchResults
#library from https://github.com/serpapi/google-search-results-python

query = input()

params = {
    "playground": "true",
    "q": "google",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": "demo",
}

engine_query = GoogleSearchResults(params)
dictionary_results = engine_query.get_dictionary()
print(dictionary_results)