import datetime
import os
from django.conf import settings
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    list_files = os.listdir(settings.FILES_PATH)

    files_and_datetime = []
    context = {}

    for files in sorted(list_files):
        stat = os.path.join(settings.FILES_PATH, files)
        time = os.stat(stat)
        st_ctime = time.st_ctime
        st_mtime = time.st_mtime
        file_info = {
            'name': files,
            'ctime': datetime.datetime.fromtimestamp(st_ctime),
            'mtime': datetime.datetime.fromtimestamp(st_mtime)
        }
        files_and_datetime.append(file_info)
        date = file_info['ctime'].date()
        context['date'] = date

    context['files'] = files_and_datetime

    return render(request, template_name, context)


def file_content(request, name):
    with open(os.path.join(settings.FILES_PATH, name)) as f:
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return render(request,
                      'file_content.html',
                      context={'file_name': name, 'file_content': f.read()}
                      )
