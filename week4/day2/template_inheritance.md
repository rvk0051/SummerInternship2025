# Template Inheritance
Template inheritance in Django is a powerful feature that allows you to create a base template containing the common elements of your site (like the header, footer, and navigation) and then define child templates that inherit from the base template and override specific sections. This promotes code reuse, reduces redundancy, and makes your templates more maintainable.

1. Base Template: This is the parent template that defines the overall structure of your site. It contains common elements and defines "blocks" that child templates can override.
2. Child Template: These templates inherit from the base template and provide content for the blocks defined in the base template.
3. Blocks: These are placeholders in the base template that child templates can fill with content.

### 1. Base Template:-
A base class is created which is to be inherited and saved in 'templates' directory.
This template defines the structure of the site.

for e.g.; We define a basic HTML structure with a header, navigation, content area, and footer and we have used `{% block title %}{% endblock %}` and `{% block content %}{% endblock %}`
here, {% block title %}{% endblock %} and {% block content %}{% endblock %} are block tags. These are placeholders that child templates can override.

### 2. Creating a child template:-
A child template is created which inherits the base template by using 'extend' keyword, e.g.;
`{% extends "base.html" %}` here, base.html is base template.
{% block title %}{% endblock %} overrides the title block in base.html.
{% block content %}{% endblock %} overrides the content block in base.html.

`{{ block.super }}`: In a child template, this tag includes the content of the parent block. It's useful when you want to add to the parent block's content rather than completely replacing it.

## Benefits of Template Inheritance
1. **Code Reuse:** Avoid repeating common elements across multiple templates.
2. **Maintainability:** Changes to the base template are automatically reflected in all child templates.
3. **Organization:** Keeps your templates organized and easy to understand.