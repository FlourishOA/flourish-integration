import csv, requests, json

titles = ("issn", "shortname", "longname", "pub_name", "category", "year", "ai", "ai_percentile",
          "ef", "ef_percentile", "EFn", "apc", "CE")

agg_influence_requests = []
agg_price_requests = []

with open("data/journals_all.txt") as f:
    r = csv.reader(f, dialect=csv.excel_tab)
    first = next(r)
    for row in r:
        cleaned_row = [i if i != 'NULL' else None for i in row]
        raw_data = dict(zip(titles, cleaned_row))

        # adding ArticleInfluence scores
        agg_influence_requests.append({
            'issn': raw_data['issn'],
            'article_influence': raw_data['ai'],
            'est_article_influence': None,
            'year': raw_data['year']
        })


with open("data/influence_requests.json", "a") as f:
    f.write(json.dumps(agg_influence_requests))

with open("data/price_requests.json", "a") as f:
    f.write(json.dumps(agg_price_requests))
