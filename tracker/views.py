from django.shortcuts import render
from .models import Food, Consume

# Create your views here.

def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        food = Food.objects.all()

    else:
        food = Food.objects.all()

        
    consumed_food = Consume.objects.filter(user=request.user)

    context = {
        'consumed_food': consumed_food,
        'food': food,
    }

    return render(request, 'tracker/index.html', context)
