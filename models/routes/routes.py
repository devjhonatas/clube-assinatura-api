# routes/routes.py

from flask import request
from flask_restful import Resource, Api
from models.models import membros, assinaturas, produtos, envios, \
                           get_next_membro_id, get_next_assinatura_id, \
                           get_next_produto_id, get_next_envio_id

def configure_routes(api: Api):

    class MembroList(Resource):
        def get(self):
            return membros, 200

        def post(self):
            data = request.get_json()
            if not data or not all(k in data for k in ('nome', 'email')):
                return {"message": "Nome e email são obrigatórios"}, 400
            
            novo_id = get_next_membro_id()
            membros[novo_id] = {'nome': data['nome'], 'email': data['email']}
            return {"id": novo_id, **membros[novo_id]}, 201

    class Membro(Resource):
        def get(self, membro_id):
            membro = membros.get(membro_id)
            if membro:
                return membro, 200
            return {"message": "Membro não encontrado"}, 404

        def put(self, membro_id):
            data = request.get_json()
            membro = membros.get(membro_id)
            if not membro:
                return {"message": "Membro não encontrado"}, 404
            
            membro.update(data)
            return membro, 200

        def delete(self, membro_id):
            if membro_id in membros:
                del membros[membro_id]
                return {"message": "Membro deletado com sucesso"}, 204
            return {"message": "Membro não encontrado"}, 404
            
    class AssinaturaList(Resource):
        def get(self):
            return assinaturas, 200

        def post(self):
            data = request.get_json()
            required_fields = ['membro_id', 'plano', 'data_inicio']
            if not data or not all(k in data for k in required_fields):
                return {"message": f"Os campos {', '.join(required_fields)} são obrigatórios"}, 400
            
            if data['membro_id'] not in membros:
                return {"message": "Membro_id não encontrado"}, 404

            novo_id = get_next_assinatura_id()
            assinaturas[novo_id] = {
                'membro_id': data['membro_id'],
                'plano': data['plano'],
                'data_inicio': data['data_inicio'],
                'ativa': data.get('ativa', True)
            }
            return {"id": novo_id, **assinaturas[novo_id]}, 201

    class Assinatura(Resource):
        def get(self, assinatura_id):
            assinatura = assinaturas.get(assinatura_id)
            if assinatura:
                return assinatura, 200
            return {"message": "Assinatura não encontrada"}, 404

        def put(self, assinatura_id):
            data = request.get_json()
            assinatura = assinaturas.get(assinatura_id)
            if not assinatura:
                return {"message": "Assinatura não encontrada"}, 404
            
            assinatura.update(data)
            return assinatura, 200

        def delete(self, assinatura_id):
            if assinatura_id in assinaturas:
                del assinaturas[assinatura_id]
                return {"message": "Assinatura deletada/cancelada com sucesso"}, 204
            return {"message": "Assinatura não encontrada"}, 404

    class ProdutoList(Resource):
        def get(self):
            return produtos, 200

        def post(self):
            data = request.get_json()
            required_fields = ['nome', 'preco']
            if not data or not all(k in data for k in required_fields):
                return {"message": f"Os campos {', '.join(required_fields)} são obrigatórios"}, 400
            
            try:
                preco = float(data['preco'])
            except ValueError:
                return {"message": "Preço deve ser um número válido"}, 400

            novo_id = get_next_produto_id()
            produtos[novo_id] = {
                'nome': data['nome'],
                'descricao': data.get('descricao', ''),
                'preco': preco
            }
            return {"id": novo_id, **produtos[novo_id]}, 201

    class Produto(Resource):
        def get(self, produto_id):
            produto = produtos.get(produto_id)
            if produto:
                return produto, 200
            return {"message": "Produto não encontrado"}, 404

        def put(self, produto_id):
            data = request.get_json()
            produto = produtos.get(produto_id)
            if not produto:
                return {"message": "Produto não encontrado"}, 404
            
            if 'preco' in data:
                try:
                    data['preco'] = float(data['preco'])
                except ValueError:
                    return {"message": "Preço deve ser um número válido"}, 400

            produto.update(data)
            return produto, 200

        def delete(self, produto_id):
            if produto_id in produtos:
                del produtos[produto_id]
                return {"message": "Produto deletado com sucesso"}, 204
            return {"message": "Produto não encontrado"}, 404

    class EnvioList(Resource):
        def get(self):
            return envios, 200

        def post(self):
            data = request.get_json()
            required_fields = ['membro_id', 'data_envio', 'itens']
            if not data or not all(k in data for k in required_fields):
                return {"message": f"Os campos {', '.join(required_fields)} são obrigatórios"}, 400

            if data['membro_id'] not in membros:
                return {"message": "Membro_id não encontrado"}, 404
            
            if not isinstance(data['itens'], list):
                return {"message": "Campo 'itens' deve ser uma lista"}, 400

            for item in data['itens']:
                if 'produto_id' not in item or 'quantidade' not in item:
                    return {"message": "Cada item deve ter 'produto_id' e 'quantidade'"}, 400
                if item['produto_id'] not in produtos:
                    return {"message": f"Produto com ID {item['produto_id']} não encontrado"}, 404
                try:
                    item['quantidade'] = int(item['quantidade'])
                    if item['quantidade'] <= 0:
                        return {"message": "Quantidade do item deve ser um número positivo"}, 400
                except ValueError:
                    return {"message": "Quantidade do item deve ser um número inteiro"}, 400

            novo_id = get_next_envio_id()
            envios[novo_id] = {
                'membro_id': data['membro_id'],
                'data_envio': data['data_envio'],
                'itens': data['itens'],
                'status': data.get('status', 'pendente')
            }
            return {"id": novo_id, **envios[novo_id]}, 201

    class Envio(Resource):
        def get(self, envio_id):
            envio = envios.get(envio_id)
            if envio:
                return envio, 200
            return {"message": "Envio não encontrado"}, 404

        def put(self, envio_id):
            data = request.get_json()
            envio = envios.get(envio_id)
            if not envio:
                return {"message": "Envio não encontrado"}, 404
            
            if 'itens' in data:
                if not isinstance(data['itens'], list):
                    return {"message": "Campo 'itens' deve ser uma lista"}, 400
                for item in data['itens']:
                    if 'produto_id' not in item or 'quantidade' not in item:
                        return {"message": "Cada item deve ter 'produto_id' e 'quantidade'"}, 400
                    if item['produto_id'] not in produtos:
                        return {"message": f"Produto com ID {item['produto_id']} não encontrado"}, 404
                    try:
                        item['quantidade'] = int(item['quantidade'])
                        if item['quantidade'] <= 0:
                            return {"message": "Quantidade do item deve ser um número positivo"}, 400
                    except ValueError:
                        return {"message": "Quantidade do item deve ser um número inteiro"}, 400

            envio.update(data)
            return envio, 200

        def delete(self, envio_id):
            if envio_id in envios:
                del envios[envio_id]
                return {"message": "Envio deletado com sucesso"}, 204
            return {"message": "Envio não encontrado"}, 404

    class MembroEnvios(Resource):
        def get(self, membro_id):
            if membro_id not in membros:
                return {"message": "Membro não encontrado"}, 404
            
            envios_do_membro = {k: v for k, v in envios.items() if v['membro_id'] == membro_id}
            return envios_do_membro, 200

    api.add_resource(MembroList, '/membros')
    api.add_resource(Membro, '/membros/<string:membro_id>')

    api.add_resource(AssinaturaList, '/assinaturas')
    api.add_resource(Assinatura, '/assinaturas/<string:assinatura_id>')

    api.add_resource(ProdutoList, '/produtos')
    api.add_resource(Produto, '/produtos/<string:produto_id>')

    api.add_resource(EnvioList, '/envios')
    api.add_resource(Envio, '/envios/<string:envio_id>')
    api.add_resource(MembroEnvios, '/membros/<string:membro_id>/envios')