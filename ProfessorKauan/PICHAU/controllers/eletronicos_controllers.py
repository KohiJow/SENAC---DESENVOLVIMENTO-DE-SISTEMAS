from models.eletronicos_models import Eletronicos
#db could not be resolved ablubleble (caralho pq tava dentro da pasta routes por isso n achava)
from db import db

import json

from flask import make_response #qq isso faz?
#pq meu novo eletronico TA VERDE???
def create_eletronico(eletronico_data):
    novo_eletronico= Eletronicos(
    nome = eletronico_data['nome'],
    categoria = eletronico_data['categoria'],
    preco = eletronico_data['preco']
    )
    
    db.session.add(novo_eletronico) #isso adiciona o eletronico novo no banco de dados?
    db.session.commit() #e isso comita?
    response = make_response(
        json.dumps({
            'mensagem': 'Eletronico cadastrado com sucesso',
            'eletronico': novo_eletronico.json()
        }, sort_keys=False)
    )
    response.headers['content-type'] = 'application/json'
    return response