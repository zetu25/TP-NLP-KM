import requests
import wikipedia
from scripts import *
import json


S = requests.Session()

# Nous utilisons l'API de Wikipedia qui pour un mot donnée
# retourne la liste des liens d'articles qui peuvent correspondre au mot
def get_search_result(term,synonym_number):
    search_results = {}
    URL = "https://fr.wikipedia.org/w/api.php"
    synonyms = return_most_n_similar(term, synonym_number)
    # Cette boucle nous permet, pour chaque mot similaire à notre mot de requete
    # de retourner les liens des articles leurs correspondant.
    for terms in synonyms:
        PARAMS = {
            "action": "opensearch",
            "search": terms,
            "format": "json",
            "origin": "*",
            "limit":"5"
        }
        R = S.get(url=URL, params=PARAMS)
        search_results[R.json()[0]] = [requests.utils.unquote(link) for link in R.json()[3]]
    return search_results


if __name__ == "__main__":
    res = get_search_result("Apple", 5)
    json_formatted_str = json.dumps(res, indent=2, ensure_ascii=False)
    print(json_formatted_str)
