from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! telegram работает, yt hf,jnftn api')


def second_page(request):
    return HttpResponse('А это вторая страница!')
