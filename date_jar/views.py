import random
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from date_jar.forms import EmailUserCreationForm, NewEvent, AddEvent, RemoveEvent
from date_jar.models import Category, Event


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html')


def profile(request):
    current_user = request.user
    dates = current_user.event.filter(done=False)
    dated = current_user.event.filter(done=True)
    return render(request, 'profile.html', locals())


def done(request, event_id):
    current_user = request.user
    event = Event.objects.get(id=event_id)
    #event.user.done = True
    event.done = True
    event.save()

    return redirect('profile')


def remove_event(request, event_id):
    form = RemoveEvent(request.POST)
    current_user = request.user
    event = Event.objects.get(id=event_id)
    event.user.remove(current_user)
    event.save()
    return redirect('profile')
    #return render(request, 'profile.html', {'form': form, 'error_message': ''})


def show_random(request):
    random_idx = random.randint(0, Event.objects.count() - 1)
    random_obj = Event.objects.all()[random_idx]
    return render(request, "home.html", random_obj)


def adventure(request):
    cat = Category.objects.filter(name="Adventure")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/adventure.html', locals())

def classic(request):
    cat = Category.objects.filter(name="The Classics")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/classic.html', locals())

def date_night_fun(request):
    cat = Category.objects.filter(name="Date Night Fun")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/date_night_fun.html', locals())

def day_trip(request):
    cat = Category.objects.filter(name="Day Trip Dates")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/day_trip.html', locals())

def eat_drink(request):
    cat = Category.objects.filter(name="Eat & Drink")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/eat_drink.html', locals())

def fun_home(request):
    cat = Category.objects.filter(name="Fun @ Home")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/fun_home.html', locals())

def get_sporty(request):
    cat = Category.objects.filter(name="Get Sporty")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/get_sporty.html', locals())

def learn(request):
    cat = Category.objects.filter(name="Learn Together")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/learn.html', locals())

def weekend(request):
    cat = Category.objects.filter(name="The Weekender")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/weekend.html', locals())

def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


# @login_required()
# def edit_profile(request):
#     if request.method == "POST":
#         form = EditProfile(request.POST)
#         if form.is_valid():
#             request.user.email = form.cleaned_data['email']
#             request.user.first_name = form.cleaned_data['first_name']
#             request.user.last_name = form.cleaned_data['last_name']
#             return redirect('profile')
#     else:
#         form = EditProfile(instance=request.user)
#     return render(request, 'edit_profile.html', {'form': form})


# def upload_picture(request, location_id):
#     if request.method == 'POST':
#         picture_form = PictureForm(request.POST, request.FILES)
#         if picture_form.is_valid():
#             pic = Picture(description=picture_form.cleaned_data['description'],
#                           image=picture_form.cleaned_data['picture'],
#                           location=Location.objects.get(pk=location_id))
#             pic.save()
#         return redirect('view_location', location_id)

def new_event(request):
    if request.method == "POST":
        form = NewEvent(request.POST)

        if form.is_valid():
            current_event = Event.objects.create(name=form.cleaned_data['name'],
                                                 description=form.cleaned_data['description'],
                                                 category=form.cleaned_data['category'],
                                                 location=form.cleaned_data['location'],
                                                 url=form.cleaned_data['url'],
                                                 address=form.cleaned_data['address'],
                                                 image=form.cleaned_data['image'],)
            current_event.user.add(request.user)


            #if current_event.count() == 0:
            #    current_event.delete()
            #    error = "..."
            #    return render(request, 'new_event.html', {'form': form, 'error_message': error})
            #return redirect('profile')
    else:
        form = NewEvent()
    return render(request, "new_event.html", {'form': form, 'error_message': ''})
    #return redirect('profile')


def add_event(request, event_id):
    form = AddEvent(request.POST)
    current_user = request.user
    # Get the Event object for this event
    event = Event.objects.get(id=event_id)
    # Add the current user to the event
    event.user.add(current_user)
    # Save the event
    event.save()
    return redirect('profile')
    #return render(request, 'profile.html', {'form': form, 'error_message': ''})
