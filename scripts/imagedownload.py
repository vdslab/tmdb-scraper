from urllib import request
# 画像のアドレス
import csv
number = 0
API_ENDPOINT = 'https://image.tmdb.org/t/p/w500'
with open('../data/csv/JP_DETAILS_REVENUE_FILTER.csv', encoding='utf_8_sig', mode='r') as f:
    dataReader = csv.reader(f)
    for row in dataReader:
        # ここは最初にposter_pathの題名が入っているせいで書いためんどいから汚い条件式だけど言ったゆるして☺
        if number <= 1473 or row[12] == "":
            number += 1
            continue
        
        URL2 = API_ENDPOINT+row[12]  # 12番目に
        URL = f"https://image.tmdb.org/t/p/w500/{row[12]}"
        request.urlretrieve(URL2, f"../data/image/image{number}.jpg")
        number += 1
