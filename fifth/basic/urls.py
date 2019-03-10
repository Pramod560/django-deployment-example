from django.urls import path
from basic import views

app_name = "basic"

urlpatterns = [

  path("other/",views.other,name='other'),
  path("relative/",views.relative,name='relative')
]
