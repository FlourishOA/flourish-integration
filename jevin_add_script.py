import requests
import json
from journalscrapers import WileyScraper
scraper = WileyScraper("http://olabout.wiley.com/WileyCDA/Section/id-828038.html")

r = requests.post('http://54.183.181.205/api-token-auth/',
                  data={
                      'username': 'user1',
                      'password': 'test1test2'
                  })
token = "Token " + json.loads(r.text)['token']
print token

for i in scraper.get_entries():
    raw_data = dict(zip(["pub", "name", "time_stamp", "is_hybrid", "issn", "apc"], i))
    journal_request_data = {
        'issn': raw_data['issn'],
        'journal_name': raw_data['name'],
        'pub_name': raw_data['pub'],
        'article_influence': None,
        'est_article_influence': None,
        'is_hybrid': raw_data['is_hybrid'],
        'category': None,
    }

    # adding information to the journal endpoint
    journal_request = requests.put(
        "http://54.183.181.205/journals/" + journal_request_data['issn'] + "/",
        headers={
            'Authorization': token,
            'Content-Type': 'application/json',
        },
        data=json.dumps(journal_request_data),
    )

    price_request_data = {
        'issn': raw_data['issn'],
        'price': raw_data['apc'],
        'time_stamp': raw_data['time_stamp']
    }

    price_request = requests.put(
        "http://54.183.181.205/prices/" + price_request_data['issn'] + "/",
        headers={
            'Authorization': token,
            'Content-Type': 'application/json',
        },
        data=json.dumps(price_request_data),
    )

    print str(journal_request_data['journal_name']) + ": (status code) " + str(journal_request.status_code)
    print "\t" + "Price status code: " + str(price_request.status_code)
