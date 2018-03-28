from bs4 import BeautifulSoup
import requests

shortcut_url = "https://support.office.com/en-us/article/Keyboard-shortcuts-in-PowerPoint-2016-for-Mac-F25F92B3-B0A8-4C60-AEC8-954B72AA81AD"
page = requests.get(shortcut_url)
soup = BeautifulSoup(page.text, 'html.parser')
sections = soup.select('table')
command_images = soup.select('img[alt="COMMAND"]')
yml = open('PowerPoint.yml', 'w+')

print(len(command_images))

for img in command_images:
  img.replaceWith('Cmd')

for section in sections:
  trs = section.find_all('tr');

  for tds in trs:
    tds_array = tds.find_all('td')
    if len(tds_array) == 2:
      shortcut_commands = tds_array[1].getText().replace('\r', '').replace('\n', '').strip().rstrip().replace('SHIFT', 'Shift').replace('CONTROL', 'Ctrl').replace('OPTION', 'Opt')
      shortcut_name = tds_array[0].getText().replace('\n', '').replace('.', '')
      # shortcut_commands = tds_array[1].getText().replace('\n', '').strip()#.replace('-', ' + ').replace('–', ' + ').replace('command', 'Cmd').replace('+', ' + ')
      yml.write('  - "{0}": "{1}"\n'.format(shortcut_name, shortcut_commands))