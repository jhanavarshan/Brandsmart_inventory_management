from django.db import models

class RawMaterial(models.Model):
    cap = models.IntegerField(default=100)
    powder = models.IntegerField(default=1000)
    container400 = models.IntegerField(default=50)
    container500 = models.IntegerField(default=50)

    def __str__(self):
        return f"Raw Materials: Cap={self.cap}, Powder={self.powder}, Container400={self.container400}, Container500={self.container500}"

class ProductionRecord(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    size = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.quantity} units (Size: {self.size}) at {self.timestamp}"