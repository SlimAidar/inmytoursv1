from django.db import models


class Tour(models.Model):
    stars_choices = (
        (1 ,1),
        (2 ,2),
        (3 ,3),
        (4 ,4),
        (5 ,5),
    )
    title = models.CharField(verbose_name="title for admin", max_length=50)
    image = models.ImageField(upload_to='media/img/tours')
    status = models.BooleanField(default=False, verbose_name="publish it now")
    price = models.IntegerField()
    stars = models.IntegerField(choices=stars_choices)
    feautured = models.BooleanField(default=True)
    destination = models.ForeignKey("tours.Destination", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TourDetail(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    descreption = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Destination(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/img/destinations')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/img/tours')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Book(models.Model):
    tour = models.ForeignKey("tours.Tour", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=500, blank=True, null=True)
    date_book = models.DateTimeField(auto_now_add=True)
