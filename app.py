firepink-app/app.py


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpassword@db/todo_app'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

@app.route('/api/todo', methods=['GET'])
def get_todo_list():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'task': todo.task} for todo in todos]
    return jsonify(todo_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')