import requests
import json
from journalscrapers import BioMedCentralScraper, ElsevierScraper, ExistingScraper, \
    HindawiScraper, PLOSScraper, SageHybridScraper, SpringerHybridScraper, SpringerOpenScraper, \
    WileyScraper
from datetime import datetime
from add_ai import get_map


web_url = 'http://54.183.181.205/'
dev_url = 'http://localhost:8000/'

r = requests.post(dev_url + 'api-token-auth/',
                  data={
                      'username': 'user1',
                      'password': 'test1test2'
                  })
token = "Token " + json.loads(r.text)['token']
print token
count = 0

scrapers = [
    #BioMedCentralScraper("https://www.biomedcentral.com/journals"),
    #ElsevierScraper("data/elsevier/2016-uncleaned.csv"),
    ExistingScraper("data/OA_journals.tsv"),
    #HindawiScraper("http://www.hindawi.com/apc/"),
    #PLOSScraper("https://www.plos.org/publication-fees"),
    #SageHybridScraper(""),
    #SpringerHybridScraper("data/springer/2016+Springer+Journals+List.csv"),
    #SpringerOpenScraper("http://www.springeropen.com/journals"),
    #WileyScraper("http://olabout.wiley.com/WileyCDA/Section/id-828038.html")
]

ai_map = get_map()

for scraper in scrapers:
    try:
        for i in scraper.get_entries():
            raw_data = dict(zip(["pub", "name", "time_stamp", "is_hybrid", "issn", "apc"], i))
            if raw_data['issn'] in ai_map:
                ai = float(ai_map[raw_data['issn']])
            else:
                ai = None

            journal_request_data = {
                'issn': raw_data['issn'],
                'journal_name': raw_data['name'],
                'pub_name': raw_data['pub'],
                'article_influence': ai,
                'est_article_influence': None,
                'is_hybrid': raw_data['is_hybrid'],
                'category': None,
            }
            # adding information to the journal endpoint
            print journal_request_data['article_influence']

            journal_request = requests.put(
                dev_url + "api/journals/" + journal_request_data['issn']+"/",
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
                dev_url + "api/prices/" + price_request_data['issn']+"/",
                headers={
                    'Authorization': token,
                    'Content-Type': 'application/json',
                },
                data=json.dumps(price_request_data),
            )
            print journal_request.status_code
            print journal_request_data
            print price_request_data
            print "Price: " + str(price_request.status_code)

    except StopIteration:
        print str(scraper) + " isn't implemented yet."

