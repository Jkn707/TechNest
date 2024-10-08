from django.db import models
from product.models import Product
from user.models import Client
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    reviewingClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    productReviewed = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.productReviewed.name + ' review by ' + self.reviewingClient.user.first_name