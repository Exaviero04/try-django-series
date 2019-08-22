from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    a_dictionary={"give_title":"this is a random title i am using",
                  "given_list":[1,2,3,4,5,"abc"]}
    #return HttpResponse("<h1 align='center'>YO </br>kem cho</h1>")
    return render(request, "home.html", a_dictionary)

def actual_home_view(*args, **kwargs):
    return HttpResponse("<h1 align='center'>YO </br>kem cho</h1>")

def childu(request,*args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1 align='center'>YO </br>kem cho</h1>")
    return render(request, "childu.html", {})