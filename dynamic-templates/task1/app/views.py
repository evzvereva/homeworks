import os


from django.conf import settings
from django.shortcuts import render
import csv

csv_file = os.path.join(settings.BASE_DIR, 'inflation_russia.csv')



def inflation_view(request):
    template_name = 'inflation.html'
    context = {}
    # чтение csv-файла и заполнение контекста
    with open(csv_file, encoding='utf-8') as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=";")
        list_dict = list(file_reader)
        context['table'] = list_dict
    print(context)

    return render(request, template_name,
                  context)
