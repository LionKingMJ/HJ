from django.shortcuts import render

# Create your views here.
def test(request):
    test = Test.objects
    return render(request, 'test.html', {'test':test})