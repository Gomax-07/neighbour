from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import *
from .forms import *


def landing_page(request):
    return render(request, "landing.html")


def hoody_list(request):
    neighbors = Neighborhood.objects.all()
    context = {
        'neighbors': neighbors
    }
    return render(request, "hoody/hoody_list.html", context)


def hoody_detail(request, pk):
    neighbor = Neighborhood.objects.get(id=pk)
    context = {
        'neighbor': neighbor
    }
    return render(request, "hoody/hoody_detail.html", context)


def hoody_create(request):
    form = NeighborhoodModelForm()
    if request.method == "POST":
        form = NeighborhoodModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hoody")
    context = {
        "form": form
    }
    return render(request, "hoody/hoody_create.html", context)


def hoody_update(request, pk):
    neighbor = Neighborhood.objects.get(id=pk)
    form = NeighborhoodForm(instance=neighbor)
    if request.method == "POST":
        form = NeighborhoodModelForm(request.POST, instance=neighbor)
        if form.is_valid():
            form.save()
            return redirect("/hoody")
    context = {
        "form": form,
        'neighbor': neighbor
    }
    return render(request, "hoody/hoody_update.html", context)
