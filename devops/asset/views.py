# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from devops.util.db import Asset

# @login_required()
def host_list(request):

    asset = Asset()
    hosts = asset.host_list()

    return render(request, 'asset/host_list.html', {'hosts' : hosts})

def host_edit(request):

    asset = Asset()
    if request.method == 'GET':

        private_ip = request.GET.get('private_ip')

        host = asset.host_query(private_ip)

        return render(request, 'asset/host_edit.html', {'host' : host})

    private_ip = request.POST.get('private_ip')
    status     = request.POST.get('status')

    asset.host_update_status(private_ip, status)

    host = asset.host_query(private_ip)

    return render(request, 'asset/host_edit.html', {'host' : host})

def host_delete(request):

    private_ip = request.GET.get('private_ip')

    asset = Asset()
    hosts = asset.host_list()

    asset.host_delete(private_ip)

    return render(request, 'asset/host_list.html', {'hosts' : hosts})

def host_add(request):

    if request.method == 'GET':
        return render(request, 'asset/host_add.html')

    private_ip = request.POST.get('private_ip')
    asset = Asset()
    asset.host_add(private_ip)

    return render(request, 'asset/host_add.html')

