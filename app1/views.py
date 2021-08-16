from django.shortcuts import render

# Create your views here.
def first_app(request):
    return render(request,'first.html',context={'name':'noohin','wishes':'good morning'})