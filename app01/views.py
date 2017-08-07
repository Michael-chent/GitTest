from django.shortcuts import render
from django.views import View

class GitTest(View):
    def get(self,request):
        return render(request,'Git_test.html')

