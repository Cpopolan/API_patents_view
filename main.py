import requests
import json


class Api_request:
    PATENT_URL = "https://api.patentsview.org"

    def __init__(self, country):
        """
        Constructor for the 'country' param .
        :param country: import country with abbreviation RO and HU as default parameters.
        """
        self.country = country

    def _set_response(self):
        """
        Receiving the response in .json format.
        :return: getting the patent titles of the RO and HU at the desired period of time
        """
        q = json.dumps({"_and": [{"_gte": {"patent_date": "2000-01-01"}},
                                 {"_lt": {"patent_date": "2010-01-01"}},
                                 {"location_country": self.country}]})
        params = {'q': q, 'f': '["patent_title"]', 'o': '{"per_page": 300}'}
        response = requests.get(url=f"{Api_request.PATENT_URL}/locations/query", params=params).json()
        return response

    def get_patent_country(self):
        """
        Extracting the patent titles from .json format.
        :return: a list and dictionary of the patenet titles
        """
        patents = self._set_response()["locations"]
        patent_title = patents[:]
        return patent_title


class files_hanling(Api_request):
    def __init__(self, country, title, file_type):
        """
        Constructor for the params.
        :param country: parameter from the parent class ( RO and HU )
        :param title: this is the title of the created file
        :param file_type: this is the file extension. Could be .txt or .csv
        """
        super().__init__(country)
        self.title = title
        self.file_type = file_type

    def get_titles(self):
        indx = 0
        for i in self.get_patent_country():
            pat = i["patents"]
            for j in pat:
                indx += 1
                x = j["patent_title"]
                self._write_files(indx, x)

    def _write_files(self, indx, x):
        """
        Creating the files in two formats.
        :param indx: this is the counter of the all patent titles. This will be stored into a file.
        :param x: this is the patent titles of the specific country patent. This will be stored into a file.
        :return: will create and write a file.
        """
        if self.file_type == "txt":
            with open(f"{self.title}.txt", "a", encoding="utf-8", errors="ignore") as text_file:
                text_file.write(f"{indx}. {x}\n")

        elif self.file_type == "csv":
            with open(f"{self.title}.csv", "a", encoding="utf-8", errors="ignore") as text_file:
                text_file.write(f"{indx}. {x}\n")


def main_ro():
    """
    :return: this is an object of the "files_handling" class
    """
    file_type = input("Ce tip de fisier doresti sa creezi pentru Romania ( txt sau csv ) ?: \n")
    if file_type == "txt" or file_type == "csv":
        title = input("Care este numele fisierului?: \n")
    else:
        print("Nu ai ales una din cele 2 formate recomandate.\nLa revedere!")
        exit()
    new_file_ro = files_hanling("RO", title, file_type)
    new_file_ro.get_titles()


def main_hu():
    """
    :return: this is an object of the "files_handling" class
    """
    file_type = input("Ce tip de fisier doresti sa creezi pentru Ungaria ( txt sau csv ) ?: \n")
    if file_type == "txt" or file_type == "csv":
        title = input("Care este numele fisierului?: \n")
    else:
        print("Nu ai ales una din cele 2 formate recomandate.\nLa revedere!")
        exit()
    new_file_hu = files_hanling("HU", title, file_type)
    new_file_hu.get_titles()


start_project = input("Cate tari doresti sa afisezi si sa creezi fisiere? ( 1 sau 2): \n")
if start_project == "1":
    main_ro()
elif start_project == "2":
    main_ro()
    main_hu()
else:
    print(" Nu ai ales nici o tara.\nLa revedere!")
