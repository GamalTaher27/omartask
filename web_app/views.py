from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Note,Util
from django.contrib.auth.models import User, Group, Permission
from .forms import Noteform
from .decorators import has_permissions


#display all Notes
@has_permissions(request.user,'full_actions')
def all_notes(request):
#    return HttpResponse('<h1> Welcome </h1>')
  # if Util.has_permission(request.user,'full_actions') :
    all_notes= Note.objects.all()
    context={
    'all_notes': all_notes
    }
    return render(request,'all_notes.html',context)
  # else:
    #   return redirect('/myweb/')


#desplay selected note
def detail(request,id):
    note=Note.objects.get(id=id)
    context={
    'note':note
    }
    return render(request,'note_details.html',context)

#add new note
def note_add(request):
  if Util.has_permission(request.user,'full_actions'or 'can_add') :
    if request.method=='POST':
        form = Noteform(request.POST)

        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')
    else:
       form=Noteform()

    context={
    'form':form
    }
    return render(request,'add.html',context)
  else:
    return redirect('/myweb')
#edit note
def edit(request,id):
    if Util.has_permission(request.user,'full_actions') :
        note = get_object_or_404(Note,id=id)
        if request.method=='POST':
            form = Noteform(request.POST, instance = note)

            if form.is_valid():
                new_form=form.save(commit=False)
                new_form.user=request.user #get current login user
                new_form.save()
                return redirect('/myweb')
        else:
           form=Noteform(instance = note)

        context={
        'form':form
        }
        return render(request,'edit.html',context)
    else:
          return redirect('/myweb')
