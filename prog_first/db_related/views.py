from django.shortcuts import render,get_object_or_404
from django.http import  Http404
from .forms import productform
from .models import db_project
# Create your views here.
def productview_db(request,my_id):
    # obj=db_project.objects.get(id=my_id)
    obj = get_object_or_404(db_project, id=my_id)
    # try:
    #     obj=db_project.objects.get(id=my_id)
    # except db_project.DoesNotExist:
    #     raise Http404
    form = productform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form=productform()

    # if request.method == "POST" and request.value == "yes":
    #     obj.delete()
    context = {"object":obj,'form': form}
    return render(request, 'project_db.html', context)