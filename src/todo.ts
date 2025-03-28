export interface ITodo {
  text: string;
  done: boolean;
}

export class Todo {
  todos: ITodo[] = [];
  newTodo: string = '';

addTodo(): void {
  if (this.newTodo.trim()) {
    this.todos.unshift({ text: this.newTodo, done: false });
    this.newTodo = '';
  }
}

  removeTodo(index: number): void {
    this.todos.splice(index, 1);
  }

  toggleTodo(todo: ITodo): void {
    todo.done = !todo.done;
  }
}
