# Sistema Archivum 📚

Sistema web desenvolvido para a disciplina de Teste de Software. O foco principal deste repositório é a implementação de automação de testes utilizando **Pytest** e **Playwright**.

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python, Flask, SQLite.
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla).
* **Automação de Testes:** Pytest (Unitário/API) e Playwright (E2E).

## 🚀 Como rodar o projeto
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   playwright install

Inicie o servidor:

   python app.py

Acesse no navegador: http://localhost:3000 (Usuário: admin / Senha: 123).

**🧪 Como rodar os testes**

Testes de API (Backend): python -m pytest tests/test_api.py -v

Testes E2E (Interface): Com o servidor ligado, rode python -m pytest tests/test_e2e.py --headed
