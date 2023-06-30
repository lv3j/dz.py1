import requests 
response = requests.get("https://swapi.dev/api/") 
urls = response.json()

def get_planets_info(): 
    root_url = urls["planets"] 
    planets_list = [] 

    for i in range(1, 6): 
        response = requests.get(f'{root_url}/{i}') 
        data = response.json() 
        data['diameter'] = int(data['diameter']) 
        planets_list.append(data) 

    planet_with_max_diameter = max(planets_list, key=lambda x: x['diameter']) 
    
    return f''\
        f'Планета с максимальным диаметром: {planet_with_max_diameter["name"]}.'\
        f' Диаметер - {planet_with_max_diameter["diameter"]}'

print(get_planets_info())

response = requests.get("https://swapi.dev/api/") 
urls = response.json() 
def get_starships_info(): 
    starships_list = [] 
    root_url = urls["starships"] 
    for i in range(1, 6): 
        response = requests.get(f'{root_url}{i}') 
        if not response.json().get("detail"): 
            data = response.json() 
            data['max_atmosphering_speed'] = int(data['max_atmosphering_speed']) 
            starships_list.append(data) 
            starship_with_max_speed = max(starships_list, key=lambda x: x['max_atmosphering_speed']) 
            return f''\
            f'Звёздный корабль с максимальной скоростью: {starship_with_max_speed["name"]}.'\
            f' Скорость - {starship_with_max_speed["max_atmosphering_speed"]}'
        
print(get_starships_info())