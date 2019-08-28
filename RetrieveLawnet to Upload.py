import requests
import xml.etree.ElementTree as ET
import csv

api_url_base = "https://test-legalresearch.api.sal.sg/v1-content/content"

def retrieve_case(doc_id):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cache-control': 'no-cache',
        'x-api-key': 'apikey',
    }
    data = {
      'apikey': 'apikey',
      'cats': 'r1',
      'l2cats': 'r1c1',
      'l3cats': '#r1c1',
      'docUrl': doc_id
    }
    search_data = requests.post(api_url_base, headers=headers, data=data).content
    with open("trial.xml", "wb") as f:
        f.write(search_data)
    return


# /Judgment/16826-SSP.xml - contains binary data in the XML file
