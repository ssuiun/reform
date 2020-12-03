from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LinkForm
from .utils import gen_url
from .models import Links

# Create your views here.
def test_view(request):
    if request.method == "POST":
        Links.objects.create(old_link=request.POST['link'],
        new_link=gen_url())
    links = Links.objects.all().order_by("-id")
    form = LinkForm()
    return render(request, "my_app/test.html", context={"form": form ,"links":links})

def redirect_view(request, new_link):
    result = Links.objects.filter(new_link=new_link).last()
    print (new_link)
    return HttpResponse("hello")