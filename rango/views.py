from django.shortcuts import render
from rango.models import category, page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    category_list = category.objects.order_by('-likes')[:5]
    page_list = page.objects.order_by('-views')[:5]
    context_dict = {'categories' : category_list, 
                    'pages' : page_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dic = {'message' : 'im rango fuck u....'}
    return render(request, 'rango/about.html', context_dic)

def category2(request, cat_name_slug):
    context_dict = {}
    categoryObj = None
    try:
        categoryObj = category.objects.get(slug = cat_name_slug)
        context_dict['category_name'] =  categoryObj.name
        
        pages = page.objects.filter(category = categoryObj)
        context_dict['category_page'] = pages
        
        context_dict['category'] = categoryObj
        
        context_dict['slug'] = cat_name_slug
    except category.DoesNotExist:
        pass
    
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
        
    return render(request, 'rango/add_category.html', {'form' : form})


def add_page(request, cat_name_slug):
    try:
        cat = category.objects.get(slug = cat_name_slug)
    except: category.DoesNotExist;  cat = None      
             
   
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit = False)
                page.category = cat
                page.views = 0
                page.save()
                return category2(request, cat_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()
    context_dict = {'form':form, 'category_slug': cat_name_slug}
    return render(request, 'rango/add_page.html',  context_dict)

def register(request):
    registered = False
    
    if request.method =='POST':
        user_form = UserForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = user_profile_form.save(commit = False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, user_profile_form.errors
    
    else:
        user_form = UserForm
        user_profile_form = UserProfileForm
    context_dict = {'user_form' : user_form,
                        'user_profile_form' : user_profile_form,
                        'registered' : registered,
                        }
    return render(request, 'rango/register.html', context_dict)
    
    
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse('Account disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'rango/login.html', {})

@login_required
def restricted(request):
    return HttpResponse('Since you are logged in you can fuck here!!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')













