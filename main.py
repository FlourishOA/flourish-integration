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
    #{"file_path": "journal_requests.json", "url_stub": "api/journals/"},
    #{"file_path": "influence_requests.json", "url_stub": "api/influence/"},
    {"file_path": "price_requests.json", "url_stub": "api/prices/"},
    ]
for rd in request_dicts:
    with open("data/" + rd['file_path'], "r") as f:
        for request_data in json.load(f):
            print request_data

            request = requests.put(
                url + rd['url_stub'] + request_data['issn'] + "/",
                headers={
                    'Authorization': token,
                    'Content-Type': 'application/json',
                },
                data=json.dumps(request_data),
            )
            print "\tEndpoint: " + str(rd['url_stub'])
            print "\tStatus: " + str(request.status_code)
