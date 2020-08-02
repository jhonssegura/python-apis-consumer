import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'Nombre':'Jhonathan', 'Curso':'Python', 'Nivel':'Intermedio'}
    headers = {'Content-Type':'application/json', 'Access-Token':'1234500'}

    response = requests.post(url, data=json.dumps(payload), headers=headers) 

    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers # Dictionary
        server = headers_response['Server']
        print(server)