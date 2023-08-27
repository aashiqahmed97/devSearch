from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response 
from . serializers import projectserializer
from projects.models import project




@api_view(['GET'])
def getRoutes(request):

    routes= [
        {'GET':'/api/projects/'},
        {"GET": "/api/projects/id"},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]


    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = project.objects.all()
    serializer = projectserializer (projects , many=True) 
    return Response(serializer.data) 

@api_view(['GET'])
def getProject(request,pk):
    project_obj = project.objects.get(id=pk)
    serializer = projectserializer (project_obj , many=False) 
    return Response(serializer.data)     
