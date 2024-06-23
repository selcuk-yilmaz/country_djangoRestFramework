from django.contrib import admin
from .models import Customer, Product, Order
# Register your models here.
admin.site.register(Customer)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','weight_unit','weight_value', 'quantity')  # admin arayüzündeki görünen column ile ilgi görmek istediğin özellikleri ekleyebilirsin
    # list_filter = ('available',)
    # search_fields = ('name', 'description')
admin.site.register(Order)