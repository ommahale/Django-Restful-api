from rest_framework.decorators import api_view,APIView
from rest_framework import viewsets
from rest_framework.response import Response
from base.models import Person
from base.serializers import PeopleSerializer

# Create your views here.

@api_view(['GET','POST','PUT','PATCH' ])
def index(request):
    courses={
        'course_name':'Python',
        'course_topics':['flask','django','sklearn'],
        'course_provider':'Om'
    }
    if request.method=='GET':
        return Response(courses)
    elif request.method=='POST':
        return Response([{'method':'post'},courses])
    else:
        return Response({'message':'none'})



''' ___________________________________________________

        CRUD OPERATIONS
    ___________________________________________________
'''

@api_view(['GET','POST','PUT','PATCH'])
def people_data(request):
    if request.method=='GET':
        objs=Person.objects.all()
        serializer=PeopleSerializer(objs,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    #Does not allow partial updation
    elif request.method=="PUT":
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    #Allows partial updation
    elif request.method=="PATCH":
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method=='DELETE':
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Object deleted'})


'''
    _________________________________________________________________________

        IMPLEMENT CRUD OPERATIONS THROUGH APIVIEW CLASS: HELPS IN SIMPLICITY
    _________________________________________________________________________

'''

class PersonAPI(APIView):
    def get(self,request):
        objs=Person.objects.all()
        serializer=PeopleSerializer(objs,many=True)
        return Response(serializer.data)

    def put(self,request):
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self,request):
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self,request):
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request):
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Object deleted'})

'''
    _________________________________________________________________________

        CRUD API USING MODEL VIEW SET
    _________________________________________________________________________

'''
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class=PeopleSerializer
    queryset=Person.objects.all()