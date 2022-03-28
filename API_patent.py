import requests
import DeleteContentFile

Patent_url = "https://api.patentsview.org"

payload_1 = {'q': '{"_and":[{"inventor_last_name":"Whitney"},{"_gte":{"patent_date":"2007-01-04"}},{"_lte":{'
                  '"patent_date":"2007-12-31"}}]}'}


############# Am incercat sa obtin o variabile numai pentru nume ################################
# payload_2 = json.loads(payload_1["q"])
# payload_3 = payload_2["_and"][0]["inventor_last_name"]
# print(payload_3)
# ____________________________________________________________________________________

def response(payload):
    response = requests.get(url=f"{Patent_url}/patents/query", params=payload)
    r = response.json()
    return r


res = response(payload_1)
inv_country = res["patents"]
x = inv_country[::]

def content():
    indx = 0
    for i in x:
        indx += 1
        pat = i["patent_title"]
        # print(f"{indx}. {pat}.")
        with open("file_3.txt", "a") as text_file:
            text_file.write(f"{indx}. {pat}\n")
            text_file.seek(0)


content()
s = DeleteContentFile.text
DeleteContentFile.stergere(s)
