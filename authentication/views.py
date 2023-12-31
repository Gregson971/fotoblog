from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "authentication/signup.html", {"form": form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)

    if request.method == "POST":
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("upload_photo_done")

    return render(request, "authentication/upload_profile_photo.html", {"form": form})


def upload_photo_done(request):
    return render(request, 'authentication/upload_profile_photo_done.html')
