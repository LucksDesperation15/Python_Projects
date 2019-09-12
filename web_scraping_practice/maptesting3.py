from bs4 import BeautifulSoup
import requests
import pandas as pd

search_count = input('How many search results would you like?\n: ')

search_per_page = 32

if int(search_count) <= search_per_page:
    run_count = 1
else:
    run_count = round(int(search_count) / search_per_page)

url_list = []
for url in range(run_count):
    url2 = 'https://www.map-testing.com/map-search/'
    search_params = '?start=' + str(run_count) + '&searchOptions=AllResults'
    final_url = url2 + search_params
    url_list.append(final_url)
    run_count -= 1

url_list.reverse()

jsonData = []

for urls in url_list:

    urlh2 = requests.get(urls)
    soup = BeautifulSoup(urlh2.text, 'html.parser')
    results = soup.find_all('div', attrs= {'class' : 'search-result'})

    for row_obj in results:
        data = {}
        row = row_obj.find("div")

        #scrap Manufacturer
        manufacturer = row.find("div", string="Manufacturer")
        data['Manufacturer']  = manufacturer.find_next('div').text.strip()

        # scrap Model Name
        modelName = row.find("div", string="Model Name")
        data['Model Name'] = modelName.find_next('div').text.strip()

        # scrap Model Number
        modelNumber = row.find("div", string="Model Number")
        data['Model Number'] = modelNumber.find_next('div').text.strip()

        # scrap MaP Report No.
        maPReportNo = row.find("div", string="MaP Report No.")
        data['MaP Report No.'] = maPReportNo.find_next('div').text.strip()

        # scrap MaP Flush Score
        maPFlushScore = row.find("div", string="MaP Flush Score")
        data['MaP Flush Score'] = maPFlushScore.find_next('span').text.strip()

        # scrap Specifications
        specifications = row.find_all("li")
        data['Specifications'] = ",".join(i.text.strip() for i in specifications)

        jsonData.append(data)

df = pd.DataFrame(jsonData)
print(df)
df.to_excel('MaPTesting2.xlsx')
