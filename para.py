from bs4 import BeautifulSoup
import requests

shortcut_url = "https://helpx.adobe.com/indesign/using/default-keyboard-shortcuts.html"
page = requests.get(shortcut_url)
soup = BeautifulSoup(page.text, 'html.parser')
sections = soup.select('.table.parbase.section')
yml = open('AfterEffects.yml', 'w+')

for section in sections:
  trs = section.find_all('tr');

  for row in trs:
    row_array = row.find_all('td')
    if len(row_array) == 3:
      yml.write('  - "{0}": "{1}"\n'.format(row_array[0].getText().replace('\n', ''), row_array[-1].getText().replace('\n', '')))