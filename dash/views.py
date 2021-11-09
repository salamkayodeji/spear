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
            message = render_to_string('ash/postemail.html', {
                'obj':obj,
            }) 
            msg = EmailMessage('Course', message, 'COINMAC <admin@coinmac.net>', msg['To'],
                               reply_to=['training@coinmac.org'],)
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
           
            messages.success(request, f'Your email to {obj.email} has been sent Successfully!')        
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
            
            message = render_to_string('dash/categoryemail.html', {
                'obj':obj,
            })    
            msg = EmailMessage('Course', message, 'COINMAC <admin@coinmac.net>', msg['To'],
                               reply_to=['training@coinmac.org'],)
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
           
            messages.success(request, f'Your email to {obj.email} has been sent Successfully!')        
    context = {
        'form':form,
    }
    template = "dash/send_email.html"
    return render(request, template, context)

