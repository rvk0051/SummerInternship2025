# Testing with cURL
cURL is a command-line tool for making HTTP requests. It is useful for quick tests and can be easily integrated into scripts.

### Basic cURL Commands

Understand all commands using example:-

#### 1. GET Request:
To retrieve a list of tasks:
```aiignore
curl -H "Authorization: Token <your_token_here>" http://localhost:8000/tasks/
```
#### 2. POST Request:
To create a new task:
```aiignore
curl -X POST -H "Authorization: Token <your_token_here>" -H "Content-Type: application/json" -d '{"title": "New Task", "description": "This is a new task.", "completed": false}' http://localhost:8000/tasks/
```
#### 3. PUT Request:
To update an existing task (replace {id} with the task ID):
```aiignore
curl -X PUT -H "Authorization: Token <your_token_here>" -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "This task has been updated.", "completed": true}' http://localhost:8000/tasks/{id}/
```

#### 4. DELETE Request:
To delete a task (replace {id} with the task ID):
```aiignore
curl -X DELETE -H "Authorization: Token <your_token_here>" http://localhost:8000/tasks/{id}/
```

#### 5. PATCH Request:
The PATCH command is an HTTP method used to apply partial modifications to a resource.
```aiignore
curl -X PATCH -H "Authorization: Token <your_token_here>" -H "Content-Type: application/json" -d '{"completed": true}' http://localhost:8000/tasks/{id}/
```

To get token in cURL:-
```aiignore
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://localhost:8000/api-token-auth/
```