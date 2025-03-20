# Obtener todos los posts (READ)
from flask import app, Flask, jsonify, request
import conection

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        connection = conection.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id, user_id, title, content FROM posts'
                cursor.execute(sql)
                results = cursor.fetchall()
                posts_data = []
                for row in results:
                    posts_data.append({
                        'id': row['id'],
                        'user_id': row['user_id'],
                        'title': row['title'],
                        'content': row['content']
                    })
                return jsonify({'data': posts_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Crear un post (CREATE)
@app.route('/posts', methods=["POST"])
def create_post():
    data = request.get_json()
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['user_id'], data['title'], data['content']))
        connection.commit()
    return jsonify({'message': 'Post creado exitosamente'}), 201

# Actualizar un post (UPDATE)
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
            cursor.execute(sql, (data['title'], data['content'], post_id))
        connection.commit()
    return jsonify({'message': 'Post actualizado'}), 200

# Eliminar un post (DELETE)
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM posts WHERE id = %s"
            cursor.execute(sql, (post_id,))
        connection.commit()
    return jsonify({'message': 'Post eliminado'}), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)