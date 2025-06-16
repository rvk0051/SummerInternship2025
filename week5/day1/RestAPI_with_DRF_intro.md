# Rest API with Django Rest Framework(DRF) 
Django REST Framework is a powerful toolkit for building Web APIs. It provides a robust and flexible way to create RESTful APIs, which are essential for modern web applications, especially those that require interaction with front-end frameworks or mobile applications.

Modern apps (React, Android, ML models, microservices) need to talk using JSON over HTTP.DRF makes building secure, scalable, flexible APIs incredibly easy.

## Why do we need REST APIs?
### * Decoupling:- 
REST APIs allow you to separate your frontend (e.g., a mobile app) from your backend (your Django application). This makes development more modular, allowing different teams to work concurrently on different parts of the application.

### * Platform Agnostic:
A REST API provides data in a standardized format (usually JSON or XML). This means any client that understands JSON (a mobile app on iOS or Android, etc) can consume your API, regardless of the technology it's built with. You're not tied to rendering HTML.

### * Scalability:
By decoupling, you can scale your frontend and backend independently. If your API is experiencing high load, you can scale your backend servers without necessarily needing to scale your frontend.