from journalscrapers import BioMedCentralScraper, ElsevierScraper, ExistingScraper, \
    HindawiScraper, PLOSScraper, SageHybridScraper, SpringerHybridScraper, SpringerOpenScraper, \
    WileyScraper

import json

scrapers = [
    BioMedCentralScraper("https://www.biomedcentral.com/journals"),
    ElsevierScraper("data/elsevier/2016-uncleaned.csv"),
    ExistingScraper("data/OA_journals.tsv"),
    HindawiScraper("http://www.hindawi.com/apc/"),
    PLOSScraper("https://www.plos.org/publication-fees"),
    SageHybridScraper(""),
    SpringerHybridScraper("data/springer/2016+Springer+Journals+List.csv"),
    SpringerOpenScraper("http://www.springeropen.com/journals"),
    WileyScraper("http://olabout.wiley.com/WileyCDA/Section/id-828038.html")
]

agg_journal_requests = []
agg_price_requests = []
for scraper in scrapers:
    try:
        for i in scraper.get_entries():
            raw_data = dict(zip(["pub", "name", "date_stamp", "is_hybrid", "issn", "apc"], i))
            print raw_data
            agg_journal_requests.append({
                'issn': raw_data['issn'],
                'journal_name': raw_data['name'],
                'pub_name': raw_data['pub'],
                'is_hybrid': raw_data['is_hybrid'],
                'category': None,
            })

            agg_price_requests.append({
                'issn': raw_data['issn'],
                'price': raw_data['apc'],
                'date_stamp': raw_data['date_stamp'],
            })
    except StopIteration:
        print str(scraper) + " isn't implemented yet."


with open("data/journal_requests.json", "a+") as f:
    f.write(json.dumps(agg_journal_requests))

with open("data/price_requests.json", "r") as f:
    pl = json.load(f)

with open("data/price_requests.json", "w") as f:
    f.write(json.dumps(pl + agg_price_requests))
