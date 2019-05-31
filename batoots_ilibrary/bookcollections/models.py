from django.db import models

# Create your models here.

class Book(models.Model):
    DOG_COLORS = (("br", "Brown"),
                ("bl", "Black"),
                ("wh", "White"),
                ("go", "Gold")
                )
    Title = models.CharField("Breed", max_length=100)
    birth_date = models.DateTimeField("Birth Date", \
         null = True, blank = True)
    color = models.CharField("Color", max_length=2, \
        choices=DOG_COLORS)
    unique_features = models.TextField("Unique Features",
        max_length=1000)
        
    def __str__(self):
        return "{} {}".format(self.color, self.breed)
