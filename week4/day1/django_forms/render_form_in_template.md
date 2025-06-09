# Rendering a Django Form in a Template
After creating a form class (like ContactForm or FeedbackForm) and it's object in views.py, we need to display it on a webpage using a Django template.

### Example:
 
    <!-- templates/contact.html -->

    <h2>Contact Us</h2>
    <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
        <button type="submit">Send</button>
    </form>

#### form methods:-
`<form method="post">`:- Sends data using POST method (not visible in URL)
these is one more form method - 'GET', 
GET for search/filter where exposing data in the URL is okay

#### CSRF token:-
`{% csrf_token %}`:- Required: Protects against Cross Site Request Forgery.

#### Display options:-
* {{ form.as_p }} - 	Each field is displayed inside <p>
* {{ form.as_table }}	Each field in an HTML <table>
* {{ form.as_ul }}	Each field inside a <ul> list

## Custom Field Rendering

     <form method="post">
     {% csrf_token %}
  
        <label for="{{ form.name.id_for_label }}">Your Name</label>
        {{ form.name }}
        {{ form.name.errors }}

        <label for="{{ form.email.id_for_label }}">Your Email</label>
        {{ form.email }}
        {{ form.email.errors }}

        <button type="submit">Send</button>
     </form>

