import requests
import json


web_url = 'http://52.175.212.92/'
dev_url = 'http://localhost:8000/'
url = web_url

r = requests.post(url + 'api-token-auth/',
                  data={
                      'username': '***REMOVED***',
                      'password': '***REMOVED***'
                  })
token = "Token " + json.loads(r.text)['token']
print token

request_dicts = [
    #{"file_path": "category_update_requests.json", "url_stub": "api/journals/"},
    #{"file_path": "journal_requests.json", "url_stub": "api/journals/"},
    #{"file_path": "influence_requests.json", "url_stub": "api/influence/"},
    {"file_path": "price_requests.json", "url_stub": "api/prices/"},
    ]
valid_issn = set()
for rd in request_dicts:
    with open("data/" + rd['file_path'], "r") as f:
        for request_data in json.load(f):
            if rd['file_path'] == "journal_requests.json":
                valid_issn.add(request_data['issn'])
            #elif request_data['issn'] in valid_issn:
            if rd['file_path'] != "influence_requests.json" or request_data['issn'] in valid_issn:
                #and rd['file_path'] != "journal_requests.json":
                request = requests.put(
                    url + rd['url_stub'] + request_data['issn'] + "/",
                    headers={
                        'Authorization': token,
                        'Content-Type': 'application/json',
                    },
                    data=json.dumps(request_data),
                )
                print request_data
                print request.status_code
            else:
                pass
