import requests
from os import system, path

class iconObject():
    def __init__(self, name, catagory):
        self.name = name
        self.catagory = catagory
        self.url = f'https://github.com/google/material-design-icons/raw/master/png/{catagory}/{name}/materialicons/48dp/1x/baseline_{name}_black_48dp.png'

    def download(self):
        if not path.exists(f'png/temp/black/{self.catagory}/{self.name}.png'):
            downloadRequest = requests.get(self.url, allow_redirects=True)
            open(f'png/temp/black/{self.catagory}/{self.name}.png', 'wb').write(downloadRequest.content)

    def process(self):
        # Create White Variant
        system(f'ffmpeg -y -i png/baseicon.png -i png/temp/black/{self.catagory}/{self.name}.png -filter_complex "[0:v][1:v] overlay=48:48:enable=\'between(t,0,20)\'" -pix_fmt yuv420p -c:a copy png/black/{self.catagory}/{self.name}.png')

        # Create Black Variant
        system(f'ffmpeg -y -i png/black/{self.catagory}/{self.name}.png -vf negate png/white/{self.catagory}/{self.name}.png')
