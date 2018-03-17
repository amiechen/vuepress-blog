from bs4 import BeautifulSoup
import requests

shortcut_url = "https://helpx.adobe.com/photoshop/using/default-keyboard-shortcuts.html"
page = requests.get(shortcut_url)
soup = BeautifulSoup(page.text, 'html.parser')
sections = soup.select('.filter-content.section')
yml = open('Photoshop.yml', 'w+')

for section in sections:
  header = section.select('.header.first-header.header-top')
  headerText = header[0].getText().strip().replace('\n', ' ').replace('\r', ' ')
  trs = section.find_all('tr');

  yml.write('{0}: \n'.format(headerText))
  for row in trs:
    row_array = row.find_all('td')
    if len(row_array) == 3:
      yml.write('  - "{0}": "{1}"\n'.format(row_array[0].getText().replace('\n', ''), row_array[-1].getText().replace('\n', '')))