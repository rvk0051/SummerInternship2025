# Types of Caching in Django
Django provides several caching strategies that you can use depending on your needs. Here are the main types of caching available in Django:

## 1. Per-View Caching
This type of caching allows you to cache the output of specific views. When a view is cached, the entire response is stored, and subsequent requests for that view will return the cached response instead of executing the view logic again.

**How to Use:** You can use the cache_page decorator to cache a view.
**Example:**
```
  from django.views.decorators.cache import cache_page
  @cache_page(60 * 15)  # output gets stored in cache for 15 minutes
  def <view_name>(request):
      # Your view logic here
      return render(request, '<template_name>', context)
```

## 2. Template Fragment Caching
This allows you to cache specific parts (fragments) of a template rather than the entire view. This is useful when you have a large template but only want to cache a small section of it.

**How to Use:** You can use the {% cache %} template tag to cache a fragment.
**Example:**
```
{% load cache %}
{# 'sidebar' is cache key (unique identifier used to store and retrieve data from a cache) #}
{% cache 500 sidebar %}  # these are 500 seconds here.
    <!-- Sidebar content that you want to cache -->
    <div>Sidebar content here</div> 
{% endcache %}
```

## 3. Site-wide Caching
This approach caches the entire site or a large portion of it. You can achieve this by using middleware that caches the output of all views.

**How to Use:** You need to add caching middleware to your MIDDLEWARE settings in settings.py.
**Example:**
```
  MIDDLEWARE = [
      'django.middleware.cache.UpdateCacheMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.cache.FetchFromCacheMiddleware',
      # Other middleware...
  ]
```

## 4. Low-Level Caching
Django also provides a low-level caching API that allows you to cache arbitrary data. 
This is useful for caching data that is not tied to a specific view or template.

**How to Use:** You can use the cache object to set and get cache values.