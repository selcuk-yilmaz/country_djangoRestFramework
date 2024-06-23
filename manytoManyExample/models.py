from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # ... (Diğer müşteri ile ilgili alanlar)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)

    # Ağırlık Seçenekleri
    WEIGHT_UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('gr', 'Gram'),
        ('adet', 'Adet'),
    )
    weight_unit = models.CharField(max_length=4, choices=WEIGHT_UNIT_CHOICES, blank=True)  # max_length düzeltildi
    weight_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.0)  # Set default to 0.0

    # Adet Seçenekleri
    QUANTITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    quantity = models.PositiveIntegerField(choices=QUANTITY_CHOICES, blank=True, default="1")  # Allow null values

    def __str__(self):
        return f"{self.name} ({self.weight_value}{self.get_weight_unit_display()} - {self.quantity}{self.get_quantity_unit_display()})"

    def get_weight_unit_display(self):
        return self._get_display(self.weight_unit)

    def get_quantity_unit_display(self):
        return self._get_display(self.quantity)

    def _get_display(self, value):
        for key, value_display in self._meta.get_field('weight_unit').choices:
            if value == key:
                return value_display
        return value

class Order(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    product = models.ManyToManyField(Product, related_name='product')



# # Bu satır, çoklu-çoklu ilişki tablosunu oluşturur
# class CustomerProduct(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order = models.ForeignKey(Product, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     # Ek alanlar (sipariş miktarı ve uygulanan indirim gibi)
#     siparis_miktari = models.DecimalField(max_digits=10, decimal_places=2)
#     uygulanan_indirim = models.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         unique_together = (('customer', 'order'),)  # Bir müşterinin aynı siparişi iki kez verememesini sağlar



