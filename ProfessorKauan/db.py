#importa a classe sqlalchemy da biblioteca flask_sqlachemy
#o flask_sqlalchemy eh uma extensao para o flask que simplifica a interacao com banco de dados relacionados, usando sql alchemy
from flask_sqlalchemy import SQLAlchemy

"""
Cria uma instancia do objeto sqlalchemy
Esta instancia sera usada para interagir com o banco de dados ao longo da api
o db sera usado para definir modelos e realizar operacoes como insercoes, att e exclusoes no banco de dados
"""

db = SQLAlchemy()
