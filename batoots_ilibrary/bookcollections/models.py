from django.db import models

# Create your models here.

class Book(models.Model):
    # a. Title (CharField, at most 250 characters)
    # b. Author (CharField, at most 250 characters)
    # c. Publisher (CharField, at most 250 characters)
    # d. Publication Year (PositiveIntegerField)
    # e. ISBN (CharField, At most 250 characters, Nullable)
    # f. Notes (TextField, At most 2500 characters, Nullable)
    title = models.CharField("Title", max_length=250)
    author = models.CharField("Author", max_length=250)
    publisher = models.CharField("Publisher", max_length=250)
    publication = models.PositiveIntegerField
    isbn = models.CharField("ISBN", max_length=250, null = True)
    notes = models.TextField("Notes", max_length = 25
        
