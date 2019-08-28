import requests
import xml.etree.ElementTree as ET

api_url_base = "https://test-legalresearch.api.sal.sg/v1-search/search"

def search_case(search_term):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cache-control': 'no-cache',
        'x-api-key': 'apikey',
        'orderBy': 'relevance'
    }
    data = {
      'apikey': 'apikey',
      'cats': 'r1',
      'l2cats': 'r1c1',
      'l3cats': '#r1c1',
      'searchTerm': search_term,
      'orderBy': 'relevance',
      'maxperpage': 20
    }
    search_data = requests.post(api_url_base, headers=headers, data=data)
    mytree = ET.fromstring(search_data.content)
    #retrieve the first result on the basis that that is the correct result
    DocID = mytree[1][0][0][0].text
    return str(DocID)
