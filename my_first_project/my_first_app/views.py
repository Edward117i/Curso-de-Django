from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def my_view(request):
    #car_list = [
        #{'title': 'BMW'}, {'title': 'Mazda'}, {'title': 'Toyota'}
   #]
    #context = {
      #"car_list": car_list
   #}
    return render(request, 'my_first_app/car_list.html')

class CarListView(TemplateView):
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self, **kwargs):
        car_list = [
            {'title': 'BMW'}, {'title': 'Mazda'}, {'title': 'Toyota'}
        ]
        context = {
            "car_list": car_list
        }
        return context

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    #Cambiar entre id y brand para ver el resultado
    if 'id' in kwargs:
        return HttpResponse(f"Detalle del auto! {kwargs['id']}")
    elif 'brand' in kwargs:
        return HttpResponse(f"El auto es de la marca! {kwargs['brand']}")
    else:
        return HttpResponse("No se encontró el auto o la marca")