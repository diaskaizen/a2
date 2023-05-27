from django.shortcuts import render, redirect
from .models import *
from store.models import *
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm, UserForm, CustomerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def profile(request):

    customer = Customer.objects.get(user=request.user)

    return render(request, 'profile/profile.html',{'customer':customer})



def status(request):

    return render(request, 'accounts/status.html',{})


def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_order = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_order': total_order,
               'delivered': delivered, 'pending': pending}

    return render(request, 'accounts/dashboard.html',context)


def customer(request):
    customer = Customer.objects.all()
    context = {'customer': customer}

    return render(request, 'accounts/customer.html', context)
def customer(request, id):
    customer = Customer.objects.get(id= id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}

    return render(request, 'accounts/customer.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, instance=profile)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            myform = customer_form.save(commit=False)
            myform.user = request.user
            myform.save()

            return redirect('/accounts/customer')

        else:
            user_form = UserForm()
            profile_form = ProfileForm()

        return render(request, 'profile/profile_edit.html', {
            'user_form': UserForm, 'profile_form': ProfileForm})

@api_view(['GET'])
def api_conf(request):
    return Response('api works', safe=False)