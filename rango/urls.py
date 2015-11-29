from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('' , 
                        url(r'^$', views.index, name= 'index'),
                        url(r'^about/$', views.about, name= 'about'),    
                        url(r'^add_category/$', views.add_category, name = 'add_category'),          
                        url(r'^category/(?P<cat_name_slug>[\w\-]+)/$', 
                            views.category2, name = 'category'),
                        url(r'^category/(?P<cat_name_slug>[\w\-]+)/add_page/$',
                            views.add_page, name = 'add_page'),
                        url(r'^login/$', views.user_login, name='user_login'),
                        url(r'^restricted/$', views.restricted, name= 'restricted'),
                        url(r'^logout/$', views.user_logout, name= 'logout'),
                        url(r'^register/$', views.register, name = 'register'),
                        )