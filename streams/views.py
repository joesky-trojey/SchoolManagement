from django.shortcuts import render
from django.forms import ModelForm
from django import  forms
from streams.models import Stream

# Create your views here.
from .models import Stream

class StreamForm(ModelForm):
  

    class Meta:
        model=Stream

        fields=['stream_name']

        widjets={
            'stream_name':forms.Select(attrs={'class':'form-control'})
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
           
        
def streamView(request):
    if request.method=='GET':
        c_form=StreamForm
        return render(request,'streams.html',context={'form':c_form})
    if request.POST:
        print('requesis Post')
        received_form=StreamForm(request.POST);
        if received_form.is_valid():
            try:
                new_stream=received_form.save()
                new_stream.stream_name=new_stream.stream_name.upper()
                # print (new_stream.stream_name)
                return render(request,'streams.html',{'form':received_form})
            except Exception as e:
                print('Oops', e.__class__,'occured ')
        else:
            return render(request,'streams.html',{'form':received_form})
