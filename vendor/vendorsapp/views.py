from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def index(request):
    c={'a':1,'n':5}
    return Response(c)