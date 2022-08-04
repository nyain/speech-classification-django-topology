from __future__ import division
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

from .models import Topology
# Create your views here.
def index(request):
    topology = Topology.objects.all()
    context = {
        'topologys' : topology,
    }

    return render(request, 'topology/index.html', context)

def addrecord(request):
  x = request.POST['full_name']
  y = request.POST['department']
  z = request.POST['division']
  a = request.POST['type_topology']
  topology = Topology(full_name = x, department = y, division = z, type_topology = a)
  topology.save()
  return HttpResponseRedirect(reverse('topology:index'))

def delete(request, id):
  topology = Topology.objects.get(id=id)
  topology.delete()
  return redirect('/topology/')

def update(request, id):
  mytopology = Topology.objects.get(id=id)
  template = loader.get_template('edit_topology.html')
  context = {
    'mytopology': mytopology,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  full_name = request.POST['full_name']
  department = request.POST['department']
  division = request.POST['division']
  type_topology = request.POST['type_topology']
  topology = Topology.objects.get(id=id)
  topology.full_name = full_name
  topology.department = department
  topology.division = division
  topology.type_topology = type_topology
  topology.save()
  return HttpResponseRedirect(reverse('topology:index'))
