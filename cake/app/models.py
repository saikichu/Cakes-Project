from django.db import models

# Create your models here.

# class CategoryChoices(models.TextChoices):

#     BIRTHDAY_CAKES = 'Birthday Cakes' , 'Birthday Cakes'

#     WEDDING_CAKES = 'Wedding Cakes' , 'Wedding Cakes'

# class ShapeChoices(models.TextChoices):

#     RECTANGLE = "Rectangle",'Rectangle'

#     ROUND = 'Round' , "Round"

# class WeightChoices(models.TextChoices):

#     HALF_KG = "1/2 kg","1/2 kg"
#     ONE_KG = "1 kg","1 kg"
#     TWO_KG = "2 kg","2 kg"


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    class Meta:

        verbose_name = "Category"

        verbose_name_plural = "Category"

class Shape(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    class Meta:

        verbose_name = "Shape"

        verbose_name_plural = "Shape"

class Weight(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    class Meta:

        verbose_name = "Weights"

        verbose_name_plural = "weights"


class Cake(models.Model):

    name = models.CharField(max_length=50)

    description = models.TextField()

    photo = models.ImageField(upload_to='cake-images')

    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    shape = models.ForeignKey("Shape", on_delete=models.PROTECT)

    weight = models.ForeignKey("Weight", on_delete=models.PROTECT)

    price = models.FloatField()

    def __str__(self):

        return self.name
    

    class Meta:

        verbose_name = 'Cakes'

        verbose_name_plural = 'Cakes'