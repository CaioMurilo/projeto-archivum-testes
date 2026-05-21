from flask import Blueprint, request, jsonify, send_from_directory
from database import get_db_connection

# Blueprint é a forma profissional de separar rotas no Flask
api = Blueprint('api', __name__)

@api.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@api.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if data and data.get('usuario') == 'admin' and data.get('senha') == '123':
        return jsonify({"token": "autenticado"}), 200
    return jsonify({"erro": "Credenciais inválidas"}), 401

@api.route('/api/livros', methods=['GET'])
def listar_livros():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM livros")
    livros = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(livros), 200

@api.route('/api/livros', methods=['POST'])
def adicionar_livro():
    data = request.json
    conn = get_db_connection()
    cursor = conn.execute("INSERT INTO livros (titulo, autor) VALUES (?, ?)", (data['titulo'], data['autor']))
    conn.commit()
    livro_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": livro_id, "titulo": data['titulo'], "autor": data['autor']}), 201

@api.route('/api/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    data = request.json
    conn = get_db_connection()
    conn.execute("UPDATE livros SET titulo = ?, autor = ? WHERE id = ?", (data['titulo'], data['autor'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Obra atualizada."}), 200

@api.route('/api/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM livros WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Obra deletada."}), 200