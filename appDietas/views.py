from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app de dietas de Tecnologias Web do Insper.")
