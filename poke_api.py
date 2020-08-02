import request

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form', offset=0):
    args = {'offset':offset} if offset else {}

    response = request.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
    
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    get_pokemons()

