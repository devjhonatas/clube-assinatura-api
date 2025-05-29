# models/models.py

membros = {}
assinaturas = {}
produtos = {}
envios = {}

next_membro_id = 1
next_assinatura_id = 1
next_produto_id = 1
next_envio_id = 1

def get_next_membro_id():
    global next_membro_id
    id_atual = next_membro_id
    next_membro_id += 1
    return str(id_atual)

def get_next_assinatura_id():
    global next_assinatura_id
    id_atual = next_assinatura_id
    next_assinatura_id += 1
    return str(id_atual)

def get_next_produto_id():
    global next_produto_id
    id_atual = next_produto_id
    next_produto_id += 1
    return str(id_atual)

def get_next_envio_id():
    global next_envio_id
    id_atual = next_envio_id
    next_envio_id += 1
    return str(id_atual)

membros['1'] = {'nome': 'João Silva', 'email': 'joao@email.com'}
membros['2'] = {'nome': 'Maria Oliveira', 'email': 'maria@email.com'}
next_membro_id = 3

produtos['1'] = {'nome': 'Café Premium 250g', 'descricao': 'Grãos especiais de Minas Gerais', 'preco': 35.00}
produtos['2'] = {'nome': 'Caneca Exclusiva do Clube', 'descricao': 'Caneca de cerâmica com logo do clube', 'preco': 49.90}
next_produto_id = 3

assinaturas['1'] = {'membro_id': '1', 'plano': 'mensal', 'data_inicio': '2023-01-01', 'ativa': True}
assinaturas['2'] = {'membro_id': '2', 'plano': 'anual', 'data_inicio': '2022-11-15', 'ativa': True}
next_assinatura_id = 3

envios['1'] = {'membro_id': '1', 'data_envio': '2023-05-20', 'itens': [{'produto_id': '1', 'quantidade': 1}], 'status': 'enviado'}
envios['2'] = {'membro_id': '2', 'data_envio': '2023-05-20', 'itens': [{'produto_id': '1', 'quantidade': 1}, {'produto_id': '2', 'quantidade': 1}], 'status': 'enviado'}
next_envio_id = 3