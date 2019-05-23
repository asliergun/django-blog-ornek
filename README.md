# Django Blog Yapımı

Başlangıç: Git anlatımı .gitignore sayfası Sqllite3 kaldırma
Github kaydolun ve aşağıdaki linkten yeni bir repostory oluşturun.
https://github.com/new

Private Repostory seçin. (Her gizli repostory'niz için 3 adet ücretsiz collabrators ekleyebilirsiniz).

Repostory aşağıdaki gibi gösterin.

![repostory-olusturma](https://user-images.githubusercontent.com/24297924/58251047-67ebf380-7d6b-11e9-9827-81d99454bc58.png)

github repostory'nizin ayarlar sayfasını açın.

Collaborators açın.

Açtığınız url

```
https://github.com/kullanıcı-adı/repostory-adı/settings/collaboration

```
yukarıdaki gibi olacaktır.

Buraya bu proje için `asliergun` kullanıcı adını eklemeniz gerekiyor.

`asliergun` ekledikten sonra Add collaborator butonuna basın.

Aşağıdaki ekrandaki gibi olacaktır.

![github-ayari2](https://user-images.githubusercontent.com/24297924/58250881-0af03d80-7d6b-11e9-91fd-a5f733ed88b6.png)


<hr>

.gitignore seçeneğinde Python seçin.

Create Repostory'e basın ve repostory'i oluşturun. 

Repostorynizi açın ve .gitignore dosyanıza basın. 

Düzenle (Edit this file) butonuna basın.

`db.sqlite3` yazan satırın başına # koyun `#db.sqlite3` olarak aşağıdaki gibi kaydedin.

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
#db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

```

gitignore dosyası projede kullanacağımız db.sqlite3 git sunucusuna gönderilmesini engelliyecekti. Şu anda engellemiyecek. 

Github Desktop Bilgisayarınıza kurun. 

Giriş yapın.

Repostorynizi clonelayın.

Repostory oluşturduğunuz yeri açın.

Öneri: Visual Studio Code kurulumu yaparak Django kodlayın. Zorunlu değil ama daha kolay olur. 

![vscode](https://user-images.githubusercontent.com/24297924/58251274-e8aaef80-7d6b-11e9-9990-5eb7104f5cf7.png)

aşağıdaki gibi Extensions basın (Sol taraftaki 5. seçenek)

Buradaki arama textbox'ına 
        1. Django
        2. Django Snippets
        3. Django Template
        
extensionslarını kurun. 

Github desktop üzerinden repostory'nizin bulunduğu konumda Visual Studio Code açın.

Herhangi bir değişiklik yapınca Github Desktop'u açın.

![github-desktop-1](https://user-images.githubusercontent.com/24297924/58251678-e1381600-7d6c-11e9-94d0-343a1ecf07bf.png)

Gördüğünüz gibi değişiklikler sol tarafta gözüküyor.

<hr>
Summary yazan textbox'a yaptığınız işleri yazabilirsiniz. Ben örnek olarak "Kodlar Eklendi" yazdım.

![github-desktop-sol](https://user-images.githubusercontent.com/24297924/58251757-16446880-7d6d-11e9-8633-2206c511f37d.png)

<hr>

Artık Sağ üstte gördüğümüz gibi "Push Origin" yazan butona basın. Artık yazdığımız kodlar Github üzerindeki Repostory'mizin içerisine yüklendi.
![github-push](https://user-images.githubusercontent.com/24297924/58251832-560b5000-7d6d-11e9-85fe-0b2ae697b7f4.png)

<hr>

1. Python 3 Kurun

    Web sitesi: https://www.python.org/ üzerinden indirebilirsiniz.
    WINDOWS Üzerinden kurulum yaparken:
        
        1.Python kurulum dosyasını çalıştırın.
        2. Çıkan ekranda "Add Python 3.5 PATH" seçin.
        3. Çıkan ekrandan "Custom installation" basın ve çıkan ekranda bütün maddeleri seçin.
        4. Kurulumu yapın.
        5. Başlata basın ve cmd yazın.
        6. cmd ekranında `python --version` yazın
        7. Çıkan ekran Python 3 yazıyorsa herhangi bir sorun yok demektir.
        8. `pip --version` yazın.
        9. Eğer pip versiyonu yazıyorsa sorun yok demektir.
        10. Eğer herhangi bir sorun çıkıyorsa bu https://www.youtube.com/watch?v=S__m5v7HiD4 videodan izleyerek gerekli Python ayarlarını yapın.
        11. `pip install django` yazarak django kurulumu yapın.
        12. Kurulum bittikten sonra `django-adimin --version` yazarak django versyonunu kontrol edin.
        13. Eğer django versiyonu yazıyorsa bir sorun yok demektir.
        14. Eğer django versiyonu yazmıyorsa Python kurulu olan dizine gidin.
        15. Python dosyasındaki Scripts klasörünü bulun ve yukarıdaki videodaki gibi Ortam değişkenlerine Scripts dizinini ekleyin.
        16. Eğer tekrardan olmadıysa bu: https://www.youtube.com/watch?v=FGkumuOxEZA&list=PLPrHLaayVkhny4WRNp05C1qRl1Aq3Wswh&index=2 videoyu izleyerek windows kurulumunu yazın.
        17. Eğer tekrar olmazsa: Bilgisayar > Özellikler > Gelişmiş sistem ayarları(Sol tarafta)>Ortam Değişkenleri>PATH (Çift tıklayın)>
            ```
             PYthon37 dosya konumu
             Python37\Scripts\ dosya konumu
            ```
            kaydedin.


![python-path](https://user-images.githubusercontent.com/24297924/58249487-b5fef800-7d67-11e9-932b-ae2b5be3a38d.jpeg)


4. Django Proje Oluşturma
```
django-admin startproject EasyBlog
```
Kodunu terminalde çalıştırdığımızda bulunduğumuz konumda EasyBlog adlı bir dosya oluşacaktır.
```
cd EasyBlog
```
EasyBlog Django Proje dosyasının içine girdik. Şu anda bulunan dosyalar 
```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-manage.py 
```
EasyBlog klasöründeki dosyaları incelersek:

`__init__.py`: İçi boş olarak gelir. `from EasyBlog import ....` gibi ifadelerde kullanılarak içerisindeki fonksiyonlar çağırılabilir. (Şu anda boş bırakılıdır).

`settings.py` Projenin ayarlar dosyasıdır. Veri tabanı bağlantısı gibi bir sürü ayarlar bu dosyadadır. Dosyanın içeriğini incelersek:

`INSTALLED_APPS` dizisi = Projemizdeki kullanacağımız Django uygulamalarının kayıtlı olduğu yerdir.
`ROOT_URLCONF`: Projemizdeki ilk çalışacak urllerin kayıtlı olduğu dosya.
`TEMPLATES`: Projemizdeki kullanacağımız Template dosyaları ve ayarlarının kayıtlı olduğu yerdir.
`WSGI_APPLICATION` : Web Server Gateway Interface (Web Sunucusu Ağ Geçidi Arabirimi) ayarlarının olduğu dosyadır. 
`DATABASES` : Veri tabanı ayarlarının olduğu yerdir.
`LANGUAGE_CODE` : Dil kodudur. `LANGUAGE_CODE = 'tr-tr'` olarak Djangoyu Türkçe yapabilirsiniz.
`TIME_ZONE`: Tarih ve Saat kodudur. `TIME_ZONE = 'Europe/Moscow'` olarak Türkiye yapabilirsiniz.
`STATIC_URL = '/static/'`: Static dosyalarımızın olacağı konumdur.
`MEDIA_URL = '/media/'`: Media dosyalarımızın olacağı konumdur.



`urls.py` Projenin ilk çalışacağı url dosyasıdır. localhost:8000/.... gibi urller gelince hangi sayfalar geleceğinin ayarlarının yapıldığı yerdir.

. Dosyanın içeriğini incelersek:
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Yukarıda yazılan bu kod localhost:8000/admin url'si çalışınca otomatik olarak django admin sayfası gelecektir.
5. Django App oluşturma
Aşağıdaki kodu proje dizininde çalıştırın.
```
python manage.py startapp EasyBlog_blog
```
Bu kod manage.py dosyasının startapp parametresi gönderip yeni bir uygulama oluşturmamızı sağlar. (Herhangi bir sorun almanız durumunda `ls` komutu ile bulunduğunuz dizinde manage.py olduğundan emin olun)

Django Uygulamanızı oluşturduktan sonra settings.py içerisinde `INSTALLED_APPS` ekletin.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EasyBlog_blog',
]
```

Dosya Düzeni:

```
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
```
EasyBlog_blog Django uygulamasının içerisindeki dosyaları anlatmak gerekirse: 
`models.py` : Django projesinin içerisinde kullanacağımız ve oluşturduğumuz Django uygulamasıyla ilgili Veri tabanı Tablolarının oluşturulacağı dosyadır. Model Class'ları yazarak tablolar oluşturulur.
`admin.py`: Oluşturduğumuz modellerin Django Admin sayfasında görüntülememiz için gereken dosyadır.
`tests.py`: Django uygulamamızın testlerini yazdığımız dosyadır.
`views.py` : Django Uygulamamızın herhangi bir url çalışınca ne olacağını gösteren dosyadır.
`migrations` klasörü: Burada herhangi bir migrate yani model oluşturduğumuzda otomatik olarak veri tabanı yaratılma dosyalarının olduğu yerdir. İçi boş olarak gelir. Veri tabanı resetlenmesi istenirse içerisindeki migrate dosyaları silinip tekrar migrate yaparak veri tabanı oluşturulabilinir.

7. Model Oluşturma - Migrate işlemi
EasyBlog_blog/models.py dosyasını açın.
Aşağıdaki class'ı models.py dosyasına yazın.
```python
class Blog(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı Adı")
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    thumbnail = models.ImageField(blank=True, null=True, verbose_name="Blog Thumbnail", upload_to='images/blog/thumbnail/')
    created_date = models.DateTimeField(auto_now=True, verbose_name="Oluşum Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

```
7. Model field alanları

Yukarıda oluşturduğumuz Blog Modelindeki fieldları açıklayalım.

`verbose_name` = Oluşturulan alanın dışarıda gözükeceği tekil alandır.

`verbose_name_plural` = Oluşturulan alanın dışarıda gözükeceği çoğul alandır.

`author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı Adı")` : ForeignKey 
Herhangi bir oluşturduğumuz tablodan veriler id ile kaydolur. Şu anda Django'nun içerisindeki User Tablosundaki (Kullanıcılar tablosu) kullanıcıların sadece bu alanda seçilebileceğini kaydettik. Bu alanda seçili olan kullanıcının otomatik olarak Id si kaydolur. Ama herhangi bir kullanıcı id'si ile kaydet SQL sorgusu yazılmaz. Otomatik olarak seçilen kullanıcının id kaydolur.

`title = models.CharField(max_length=120, verbose_name="Başlık")`: Maksimum 120 Char karakteri olabilecek alan.

`content = TextField(verbose_name="İçerik")` : Herhangi bir sınırlama olmadan istenilen kadar Char karakteri kayıtolur.

`thumbnail = models.ImageField(blank=True, null=True, verbose_name="Blog Thumbnail",null=True, upload_to='images/blog/thumbnail/')` Resim olarak kaydedilebilecek alandır. Herhangi bir resim kaydolunca settings.py dosyasındaki MEDIA_URL alanına otomatik olarak kaydolur. MEDIA_URL altındaki kaydolan media urlsinin altında `images/blog/thumbnail` dosyasına resim kaydolur. Eğer böyle bir dosya dizini yoksa otomatik olarak oluşturulur. settings.py içerisinde 

```
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

satırları eklenmezse hata alınır.

`created_date = models.DateTimeField(auto_now=True, verbose_name="Oluşum Tarihi")` : Tarih alanıdır. auto_now=True parametresi kullanıldığından ötürü herhangi bir şekilde kayıt ekleme veya silme işlemi yapılamaz. Otomatik olarak kaydolan zaman kaydolur.

8. Migrate Oluşturma
```
python manage.py makemigrations
```
makemigrations : Django Projemize settings.py içerisindeki `INSTALLED_APPS` bölümünde kayıtlı olan Django Uygulamalarının içerisindeki models.py dosyalarında herhangi bir dosya değişikliği yapılıp yapılmadığını kontrol eder. Eğer bir değişiklik yapılmışsa bunu terminal ekranında gösterir. Eğer veri tabanında oluşabilecek bir hata bulunursa Error mesajı olarak gösterir.

```
python manage.py migrate
```
migrate: Eğer makemigrations komutundan sonra başarılı bir makemigrations alınmışsa veri tabanında oluşturulacak veri tabanı komutlarını çalıştırır. Sonuç olarak herhangi bir bir hata bulunursa Error mesajı olarak gösterir.

Not: `python manage.py migrate` komutunu herhangi bir tablo oluşturmadan çalıştırıldığında django uygulamalarının içindeki models.py dosyaları çalıştırılarak tablolar oluşur. Bu tablolar settings.py içerisindeki INSTALLED_APPS deki kayıtlı olan django uygulamalarıdır.

Not 2: Her zaman ilk makemigrations daha sonra migrate yapılmalıdır.

```
python manage.py makemigrations
python manage.py migrate
```


Not 3: Eğer `No changes detected` hatası aldıysanız settings.py içerisindeki INSTALLED_APPS bölümünde oluşturduğunuz Django Uygulamasını kontrol edin.


9. Django Projesi oluşturma ve Django Admin Paneli

Django Paneline giriş yapmak için superuser oluşturulması gerekir.


```
python manage.py createsuperuser
```
Kodunu çalıştırarak Django superuser oluşturun.

Super User bütün yetkilere sahip olan django kullanıcısıdır.


```
python manage.py runserver
```

kodunu çalıştırdığımızda otomatik olarak localhost:8000 portunda projemiz çalışmaya başlayacaktır. 
 
Not: Eğer hata alırsanız settings.py dosyasında Debug = False olduğundan emin olun.

http://localhost:8000/ urlsinde ilk django sayfamız gelir. 

http://localhost:8000/admin urlsini girdiğimizde Django Yönetimi Giriş Paneli gelir. Daha önce oluşturduğumuz superuser kullanıcı adı ve şifresiyle giriş yapın.

Şu anda Kullanıcılar ve Gruplar sekmelerini görüyoruz. Kullanıcılar sekmesinden yeni kullanıcı ekleyebilir, kullanıcı silebilir, tüm kullanıcıları görebilirsiniz.

Daha önce oluşturduğumuz EasyBlog_blog uygulamasındaki Blog modelini görebilmek için EasyBlog_blog/admin.py dosyasını açın.

Aşağıdaki gibi kaydedin.

```python
from django.contrib import admin
from EasyBlog_blog.models import Blog

admin.site.register(Blog)
```



Şu anda http://localhost:8000/admin yenilediğimizde EASYBLOG_BLOG sekmesini ve Bloglar URLsini admin panelimizde görüyoruz.

Bloglar urlsine tıklayınca yeni blog ekleyebilir, blog silebilir, tüm blogrı görebilirsiniz.

9. Url oluşturma (Include Yapısı)
EasyBlog/urls.py dosyasını açın.

Aşağıdaki gibi yazıp kaydedin.

```python
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include("EasyBlog_blog.urls")),
]

```
Şuanda http://localhost:8000 urlsini girince EasyBlog_blog uygulamasının içerisindeki urllerimiz çalışacak.

Tabi bunun için EasyBlog_blog django uygulamasının içine urls.py dosyasını oluşturun.

EasyBlog_blog/urls.py dosyasını aşağıdaki bilgileri girin ve kaydedin. 

```python
from django.conf.urls import url
from EasyBlog_blog.views import IndexView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name = 'EasyBlog_blog'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Şu anda 
1. http://localhost:8000 urlsi girince EasyBlog_blog urlleri çalışacak.
2. EasyBlog_blog django uygulamasının içerisindeki urls.py içerisindeki herhangi bir url gelmeyince (yani http://localhost:8000 urlsi / gelince)  EasyBlog_blog içerisine views yazacağımız IndexView çalışacak.
<hr>

EasyBlog_blog/views.py dosyasını aşağıdaki bilgileri girin ve kaydedin. 
```python
from django.shortcuts import render, HttpResponse

def IndexView(request):
    return HttpResponse("Hello World")

```
Şu anda 
1. http://localhost:8000 urlsi girince EasyBlog_blog urlleri çalışacak.
2. EasyBlog_blog django uygulamasının içerisindeki urls.py içerisindeki herhangi bir url gelmeyince (yani http://localhost:8000 urlsi / gelince)  EasyBlog_blog içerisine yazdığımız IndexView çalışacak.
3. EasyBlog_blog/views.py içerisindeki IndexView "Hello World" HttpResponse'unu gönderiyor. Buda http://localhost:8000 girince "Hello World" yazısını çıkarıyor.

11. Template oluşturma

Templateler son kullanıcının gördüğü arayüzdür.

settings.py içerisindeki `TEMPLATES` bölümündeki `'DIRS'` içerisine `['templates'],` yazın.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Şu anda herhangi bir template göstermek istediğimizde django, django projemizin içerisinde templates adlı klasörün içerisindeki template dosyaları çalışacak.

Bunun için django projemizin içerisine templates dosyası oluşturun. (Aşağıdaki gibi dizin yapısı olmalı)

```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
-manage.py
```
EasyBlog_blog/views.py dosyasını açın ve aşağıdaki gibi girin.

```python
from django.shortcuts import render, HttpResponse

def IndexView(request):
    return render(request, "web/index.html")

```
Şu anda IndexView çalışınca templates klasörü altındaki web klasörü altındaki index.html dosyası çalışacak.

`return render(request, "web/index.html")` = templates/web/index.html dosyasını çalıştır demek.

Bunun için templates klasörünün içerisine web klasörü oluşturun.

```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
-manage.py
```

Oluşturduğumuz web klasörünün içine index.html dosyasını oluşturun.

```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
        -index.html
-manage.py
```

templates/web/index.html dosyasının içine aşağıdaki gibi girip kaydedin.

```html
<!doctype html>
<html lang="en">
  <head>
    <title>EasyBlog</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>
  <body>
      <h1>Index Template'inden yazıldı</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" ></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
```

Şu anda IndexView kullandığımız url templates/web/index.html html sayfasını çalıştıracak. Kontrol etmek için http://localhost:8000/ urlsine gidin.


12. Static oluşumu
Proje dizininde static dosyası oluşturun. 
settings.py dosyasında INSTALLED_APPS de `'django.contrib.staticfiles',` ekli olduğundan emin olun.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EasyBlog_blog',
]

```

settings.py dosyasında 
```python
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
```
satırını ekleyin.

Proje dizininde static adlı klasör oluşturun.

```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
        -index.html
-static
-manage.py
```

oluşturduğumuz static klasörünün altında web adlı klasör oluşturun.
```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
        -index.html
-static
    -web
-manage.py
```
Oluşturduğumuz web klasörünün altında css adlı klasör oluşturun.
```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
        -index.html
-static
    -web
        -css
-manage.py
```
Oluşturduğumuz css adlı klasörün içinde style.css CSS dosyasını oluşturun.

```
-EasyBlog
    -__init__.py
    -settings.py
    -urls.py
    -wsgi.py
-EasyBlog_blog
    -migrations
        -__init__.py
    -__init__.py
    -admin.py
    -apps.py
    -models.py
    -tests.py
    -views.py
-templates
    -web
        -index.html
-static
    -web
        -css
            -style.css
-manage.py
```

style.css dosyasının içerisine aşağıdaki css'i girin ve kaydedin.

```css
h1{
    color: blue;
}

```
Oluşturduğumuz templates/web/index.html dosyasına gidin ve aşağıdaki gibi kaydedin.

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>EasyBlog</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{% static 'web/css/style.css' %}">
  </head>
  <body>
      <h1>Index Template'inden yazıldı</h1>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
```

`{% load static %}` = static dosyalarının bu templatede kullanılacağını gösteriyor.

`<link rel="stylesheet" href="{% static 'web/css/style.css' %}">` = static/web/css/style.css kullanılacağını gösteriyor. 

Böylelikle artık style.css yazdığımız css'ler templatelerimizde kullanılabilecek.

13. HTML Template oluşturup extends oluşturma

EasyBlog_blog/views.py içerisinde aşağıdaki gibi AboutView oluşturun.

```python
def AboutView(request):
    return render(request, 'web/about.html')
```
templates/web/about.html dosyasını oluşturun.
```
-templates
    -web
        -index.html
        -about.html
```
about.html dosyasına aşağıdaki bilgileri girin.

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>Hakkında</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{% static 'web/css/style.css' %}">
  </head>
  <body>
      <h1>Hakkında Sayfası</h1>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
```

EasyBlog_blog/urls.py içerisine hakkinda urlsini aşağıdaki gibi ekleyin.

```python
from django.conf.urls import url
from EasyBlog_blog.views import IndexView, AboutView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name = 'EasyBlog_blog'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^hakkinda/', AboutView, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```

Artık localhost:8000/hakkinda urlsi girilince AboutView'ı çalışacak. AboutView'ı web/about.html'i çalıştıracak.

<hr>

index.html ve about.html sayfalarındaki css ve js dosyaları aynı. Bu dosyaları tekrardan yazmak yanlış bir kullanımdır. Bunun yerine base.html adlı bir dosya oluşturup bu dosyadan extends etmek doğrudur.

## base.html yapımı
Aşağıdaki gibi templates/web/base.html dosyasını oluşturun.

```
-templates
    -web
        -index.html
        -about.html
        -base.html
```
base.html aşağıdaki gibi oluşturun.

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>{% block headerTitle %} {% endblock headerTitle %}</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{% static 'web/css/style.css' %}">
    {% block pageHeader %}

    {% endblock pageHeader %}
  </head>
  <body>
    {% block content %}

    {% endblock content %}

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    {% block pageJs %}

    {% endblock pageJs %}
  </body>
</html>
```

Yazdığımız block'ları diğerki html sayfalarında kullanacağız.

Blockları tanımlamak gerekirse: 
`{% block headerTitle %} {% endblock headerTitle %}` = Sayfa title'ı
`{% block pageHeader %} {% endblock pageHeader %}` = Sayfada header html bloğunun içinde yazılacak ekstra css veya js dosyaları yolu veya style'ı.
`{% block content %} {% endblock content %}` = Sayfa body bloğu içeriği.
`{% block pageJs %} {% endblock pageJs %}` = html sonuna eklenebilecek js kodları bloğu.

base.html kaydettikten sonra index.html ve about.html aşağıdaki gibi değiştirin.

index.html
```html
{% extends "web/base.html" %}
{% load static %}
{% block headerTitle %}EasyBlog {% endblock headerTitle %}

{% block content %}
<h1>Index Template'inden yazıldı</h1>
{% endblock content %}
```

about.html
```html
{% extends "web/base.html" %}
{% load static %}
{% block headerTitle %}Hakkında {% endblock headerTitle %}

{% block content %}
<h1>Hakkında Sayfası</h1>
{% endblock content %}
```

Yukarıdaki gibi {% extends "web/base.html" %} yazılınca web/base.html içerisindeki bütün özellikler eklediğimiz .html sayfasına importlanıyor.

base.html'e yazdığımız blockların içerisine yazdıklarımız base.html'de nerede yazdıysak orada yazılıyor.

14. Anasayfaya Blog Tüm Blog Yazılarını görüntüleme (Blog.objects.all())
EasyBlog_blog/views.py dosyasını açın. Aşağıdaki kodu ekleyin

```python
from EasyBlog_blog.models import Blog
```
Bu kod EasyBlog_blog Django uygulamasının içerisindeki models.py içerisindeki Blog Model'ini şu anki views.py dosyasının içerisine getiriyor.

IndexView'u aşağıdaki gibi değiştirin. 
```python
def IndexView(request):
    blog = Blog.objects.all()
    context = {
        "blog": blog
    }
    return render(request, 'web/index.html', context)
```
Şu anda bütün Blog tablosundaki bütün veriler index.html'e blog olarak gidiyor.

index.html dosyasının içerisindeki content block'una aşağıdaki kodları ekleyin.

```html

{% for blogs in blog %}
<div class="row">
    <div class="col-md-10 offset-md-3">

    <!-- Post Content Column -->
    <div class="col-lg-8">

      <!-- Title -->
      <a href="#"><h2 class="mt-4">{{blogs.title}}</h2></a> 
        
      <!-- Author -->
      <p class="lead">
        
        {{blogs.author.username}} tarafından yayınlandı
      </p>

      <hr>

      <!-- Date/Time -->
      <p>{{blogs.created_date}}</p>
      <hr>
      <!-- Preview Image -->
      {% if blogs.thumbnail %}
      <a href="#"><img class="img-fluid rounded" src="{{blogs.thumbnail.url}}" alt=""></a>
      {% endif %}
    
      <hr>
      <a style ="float : right;" href="#" class ="btn btn-danger">Devamını Oku</a>
      <hr>
         
        </div>
      </div>
      </div>

{% endfor %}
```

http://localhost:8000/ urlsine girdiğinizde şu ana kadar yazılı olan tüm blogları görebilirsiniz.

IndexView'unu aşağıdaki gibi `order_by('-created_date')` created_date alanına göre sıralı gelecektir.
```python
def IndexView(request):
    blog = Blog.objects.order_by('-created_date')
    context = {
        "blog": blog
    }
    return render(request, 'web/index.html', context)
```

15. Blog sayfası oluşturmak
EasyBlog_blog/views.py dosyasına BlogDetailView'unu yazın.
```python
def BlogDetailView(request,id):
    blog = Blog.objects.filter(id=id).first()
    context = {
        "blog": blog
    }
    return render(request, 'web/blog-detail.html',context)
```
EasyBlog_blog/urls.py dosyasına BlogDetailView ekleyin.

```python
from django.conf.urls import url
from EasyBlog_blog.views import IndexView, AboutView, BlogDetailView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name = 'EasyBlog_blog'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^hakkinda/', AboutView, name='about'),
    url(r'^blog/(?P<id>\d+)/$', BlogDetailView, name='blog_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



```

Yukarıdaki kod http://localhost:8000/blog/1 gibi Blog modelinin id alanı gönderildiğinde gelecek olan sayfadır.

index.html sayfasındaki content bloğunu aşağıdaki gibi url bloklarını ekleyin.


```html

{% for blogs in blog %}
<div class="row">
    <div class="col-md-10 offset-md-3">

    <!-- Post Content Column -->
    <div class="col-lg-8">

      <!-- Title -->
      <a href="{% url 'EasyBlog_blog:blog_detail' id=blogs.id %}"><h2 class="mt-4">{{blogs.title}}</h2></a> 
        
      <!-- Author -->
      <p class="lead">
        
        {{blogs.author.username}} tarafından yayınlandı
      </p>

      <hr>

      <!-- Date/Time -->
      <p>{{blogs.created_date}}</p>
      <hr>
      <!-- Preview Image -->
      {% if blogs.thumbnail %}
      <a href="{% url 'EasyBlog_blog:blog_detail' id=blogs.id %}"><img class="img-fluid rounded" src="{{blogs.thumbnail.url}}" alt=""></a>
      {% endif %}
    
      <hr>
      <a style ="float : right;" href="{% url 'EasyBlog_blog:blog_detail' id=blogs.id %}" class ="btn btn-danger">Devamını Oku</a>
      <hr>
         
        </div>
      </div>
      </div>

{% endfor %}

```

`{% url 'EasyBlog_blog:blog_detail' id=blogs.id %}` bu kod `blog_detail` olarak tanımladığımız url'ye id paremetresi gönderiyor.

<hr>
## objects.get(id=id) metodu

```python
def BlogDetailView(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog": blog
    }
    return render(request, 'web/blog-detail.html',context)
```
yukarıdaki kod sayesinde `Blog.objects.filter(id=id).first()` yazmadan `Blog.objects.get(id=id)` get yazarak direkt object getirilebilir.

16. Navbar ekleme
templates/web/components klasörünü oluşturun.

```
-templates
    -web
        -components
        -index.html
        -about.html
        -base.html
```
components klasörü içine header.html dosyasını oluşturun.
```
-templates
    -web
        -components
            -header.html
        -index.html
        -about.html
        -base.html
```

header.html dosyasını aşağıdaki gibi oluşturun.

```html
<nav class="navbar navbar-dark bg-dark">
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="{% url 'EasyBlog_blog:homepage'  %}">Blog</a>
        
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'EasyBlog_blog:about'  %}">Hakkımızda</a>
            </li>
            
          </ul>
        </div>
</nav>
```

{% url 'EasyBlog_blog:homepage'  %} gibi url blokları sayesinde EasyBlog_blog/urls.py içerisinde tanımladığımız urlleri kullanabiliriz. Bunun en büyük faydası eğer url değişirse buradaki url de değişecek. Böylelikle sabit bir url yazmaktan kurtulmuş olunur.

base.html dosyasını aşağıdaki gibi `{% include "web/components/header.html" %}` ekleyin.

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>{% block headerTitle %} {% endblock headerTitle %}</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{% static 'web/css/style.css' %}">
    {% block pageHeader %}

    {% endblock pageHeader %}
  </head>
  <body>
  {% include "web/components/header.html" %}
    {% block content %}

    {% endblock content %}

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    {% block pageJs %}

    {% endblock pageJs %}
  </body>
</html>

```
  
Àrtık bütün base.html extends edilen sayfalarda navbar olacaktır.

17. İletişim sayfası yapımı

EasyBlog_blog/models.py aşağıdaki Contact Modelini ekleyin.

```python
class Contact(Model):
    name = models.CharField(max_length=50, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name='Email Adresi', blank=False, null=False)
    title = models.CharField(max_length=200, verbose_name="Başlık")
    message = models.TextField(blank=True, null=True, verbose_name='Mesaj')
    created_date = models.DateTimeField(auto_now=True, verbose_name="Tarih")

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişimler'

    def __str__(self):
        return self.title

```

```
python manage.py makemigrations
python manage.py migrate

```
EasyBlog_blog/forms.py dosyasını oluşturun ve aşağıdaki kodları ekleyin.

```python
from django import forms
from django.forms import ModelForm, TextInput
from djangoecommerce_app.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "title", "message"]
        widgets = {
            'name': TextInput(attrs={'id': 'input_name','class':'form-control', 'name': 'your-name', 'placeholder':'Name'}),
            'email': TextInput(attrs={'id': 'input_email','class':'form-control', 'name': 'your-email', 'placeholder':'Email'}),
            'subject': TextInput(attrs={'id': 'subject','class':'form-control', 'name': 'your-subject', 'placeholder':'Subject'}),
            'message': TextInput(attrs={'id': 'subject','class':'form-control', 'name': 'your-message', 'placeholder':'Message'}),
}

```
EasyBlog_blog/views.py içerisine aşağıdaki gibi ContactView oluşturun.

```python
def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        Contact = form.save(commit=True)
        return redirect("EasyBlog_blog:contact")
    context = {
        "form": form
    }
    return render(request, 'web/contact.html',context)
```
teplates/web/contact.html dosyasını oluşturun ve aşağıdaki gibi doldurun.

```html
{% extends "web/base.html" %}
{% load static %}
{% block headerTitle %}İletişim {% endblock headerTitle %}

{% block content %}
<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">
        Kaydet
    </button>
</form>
{% endblock content %}
```

EasyBlog_blog/urls.py iletisim ekleyin

```python
from django.conf.urls import url
from EasyBlog_blog.views import IndexView, AboutView, BlogDetailView, ContactView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name = 'EasyBlog_blog'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^hakkinda/', AboutView, name='about'),
    url(r'^blog/(?P<id>\d+)/$', BlogDetailView, name='blog_detail'),
    url(r'^iletisim/', ContactView, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```
Artık http://localhost:8000/iletisim sayfasından iletişim tablosuna kayıt yapılabilir.

20. Giriş yapan kullanıcı kontrolü
Herhangi bir viewsın kayıtlı kullanıcı olup olmadığının kontrolü @login_required decorator ile yapılır.

İlk olarak import edin
```python
from django.contrib.auth.decorators import login_required
```

İkinci olarak settings.py dosyasına `LOGIN_URL = 'login/'`login urlnizi ekleyin.


Daha sonra hangi view'un sadece login olan kullanıcıların giriş yapmasını istiyorsanız üstüne `@login_required` ekleyin.

```python
@login_required
def ExampleLoginRequiredView(request):
    return render(request, 'web/index.html')
```

Böylelikle sadece login olan kullanıcılar bu viewu ve bu view'a bağlı olan URL'leri kullanabilir. Eğer herhangi bir giriş olmadıysa settings.py'deki LOGIN_URL çalışır.
