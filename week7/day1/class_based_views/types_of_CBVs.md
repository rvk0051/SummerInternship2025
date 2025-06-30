# Types of Class-Based Views

Class-Based Views are categorized based on their origin (Django core or Django REST Framework) and the level of abstraction they provide for common web application or API patterns.

---

## 1. Django's Built-in CBVs

These views are part of Django's core framework and are designed for both traditional web applications rendering templates and handling forms.

### **View (Base Class)**

- **Purpose**:  
  The most fundamental Class-Based View. It's a direct replacement for function-based views when you need custom logic for different HTTP methods (`get()`, `post()`, etc.) and wish to leverage class-based structure. It provides a `dispatch()` method that intelligently routes incoming requests to the appropriate HTTP method handler.

- **When to Use**:  
  Ideal for highly custom scenarios that don't fit into Django's generic patterns, or when you simply prefer the class-based structure for basic views.


### **Generic Display Views**

- **TemplateView**: Renders a specified template with an optional context dictionary. Useful for static pages or data display without complex form handling.
- **RedirectView**: Handles HTTP redirects (e.g., 301, 302). Useful for redirecting old URLs to new ones.


### **Generic Editing Views**

- **FormView**: Displays and processes a form. Handles form instantiation, validation, and redirection upon success.
- **CreateView**: Displays a form to create a new model instance and saves it to the database.
- **UpdateView**: Displays a form pre-filled with existing object data and updates it upon submission.
- **DeleteView**: Presents a confirmation page and deletes the object upon confirmation.


### **Generic List & Detail Views**

- **ListView**: Displays a list of objects from a `QuerySet`, with pagination and list context.
- **DetailView**: Displays a single object fetched via primary key or slug.


### **Key Concept for Django's Generic Views**

These generic views significantly reduce boilerplate for CRUD and list/detail patterns. They use sensible defaults and expose hook methods such as:
- `get_queryset()`
- `get_context_data()`
- `form_valid()`

Common attributes include:
- `model`
- `queryset`
- `template_name`
- `context_object_name`

---

## 2. Django REST Framework (DRF) CBVs

Django REST Framework (DRF) extends Django's CBVs to support web APIs with built-in content negotiation, serialization, and permission handling.


### **APIView (Base Class for DRF)**

- **Purpose**:  
  Core DRF CBV extending Django's `View`, providing:
  - Request parsing
  - Flexible `Response` objects
  - Authentication and permissions
  - Throttling
  - Content negotiation

- **Distinction from Django's View**:  
  Unlike Django’s `View`, DRF’s `APIView` integrates with authentication, permissions, and serializers, making it better for API endpoints.


### **DRF Generic APIViews (`generics.*`)**

Built on top of `APIView` and Django's generic views. These views streamline API development by reducing the code for CRUD operations.

#### **Examples**:

- `CreateAPIView`: Handles `POST` for creating instances.
- `ListAPIView`: Handles `GET` for listing multiple instances.
- `RetrieveAPIView`: Handles `GET` for retrieving a single instance.
- `UpdateAPIView`: Handles `PUT`, `PATCH` for updating instances.
- `DestroyAPIView`: Handles `DELETE` for deleting instances.

#### **Combinations**:

- `ListCreateAPIView`
- `RetrieveUpdateAPIView`
- `RetrieveDestroyAPIView`
- `RetrieveUpdateDestroyAPIView`

#### **How They Work**:

You define:
- `queryset`
- `serializer_class`

The view takes care of serialization, validation, and DB operations.

---

## 3. ViewSets (DRF Specific)

ViewSets abstract away individual endpoints into grouped actions for RESTful resources.


### **Purpose**

ViewSets group related actions (list, create, retrieve, update, destroy) into a single class and are mapped to HTTP methods using DRF Routers.


### **When to Use**

Recommended for standard RESTful APIs with common CRUD patterns. They simplify URL routing using Routers.


### **Distinction from APIViews**

- **APIView**: Represents a single endpoint (e.g., `GET /users/`)
- **ViewSet**: Represents a set of endpoints (e.g., `GET /users/`, `POST /users/`, `PUT /users/1/`, etc.)
- **Routing**: Use `.as_view()` with APIViews; register ViewSets using DRF’s `Router`.


### **Key Attributes & Methods**

- `queryset`
- `serializer_class`
- `permission_classes`
- Common actions: `list()`, `retrieve()`, `create()`, `update()`, `partial_update()`, `destroy()`


### **Types of ViewSets**

- **ViewSet**: Base class for fully custom behavior.
- **GenericViewSet**: Extends `GenericAPIView`, allows composition via mixins.
- **ModelViewSet**: Combines all CRUD mixins—most commonly used.
- **ReadOnlyModelViewSet**: Supports only `list()` and `retrieve()`—ideal for read-only APIs.
