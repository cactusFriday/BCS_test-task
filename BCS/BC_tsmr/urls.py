from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'tranc_list'
urlpatterns = [
    # 
    path('', views.index, name='tranc_list'),
    path('<int:tx_id>/', views.transaction, name='tx-id')
]