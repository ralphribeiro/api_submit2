from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Transacao(db.Model):
    """
        Modelo de Transação
    """
    id = db.Column(db.Integer, primary_key=True)
    estabelecimento = db.Column(db.String(100), nullable=False)
    cliente = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'''
            estabelecimento={self.estabelecimento},
            cliente={self.cliente},
            valor={self.valor},
            descricao={self.descricao}
            '''
