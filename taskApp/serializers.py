from rest_framework import serializers
from taskApp.models import Sections, Books


class BookSerializer(serializers.ModelSerializer):


    class Meta:

        model = Books
        fields = (
            'BookId',
            'BookTitle'
        )

class SectionSerializer(serializers.ModelSerializer):
    

    class Meta:

        model = Sections
        fields = (
            'SectionId',
            'SectionTitle',
            'Content',
            'Parent',
            'Book',
            'isParent'
            )