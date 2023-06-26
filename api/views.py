from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/project'},
        {'GET': 'api/project/id'},
        {'POST': 'api/project/id'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token'},

    ]

    return Response(routes)