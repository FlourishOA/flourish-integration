import requests
import json
import csv


web_url = 'http://54.183.181.205/'
dev_url = 'http://localhost:8000/'
url = dev_url

r = requests.post(url + 'api-token-auth/',
                  data={
                      'username': 'user1',
                      'password': 'test1test2'
                  })
token = "Token " + json.loads(r.text)['token']
print token
with open("data/journal_requests.json", "r") as f:
    valid_issns = {journal['issn'] for journal in json.load(f)}

with open("data/journals_EF_AI_2014.txt", "r") as f:
    for journal in csv.reader(f, dialect=csv.excel_tab):
        if journal[1] in valid_issns:
            request_data = {"issn": journal[1], "category": journal[23]}
            csrf_request = requests.get(
                url + "api/journal/" + journal[1] + "/"
            )
            request = requests.put(
                url + "api/journal/" + journal[1] + "/",
                headers={
                    'Authorization': token,
                    'Content-Type': 'application/json',
                },
                data=json.dumps(request_data),
            )
            print request.status_code
