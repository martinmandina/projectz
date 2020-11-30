from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
        url('^$', views.main, name='index'),
        url(r'^project/$',views.project_new,name='new-project'),
        url(r'^profilenew/$',views.profile_new,name = 'new_profile'),
        url(r'^profile/$',views.profile,name='profile'),
        url(r'^search/',views.project_search, name='search_results'),

  ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



