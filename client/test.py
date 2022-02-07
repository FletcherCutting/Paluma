import requests

def choice_ping(url):
    identifier = input('Identifier: ')
    response = requests.get(url + 'ping/{}'.format(identifier))

if __name__ == '__main__':
    url = 'http://localhost:5000/'

    print('1) Ping')
    testChoice = input('\n> ')

    if testChoice == '1':
        choice_ping(url)
