# Material Design icons for Stream Deck

from os import path, mkdir
from json import loads 
from iconObject import iconObject
import requests

# Create Folders (I know its messy)
if not path.exists('png'):
    mkdir('png')
if not path.exists('png/temp'):
    mkdir('png/temp')
if not path.exists('png/temp/white'):
    mkdir('png/temp/white')
if not path.exists('png/temp/black'):
    mkdir('png/temp/black')
if not path.exists('png/white'):
    mkdir('png/white')
if not path.exists('png/black'):
    mkdir('png/black')

while True:
    if not path.exists('png/baseicon.png'):
        input('Could not find a base icon image. Please put the base icon at data/baseicon.png then press enter.')

    else:
        break

print('Grabbing icon list from Google Material Design Icons Repo')
iconList = requests.get('https://github.com/google/material-design-icons/raw/master/update/current_versions.json', allow_redirects=True)
iconListJSON = loads(iconList.content)

print('Creating icon objects')
iconList = {}
for icon in iconListJSON.keys():
    iconCategory = icon.split('::')[0]
    iconName = icon.split('::')[1]
    if not path.exists('png/temp/white/' + iconCategory):
        mkdir('png/temp/white/' + iconCategory)
        # mkdir('png/temp/black/' + iconCategory)
        mkdir('png/white/' + iconCategory)
        mkdir('png/black/' + iconCategory)

    iconList[iconName] = iconObject(iconName, iconCategory)

iconCount = len(iconList.items())


print('Downloading all icons. This WILL take a while')
currentIcon = 1
for icon in iconList.items():
    print(f'{currentIcon}/{iconCount} Downloaded', end='\r')
    icon[1].download()
    currentIcon += 1
print(f'Downloaded {iconCount} icons               ')

print('Converting icons...')
currentIcon = 1
for icon in iconList.items():
    print(f'{currentIcon}/{iconCount} Processed', end='\r')
    icon[1].process()
    currentIcon += 1