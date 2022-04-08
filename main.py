import requests
import json
import delete_files


class Api_request:
    PATENT_URL = "https://api.patentsview.org"

    def __init__(self, country):
        """
        :param country: import country RO and HU as default parameters.
        """
        self.country = country

    def _set_response(self):
        """
        :return: getting the patent titles of the RO and HU at the desired period of time
        """
        q = json.dumps({"_and": [{"_gte": {"patent_date": "2008-01-01"}},
                                 {"_lt": {"patent_date": "2010-01-01"}},
                                 {"location_country": self.country}]})
        params = {'q': q, 'f': '["patent_title"]', 'o': '{"per_page": 300}'}
        response = requests.get(url=f"{Api_request.PATENT_URL}/locations/query", params=params).json()
        return response

    def get_patent_country(self):
        """
        :return: a list and dictionary of titles
        """
        patents = self._set_response()["locations"]
        patent_title = patents[:]
        return patent_title


class files_hanling(Api_request):
    def __init__(self, country, title, file_type):
        """
        :param country: parameter from the parent class ( RO and HU )
        :param title: this is the title of the created file
        :param file_type: this is the file extension. Could be .txt or .csv
        """
        super().__init__(country)
        self.title = title
        self.file_type = file_type

    def get_titles(self):
        """
        :return: this is the patent title
        """
        indx = 0
        for i in self.get_patent_country():
            pat = i["patents"]
            for j in pat:
                indx += 1
                x = j["patent_title"]
                self._write_files(indx, x)

    def _write_files(self, indx, x):
        """
        :param indx: this is the counter of the all patent titles. This will be stored into a file.
        :param x: this is the patent titles of the specific country patent. This will be stored into a file.
        :return: will create and write a file.
        """
        if self.file_type == "txt":
            with open(f"{self.title}.txt", "a", encoding="utf-8") as text_file:
                text_file.write(f"{indx}. {x}\n")

        elif self.file_type == "csv":
            with open(f"{self.title}.csv", "a", encoding="utf-8") as text_file:
                text_file.write(f"{indx}. {x}\n")



def main_ro():
    """
    :return: this is an object of the "files_handling" class
    """
    file_type = input("Ce tip de fisier doresti sa creezi ( txt sau csv ) ?: \n")
    title = input("Care este numele fisierului?: \n")
    new_file_ro = files_hanling("RO", title, file_type)
    new_file_ro.get_titles()
    return file_type, title


def main_hu():
    """
    :return: this is an object of the "files_handling" class
    """
    file_type = input("Ce tip de fisier doresti sa creezi ( txt sau csv ) ?: \n")
    title = input("Care este numele fisierului?: \n")
    new_file_hu = files_hanling("HU", title, file_type)
    new_file_hu.get_titles()
    return file_type, title


main_ro()
main_hu()

