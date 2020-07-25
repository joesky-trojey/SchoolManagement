from django.urls import path,include
from .views import  addStudent,printPdf,view_student,studentIndex
# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns=[
    path('',studentIndex,name='students'),
    path('add_student/',addStudent,name='add_student'),
    path('print/',printPdf,name='printpdf'),
    path('view_student/',view_student,name='view_student'),
   

]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)