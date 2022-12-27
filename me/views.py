from functools import total_ordering
from tokenize import group
from django.shortcuts import  redirect, render
from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from .filter import orderFilter
from django.template.context_processors import csrf
from django.contrib.auth import authenticate,login,logout
from . models import *
from django.contrib.auth.decorators import login_required
from . forms import OrderForm,CreateUserForm,CustomerForm,Order_1
from django.contrib.auth.models import Group
from .decorator import unauthenticated_user,allowed_user,admin_only
# Create your views here.

@unauthenticated_user
def register(request):
    #form1=CreateUserForm()
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        print("2")
        if form.is_valid():
            print("3")
            user=form.save()
            username=form.cleaned_data.get('username')

            messages.success(request,"Accouunt was ctered for "+username)
            return redirect('login')
        
    print("4")
    contex={'form':form}
    #contex.update(csrf(request))
    
    return render(request,'accounts/register.html',contex)


@unauthenticated_user
def login1(request):
    if request.method =='POST':

        username=request.POST['username']
        password=request.POST['password']
        # customers=customer.objects.get(name=username)
        # print(customers.id)
        print(username,password)
        print(request.user.username)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            
            login(request,user)
            print("enter success")
            
            return redirect('home')

            
        else:

            messages.info(request,"username OR password incorrect")
                    
    return render(request,'accounts/login.html')
              
    


  

def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):

    

   orders=order.objects.all()
   customers=customer.objects.all()
   total_customers=customers.count()
   total_orders=orders.count()
   delivered=orders.filter(status='Delivered').count()
   pending=orders.filter(status='pending').count()
   context={'orders':orders,'customers':customers,
   'total_orders':total_orders,'delivered':delivered,'pending':pending}
    

   return render(request,'accounts/dashboard.html',context)
@login_required(login_url='login')
@allowed_user(allowed_rows=['customer'])
def userpage(request):
    
    customers=customer.objects.all()
    
    orders=request.user.customer.order_set.all()

    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()
    sample=request.user
    
    saam=request.user.username
    obj=customer.objects.get(name=sample)
    ob=obj.id
    print(ob)
    context={'orders':orders,
   'total_orders':total_orders,'delivered':delivered,'pending':pending,'customer':obj}
    return render(request,'accounts/user.html',context)


@login_required(login_url='login')
@allowed_user(allowed_rows=['customer'])
def accountSetting(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/account.html',context)

@login_required(login_url='login')
@allowed_user(allowed_rows=['admin'])
def products(request):
    prod=product.objects.all()
    return render(request,'accounts/products.html',{'products':prod})

@login_required(login_url='login')
@allowed_user(allowed_rows=['admin'])
def customer1(request,pk_test):
    customers=customer.objects.get(id=pk_test)
    orders=customers.order_set.all()
    orders_count=orders.count()

    myfilter=orderFilter(request.GET,queryset=orders)
    orders=myfilter.qs

    contex={'customer':customers,'orders':orders,'orders_count':orders_count,'myfilter':myfilter}
    return render(request,'accounts/customer.html',contex)
@login_required(login_url='login')
@allowed_user(allowed_rows=['admin'])
def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(customer,order,fields=('product','status'),extra=10)
    customers=customer.objects.get(id=pk)
    #form=OrderForm(initial={'customers':customers})
    formset=OrderFormSet(queryset=order.objects.none(),instance=customers)

    if request.method=="POST":
        #print("post",request.POST) 
        #form=OrderForm(initial={'customers':customers})
        #form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customers)

        if formset.is_valid():

            formset.save()
            return redirect('/')

    contex={'formset':formset}

    return render(request,'accounts/order_form.html',contex)
@login_required(login_url='login')
@allowed_user(allowed_rows=['admin'])
def update_order(request,pk):

    
    orders=order.objects.get(id=pk)

    form=OrderForm(instance=orders)
    print("generated")
    if request.method=='POST':
        form=OrderForm(request.POST,instance=orders)
        if form.is_valid():

            form.save()
            return redirect('/')


    contex={'form':form}



    return render(request,'accounts/order_form.html',contex)

@login_required(login_url='login')
@allowed_user(allowed_rows=['admin'])
def delete_order(request,pk):

    #form=OrderForm()
    orders=order.objects.get(id=pk)
    if request.method=="POST":
        orders=order.objects.get(id=pk)
        orders.delete()
        return redirect('/')

    contex={'form':orders}


    return render(request,'accounts/delete.html',contex)



@login_required(login_url='login')
@allowed_user(allowed_rows=['customer'])
def createOrder_user(request,pk):
    OrderFormSet=inlineformset_factory(customer,order,fields=('product','note'),extra=2)
    customers=customer.objects.get(id=pk)
    print(customers)
    #form=OrderForm(initial={'customers':customers})
    formset=OrderFormSet(queryset=order.objects.none(),instance=customers)

    if request.method=="POST":
        #print("post",request.POST) 
        #form=OrderForm(initial={'customers':customers})
        #form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customers)

        if formset.is_valid():

            formset.save()
            return redirect('/')

    contex={'formset':formset}

    return render(request,'accounts/customerorder.html',contex)

    # OrderFormSet=inlineformset_factory(customer,order,fields=('product','note'),extra=1)
    # customers=customer.objects.get(id=pk)
    # print(customers)
    # #form=OrderForm(initial={'customers':customers})
    # formset=OrderFormSet(queryset=order.objects.none(),instance=customers)
    # if request.method=="POST":


    #     formset=OrderFormSet(queryset=order.objects.none(),instance=customers)

    #     formset=OrderFormSet(request.POST,instance=customers)

    #     if formset.is_valid():

    #         formset.save()
    #         return redirect('/')
    #     else:
    #         print("its not working")

    # contex={'formset':formset}

    # return render(request,'accounts/customerorder.html',contex)

