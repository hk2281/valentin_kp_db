from django.contrib import admin
from .models import Product, Applience,Resources,Provider,Client,ContrAgent


class a_ContrAgent(admin.ModelAdmin):
    list_display = [
        'contrAgent','name','remainder','provider','client'
    ]

class a_Applience(admin.ModelAdmin):
    list_display = [
        'applience','name','resource','coast','manafacture'
    ]


class a_Resources(admin.ModelAdmin):
    list_display = [
        'resouces','name','cost_per_tonna',
    ]

class a_Provider(admin.ModelAdmin):
    list_display = [
        'provider','name','contact','address'
    ]

class a_Client(admin.ModelAdmin):
    list_display = [
        'client','name','last_name','contact','address'
    ]

class a_Product(admin.ModelAdmin):
    list_display = [
        'product','name','cost','amount'
    ]




admin.site.register(Product,a_Product)
admin.site.register(Client,a_Client)
admin.site.register(Provider,a_Provider)
admin.site.register(Resources,a_Resources)
admin.site.register(Applience,a_Applience)
admin.site.register(ContrAgent,a_ContrAgent)