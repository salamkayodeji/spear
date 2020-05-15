from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gov.models import Post, Category, event, Gallery, contact
import smtplib
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views import generic
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string
from email.message import EmailMessage










# Create your views here.

class Home(ListView):
    model = Category
    context_object_name = 'category'    
    template_name = 'dash/home.html'
    paginate_by='15'


   

    

class PostList(ListView):
    model = Post
    template_name = 'dash/post_list.html'
    context_object_name = 'post'
    def get_queryset(self, *args, **kwargs):

        return  Post.objects.filter(coursecategory=self.kwargs ['pk'])


            




class PostCreate(CreateView):
     model=Post
     fields = ('category', 'coursename', 'amount', 'content', 'img', 'author', 'date_1', 'date_2', 'date_3', 'date_4', 'date_5', 'date_6', 'date_7', 'date_8')
     template_name = 'admin/gov/post/add'


class PostUpdate(UpdateView):
     model=Post
     fields = ('category', 'coursename', 'amount', 'content', 'img', 'author', 'date_1', 'date_2', 'date_3', 'date_4', 'date_5', 'date_6', 'date_7', 'date_8')
     template_name = 'dash/post_form.html'

class PostDelete(DeleteView): 
    model = Post
    template_name = 'dash/post_confirm_delete.html'
    success_url =  reverse_lazy('dash:post_list')


class CategoryCreate(CreateView):
     model=Category
     fields = ('category', 'logo', 'creator')
     template_name = 'dash/category_form.html'
     success_url =  reverse_lazy('dash:Home')
     
     

class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'dash/category_form.html'
    fields = ('category', 'logo', 'creator')

class CategoryDelete(DeleteView): 
    model = Category
    template_name = 'dash/category_confirm_delete.html'
    success_url =  reverse_lazy('dash:Home')
    
class CategoryDetail(DetailView):
    model = Category
    template_name = 'dash/Home.html'


#def send_mail(request, pk=None):
 #   instance = get_object_or_404(Post, pk=pk)



  #  form = send_mail(request.POST or None)
   # if form.is_valid():
    #    form.save()
    #template_name = 'dash/send_email.html'

    #context = { "results": results,
   #     "form": form}
   # return render(request, template_name, context)  
@login_required

def postemail(request, pk):
    obj = Post.objects.get(id=pk)
    form = SendForm(instance=obj)
    if request.method == 'POST':
        form = SendForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            msg = EmailMessage()
            msg['Subject'] = 'Course'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = [obj.email]
            
            with open(settings.BASE_DIR + "/templates/postmail.txt") as f:
                signup_message = f.read()   
            context={
                'obj':obj
            }
            html_template = get_template("dash/postemail.html").render(context)
            msg.add_alternative(html_template, subtype='html')

            with smtplib.SMTP('smtp.mailgun.org', 587) as smtp:
                smtp.login('postmaster@sandbox38165242a5844e3d92d7f050545fa9bc.mailgun.org', '856e47cf87b582c06355cb69e72aa797-9dda225e-84fd6b21')

                smtp.send_message(msg)
    context = {
        'form':form,
    }
    template = "dash/send_email.html"
    return render(request, template, context)

    
@login_required

def categoryemail(request, pk):
    obj = Post.objects.filter(pk=pk).first()
    form = CategorySendForm(instance=obj)
    
    if request.method == 'POST':
        form = CategorySendForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            msg = EmailMessage()
            msg['Subject'] = 'Course'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = [obj.email]
            
            with open(settings.BASE_DIR + "/templates/postmail.txt") as f:
                signup_message = f.read()   
            context={
                'obj':obj
                
            }
            html_template = get_template("dash/categoryemail.html").render(context)
            msg.add_alternative(html_template, subtype='html')

            with smtplib.SMTP('smtp.mailgun.org', 587) as smtp:
                smtp.login('postmaster@sandbox38165242a5844e3d92d7f050545fa9bc.mailgun.org', '856e47cf87b582c06355cb69e72aa797-9dda225e-84fd6b21')

                smtp.send_message(msg)
    context = {
        'form':form,
    }
    template = "dash/send_email.html"
    return render(request, template, context)