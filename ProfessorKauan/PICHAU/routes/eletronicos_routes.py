from flask import Blueprint, request

from controllers.eletronicos_controllers import create_eletronico

eletronicos_routes = Blueprint('eletronicos_routers',__name__)

@eletronicos_routes.route('/eletronico', methods=['POST'])
def eletronicos_post():
    eletronicos_data = request.json
    return create_eletronico(request.json)