from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^add_category/$', views.add_category, name='add_category'),
		url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
		url(r'^category/(?P<category_name_url>[\w\-]+)/$', views.category, name='category'),  # New!
		url(r'^register/$', views.register, name='register'),
	)