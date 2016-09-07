import requests
import json


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

request_dicts = [
    {"file_path": "category_update_requests.json", "url_stub": "api/journals/"},
    #{"file_path": "influence_requests.json", "url_stub": "api/influence/"},
    #{"file_path": "price_requests.json", "url_stub": "api/prices/"},
    ]
valid_issn = set()
for rd in request_dicts:
    with open("data/" + rd['file_path'], "r") as f:
        for request_data in json.load(f):
            if rd['file_path'] == "journal_requests.json":
                valid_issn.add(request_data['issn'])
            if rd['file_path'] != "influence_requests.json" or request_data['issn'] in valid_issn:
                request = requests.put(
                    url + rd['url_stub'] + request_data['issn'] + "/",
                    headers={
                        'Authorization': token,
                        'Content-Type': 'application/json',
                    },
                    data=json.dumps(request_data),
                )
            else:
                pass
