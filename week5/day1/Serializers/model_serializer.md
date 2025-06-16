# ModelSerializer
ModelSerializer is an abstraction layer over Django's default serializer that enables the easy creation of a serializer for a model. A wrapper for the standard Django Framework, the Django REST Framework is primarily used to develop different types of APIs.

A ModelSerializer, similar to a ModelForm, offers an API for building serializers from your models. The Form and ModelForm classes in Django function quite similarly to the serializers in the REST framework. It offers a ModelSerializer class that acts as a convenient shortcut for developing serializers that deal with model instances and querysets, as well as a Serializer class that allows you a strong, general approach to managing the output of your responses.

With the help of the ModelSerializer class, you can quickly generate a Serializer class in django with fields that match the Model fields. Similar to a standard Serializer class, the ModelSerializer class has the following differences:

Based on the model, it will create a set of fields for you automatically.
Validators like unique together validators will be generated automatically for the serializer.
It features straightforward.create()and.update default implementations ()`.

### Syntax:-
```aiignore
class SerializerName(serializers.ModelSerializer):
    class Meta:
        model = ModelName
        fields = List of Fields

```

### Specifying Which Fields Should be Included, Example:-
```aiignore
class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    #here we are including only a few fields
    fields = ('name','species','weight','height','file')
```

### Specifying Which Fields Should be Excluded, Example:-
```aiignore
class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    # specify field names
    exclude = ['timestamp']

```