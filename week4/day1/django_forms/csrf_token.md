# CSRF
CSRF stands for Cross-Site Request Forgery.

It’s a type of cyber attack where a malicious site tricks a user into unknowingly submitting a request to another site where they’re already logged in.

 ### Example Attack Without CSRF Protection
Suppose one is logged into 'mybank.com', and without CSRF protection, another website could silently send:
 
    <form action="https://mybank.com/transfer" method="post">
      <input type="hidden" name="amount" value="10000">
      <input type="hidden" name="to_account" value="attacker123">
      <input type="submit">
    </form>
If one visit that site and it auto-submits, it could steal your money without you clicking anything!

# CSRF token in Django
Django uses a unique token to make sure each POST request is coming from your own website — not from an external one, this token is called CSRF token.
We use csrf token in forms when method is post.
It's working is mentioned below:

* When Django renders the form, it injects a hidden input:
      
`<input type="hidden" name="csrfmiddlewaretoken" value="random-secure-token">`
* This token is tied to your session (stored in cookies).

* Django checks this token on every POST request.

* If it’s missing or wrong, you get:
`403 Forbidden — CSRF verification failed`