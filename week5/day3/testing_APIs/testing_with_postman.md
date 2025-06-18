# Testing with Postman
Postman is a popular API client that provides a user-friendly interface for testing APIs. Here’s how to use it:

## 1. Create a New Request
Open Postman and click on "New" to create a new request.
Select "Request" and give it a name and a collection (optional).

Let’s say you have:

Token URL: `http://127.0.0.1:8000/api-token-auth/`

Protected API: `http://127.0.0.1:8000/books/`

## 2. Get Token
* Set method: POST

* URL: http://127.0.0.1:8000/api-token-auth/

* Go to Body > raw > JSON and enter:
```aiignore
{
  "username": "your_username",
  "password": "your_password"
}
```

* Hit Send.

* for e.g.; you get:
```aiignore
{
  "token": "abc123xyz456..." 
}
```
## 3. Access Protected API
Now test your protected endpoint:
* Method: GET

* URL: http://127.0.0.1:8000/books/

* Go to Headers and set:
```aiignore
Key: Authorization
Value: Token abc123xyz456...
```
* Hit Send ➝ you should get a response with the data.
* If token is wrong or missing, you’ll get:
```
{
  "detail": "Authentication credentials were not provided."
}
```