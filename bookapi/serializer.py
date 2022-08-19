from rest_framework import serializers
from django.forms import ValidationError
from .models import Book

#OPTION ONE FOR SERIALIZING
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)

#     def put(self, instance, data):
#         instance.title = data.get("title", instance.title)
#         instance.number_of_pages  = data.get("number_of_pages ", instance.number_of_pages )
#         instance.publish_date = data.get("publish_date", instance.publish_date)
#         instance.quantity = data.get("quantity", instance.quantity)

#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        description = serializers.SerializerMethodField()
        model = Book
        fields = '__all__' 

    def validate(self, data):
        if  data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("too heavy for inventory")
            
    def get_description(self, data):
        return "This book is called" + data.title + "and it is" + str(data.number_of_pages) + "long"