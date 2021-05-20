import json
import csv
import pprint

header = sorted(['adult', 'backdrop_path',
                 # 'belongs_to_collection',
                 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path',
                 #  'production_companies', 'production_countries',
                 'release_date', 'revenue', 'runtime',
                 #  'spoken_languages',
                 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'])

with open('../data/csv/JP_DETAILS.csv', encoding='utf-8', mode='a') as f_w:
    writer = csv.writer(f_w)
    writer.writerow(header)
    for year in range(2000, 2021 + 1):
        with open(f'../data/{year}/JP_DETAILS.json', encoding='utf-8') as f_r:
            json_load = json.load(f_r)

            for row in json_load['data']:
                r = []
                for h in header:
                    if h in row:
                        r.append(row[h])
                    else:
                        r.append(None)
                writer.writerow(r)
