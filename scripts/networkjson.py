# coding: utf-8
import pprint
import json
years = 2000
count_dict = {}
id_list = set()
id_name_dict = {}
for year in range(years, 2021+1):
    json_open = open(
        "../data/{year}/JP_CREDITS.json".format(year=year), "r", encoding="utf-8")
    json_load = json.load(json_open)
    json_load = json_load["data"]
    for json_about in json_load:
        if "cast" in json_about and len(json_about["cast"]) != 0:
            allcast = []
            for json_cast in json_about["cast"]:
                id_list.add(json_cast["id"])
                id_name_dict[json_cast["id"]] = json_cast["name"]
                allcast.append(json_cast["id"])
            allcast.sort()
            for i in range(len(allcast)-1):  # ここらへん添え字だから許して
                if f"{allcast[i]}" not in count_dict:
                    count_dict[f"{allcast[i]}"] = {}
                for j in range(i+1, len(allcast)):
                    if f"{allcast[j]}" in count_dict[f"{allcast[i]}"]:
                        count_dict[f"{allcast[i]}"][f"{allcast[j]}"] += 1
                    else:
                        count_dict[f"{allcast[i]}"][f"{allcast[j]}"] = 1
id_list = sorted(list(id_list))
network_json = {"id": id_list, "id_name": id_name_dict, "count": count_dict}


with open('networkData.json', 'w',  encoding="utf-8_sig") as f:
    json.dump(network_json, f, ensure_ascii=False)

# JSONファイルのロード
with open('networkData.json', 'r',  encoding="utf-8_sig") as f:
    json_output = json.load(f)
