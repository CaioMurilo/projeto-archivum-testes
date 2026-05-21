import pytest
import os
import database
from app import create_app

# Força os testes a usarem um banco de dados temporário
database.DB_NAME = 'test_archivum.db'

@pytest.fixture
def client():
    # Prepara o servidor falso para os testes
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
    # Limpa o banco de dados temporário após o teste
    if os.path.exists('test_archivum.db'):
        os.remove('test_archivum.db')

def test_login_sucesso(client):
    """Testa se o sistema aceita credenciais corretas"""
    response = client.post('/api/login', json={"usuario": "admin", "senha": "123"})
    assert response.status_code == 200
    assert response.json['token'] == 'autenticado'

def test_login_falha(client):
    """Testa se o sistema bloqueia senhas incorretas"""
    response = client.post('/api/login', json={"usuario": "admin", "senha": "errada"})
    assert response.status_code == 401

def test_crud_livros(client):
    """Testa o fluxo completo de Criar, Ler, Atualizar e Deletar um livro"""
    
    # 1. CREATE (Registrar)
    res_post = client.post('/api/livros', json={"titulo": "O Príncipe", "autor": "Maquiavel"})
    assert res_post.status_code == 201
    livro_id = res_post.json['id']

    # 2. READ (Consultar)
    res_get = client.get('/api/livros')
    assert res_get.status_code == 200
    assert len(res_get.json) > 0

    # 3. UPDATE (Atualizar)
    res_put = client.put(f'/api/livros/{livro_id}', json={"titulo": "O Príncipe Editado", "autor": "Maquiavel"})
    assert res_put.status_code == 200

    # 4. DELETE (Deletar)
    res_del = client.delete(f'/api/livros/{livro_id}')
    assert res_del.status_code == 200