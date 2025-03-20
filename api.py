from flask import Flask, request, jsonify
import conection

# Obtener todos los usuarios (READ)
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def read():
    try:
        connection = conection.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id, email, password FROM users'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'id': row['id'], 'email': row['email'], 'password': row['password']})
                return jsonify({'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Crear un usuario (CREATE)
@app.route('/users', methods=["POST"])
def create():
    data = request.get_json()
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (data['email'], data['password']))
        connection.commit()
    return jsonify({'message': 'Creacion exitosa'}), 201

# Crear un usuario (UPDATE)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET email = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (data['email'], data['password'], user_id))
        connection.commit()
    return jsonify({'message': 'Usuario actualizado'}), 200

# Eliminar un usuario (DELETE)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = conection.conectar()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
        connection.commit()
    return jsonify({'message': 'Usuario eliminado'}), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
   
