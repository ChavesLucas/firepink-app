frontend/app.js

window.onload = async () => {
  const response = await fetch('/api/todo');
  const todos = await response.json();

  const todoList = document.getElementById('todo-list');
  todos.forEach(todo => {
    const li = document.createElement('li');
    li.textContent = todo.task;
    todoList.appendChild(li);
  });
};