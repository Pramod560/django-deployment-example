from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={'text':'Hello world!', 'number':100}
    return render(request,'basic/index.html', context=mydict)

def other(request):
    return render(request,'basic/other.html')

def relative(request):
    return render(request,'basic/relative_url.html')
