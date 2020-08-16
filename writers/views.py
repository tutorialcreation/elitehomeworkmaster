from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import JoinWritersForm,DocumentForm
from .models import WritersJoin,Document

# Create your views here.
def index(request):
    return render(request,'writers_index.html')


def writersjoin(request):
    form=JoinWritersForm(request.POST or None)
    if form.is_valid():
        form.save()

    context={'form':form}

    return render(request,'writers_join.html',context)


def document_form(request):
    data=Document.objects.all()
    if request.method=='POST':
        # import pdb; pdb.set_trace()
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'writers_upload.html',{
                'form':form,'data':data
            })
    else:
        form=DocumentForm()

    return render(request,'writers_upload.html',{
        'form':form,'data':data
    })



class documentList(ListView):
    model=Document
    template_name='writers_upload.html'