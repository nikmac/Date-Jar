from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from date_jar.forms import EmailUserCreationForm, NewEvent, AddEvent
from date_jar.models import Category, Event


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html')


def profile(request):
    current_user = request.user
    # if not current_user.event.exists():
    #     current_user.event.create(name='name', user='user',)

    dates = current_user.event.filter(done=False)
    dated = current_user.event.filter(done=True)
    #data = {'dates': dates, 'dated': dated}
    return render(request, 'profile.html', locals())


def adventure(request):
    cat = Category.objects.filter(name="Adventure")
    data = Event.objects.filter(category=cat)
    return render(request, 'categories/adventure.html', locals())

def classic(request):
    return render(request, 'categories/classic.html')

def date_night_fun(request):
    return render(request, 'categories/date_night_fun.html')

def day_trip(request):
    return render(request, 'categories/day_trip.html')

def eat_drink(request):
    return render(request, 'categories/eat_drink.html')

def fun_home(request):
    return render(request, 'categories/fun_home.html')

def get_sporty(request):
    return render(request, 'categories/get_sporty.html')

def learn(request):
    return render(request, 'categories/learn.html')

def weekend(request):
    return render(request, 'categories/weekend.html')

def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


class EditProfile(object):
    pass


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
            current_event.users.add(request.user)
            # current_event.event = Event.objects.filter(text__icontains=current_event)

            if current_event.event.count() == 0:
                current_event.delete()
                error = "..."
                return render(request, 'new_event.html', {'form': form, 'error_message': error})
            return redirect('profile')
    else:
        form = NewEvent()
    return render(request, "new_event.html", {'form': form, 'error_message': ''})


def add_event(request, event_id):
    form = AddEvent(request.POST)
    current_user = request.user
    # Get the Event object for this event
    event = Event.objects.get(id=event_id)
    # Add the current user to the event
    event.user.add(current_user)
    # Save the event
    event.save()

    return render(request, 'profile.html', {'form': form, 'error_message': ''})

# def remove_event(request, event_id):
#     form = RemoveEvent(request.POST)
#     current_user = request.user
#     event = Event.objects.get(id=event_id)
#     event.user.delete(current_user)
#     event.save()
#
#     return render(request, 'profile.html', {'form': form, 'error_message': ''})

