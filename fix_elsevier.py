from journalscrapers import ElsevierScraper
import requests
import json

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
scraper = ElsevierScraper("data/elsevier/2016-uncleaned.csv")

agg_journal_requests = []
agg_price_requests = []
try:
    for i in scraper.get_entries():
        raw_data = dict(zip(["pub", "name", "date_stamp", "is_hybrid", "issn", "apc"], i))

        request_data = {
            'issn': raw_data['issn'],
            'price': raw_data['apc'],
            'date_stamp': raw_data['date_stamp'],
        }
        request = requests.put(
            url + "api/prices/" + request_data['issn'] + "/",
            headers={
                'Authorization': token,
                'Content-Type': 'application/json',
            },
            data=json.dumps(request_data),
        )
        print request.status_code
except StopIteration:
    print str(scraper) + " isn't implemented yet."

