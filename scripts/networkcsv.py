import csv
import pprint
import json
header = ["id1", "name1", "id2", "name2", "count"]
years = 2000
with open('../data/csv/networkData_1.csv', encoding='utf_8_sig', mode='w', newline="") as f_w1:
    writer1 = csv.writer(f_w1)
    w_1 = [header]
    with open('../data/csv/networkData_2~.csv', encoding='utf_8_sig', mode='w', newline="") as f_w2:
        writer2 = csv.writer(f_w2)
        w_2 = [header]
        with open('../scripts/networkData.json', encoding='utf-8_sig', newline="") as f_r:
            json_load = json.load(f_r)
            for row in json_load["id"]:
                if f"{row}" in json_load["count"]:
                    for id_, count in json_load["count"][f"{row}"].items():
                        if count < 2:
                            r = []
                            r.append(row)
                            r.append(json_load["id_name"][f"{row}"])
                            r.append(id_)
                            r.append(json_load["id_name"][f"{id_}"])
                            r.append(count)
                            w_1.append(r)
                        else:
                            r = []
                            r.append(row)
                            r.append(json_load["id_name"][f"{row}"])
                            r.append(id_)
                            r.append(json_load["id_name"][f"{id_}"])
                            r.append(count)
                            w_2.append(r)
        writer2.writerows(w_2)

    writer1.writerows(w_1)
