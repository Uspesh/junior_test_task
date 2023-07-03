from django.shortcuts import render


def main_page(request):
    return render(request=request, template_name='online_catalog/index.html', context={'title': 'Главная страница'})
