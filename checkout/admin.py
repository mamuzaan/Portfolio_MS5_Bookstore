from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    readonly_fields = ('order_number', 'date', 'order_total', 'grand_total', 'genuine_basket', 'stripe_pid',)
    list_display = ('order_number', 'date', 'name', 'email', 'phone_number', 'order_total', 'delivery_cost', 'grand_total',)
    ordering = ('-date',)

    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user_profile', 'name', 'email', 'phone_number', 'date', 'genuine_basket', 'stripe_pid',)
        }),
        ('Delivery Address', {
            'fields': ('street_address', 'town_or_city', 'postcode', 'county', 'country',)
        }),
        ('Order Totals', {
            'fields': ('order_total', 'delivery_cost', 'grand_total',)
        }),
    )


admin.site.register(Order, OrderAdmin)
