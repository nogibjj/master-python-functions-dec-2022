import functions_framework
import wikipedia
import yake

# build a function that returns the results of a wikipedia search
def wiki_search(search_term):
    search_results = wikipedia.search(search_term)
    return search_results


# build a function that returns the entire content of a wikipedia article
def wiki_content(search_term):
    content = wikipedia.page(search_term).content
    return content


# build a function that returns the top 10 keywords from a wikipedia article using Yake
def wiki_keywords(search_term):
    content = wiki_content(search_term)
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    return keywords


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function."""

    request_json = request.get_json(silent=True)

    if request_json and "name" in request_json:
        search_term = request_json["name"]
    keywords = wiki_keywords(search_term)
    return keywords
