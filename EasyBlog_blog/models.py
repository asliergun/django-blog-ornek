from django.db import models


class Blog(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı Adı")
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    thumbnail = models.ImageField(
        blank=True, null=True, verbose_name="Blog Thumbnail", upload_to='images/blog/thumbnail/')
    created_date = models.DateTimeField(
        auto_now=True, verbose_name="Oluşum Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad Soyad")
    email = models.EmailField(
        verbose_name='Email Adresi', blank=False, null=False)
    title = models.CharField(max_length=200, verbose_name="Başlık")
    message = models.TextField(blank=True, null=True, verbose_name='Mesaj')
    created_date = models.DateTimeField(auto_now=True, verbose_name="Tarih")

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişimler'

    def __str__(self):
        return self.title
