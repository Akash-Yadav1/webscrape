import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.skysports.com/premier-league-table')
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')
# print(league_table)
n = 0
for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find(
            'td', class_='standing-table__cell standing-table__cell--name').text.strip()
        n += 1
        print(pl_team)
print(n)
