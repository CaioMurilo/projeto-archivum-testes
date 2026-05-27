# utils.py

def validar_dados_livro(titulo, autor):
    """
    Função pura de validação (Regra de Negócio).
    Não depende de banco de dados nem de rotas.
    """
    if not titulo or not str(titulo).strip():
        return False, "O título não pode ser vazio."
    
    if not autor or not str(autor).strip():
        return False, "O autor não pode ser vazio."
        
    if len(titulo) < 2:
        return False, "O título é muito curto."
        
    return True, "Dados válidos."