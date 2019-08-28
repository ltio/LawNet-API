from SearchLawnet import search_case
from RetrieveLawnet import retrieve_case

def final_api(search_query):
    document_id = search_case(search_query)
    retrieve_case(document_id)

final_api("[2015] SGDC 1")
