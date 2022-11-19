from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.request import Request

@api_view(['GET'])
def home(request:Request):
    data=request.data
    print(data)

    return Response({'result':data})