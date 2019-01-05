from django.conf.urls import url
from . import views



app_name="web_app"

urlpatterns = [
    url(r'^$', views.all_notes ,name='all_notes'),
    url(r'^(?P<id>\d+)$',views.detail ,name='detail'),
    url(r'^add$', views.note_add,name='add_note'),
    url(r'^(?P<id>\d+)/edit$',views.edit ,name='edit'),
]
