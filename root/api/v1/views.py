from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import InfoSerialize
from rest_framework import status


@api_view()
def test(request):
    return Response({"message": "Hello, World!"})


@api_view(["GET", "POST", "UPDATE", "DELETE"])
def test2(request):
    info = {
        "name": "atra",
        "family": "soufi",
    }
    serializer = InfoSerialize(info)
    return Response(serializer.data, status=status.HTTP_200_OK)
