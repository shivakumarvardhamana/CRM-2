from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def warapper_func(request,*args,**kwargs):

        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return warapper_func

def allowed_user(allowed_rows=[]):

    def decorator(view_fun):
        def wrapper_func1(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_rows:


                return view_fun(request,*args,**kwargs)
            else:
                return HttpResponse("you are not allowed")
        return wrapper_func1
    return decorator

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='customer':
            return redirect('user-page')
        if group=='admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function