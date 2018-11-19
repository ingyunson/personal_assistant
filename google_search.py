from lib.google_search_results import GoogleSearchResults
#library from https://github.com/serpapi/google-search-results-python

def search(keyword):
    query = keyword

    params = {
        "playground": "true",
        "q": query,
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": "demo",
    }

    engine_query = GoogleSearchResults(params)
    dictionary_results = engine_query.get_dictionary()
    return dictionary_results