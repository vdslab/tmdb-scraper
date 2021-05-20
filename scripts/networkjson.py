# coding: utf-8
import pprint
import json
# print([json.dumps(l) for l in csv.DictReader(open('data2.csv'))])
years = 2000
genres_data = []
json_list = {}
id_list = set()
id_name = {}
for year in range(years, 2022):
    json_open = open(
        "../data/{year}/JP_CREDITS.json".format(year=year), "r", encoding="utf-8")
    json_load = json.load(json_open)
    json_load = json_load["data"]
    # print(json_load[0]["cast"])
    for i in json_load:
        if "cast" in i and len(i["cast"]) != 0:
            allcast = []
            for j in i["cast"]:
                id_list.add(j["id"])
                id_name[j["id"]] = j["name"]
                allcast.append(j["id"])
            allcast.sort()
            for j in range(len(allcast)-1):
                if f"{allcast[j]}" not in json_list:
                    json_list[f"{allcast[j]}"] = {}
                for k in range(j+1, len(allcast)):
                    if allcast[k] in json_list[f"{allcast[j]}"]:
                        json_list[f"{allcast[j]}"][f"{allcast[k]}"] += 1
                    else:
                        json_list[f"{allcast[j]}"][f"{allcast[k]}"] = 1
id_list = sorted(list(id_list))
network_json = {"id": id_list, "id_name": id_name, "count": json_list}


with open('networkData2021.json', 'w',  encoding="utf-8_sig") as f:
    json.dump(network_json, f, ensure_ascii=False)

# JSONファイルのロード
with open('networkData2021.json', 'r',  encoding="utf-8_sig") as f:
    json_output = json.load(f)
