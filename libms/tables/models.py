from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields import checks




class publisher(models.Model):
	id = models.IntegerField()
	publisher_name = models.CharField(primary_key = True, max_length = 50)
	phone = models.CharField(max_length  = 15)
	address = models.CharField(max_length = 50)

	def __str__(self):
		return self.publisher_name

class book(models.Model):
	id = models.IntegerField()
	book_id = models.IntegerField(primary_key = True)
	title = models.CharField(max_length = 50)
	book_publisher = models.ForeignKey("publisher", on_delete = models.CASCADE)

	def __str__(self):
		return self.title

class book_authors(models.Model):
	id = models.IntegerField()
	book_id = models.ForeignKey("book", on_delete = models.CASCADE)
	author_name = models.CharField(primary_key = True, max_length = 50)

	def __str__(self):
		return self.author_name

class library_branch(models.Model):
	id = models.IntegerField()
	branch_id = models.IntegerField(primary_key = True)
	branch_name = models.CharField(max_length = 50)
	branch_address = models.CharField(max_length = 50)

	def __str__(self):
		return self.branch_name

class book_copies(models.Model):
	book_id = models.ForeignKey("book", on_delete = models.CASCADE)
	branch_id = models.ForeignKey("library_branch", on_delete = models.CASCADE)
	no_copies = models.IntegerField()

	def __str__(self):
		return self.book_id

class borrower(models.Model):
	id = models.IntegerField()
	card_no = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 15)

	def __str__(self):
		return self.name

class book_loans(models.Model):
	book_id = models.ForeignKey("book", on_delete = models.CASCADE)
	branch_id = models.ForeignKey("library_branch", on_delete = models.CASCADE)
	card_no = models.ForeignKey("borrower", on_delete = models.CASCADE)
	date_out = models.DateField(auto_now = False)
	due_date = models.DateField(auto_now = False)
	returned_date = models.DateField(auto_now = False)

	def __str__(self):
		return self.book_id
