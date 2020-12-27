import csv
import json
import sys, os
from bs4 import BeautifulSoup

if __name__ == '__main__':

    csv_file = sys.argv[1]
    results = []

    with open(csv_file, "r") as f:

        reader = csv.DictReader(f)

        for row in reader:
            results.append(row)

    results = json.dumps(results, ensure_ascii=False)


    #  處理html

    with open("index.html", "r") as f:
        soup = BeautifulSoup(f, 'html.parser')
        script = soup.find('script', id='song_data')
        new_tag = soup.new_tag("script", id='song_data')
        new_tag.string = f"let song_data = {results}"
        
        if script:
            script.insert_after(new_tag)
            script.extract()

        else:
            script = soup.script
            script.insert_before(new_tag)

        

        with open("index2.html", "w") as file:
            file.write(str(soup))


    os.remove("index.html")
    os.rename("index2.html", "index.html")