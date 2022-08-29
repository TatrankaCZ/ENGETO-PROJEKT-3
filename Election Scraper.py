import requests
from bs4 import BeautifulSoup
import csv
import argparse

def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("table", class_="table")
    return results

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("file")
args = parser.parse_args()

results = get_html(args.url)

print("Stahuji data z odkazu...")

with open(args.file, "w", encoding="utf8", newline="") as f:
    file_ = csv.writer(f)
    header = ["Code", 
              "Location", 
              "Registered", 
              "envelopes", 
              "valid", 
              "Občanská Demokratická Strana", 
              "Řád Národa Vlastenecká Unie", 
              "CESTA", 
              "Česká Strana Sociálně Demokratická", 
              "Pravý Bok", 
              "Radostné Česko", 
              "Starostové a Nezávislí", 
              "Komunistická Strana Čech a Moravy", 
              "Zelení", 
              "Rozumní", 
              "Společ.proti výst.v Prok.údolí", 
              "Svobodní", 
              "Blok Proti Islamizaci", 
              "Občanská Demokratická Aliance", 
              "Piráti", 
              "OBČANÉ 2011", 
              "Unie H.A.V.E.L.",
              "Česká Národní Fronta",
              "Referendum o EU",
              "TOP 09",
              "ANO",
              "Dobrá Volba 2016",
              "Republikánská Strana Československa Miroslava Sládka",
              "Křesťanská a Demokratická Unie - Československá Strana Lidová",
              "Česká Strana Národně Sociální",
              "Realisté",
              "SPORTOVCI",
              "Dělnické Strany Sociální Spravedlnosti",
              "Svoboda a Přímá Demokracie",
              "Strana Práv Občanů",
              "Národ Sobě"]
    file_.writerow(header)
    for result in results:
        codes = result.find_all("td", class_="cislo")
        locations = result.find_all("td", class_="overflow_name")

        for x in range(len(codes)):
            code = codes[x].text
            location = locations[x].text
            second_page = str(codes[x]).split("\"")[5].replace("amp;", "")
            url = "https://volby.cz/pls/ps2017nss/" + str(second_page)
            html_new = get_html(url)
            registration = html_new[0].find("td", headers="sa2").text.replace("\xa0", "")
            envelopes = html_new[0].find("td", headers="sa3").text.replace("\xa0", "")
            valid = html_new[0].find("td", headers="sa6").text.replace("\xa0", "")
            sides = {
                1:"0",
                2:"0",
                3:"0",
                4:"0",
                5:"0",
                6:"0",
                7:"0",
                8:"0",
                9:"0",
                10:"0",
                11:"0",
                12:"0",
                13:"0",
                14:"0",
                15:"0",
                16:"0",
                17:"0",
                18:"0",
                19:"0",
                20:"0",
                21:"0",
                22:"0",
                23:"0",
                24:"0",
                25:"0",
                26:"0",
                27:"0",
                28:"0",
                29:"0",
                30:"0",
                31:"0"
            }
            for tables in html_new:
                side_ids = tables.find_all("td", headers="t1sa1 t1sb1")
                side_votes = tables.find_all("td", headers="t1sa2 t1sb3")
                for y in range(len(side_ids)):
                    sides[int(side_ids[y].text)] = side_votes[y].text.replace("\xa0", "")
                side_ids = tables.find_all("td", headers="t2sa1 t2sb1")
                side_votes = tables.find_all("td", headers="t2sa2 t2sb3")
                for y in range(len(side_ids)):
                    sides[int(side_ids[y].text)] = side_votes[y].text.replace("\xa0", "")
            data = [code,
                    location,
                    registration,
                    envelopes,
                    valid,
                    sides[1],
                    sides[2],
                    sides[3],
                    sides[4],
                    sides[5], 
                    sides[6], 
                    sides[7], 
                    sides[8], 
                    sides[9], 
                    sides[10], 
                    sides[11], 
                    sides[12], 
                    sides[13], 
                    sides[14], 
                    sides[15], 
                    sides[16], 
                    sides[17], 
                    sides[18], 
                    sides[19], 
                    sides[20], 
                    sides[21], 
                    sides[22], 
                    sides[23], 
                    sides[24], 
                    sides[25], 
                    sides[26], 
                    sides[27], 
                    sides[28], 
                    sides[29], 
                    sides[30], 
                    sides[31]]
            file_.writerow(data)

print("Hotovo")