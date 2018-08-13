#!/bin/python3
import boto3 as aws
import pyperclip as xclip
import random
import string
import subprocess
import sys

from pathlib import Path
from shutil import which

s3 = aws.client('s3')

def random_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main():
    file_name = random_generator() + '.png'
    file_path = Path.home() / 'screenshots' / file_name
    
    if len(sys.argv) == 1 or sys.argv[1] == 'full':
        subprocess.check_call(['deepin-screenshot', '-f', '-s', file_path])
    elif sys.argv[1] == 'region':
        subprocess.check_call(['deepin-screenshot', '-s', file_path])
    elif sys.argv[1] == 'active':
        subprocess.check_call(['deepin-screenshot', '-w', '-s', file_path])
    else:
        raise ValueError('No valid mode passed')

    s3.upload_file(
        str(file_path), 'files.charlesmilette.net', file_name,
        ExtraArgs={'ContentType': 'image/png'}
    )
    
    xclip.copy('https://yiff.forsale/' + file_name)
    if which('pacat') is not None:
        sound = Path(__file__).parent / 'assets' / 'capture-success.wav'
        subprocess.check_call(['pacat', str(sound)])

if __name__ == '__main__': main()
