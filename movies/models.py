from django.db import models
from users.models import User


# Create your models here.
class MovieRatings(models.TextChoices):
    Default = "G"
    PG = "PG"
    PG_13 = "PG_13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default="", null=True)
    rating = models.CharField(
        max_length=20, choices=MovieRatings.choices, default=MovieRatings.Default
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    order = models.ManyToManyField(
        "users.User",
        through="MovieOrder",
        related_name="orders",
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
