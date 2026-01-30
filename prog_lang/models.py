from django.db import models

class ProgLang(models.Model):
#CharField-  строковое поле с ограничением по длине
    title = models.CharField(max_length=100, verbose_name='укажите язык программирования')
#TextField-  текстовое поле без ограничения по длине
    description = models.TextField(verbose_name='описание языка программирования')
#ImageField-  поле для загрузки изображений
    image = models.ImageField(upload_to='prog_lang/', verbose_name='загрузите изображение языка программирования')
#PositiveBigIntegerField-  поле для хранения больших положительных целых чисел
    created_date_lang = models.PositiveBigIntegerField(verbose_name='год создания языка', blank=True)
#DateTimeField-  поле для хранения даты и времени
    created_at = models.DateTimeField(auto_now_add=True)
#DateTimeField-  поле для хранения даты и времени



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'
        ordering = ['-created_at']