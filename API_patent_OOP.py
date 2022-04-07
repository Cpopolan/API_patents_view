import json
import requests
from DeleteContentFile import stergere
from get_file_type import write_to_file


class Api:
    PATENT_URL = "https://api.patentsview.org"

    def __init__(self, country):
        self.country = country

    def get_patents_country(self):
        q = json.dumps({"location_country": self.country})
        params = {'q': q, 'f': '["patent_title"]', 'o': '{"per_page": 300}'}
        response = requests.get(url=f"{Api.PATENT_URL}/locations/query", params=params).json()
        patents = response["locations"]
        patent_title = patents[:]
        return patent_title

    def get_content(self):

        indx = 0
        for i in self.get_patents_country():
            pat = i["patents"]
            for j in pat:
                indx += 1
                x = j["patent_title"]


api_obj = Api("RO")
api_obj.get_content()
write_to_file()
stergere()
