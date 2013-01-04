from django.http import HttpResponse

def testindex(request):
    return HttpResponse("Hello, world. You're at the root index.")