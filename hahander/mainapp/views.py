import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainapp.models import Mothers
from authapp.models import User
from mainapp.models import Read


def main(request):
    users = list(User.objects.all().exclude(image='users_image/11.png').exclude(image=''))
    ri = random.randint(0, len(users)-1)
    context = {'u': users[ri]}
    return render(request, 'mainapp/index.html', context)


def likes(request):
    user_select = request.user.id
    mam = list(set(Mothers.objects.all().filter(mom_id=user_select).values_list('mom_like_id_user', flat=True)))
    m = User.objects.all().filter(id__in=mam)
    context = {'moms': m}
    return render(request, 'mainapp/likes.html', context)


def like_mom(request, mom):
    if request.method == 'GET' and mom != request.user.id:
        mom = Mothers.objects.create(mom_like_id_user=request.user.id, mom_id=mom)
        mom.save()
    return HttpResponseRedirect('/')


def read(request):
    context = {'rd': Read.objects.all()}
    return render(request, 'mainapp/read.html', context)
