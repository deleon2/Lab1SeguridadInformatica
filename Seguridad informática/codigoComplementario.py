# Universidad Finis Terrae
# Seguridad Informática, Laboratorio N°1
# Integrantes: Felipe Vera - Marcelo Ibarra

## Código Primer Desafío ##

import requests

headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"ffxjwjnrr"}'

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)

print(response.text)



## Código segundo desafío ##


headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)
print(response.text)
