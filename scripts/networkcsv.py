import csv
import pprint
import json
header = ["id1", "name1", "id2", "name2", "count"]
years = 2000
with open(f'../data/csv/networkData.csv', encoding='utf_8_sig', mode='w', newline="") as f_w:
    writer = csv.writer(f_w)
    w = [header]
    with open(f'../src/networkData.json', encoding='utf-8_sig', newline="") as f_r:
        json_load = json.load(f_r)
        for row in json_load["id"]:
            if f"{row}" in json_load["count"]:
                for id_, count in json_load["count"][f"{row}"].items():
                    if count >= 0:
                        r = []
                        r.append(row)
                        r.append(json_load["id_name"][f"{row}"])
                        r.append(id_)
                        r.append(json_load["id_name"][f"{id_}"])
                        r.append(count)
                        w.append(r)
    writer.writerows(w)
