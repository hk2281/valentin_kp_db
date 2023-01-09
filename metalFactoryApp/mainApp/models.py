from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Product(models.Model):

    product = models.AutoField(primary_key=True,verbose_name='id клуба')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название')
    cost = models.CharField(max_length=30,verbose_name='адрес')
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о продукции')
        verbose_name_plural = _('продукция')

class Applience(models.Model):

    applience = models.AutoField(primary_key=True, verbose_name='id оборудования')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название')
    resource = models.CharField( max_length = 30, choices=[
        ("плохое","плохое"),
        ("Удовлетворительное","удовлетворительное"), 
        ("хорошее","хорошее")
        ])
    coast = models.FloatField(blank=True, null=True)
    manafacture = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о оборудовании')
        verbose_name_plural = _('Оборудование')

class Resources(models.Model):
    
    resouces = models.AutoField(primary_key=True,verbose_name='id ресурса')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название ресурса')
    cost_per_tonna = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о ресурсах')
        verbose_name_plural = _('ресурсы')


class Provider(models.Model):
    
    provider = models.AutoField(primary_key=True,verbose_name='id провайдера')
    name = models.CharField(max_length=30, unique=True,verbose_name='имя')
    contact = models.CharField(max_length=12, verbose_name='контактная информация')
    address = models.CharField(max_length=30, blank=True, null=True,verbose_name='адрес')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о поставщиках')
        verbose_name_plural = _('поставщики')

class Client(models.Model):
    
    client = models.AutoField(primary_key=True,verbose_name='id клиента')
    name = models.CharField(max_length=30, unique=True,verbose_name='имя')
    last_name = models.CharField(max_length=30, unique=True,verbose_name='фамилия')
    contact = models.CharField(max_length=12, verbose_name='контактная информация')
    address = models.CharField(max_length=30, blank=True, null=True,verbose_name='адрес')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о клиентах')
        verbose_name_plural = _('клиенты')

class ContrAgent(models.Model):

    contrAgent = models.AutoField(primary_key=True,verbose_name='id контрагента')
    name = models.CharField(max_length=30, unique=True,verbose_name='имя')
    remainder = models.FloatField(default=0.0, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,verbose_name='поставщик')
    client =  models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name='поставщик')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о контрагентах')
        verbose_name_plural = _('контрагенты')
