# Declaring Serializers
Similar to constructing a form or model in Django, creating a basic serializer requires importing the serializers class from the rest framework and defining the serializer's fields. Declaring serializers in Django:
```
#Model.py
from distutils.co mmand.upload import upload
from django.db import models
from PIL import Image
from rest_framework import serializers

class RecordSerializer(serializers.Serializer):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=30, decimal_places=1)
    height = models.DecimalField(max_digits=20, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
```

Just like when building a form or model in Django, the first step in establishing a basic serializer is to import the serializers class from the rest framework and define the serializer's fields.
```
from re import search
from unit test.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Records
# from .tasks import file_resize

class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    fields = ('name','species','weight','height','timestamp','latitude','longitude')

```

## Using Serializer to Serialize Data
To serialize a record or list of records, we may now use RecordSerializer. Once more, utilizing a Form class appears to be very similar to using the Serializer class.

```aiignore
serializer = RecordSerializer(comment)
serializer.data
# {"id": 5, "name": "Guppy", "species": "Poecilia reticulata", "weight": 1.5, "height": 5.8, "file": "guppy.jpg", "is_cropped": false, "timestamp": "2022-02-19T15:06:38.982341Z","latitude": 15.0, "longitude": 18.0 }

```
