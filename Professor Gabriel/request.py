import requests
 
def buscar_usuario():
    url= 'https://jsonplaceholder.typicode.com/users/10'
 
    try:
        response = requests.get(url)
        response.raise_for_status()
 
        usuario = response.json()
 
        usuario_info = f"Nome: {usuario['name']}\n Email:{usuario['email']}\n"
        print(usuario_info)
 
    except requests.exceptions.RequestException as e:
        print (f'Falha ao buscar usuário: {e}')
 
if __name__ == '__main__':
    buscar_usuario()
    