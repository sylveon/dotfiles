import boto3 as aws
import pyperclip as xclip
import pyscreenshot as scrot
import random
import string

from io import BytesIO
from pathlib import Path

s3 = aws.client('s3')

def random_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main():
    file_name = random_generator() + '.png'
    file_path = Path.home() / 'screenshots' / file_name
    
    scrot.grab().save(file_path.open('xb'))
    s3.upload_file(str(file_path), 'files.charlesmilette.net', file_name)
    
    xclip.copy('https://charles.getsharex.com/' + file_name)

if __name__ == '__main__': main()
