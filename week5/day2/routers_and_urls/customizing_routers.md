# Customizing Routers
While Routers provide a lot of automation, their behavior could be customized.
## examples:-
* ### lookup_field:
 In your ViewSet, you can change the field used for detail lookups (instead of pk):
```aiignore
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn' # Now, URL will be /books/some-isbn-value/
```
* ### trailing_slash: 
By default, Routers generate URLs with a trailing slash (e.g., /books/). You can disable this during router instantiation:
`By default, Routers generate URLs with a trailing slash (e.g., /books/). You can disable this during router instantiation:

* ### Custom Actions:
ViewSets allow defining custom actions (e.g., `@action(detail=True, methods=['post']) def publish(self, request, pk=None):`). 
Routers automatically generate URLs for these custom actions as well (e.g., `/books/{pk}/publish/`).

