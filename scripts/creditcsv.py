import json
import csv
import pprint

header = ['id', 'cast', 'crew']
with open('../data/csv/JP_CREDITS.csv', encoding='utf_8_sig', mode='w', newline="") as f_w:
    writer = csv.writer(f_w)
    w = [header]
    for year in range(2000, 2021 + 1):
        with open(f'../data/{year}/JP_CREDITS.json', encoding='utf-8', newline="") as f_r:
            json_load = json.load(f_r)
            for data in json_load['data']:
                r = []
                if "id" in data:
                    r.append(data["id"])
                else:
                    r.append(False)
                if "cast" in data:
                    r.append(len(data["cast"]))
                else:
                    r.append(False)
                if "crew" in data:
                    r.append(len(data["crew"]))
                else:
                    r.append(False)
                w.append(r)
    writer.writerows(w)
