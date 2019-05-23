from django.conf.urls import url
from EasyBlog_blog.views import IndexView, AboutView, BlogDetailView,ContactView

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
