import json
import csv
import pprint

header = sorted(['adult', 'backdrop_path',
                 'belongs_to_collection',  # dict
                 'budget',
                 'genres',  # array
                 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path',
                 'production_companies', 'production_countries',  # array
                 'release_date', 'revenue', 'runtime',
                 'spoken_languages',  # array
                 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'])

with open('../data/csv/JP_DETAILS_REVENUE.csv', encoding='utf_8_sig', mode='w', newline="") as f_w:
    writer = csv.writer(f_w)
    w = [header]
    # writer.writerow(header)
    for year in range(2000, 2021 + 1):
        with open(f'../data/{year}/JP_DETAILS.json', encoding='utf-8') as f_r:
            json_load = json.load(f_r)

            for row in json_load['data']:
                r = []
                if "revenue" in row and row["revenue"] != 0:
                    for h in header:
                        if h in row:
                            r.append(row[h])
                    w.append(r)
                # writer.writerow(r)
    writer.writerows(w)
