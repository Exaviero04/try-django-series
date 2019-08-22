from django.shortcuts import render
from.models import product
# Create your views here.
def detail_view(request):
    obj = product.objects.get(id=3)
    print(obj.title)
    context = {
         "object":obj,
    }
    return render(request, "random/detail.html", context)

