from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Полное описание')
    price = models.FloatField(db_index=True, verbose_name='Цена, руб.')
    in_stock = models.BooleanField(default=True, db_index=True,
                                   verbose_name='Есть в наличии')
    featured = models.BooleanField(default=False, db_index=True,
                                   verbose_name='Рекомендуемый')
    image = models.ImageField(upload_to='goods/list',
                              verbose_name='Основное изображение')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #Если это не новый товар
        if self.pk:
            this_record = Good.objects.get(pk = self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save = False)
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Good, self).delete(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class GoodImage(models.Model):
    good = models.ForeignKey(Good)
    image = models.ImageField(upload_to='goods/detail', verbose_name='Дополнительное изображение')

    def save(self, *args, **kwargs):
        #Если это не новая картинке
        if self.pk:
            this_record = GoodImage.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        super(GoodImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(GoodImage, self).delete(*args, **kwargs)
    class Meta:
        verbose_name = 'изображение к товару'
        verbose_name_plural = 'изображения к товару'
