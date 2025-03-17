from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Helikopteri
from .serializers import HelikopteriSerializer

@api_view(['GET'])
def helikopteri_list(request):
    """
    Returns all helicopters in JSON format.
    """
    helikopteri = Helikopteri.objects.all()
    serializer = HelikopteriSerializer(helikopteri, many=True)
    return Response(serializer.data)  # JSON response


@api_view(['GET'])
def helikopteri_specific(request, pk):
    """
    Returns a helicopter in JSON format.
    """
    helikopteri = Helikopteri.objects.get(h_id=pk)
    serializer = HelikopteriSerializer(helikopteri, many=False)
    return Response(serializer.data)  # JSON response