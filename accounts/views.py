from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user, get_user_model, login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST
from .models import Profile
from .forms import ProfileForm

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request,user)
            return redirect('movies:home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html', context)


@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:home')

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'movies:home')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html', context)


#@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:home')




@require_http_methods(['GET','POST'])
@login_required
def update(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect('accounts:profile', user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    context = {
        'user_change_form': user_change_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:home')


@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('movies:home')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def profile(request,username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)

    # runtime
    reviews =  person.review_set.all()
    user_runtime = 0
    for review in reviews:
        user_runtime += review.movie.runtime
    user_runtime //= 60
    
    # rank
    rank_cnt = get_rank_cnt(reviews)

    context = {
        'person':person,
        'user_runtime': user_runtime,
        'rank_cnt': rank_cnt
    }
    return render(request,'accounts/profile.html',context)


def get_rank_cnt(reviews):
    one = two = three = four = five = 0
    for review in reviews:
        rank = review.rank
        if rank == 1:
            one += 1
        elif rank == 2:
            two += 1
        elif rank == 3:
            three += 1
        elif rank == 4:
            four += 1
        else:
            five
    rank_cnt = {
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five
    }
    return rank_cnt


@require_POST
def follow(request,user_pk):
    User =get_user_model()
    you = get_object_or_404(User,pk=user_pk)
    if request.user.is_authenticated:
        me = request.user
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_follow=False
            else:
                you.followers.add(me)
                is_follow=True
            data = {
                'is_follow': is_follow,
                'cnt_following': you.followings.count(),
                'cnt_follower': you.followers.count(),
            }
            return JsonResponse(data)
        return HttpResponse(status=200)
    return redirect('accounts:login')