# TemplateView
* A built-in Django class-based view.
* Used when you just want to render a static HTML page or pass simple context to a template.
* Inherits from django.views.generic.base.TemplateView.

## Using TemplateView in views:-

    from django.views.generic import TemplateView
     
    # Using 'TemplateView'
    class LibraryHomeView(TemplateView):
        template_name = 'library/home.html'

        def get_context_data(self, **kwargs):
        # passes context 'message' to template 'library/home.html'
            context = super().get_context_data(**kwargs)
            context['message'] = 'Welcome to Online Library!'
            return context

