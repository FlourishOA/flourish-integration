import requests
import json
import csv


web_url = 'http://52.175.212.92/'
dev_url = 'http://localhost:8000/'
url = web_url

r = requests.post(url + 'api-token-auth/',
                  data={
                      'username': '',
                      'password': ''
                  })
token = "Token " + json.loads(r.text)['token']
print token
with open("data/journal_requests.json", "r") as f:
    valid_issns = {journal['issn'] for journal in json.load(f)}

with open("data/journals_EF_AI_2014.txt", "r") as f:
    client = requests.session()

    for journal in csv.reader(f, dialect=csv.excel_tab):
        if journal[1] in valid_issns and journal[23] != "NULL":
            request_data = {"issn": journal[1], "category": journal[23]}

            request = requests.put(
                url + "api/journals/" + journal[1] + "/",
                headers={
                    'Authorization': token,
                    'Content-Type': 'application/json',
                },
                data=json.dumps(request_data),
            )
            print request.status_code

