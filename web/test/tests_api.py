from unittest import TestCase
from flask import url_for

from app import create_app
from app.resources import Transacao


class TestApi(TestCase):
    def setUp(self) -> None:
        self.app = create_app('testes')
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()

    def test_cadastro_deve_inserir_registro_na_base(self):
        chamada = {
            'estabelecimento': 'loja',
            'cliente': 'ralph',
            'valor': 1.0,
            'descricao': 'compra teste'
        }

        transacao_teste = Transacao(
            estabelecimento=chamada['estabelecimento'],
            cliente=chamada['cliente'],
            valor=chamada['valor'],
            descricao=chamada['descricao']
        )

        self.client.post(
            url_for('api.cadastra_transacao'),
            json=chamada
        )

        esperado = Transacao.query.filter_by(cliente='ralph').first()
        self.assertEqual(str(esperado), str(transacao_teste))

    def test_cadastro_valido_deve_retornar_json_com_aceito_igual_a_true(self):
        chamada = {
            'estabelecimento': 'restaurante x',
            'cliente': 'messi',
            'valor': 1000.01,
            'descricao': 'compra burlesca'
        }
        esperado = {"aprovado": True}

        response = self.client.post(
            url_for('api.cadastra_transacao'),
            json=chamada
        )
        self.assertEqual(response.json, esperado)

    def test_cadastro_valido_deve_retornar_201(self):
        chamada = {
            'estabelecimento': 'restaurante y',
            'cliente': 'lebrão',
            'valor': 10000.01,
            'descricao': 'compra hiper burlesca'
        }
        esperado = 201

        response = self.client.post(
            url_for('api.cadastra_transacao'),
            json=chamada
        )
        self.assertEqual(response.status_code, esperado)

    def test_cadastro_com_campo_invalido_deve_retornar_erro_422(self):
        chamada = {
            'bananas': 'xxx',
            'de': 'yyy',
            'pijamas': 0.0,
            'b1b2': 'zzz'
        }
        esperado = 422

        response = self.client.post(
            url_for('api.cadastra_transacao'),
            json=chamada
        )
        self.assertEqual(response.status_code, esperado)

    # def tearDown(self) -> None:
    #     self.app.db.drop_all()
