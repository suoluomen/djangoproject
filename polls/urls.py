from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'polls'  # 关键是这行
urlpatterns = [
    url(r'^indextest$', views.indextest, name='indextest'),
    url(r'^$', views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]