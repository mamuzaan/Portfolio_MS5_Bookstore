from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    readonly_fields = ('order_number', 'date', 'order_total_price', 'grand_total_price', 'genuine_basket', 'stripe_pid',)
    list_display = ('order_number', 'date', 'name', 'email', 'phone_number', 'order_total_price', 'delivery_cost', 'grand_total_price',)
    ordering = ('-date',)

    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'name', 'email', 'phone_number', 'date', 'genuine_basket', 'stripe_pid',)
        }),
        ('Delivery Address', {
            'fields': ('street_address', 'town_or_city', 'postcode', 'county', 'country',)
        }),
        ('Order Totals', {
            'fields': ('order_total_price', 'delivery_cost', 'grand_total_price',)
        }),
    )


admin.site.register(Order, OrderAdmin)
