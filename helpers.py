import os
from flask1 import app


def get_imagem(id: int):
    for nome_arquivo in os.listdir(app.config.get('UPLOAD_PATH')):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo


def deletar_arquivo(id: int):
    arquivo = get_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
