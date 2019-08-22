from django.shortcuts import render, get_object_or_404, redirect
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
    queryset=db_project.objects.all()
    form = productform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form=productform()


    context = {"object_list":queryset,'form': form}
    return render(request, 'project_db.html', context)


def product_delete(request,my_id):
    obj = get_object_or_404(db_project, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect("../..")
    context = {"object":obj}
    return render(request, 'product_delete.html', context)