# tests/test_unit.py
from utils import validar_dados_livro

def test_validar_dados_sucesso():
    """Testa se a função aceita dados corretos"""
    valido, msg = validar_dados_livro("1984", "George Orwell")
    assert valido is True
    assert msg == "Dados válidos."

def test_validar_dados_titulo_vazio():
    """Testa se a função barra títulos em branco"""
    valido, msg = validar_dados_livro("", "George Orwell")
    assert valido is False
    assert msg == "O título não pode ser vazio."

def test_validar_dados_titulo_curto():
    """Testa se a função barra títulos com apenas 1 letra"""
    valido, msg = validar_dados_livro("A", "Autor Teste")
    assert valido is False
    assert msg == "O título é muito curto."