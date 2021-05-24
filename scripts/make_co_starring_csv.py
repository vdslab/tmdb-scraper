import json
import csv

year_from = 2000
year_to = 2021

threshold = 1

count = {}
name_id_map = {}
header = ['id_1', 'name_1', 'id_2', 'name_2', 'count']
write_data = [header]

for year in range(year_from, year_to + 1):
    with open(f'../data/{year}/JP_CREDITS.json', encoding='utf-8', mode='r') as f_r:
        json_load = json.load(f_r)

        for row in json_load['data']:
            if 'cast' in row:
                row['cast'].sort(key=lambda x: x['id'])

                for i_f, c_f in enumerate(row['cast']):
                    name_id_map[c_f['id']] = c_f['name']
                    if c_f['id'] not in count:
                        count[c_f['id']] = {}

                    for c_t in row['cast'][i_f+1:]:
                        if c_t['id'] in count[c_f['id']]:
                            count[c_f['id']][c_t['id']] += 1
                        else:
                            count[c_f['id']][c_t['id']] = 1

for i_f in name_id_map:
    for i_t in count[i_f]:
        if count[i_f][i_t] > threshold:
            write_data.append([i_f, name_id_map[i_f],  i_t,
                               name_id_map[i_t], count[i_f][i_t]])

with open(f'../data/csv/CO-STARRING_gt{threshold}.csv', encoding='utf_8_sig', mode='w') as f_w:
    writer = csv.writer(f_w)
    writer.writerows(write_data)
