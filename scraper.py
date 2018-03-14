from bs4 import BeautifulSoup
import requests

shortcut_url = "https://helpx.adobe.com/illustrator/using/default-keyboard-shortcuts.html"

page = requests.get(shortcut_url)
soup = BeautifulSoup(page.text, 'html.parser')
trs = soup.find_all('tr');

for row in trs:
  row_array = row.find_all('td')
  if len(row_array) == 3:
    print ("{0}: {1}".format(row_array[0].getText().replace('\n', ' '), row_array[-1].getText().replace('\n', ' ')))
