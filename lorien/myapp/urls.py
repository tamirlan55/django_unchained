from django.urls import path
from myapp.views import test_page, id_item

app_name = 'myapp'

urlpatterns = [
    #http://127.0.0.1:8000/myapp/test_page
    path('', test_page),
    path('<int:my_id>/', id_item, name = 'detail'),
]