import requests
from DeleteContentFile import stergere

Patent_url = "https://api.patentsview.org"

# payload_1 = {'q': '{"_and":[{"inventor_last_name":"Whitney"},{"_gte":{"patent_date":"2007-01-04"}},{"_lte":{'
#                   '"patent_date":"2007-12-31"}}]}'}
payload_2 = {'q': '{"location_country":"RO"}', 'f': '["patent_title"]', 'o': '{"per_page": 208}'}


def response(payload):
    response = requests.get(url=f"{Patent_url}/locations/query", params=payload)
    r = response.json()
    return r


res = response(payload_2)
patents = res["locations"]
patentTitle = patents[:]


def content():
    indx = 0
    for i in patentTitle:
        y = i["patents"]
        for j in y:
            indx += 1
            x = j["patent_title"]
            with open("patentTitles.txt", "a") as text_file:
                text_file.write(f"{indx}. {x}\n")
                text_file.seek(0)


content()
stergere()
