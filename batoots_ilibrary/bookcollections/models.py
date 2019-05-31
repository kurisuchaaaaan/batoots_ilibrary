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
    notes = models.TextField("Notes", max_length = 2500, null = True)

class Dog(models.Model):
    #tuple
    DOG_COLORS = (("br", "Brown"),
                  ("bl", "Black"),
                  ("wh", "White"),
                  ("go", "Gold")
                 )

    breed = models.CharField("Breed", max_length=100)

    #blank = true : required , null= True : nullable
    birth_date = models.DateTimeField("Birth Date", null= True, blank = True)
    
    #colors
    color = models.CharField("Color", max_length=2, choices=DOG_COLORS)

    #textarea
    unique_features = models.TextField("Unique Features", max_length=100)

    #handle toString function overried
    def __str__(self):
        return "{} {}".format(self.color, self.breed)
        