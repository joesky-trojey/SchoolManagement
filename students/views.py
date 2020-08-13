from django.shortcuts import render
from django.http import HttpResponseRedirect
from  django.forms import ModelForm
from .models import Student
from django import forms
from forms.models import Forms as Form_name
from django.forms import ModelChoiceField
from django.contrib import messages
from streams.models import Stream

# from django.http import FileResponse
# from fpdf import FPDF
# from reportlab.pdfgen import canvas
# import io
# from .views import *
# from django.http import HttpResponseRedirect

# from .forms import NameForm
# Create your views here.
class studentsForm(ModelForm):
    classes=[('','Select class')]
    for e in Form_name.objects.all():
        lis=(int(e.form_id),str(e.form_name))
        classes.append(lis)
    streams=[('','Select Stream')];
    for stream in Stream.objects.all():
        streams.append((stream.stream_id,stream.stream_name))
        
        # print (e.form_name)
   
   
    class Meta:
        model=Student
     #forms.ModelMultipleChoiceField(queryset=Form_name.objects.all())
        # form=forms.ModelChoiceField(queryset=Form.objects.all(),initial='')
        fields=['admission_number','fname','sname','surname','class_id','kcpe','passport','stream_id']
        widgets={
        'admission_number':forms.NumberInput(attrs={'class':'form-control','required':'true'}),
        'fname':forms.TextInput(attrs={'class':'form-control'}),
        'surname':forms.TextInput(attrs={'class':'form-control'}),
        'sname':forms.TextInput(attrs={'class':'form-control'}),
        'passport':forms.FileInput(attrs={'class':'form-control'}),
        'stream_id':forms.Select(choices='',attrs={'class':'form-control'}),
        'class_id':forms.Select(choices='',attrs={'class':'form-control'}),
        # 'class_id':forms.MultipleChoiceField(queryset=Form_name.objects.all(), to_field_name='None'),
        'kcpe':forms.NumberInput(attrs={'class':'form-control'}),
        
        }
        # error_messages={
        #     'kcpe': {'max_length': "the KCPE marks should not bemore than a hundred ")
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_id'].choices=self.classes
        self.fields['stream_id'].choices=self.streams 


     
      
def studentIndex(request):
    students=Student.objects.all()
   

    return render(request, 'student_index.html',context={'info':'All students',"students":students})
   

        


def addStudent(request):
    if request.method=='GET':
        print('using Get')
        c_form=studentsForm
        return render(request,'add_student.html',context={'form':c_form})
    if request.POST:
        # request.POST.class_id=int(request.POST.get('class_id'))
        adm_number=0
        print(request.POST.get('class_id_id'))
        received_form=studentsForm(request.POST,request.FILES)
        if received_form.is_valid():
            try:
                new_student=received_form.save()
                adm_number=new_student.admission_number
                print()
                #print(err);
            except err:
                print ('err')
                
        else:
            print(received_form.errors)
            return render(request,'add_student.html',{'form':received_form})

        # stud1=Student.objects.get(pk=1)

        print('reqested via post')
        info="New student"
        return HttpResponseRedirect('../view_student?adm_no='+str(adm_number))
        #return render(request,'view_student.html',context={'info':info})

    # if request.method=='POST':
    #     if c_form.is_valid:
    #         c_form.save()
    #     else:
    #         print('Not valid')
def view_student(request):
    info="Showing student"
    adm_no=request.GET.get('adm_no')

    student=Student.objects.get(pk=adm_no)
    return render(request,'view_student.html', context={'info':info,'adm_number':adm_no,'student':student})


# views
#   subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)



# from django.core.mail import send_mail

# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']

#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)

#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')

def printPdf(request):
    return render(request,'print.html',context={})



# @require_http_methods(["GET", "POST"])
# def user_profile_list_view(request):
#     """Directory of user profiles."""
#     user_profession = request.GET.get('profession', None)
#     if user_profession:
#         users = User.objects.filter(profession=user_profession)
#     else:
#         users = User.objects.all()
#     context = {'title': 'User Profile Directory',
#                'users': users,
#                'path': request.path}
#     return render(request, 'function_views/users.html', context)



    # # Create a file-like buffer to receive PDF data.
    # buffer = io.BytesIO()

    # # Create the PDF object, using the buffer as its "file."
    # p = canvas.Canvas(buffer)

    # # Draw things on the PDF. Here's where the PDF generation happens.
    # # See the ReportLab documentation for the full list of functionality.
    # p.drawString(297, 210, "Hello world.")

    # # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()

    # # FileResponse sets the Content-Disposition header so that browsers
    # # present the option to save the file.
    # buffer.seek(0)
    # return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=12)
    # pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
    # pdf.output('cc')
   # return FileResponse(request,pdf.output("simple_demo.pdf"),context={})