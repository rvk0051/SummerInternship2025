# Specifying which Fields Should be Read-Only
It could be a good idea to mark many fields as read-only. You can use the read_only_fields Meta option instead of explicitly adding the read only=True attribute to each field

### Example:-
```aiignore
class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    fields = ('name','species','weight','height','timestamp','latitude','longitude')
    read_only_fields = ('name')

```
It is not necessary to add read-only fields to the read-only fields option for model fields with editable=False set or for AutoField fields because they are read-only by default.

# Specifying Which Fields Should be Write-Only
It may be desirable to designate numerous fields as write-only. You can use the write_only_fields Meta option instead of explicitly adding the write only=True attribute to each field

```aiignore
class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    fields = ('name','species','weight','height','timestamp','latitude','longitude')
    write_only_fields = ('species',)  # Note: Species field is write-only

```