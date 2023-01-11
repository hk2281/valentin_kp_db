from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator




class Applience(models.Model):

    applience = models.AutoField(primary_key=True, verbose_name='id оборудования')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название')
    resource = models.CharField( max_length = 30, choices=[
        ("плохое","плохое"),
        ("Удовлетворительное","удовлетворительное"), 
        ("хорошее","хорошее")
        ])
    coast = models.FloatField(blank=True, null=True, verbose_name='затрата в час',
     validators=[MinValueValidator(0.0)])
    manafacture = models.CharField(max_length=30,verbose_name='производитель')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о оборудовании')
        verbose_name_plural = _('Оборудование')

class Resources(models.Model):
    
    resouces = models.AutoField(primary_key=True,verbose_name='id ресурса')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название ресурса')
    cost_per_tonna = models.FloatField(blank=True, null=True,verbose_name='стоимость за тонну',validators=[MinValueValidator(0.0)])

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о ресурсах')
        verbose_name_plural = _('ресурсы')


class Product(models.Model):

    product = models.AutoField(primary_key=True,verbose_name='id клуба')
    name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название')
    amount = models.IntegerField(blank=True, null=True,verbose_name='кол-во',validators=[MinValueValidator(0)])
    cost = models.FloatField(blank=True,null=True, verbose_name='цена',validators=[MinValueValidator(0.0)])
    aplience = models.ForeignKey(Applience, on_delete=models.CASCADE,verbose_name='оборудование', blank=True, null=True)
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE,verbose_name='используемые ресурсы', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о продукции')
        verbose_name_plural = _('продукция')

class Provider(models.Model):
    
    provider = models.AutoField(primary_key=True,verbose_name='id провайдера')
    name = models.CharField(max_length=30, unique=True,verbose_name='название')
    contact = models.CharField(max_length=12, verbose_name='контактная информация')
    address = models.CharField(max_length=30, blank=True, null=True,verbose_name='адрес')
    Product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='продукт',blank=True, null=True)

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
        return self.name + " " + self.last_name

    class Meta:
        verbose_name = _('данные о клиентах')
        verbose_name_plural = _('клиенты')

class ContrAgent(models.Model):

    contrAgent = models.AutoField(primary_key=True,verbose_name='id контрагента')
    name = models.CharField(max_length=30, unique=True,verbose_name='имя')
    remainder = models.FloatField(default=0.0, blank=True,validators=[MinValueValidator(0.0)],
    verbose_name='остатоки')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,verbose_name='поставщик')
    client =  models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name='клиент')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('данные о контрагентах')
        verbose_name_plural = _('контрагенты')
