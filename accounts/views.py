
from .models import Country
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

class UserCreationView(APIView):
    def get(self,request):
        user = Country.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data , status = 200)
    def post(self,request ):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@csrf_exempt
def UserCreate(request):
    """
    Creates the user.
    """
    if request.method == "GET":

        user = Country.objects.all()
        serializer = UserSerializer(user, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = UserSerializer(data =data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status = 201)
        return JsonResponse(serializer.errors, status = 400)
    else :
        return  HttpResponse( status = 404)

@csrf_exempt
def user_details(request,id):
    try:
        instance = Country.objects.get(id =id)
    except Country.DoesNotExist as e:
        return JsonResponse({"error":"given user object not found"}, status = 404)


    if request.method == "GET":


        serializer = UserSerializer(instance)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = UserSerializer(instance, data =data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status = 200)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse( status = 200)


