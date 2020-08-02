import requests

if __name__ == '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'

    # Realiza la peticion sin descargar el contenido
    response = requests.get(url, stream=True) 
    with open('image.jpg', 'wb') as file:
        # Descarga el contenido poco a poco
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()