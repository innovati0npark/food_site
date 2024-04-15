from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Food, Category
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.


# def index(request):
#     # get(그냥 주소 입력해서 오면) -> 페이지만 보여주고
#     # post -> DB에 입력하는 과정을 넣자
#     if request.method=='GET':
#         return render(request=request, template_name='chinese/index.html')# 그냥 페이지만 보여주면 됨
    
#     elif request.method=='POST':
#         # Food.objects.create(name='라떼')
#         # request.POST['lion_name']
#         # Category 인스턴스 가져오는 영역
#         category = Category.objects.create(name=request.POST['category'])

#         # Food 내용을 구성 영역
#         food_name = request.POST['name']
#         food_price = request.POST['price']
#         food_description = request.POST['description']

#         #이미지 저장-url 설정-파일이름 충돌방지

#         Food.objects.create(category= category,name=food_name, price =food_price , description=food_description)        
#         return render(request=request, template_name='chinese/index.html')# 그냥 페이지만 보여주면 됨
#         # Food.objects.create(name=request.POST['description']).save()
    

    

# def index(request):
#     if request.method=="POST":
#         if 'username' in request.POST:
#             Food.objects.create(name=request.POST['username']).save()
#             # Food.objects.create(name=request.POST['description']).save()
#         elif 'description' in request.POST:
#             Food.objects.create(name=request.POST['description']).save()
#     elif request.method=="GET":
#         pass      #그냥 페이지 보여줌.
#     return render(request=request, template_name='chinese/index.html',)

def add_food(request):
    if request.method == 'GET':
        return render(request=request, template_name='chinese/add_food.html')
    
    elif request.method == 'POST':
        category = Category.objects.create(name=request.POST['category'])

        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        fs = FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)


        Food.objects.create(category= category,name=food_name, price =food_price , description=food_description, img_url=url)        
        return redirect('index')

def food_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'chinese/food_detail.html', context)
    

def food_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('index')
