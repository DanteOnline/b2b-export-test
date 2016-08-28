from django.contrib import admin
from goods.models import Good, GoodImage

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'in_stock', 'featured']
admin.site.register(Good, GoodAdmin)

class GoodImageAdmin(admin.ModelAdmin):
    list_display = ['good','image']
admin.site.register(GoodImage, GoodImageAdmin)