from django.contrib import admin
from .models import Item, Order, OrderItem,Type,Profile

class OrderItemInLine(admin.TabularInline):
    model = OrderItem


class OrderInLine(admin.ModelAdmin):
    inlines = (OrderItemInLine,)


admin.site.register(Item)
admin.site.register(Type)
admin.site.register(Profile)
admin.site.register(Order, OrderInLine)
