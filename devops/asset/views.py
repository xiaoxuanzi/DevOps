# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from ..dbtool import Asset

# @login_required()
def host_list(request):

    asset = Asset()
    hosts = asset.host_list()

    return render(request, 'asset/host_list.html', {'hosts' : hosts})