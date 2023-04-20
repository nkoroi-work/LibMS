from rest_framework import serializers
from .models import *

class publisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = publisher 
        fields = ('publisher_name', 'phone', 'address')

class bookSerializer(serializers.ModelSerializer):

    class Meta:
        model = book 
        fields = ('book_id','title', 'book_publisher')

class book_copiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = book_copies 
        fields = ('book_id', 'branch_id', 'no_copies')

class book_authorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = book_authors 
        fields = ('book_id', 'author_name')

class library_branchSerializer(serializers.ModelSerializer):

    class Meta:
        model = publisher 
        fields = ('branch_id', 'branch_name', 'branch_address')

class borrowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = borrower 
        fields = ('card_no', 'name', 'address', 'phone')

class book_loansSerializer(serializers.ModelSerializer):

    class Meta:
        model = book_loans 
        fields = ('book_id', 'branch_id','card_no', 'date_out', 'due_date', 'returned_date')