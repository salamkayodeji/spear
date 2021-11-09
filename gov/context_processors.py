from .models import event

def basetest(request):

    hello = event.objects.values_list("coursename", flat=True)

    print(hello)    

    return {
        'testname': hello
    }

