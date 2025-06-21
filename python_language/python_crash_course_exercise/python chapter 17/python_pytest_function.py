import requests

def api_request():
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+stars:>10000&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    return requests.get(url, headers=headers)