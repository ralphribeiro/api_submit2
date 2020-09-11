from flask import Blueprint, jsonify
from flask.globals import current_app, request

from app.resources import Transacao


api = Blueprint('api', __name__, url_prefix='/api/v1')


def valida_transacao(json: dict):
    try:
        estabelecimento = json['estabelecimento']
        cliente = json['cliente']
        valor = json['valor']
        descricao = json['descricao']
        return Transacao(
            estabelecimento=estabelecimento,
            cliente=cliente,
            valor=valor,
            descricao=descricao
        )
    except Exception as e:
        return e


@api.route('/transacao', methods=['POST'])
def cadastra_transacao():
    transacao = valida_transacao(request.json)

    if isinstance(transacao, Transacao):
        current_app.db.session.add(transacao)
        current_app.db.session.commit()
        return {"aprovado": True}, 201

    return jsonify({'erro': f'Erro, campo {transacao} inválido.'}), 422
