from django.db import models

# Create your models here.
class Item(models.Model):
    measurment_unit = (
        ('Nos', 'Nos'),
        ('Meter', 'Meter'),
        ('Kg', 'Kg'),
        ('Kilo meter', 'Kilo meter'),
    )
    item_code = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_measurement = models.CharField(max_length=50, choices = measurment_unit)
    item_quantity = models.IntegerField()
    item_image = models.FileField(upload_to='static/images', max_length=100, blank=False)
    supplier_name = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    
