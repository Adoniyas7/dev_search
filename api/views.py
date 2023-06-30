from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from .serializers import ProjectSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/project/id'},
        {'POST': 'api/project/id'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token'},

    ]

    return Response(routes)

@api_view(['GET'])
def projects(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)
    # Response('')