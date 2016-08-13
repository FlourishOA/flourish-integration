from journalscrapers import BioMedCentralScraper, ElsevierScraper, ExistingScraper, \
    HindawiScraper, PLOSScraper, SageHybridScraper, SpringerHybridScraper, SpringerOpenScraper, \
    WileyScraper

import json
import csv

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

with open("OA_journal_prices_2016.csv", "w") as f:
    for scraper in scrapers:
        writer = csv.writer(f)
        writer.writerow(["publisher_name", "journal_name", "date_stamp", "is_hybrid", "issn", "apc"])
        try:
            for i in scraper.get_entries():
                writer.writerow([j.encode('utf8') if type(j) != bool else j for j in i])
        except StopIteration:
            print str(scraper) + " isn't implemented yet."



