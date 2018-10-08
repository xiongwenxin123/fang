from django.shortcuts import render
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie


# @cache_page(timeout=300, cache='page')
# @vary_on_cookie
def home(request):
    return render(request, "index.html", {})


def publish(request):
    return render(request, 'publish.html', {})


def search(request):
    pass
