import requests
import sys
import os

def upload_file(filepath):
    url = 'http://127.0.0.1:8888/'
    files = {'file': open(filepath, 'rb')}
    response = requests.post(url, files=files)
    print(response.text)


def list_files():
    path = 'static/music'
    l_files = os.listdir(path) 
    for file in l_files:
        print(f' {file} ')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'upload':
            if len(sys.argv) > 2:
                filepath = sys.argv[2]
                if not os.path.exists(filepath):
                    print('File not found')
                    exit(1)
                upload_file(filepath)
            else:
                print('Please provide a file path')
        elif sys.argv[1] == 'list':
            list_files()
        else:
            print('Invalid command')
    else:
        print('Please provide a command (upload or list)')