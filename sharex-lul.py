import boto3 as aws
import os
import pyperclip as xclip
import pyscreenshot as scrot
import random
import string
import sys

from io import BytesIO
from pathlib import Path
from shutil import which

s3 = aws.client('s3')

def random_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main():
    file_name = random_generator() + '.png'
    file_path = Path.home() / 'screenshots' / file_name
    
    if len(sys.argv) == 1 or sys.argv[1] == 'full':
        scrot.grab().save(file_path.open('xb'))
    elif sys.argv[1] == 'region':
        os.system(f'scrot "{file_path}" -s')
    elif sys.argv[1] == 'active':
        os.system(f'scrot "{file_path}" -ub')
    else:
        raise ValueError('No valid mode passed')

    s3.upload_file(
        str(file_path), 'files.charlesmilette.net', file_name,
        ExtraArgs={'ContentType': 'image/png'}
    )
    
    xclip.copy('https://charles.getsharex.com/' + file_name)
    if which('pacat') is not None:
        sound = Path(__file__).parents[0] / 'assets' / 'capture-success.wav'
        os.system(f'pacat "{sound}"')

if __name__ == '__main__': main()
