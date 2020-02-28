from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, event, Gallery, contact
from django.urls import reverse_lazy
from django.views import generic
from ckeditor.widgets import CKEditorWidget
from django.views import generic
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings





# Create your views here.

#class Home(ListView):
 #   model = event
  #  template_name = 'govlink/home.html'
   # context_object_name= 'event'
class Home(ListView):
    context_object_name = 'Category'    
    template_name = 'govlink/home.html'
    queryset = Category.objects.filter(popular='1')


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['event'] = event.objects.all()
        context['gallery'] = Gallery.objects.all()
        # And so on for more models
        return context

    
    
    
    
    

class CourseCategory(ListView):
    model = Category
    template_name = 'govlink/course_categories.html'
    context_object_name= 'categories'
    paginate_by='15'


    
class gallery(ListView):
    model = Gallery
    template_name = 'govlink/gallery.html'
    context_object_name= 'gallery'
        
    





class CourseList(ListView):
    model = Post
    template_name = 'govlink/course_list.html'
    context_object_name = 'post'
    def get_queryset(self, *args, **kwargs):

        return  Post.objects.filter(coursecategory=self.kwargs ['pk'])
    
   
   
       
class coursedetail(DetailView):
    model= Post
    template_name= 'govlink/course_detail.html'
    
   
    
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(coursename__icontains=query) | Q(venue_4__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     
                     'submitbutton': submitbutton}

            return render(request, 'govlink/search.html', context)

        else:
            return render(request, 'govlink/search.html')

    else:
        return render(request, 'govlink/search.html')

def contact_us(request):

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('message'):
            post=contact()
            post.name= request.POST.get('name')
            post.email= request.POST.get('email')
            post.subject= request.POST.get('subject')
            post.message= request.POST.get('message')
                
            post.save()
	
            messages.success(request, "Your post has been successfully created")
                

            return render(request, 'govlink/contact.html')  

       
        else:
            
            context= {'error': 'The post was not successfully created. Please enter a title and content'} 
            return render(request,'govlink/contact.html', context)
    else:
            return render(request, 'govlink/contact.html')

        
   