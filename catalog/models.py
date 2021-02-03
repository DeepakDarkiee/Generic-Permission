from django.db import models

# Create your models here.class
class Book(models.Model):
    book_name=models.CharField(max_length=100)
    book_author=models.ForeignKey("Author", on_delete=models.CASCADE)
    book_id=models.IntegerField()

    def __str__(self):
        return self.book_name
    class Meta:
         permissions = (
            ('publish_book', 'can publish book'),
            ('add_author_book', 'can add author book'),
        )


class Author(models.Model):
    author_name=models.CharField(max_length=100)
    def __str__(self):
        return self.author_name


