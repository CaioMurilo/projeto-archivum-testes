from playwright.sync_api import Page, expect

# ATENÇÃO: O servidor (python app.py) precisa estar rodando em outro terminal para este teste funcionar!

def test_fluxo_login_e_cadastro_e2e(page: Page):
    """Simula um usuário real fazendo login e adicionando uma obra pelo navegador"""
    
    # 1. Acessa a página inicial
    page.goto("http://localhost:3000")

    # 2. Faz Login
    page.fill("#usuario", "admin")
    page.fill("#senha", "123")
    page.click("text=Entrar")

    # 3. Verifica se a tela do acervo apareceu
    expect(page.locator("#appSection")).to_be_visible()

    # 4. Cadastra uma nova obra
    page.fill("#titulo", "Ética a Nicômaco")
    page.fill("#autor", "Aristóteles")
    page.click("text=Adicionar ao Acervo")

    # 5. Verifica se o livro apareceu na lista visível da tela
    expect(page.locator("#listaLivros")).to_contain_text("Ética a Nicômaco")