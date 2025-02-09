from django.db import models
from ckeditor.fields import RichTextField


class Slider(models.Model):
    img = models.ImageField(upload_to='images/', verbose_name='Баннер', null=True, blank=True)
    on_title = models.CharField(max_length=30, verbose_name='Над заголовок')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    under_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Под заголовок')
    button_title = models.CharField(max_length=30, default='Связаться', verbose_name='Имя кнопки')
    click_button = models.CharField(max_length=255, verbose_name='Ссылка', help_text='https://t.me/afina_fabric')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'слайд'
    
class Advantage(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    desc = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='images/', verbose_name='фото иконки')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Блок "почему мы?"'
        verbose_name = 'Блок "почему мы?"'

class WhoWe(models.Model):
    img = models.ImageField(upload_to='images/', verbose_name='фото', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desc = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Блок "кто мы?"'
        verbose_name = 'Блок "кто мы?"'