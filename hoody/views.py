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
    form = NeighborhoodForm()
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


def hoody_delete(request, pk):
    neighbor = Neighborhood.objects.get(id=pk)
    neighbor.delete()
    return redirect("/hoody")


# profile_views

def profile_list(request):
    profiles = User.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, "profile/profile_list.html", context)


def profile_create(request):
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hoody/profile_list/")
    context = {
        "form": form
    }
    return render(request, "profile/profile_create.html", context)


def profile_update(request, pk):
    profile = User.objects.get(id=pk)
    form = UserForm()
    if request.method == "POST":
        form = UserModelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("/hoody/profile_list/")
    context = {
        "form": form,
        'profile': profile
    }
    return render(request, "profile/profile.html", context)


def profile_delete(request, pk):
    profile = User.objects.get(id=pk)
    profile.delete()
    return redirect("/profile/profile_list/")


# business views
def business_list(request):
    businesses = Business.objects.all()
    context = {
        'businesses': businesses
    }
    return render(request, "business/business_list.html", context)


# post_views
