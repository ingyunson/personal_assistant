from lib.google_search_results import GoogleSearchResults
#library from https://github.com/serpapi/google-search-results-python

params = {
    "q" : "Coffee", #Search Keyword
    "location" : "Seoul, South Korea",
    "hl" : "en",
    "gl" : "us",
    "google_domain" : "google.com",
    "api_key" : "demo",
    "num" : "10"
}

query = GoogleSearchResults(params)
dictionary_results = query.get_dictionary()
print(dictionary_results)