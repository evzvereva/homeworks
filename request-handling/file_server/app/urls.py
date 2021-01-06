from django.urls import path, register_converter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from django.utils.datetime_safe import datetime

from app.views import file_list, file_content

import datetime


class DataConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.datetime.strptime(value, self.format)

    def to_url(self, value: datetime):
        return value.strftime(self.format)


register_converter(DataConverter, 'dt')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<dt:date>/', file_list, name='file_list'),  # задайте необязательный параметр "date"
    # для детальной информации смотрите HTML-шаблоны в директории templates
    path('file/<name>/', file_content, name='file_content'),
]
