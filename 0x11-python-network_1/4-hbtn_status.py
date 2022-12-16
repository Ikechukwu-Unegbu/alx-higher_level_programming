#!/usr/bin/python3
"""hbtn status endpoint call"""

if __name__ == '__main__':
    import requests

    res = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
