export class Api {
  private baseUrl = 'http://localhost:8000';

  async getTodos() {
    const response = await fetch(`${this.baseUrl}/todos/`);
    return response.json();
  }

  async createTodo(text: string) {
    const response = await fetch(`${this.baseUrl}/todos/`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({text}),
    });
    return response.json();
  }

  async updateTodo(id: number, done: boolean) {
    const response = await fetch(`${this.baseUrl}/todos/${id}`, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({done}),
    });
    return response.json();
  }

  async deleteTodo(id: number) {
    await fetch(`${this.baseUrl}/todos/${id}`, {method: 'DELETE'});
  }
}
