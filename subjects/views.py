from django.shortcuts import render, reverse

# Create your views here.
from .models import Subject
from django.forms import ModelForm
from django import forms


class SubjectForm(ModelForm):
    

    class Meta:
        model=Subject
        fields=['subject_name','shorthand','optionality',]
      
        widjets={
            'subject_name':forms.TextInput(attrs={'class':'form-control'}),
            'shorthand':forms.TextInput(attrs={'class':'form-control '}),
            'optionality':forms.TextInput(attrs={'class':'form-control'})
             

        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # choice=[('','Select Optionality'),(1,'Comparsory'),(0,'Optional')]
        # self.fields['optionality'].choices=choice

def subjects(request):
    all_subjects=Subject.objects.all()
    for subject in all_subjects:
        if int(subject.optionality)==1:
            subject.optionality='Compulsory'
        else:
            subject.optionality="Optional"
    if request.method=='GET':
        c_form=SubjectForm
  
        return render(request,'subjects.html',context={'form':c_form,'subjects':all_subjects})  

    if request.method=="POST":

        received_subject=SubjectForm(request.POST)
        if received_subject.is_valid():
            try:
                received_subject.save()
                request.method='GET'
                return render(request,'subjects.html',context={'form':SubjectForm,'subjects':all_subjects})
            except Exception as e:
                print (e)
                return render (request,'subjects.html',context={'form':"Some error happened here"+str(e.__class__) })
        else:
            return render(request,'subjects.html',{'form':received_subject,'subjects':all_subjects})

def updateSubject(request, book_id):
    all_subjects=Subject.objects.all()
    subject_identifier=int(book_id)
    try:
        subject=Subject.get(subject_id=subject_identifier)
    except Subject.DoesNotExist:
        print('subject does not exist')
        return redirect('subjects');
    subject_form=SubjectCreate(request.POST or None, instance=subject)
    if subject_form.is_valid():
        subject_form.save()
        return redirect('subjects')
    return render(request,'subjects.html',{'form':subject,'subjects':all_subjects})

    
# def deleteSubject(request, book_id):
#     book_id = int(book_id)
#     try:
#         book_sel = Book.objects.get(id = book_id)
#     except Book.DoesNotExist:
#         return redirect('index')
#     book_sel.delete()
#     return redirect('index')
