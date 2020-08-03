import requests

"""
Para registro de una nueva aplicacion, ingresar a la siguiente URL.
https://github.com/settings/applications/new
"""

client_id = 'ea25523c2547226b9901'
client_secret = '3a045673966c70dcf522660a325dd9ee7b996f6d'

code = 'e8af5cf265a9030eec96'

"""
Ingresar a la siguiente URL que deberia redireccionar a la mi website
https://github.com/login/oauth/authorize?client_id=ea25523c2547226b9901&scope=respo
"""

if __name__ == '__main__':
    
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id':client_id, 'client_secret':client_secret, 'code':code}
    headers = {'Accept':'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)