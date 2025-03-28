import './todo.css';
import { Api } from './api';

export interface ITodo {
  id: number;
  text: string;
  done: boolean;
}

export class Todo {
  todos: ITodo[] = [];
  newTodo: string = '';
  api = new Api();

  async attached() {
    this.todos = await this.api.getTodos();
  }

  async addTodo() {
    if (this.newTodo.trim()) {
      const created = await this.api.createTodo(this.newTodo);
      this.todos.unshift(created);
      this.newTodo = '';
    }
  }

  async removeTodo(index: number, id: number) {
    await this.api.deleteTodo(id);
    this.todos.splice(index, 1);
  }

  async toggleTodo(todo: ITodo) {
    await this.api.updateTodo(todo.id, todo.done);
  }

  onToggleRequested(todo: ITodo) {
    setTimeout(() => {
      this.toggleTodo(todo);
    });
  }
}
