from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=30, verbose_name='наименование категории')
    category_description = models.CharField(max_length=100, verbose_name='описание категории')

    def __str__(self):
        return f'{self.category_name} - {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=30, verbose_name='наименование товара')
    product_description = models.CharField(max_length=100, verbose_name='описание товара')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='наименование категории')
    price = models.IntegerField(verbose_name='цена за покупку')
    create_date = models.DateField(auto_now=False, auto_now_add=False,
                                   verbose_name='дата создания')
    final_change_date = models.DateField(auto_now=False, auto_now_add=False,
                                         verbose_name='дата последнего изменения')

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Contacts(models.Model):
    contact_name = models.CharField(max_length=30, verbose_name='имя контакта')
    contact_email = models.CharField(max_length=30, verbose_name='email контакта')

    def __str__(self):
        return f'{self.contact_name} - {self.contact_email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('contact_name',)


class Blog(models.Model):
    article_name = models.CharField(max_length=30, verbose_name='заголовок')
    slug = models.CharField(max_length=30, verbose_name='slug')
    contents = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    create_date = models.DateField(auto_now=False, auto_now_add=False,
                                   verbose_name='дата создания')
    publication_date = models.DateField(auto_now=False, auto_now_add=False,
                                        verbose_name='дата публикации')
    views_count = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.article_name} - {self.slug}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('article_name',)
