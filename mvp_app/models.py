from django.db import models
from pytils.translit import slugify
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name="Категория"
        verbose_name_plural= "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

        

class Job(models.Model):
    title = models.CharField("Название аренды", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    clientname = models.CharField("Имя пользователя", max_length=150)
    description = models.TextField("Описание товара")
    image = models.CharField("URL-фото", max_length=500)
    salary = models.CharField("Цена", max_length=80)
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефоне", max_length=15)
    insta = models.CharField("Инстаграм", max_length=30)
    like = models.CharField("Лайки", max_length=30)
    view = models.CharField("Просмотры", max_length=30)
    created_at = models.DateTimeField("Дата публикации", default=datetime.now)
    

    class Meta:
        verbose_name="Аренда"
        verbose_name_plural= "Аренды"

    def __str__(self):
        return self.title
    

