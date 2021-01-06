from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся

counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    click = request.GET.get('from-landing')
    if click:
        counter_click.update({click})
        # print(click)
    # print(sum(counter_click.values()))

    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    show = request.GET.get('ab-test-arg')
    # print(show)
    counter_show.update({show})
    if show == 'original':
        # print(sum(counter_show.values()))
        return render(request, 'landing.html')
    elif show == 'test':
        # print(sum(counter_show.values()))
        return render(request, 'landing_alternate.html')
    else:
        return render(request, 'index.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    try:
        result = counter_click['original'] / counter_show['original']
    except:
        result = 0.0
    try:
        result2 = counter_click['test'] / counter_show['test']
    except:
        result2 = 0.0
    return render(request, 'stats.html', context={
        'test_conversion': result,
        'original_conversion': result2,
    })
