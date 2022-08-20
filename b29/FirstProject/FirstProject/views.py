from django.http import HttpResponse

def view1(request):
    resp = HttpResponse('<h1 style="color :Skyblue;">This is View 1</h2>')
    return resp