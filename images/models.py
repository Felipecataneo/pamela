from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse



class Paciente(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nome)


    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}'.format(self.nome))


        self.slug = slugify('{}'.format(self.nome))
        self.last_updated = timezone.localtime(timezone.now())
        super(Paciente, self).save(*args, **kwargs)



class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    imagem1 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem1.jpg', upload_to='img1')
    imagem2  = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem2.jpg', upload_to='img2')
    imagem3 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem3.jpg', upload_to='img3')
    imagem4 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem4.jpg', upload_to='img4')
    imagem5 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem5.jpg', upload_to='img5')
    imagem6 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem6.jpg', upload_to='img6')
    imagem7 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem7.jpg', upload_to='img7')
    imagem8 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem8.jpg', upload_to='img8')
    imagem9 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem9.jpg', upload_to='img9')
    imagem10 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem10.jpg', upload_to='img10')
    imagem11 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem11.jpg', upload_to='img11')
    imagem12 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_imagem12.jpg', upload_to='img12')




   ##Related Fiels
    category = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.category.nome)


    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}'.format(self.category.nome))


        self.slug = slugify('{}'.format(self.category.nome))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)
