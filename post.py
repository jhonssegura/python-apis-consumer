import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'Nombre':'Jhonathan', 'Curso':'Python', 'Nivel':'Intermedio'}

    # Payload serializado
    # response = requests.post(url, data=json.dumps(payload)) 
    response = requests.post(url, data=payload)
    print(response.url)

    if response.status_code == 200:
        print(response.content)