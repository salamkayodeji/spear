from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gov.models import Post, Category, event, Gallery, contact
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
            subject = "Course"
            from_email = settings.EMAIL_HOST_USER
            
            recipient_list = [obj.email]
            emails= []

            if ',' in recipient_list:
                for recipient in recipient_list:

                    emails = recipient_list.split(',')
            else:
                emails.append(recipient_list) 

            with open(settings.BASE_DIR + "/templates/postmail.txt") as f:
                signup_message = f.read()
            message  = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=emails)
            context={
                'obj':obj
            }
            html_template = get_template("dash/postemail.html").render(context)
            message.attach_alternative(html_template, "text/html")
            message.send()
    context = {
        'form':form,
    }
    template = "dash/send_email.html"
    return render(request, template, context)
@login_required

def categoryemail(request, pk):
    obj = Category.objects.get(pk=pk)
    form = CategorySendForm(instance=obj)
    
    if request.method == 'POST':
        form = CategorySendForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            subject = "Course"
            from_email = settings.EMAIL_HOST_USER
            to_email = [obj.email]
            with open(settings.BASE_DIR + "/templates/categoryemail.txt") as f:
                signup_message = f.read()
            message  = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
          
            context={
                'obj':obj,
            }
            html_template = get_template("dash/categoryemail.html").render(context)
            message.attach_alternative(html_template, "text/html")
            message.send()
    context = {
        'form':form,
    }
    template = "dash/send_email.html"
    return render(request, template, context)