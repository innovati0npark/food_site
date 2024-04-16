from django.shortcuts import render
from chinese.models import Category, Food


def index(request):
    # category = Category.objects.all()
    unique_categories = Category.objects.values_list('name', flat=True).distinct()
    food = Food.objects.all()
    context = {
        'unique_categories':unique_categories,
        'food':food
    }
    return render(request, 'index.html', context)