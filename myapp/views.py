from django.shortcuts import render, redirect, get_object_or_404
from myapp.form import UserForm
from myapp.models import Users


# HOME PAGE
def homePage(request):
    return render(request, "home.html")


# CREATE NEW USER
def create_emp(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = UserForm()

    return render(request, "user.html", {"form": form})


# SUCCESS PAGE
def successPage(request):
    return render(request, "success.html")


# GET ALL USERS
def getAllUser(request):
    users = Users.objects.all()
    return render(request, "view_emp.html", {"users": users})


# DELETE USER
def delete(request, id):
    user = get_object_or_404(Users, id=id)

    if request.method == "POST":
        user.delete()
        return redirect("getallurl")

    return render(request, "delete.html", {"user": user})


# UPDATE USER
def update_emp(request, id):
    user = get_object_or_404(Users, id=id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("getallurl")
    else:
        form = UserForm(instance=user)

    return render(request, "update.html", {"form": form})




            


