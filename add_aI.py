import csv

def get_map():
    ai_map = {}
    with open("data/journals_EF_AI_2014.txt") as f:
        r = csv.reader(f, dialect=csv.excel_tab)
        first = next(r)
        for row in r:
            ai_map[row[1]] = row[15]
    return ai_map


