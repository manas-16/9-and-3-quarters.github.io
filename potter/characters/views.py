from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import character,book,bonus
from .models import user,movie
from .forms import userForm
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    mx = {'auth':2}
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        all_users = user.objects.all()
        for useri in all_users:
            list1 = str(useri).split('-')
            uemail = list1[0]
            upassword = list1[1]
            uname = list1[2]


            if(uemail==email):
                if(upassword==password):
                    val = {'auth' : 1 ,'useri':useri}
                    return render(request , 'characters/index.html',val)

                else:
                    val = {'auth' : 0}
                    return render(request , 'characters/index.html',val)
    return render(request , 'characters/index.html', mx)



def detail(request , character_id):
    return HttpResponse("<h2>Details for character:" + str(character_id)+"</h2>")


def all_char(request):
    template=loader.get_template('characters/all_char.html')
    all_characters = character.objects.all()
    context = {'all_characters': all_characters}
    return render(request,'characters/all_char.html',context)



def all_books(request):
    template=loader.get_template('characters/all_books.html')
    all_books = book.objects.all()
    a_bonus = bonus.objects.all()
    context = {'all_books': all_books,'a_bonus':a_bonus}
    return render(request,'characters/all_books.html',context)





def signup(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password', '')
            cpassword = request.POST.get('cpassword', '')
            if cpassword!=password:
                form = userForm()
            else:
                form.save()
            return HttpResponseRedirect(reverse('characters:index'))
    else:
        form = userForm()
    return render(request, 'characters/signup.html' , {'form':form})



value = '0'

def all_movies(request):
    template=loader.get_template('characters/all_movies.html')
    all_movies = movie.objects.all()
    context = {'all_movies': all_movies}
    return render(request,'characters/all_movies.html',context)



def movie_detail(request , movie_id):
    dmovie = movie.objects.get(id=movie_id)
    value = movie_id
    context = {'dmovie': dmovie}

    return render(request,'characters/movie_detail.html',context)



def book_detail(request , book_id):
    dbook = book.objects.get(id=book_id)

    context = {'dbook': dbook}

    return render(request,'characters/book_detail.html',context)


def edit(request , user_id):
    uk = user.objects.get(id=user_id)
    if request.method == 'POST':
        uk = userForm(request.POST, instance=uk)
        if uk.is_valid():
            uk.save()
            return HttpResponseRedirect(reverse('characters:index'))

    return render(request, 'characters/edit.html' , {'uk':uk})
