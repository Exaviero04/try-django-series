from django.db import models
from django.urls import reverse
# Create your models here.
class db_project(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(default="yo")
    price = models.DecimalField(max_digits=400,decimal_places=2)
    summary=models.TextField(default="random_stuff")

    def get_absolute_url(self):
        return reverse("db_related:details", kwargs={"my_id": self.id}) #f"/create/{self.id}/update"
