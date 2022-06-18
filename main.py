import requests
import re
from bs4 import BeautifulSoup

teamUrls = [
    "https://www.procyclingstats.com/team/ag2r-citroen-team-2022",
    "https://www.procyclingstats.com/team/astana-qazaqstan-team-2022",
    "https://www.procyclingstats.com/team/bora-hansgrohe-2022",
    "https://www.procyclingstats.com/team/cofidis-2022",
    "https://www.procyclingstats.com/team/bahrain-victorious-2022",
    "https://www.procyclingstats.com/team/ef-education-easypost-2022",
    "https://www.procyclingstats.com/team/groupama-fdj-2022",
    "https://www.procyclingstats.com/team/ineos-grenadiers-2022",
    "https://www.procyclingstats.com/team/intermarche-wanty-gobert-materiaux-2022",
    "https://www.procyclingstats.com/team/israel-premier-tech-2022",
    "https://www.procyclingstats.com/team/team-jumbo-visma-2022",
    "https://www.procyclingstats.com/team/lotto-soudal-2022",
    "https://www.procyclingstats.com/team/movistar-team-2022",
    "https://www.procyclingstats.com/team/quick-step-alpha-vinyl-2022",
    "https://www.procyclingstats.com/team/team-bikeexchange-jayco-2022",
    "https://www.procyclingstats.com/team/team-dsm-2022",
    "https://www.procyclingstats.com/team/trek-segafredo-2022",
    "https://www.procyclingstats.com/team/uae-team-emirates-2022",
]

URL = teamUrls[0]
page = requests.get(URL)

bSoup = BeautifulSoup(page.content, "html.parser")

riders = bSoup.find_all('a', href=re.compile("rider/"))

extracted_riders = []

i = 0
while i < len(riders):
    print(riders[i].get('href').replace("rider/", ""))
    extracted_riders.append(riders[i].get('href').replace("rider/", ""))
    i = i+1
rider_dictionary = list(dict.fromkeys(sorted(extracted_riders)))


print(len(rider_dictionary))
with open('UAE Team Emirates', 'w') as data:
    data.write(str(rider_dictionary))

print(rider_dictionary)
