from django.shortcuts import render


def main_page(request):
    return render(request, 'articles/main_page.html')
