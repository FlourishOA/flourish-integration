import requests
import json
import journalscrapers

r = requests.post('http://54.183.181.205/api-token-auth/',
                  data={
                      'username': 'user1',
                      'password': 'test1test2'
                  })
token = "Token " + json.loads(r.text)['token']
print token


for i in journalscrapers. \
        ExistingScraper("data/OA_journals.tsv").\
        get_entries():
    raw_data = dict(zip(["pub", "name", "time_stamp", "is_hybrid", "issn", "apc"], i))
    request_data = {
        'issn': raw_data['issn'],
        'journal_name': raw_data['name'],
        'article_influence': None,
        'est_article_influence': '15.20000',
        'is_hybrid': raw_data['is_hybrid'],
        'category': None,
    }

    r = requests.put(
        "http://54.183.181.205/journals/" + request_data['issn']+"/",
        headers={
            'Authorization': token,
            'Content-Type': 'application/json',
        },
        data=json.dumps(request_data),
    )
    print r.text
    print r.status_code

