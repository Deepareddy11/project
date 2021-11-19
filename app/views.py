from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Mithun','age':14}
    return render(request,'h1.html',context=d)


def jinja_operation(request):
    d={'a':100,'b':894,'c':675,'name':'Deepa'}
    return render(request,'h4.html',d)