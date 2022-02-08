import requests

def choice_ping(url):
    identifier = input('Identifier: ')
    response = requests.get(url + 'ping/{}'.format(identifier))

def choice_log(url):
    identifier = input('Identifier: ')
    info = input('Info: ')
    response = requests.get(url + 'log/{}/{}'.format(identifier, info))

if __name__ == '__main__':
    url = 'http://localhost:5000/'

    print('1) Ping')
    print('2) Log')
    testChoice = input('\n> ')

    if testChoice == '1':
        choice_ping(url)
    elif testChoice == '2':
        choice_log(url)
