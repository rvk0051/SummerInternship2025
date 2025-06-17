# Authentication Classes in DRF:-
DRF provides several built-in authentication classes, custom ones can also be implemented. Here are the most common:

## `rest_framework.authentication.TokenAuthentication`:-
* It is used for Stateless APIs (APIs that don't rely on server-side sessions). 
* It works by requiring clients to include a unique, secret token in the Authorization header of their HTTP requests.
* ### Features:-
1. **Stateless:** The server doesn't need to maintain session state, making it scalable.
2. **Mobile-Friendly:** Ideal for mobile applications or other clients that don't handle cookies well.
3. **Secure:** When combined with HTTPS, tokens provide a robust security mechanism.
* ### Working:-
1. A user logs in (e.g., via a username/password endpoint) and receives a unique token string.
2. For subsequent requests, the client includes this token in the Authorization header, prefixed with Token (e.g., Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b).
3. DRF's TokenAuthentication class intercepts this header, validates the token against stored tokens, and if valid, associates the request with the corresponding user.
* ### Setup:-
1. Add 'rest_framework.authtoken' to your INSTALLED_APPS in settings.py.
2. Run migrations to create the _authtoken_token_ table.
3. Tokens are generated either manually, by signals (e.g., when a new user is created), or by using a custom login endpoint.

## `rest_framework.authentication.SessionAuthentication`:-
* This works with Django's default session framework. It's suitable for browser-based clients that rely on cookies for session management, similar to a traditional Django web application.
* ### Working:-
1. A user logs in via a standard Django login view.
2. Django sets a session cookie in the user's browser.
3. Subsequent requests automatically send this cookie, and DRF authenticates the user based on the session ID in the cookie.
* ### Use Cases:-
1. Used in conjunction with TokenAuthentication for the browsable API (so you can log in through the browser).
2. For APIs consumed by the same Django application's frontend (e.g., a Django template rendering a React component that makes AJAX calls to the same Django backend).
* ### CSRF Protection: 
Requires CSRF token inclusion for POST, PUT, PATCH, DELETE requests when used with browser-based clients.

## `rest_framework.authentication.BasicAuthentication`:-
* This is the simplest authentication scheme, using standard HTTP Basic Authentication. 
* The client sends a base64-encoded string of username:password in the Authorization header.
* ### Working:-
The server decodes the string and attempts to authenticate the user with the provided username and password.
* ### Use Cases:-
1. Often used for simple scripts, internal tools, or very low-security APIs.
2. Not recommended for public-facing APIs or sensitive data due to the clear-text (though base64-encoded) transmission of credentials.
* ### Security Concern: 
Credentials are not encrypted; always use this with HTTPS.

## Custom Authentication:-
DRF allows you to create your own authentication classes by subclassing rest_framework.authentication.BaseAuthentication and implementing the authenticate() method. This is useful for integrating with OAuth, JWT (JSON Web Tokens), or other custom authentication mechanisms.