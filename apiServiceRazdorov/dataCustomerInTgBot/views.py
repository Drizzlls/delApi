from .serializers import DataCustomerBotSerializer, DataNewClietnBotSerializer, GetClietnBotSerializer
from .currentСlient import CurrentClient
from rest_framework.views import APIView
from rest_framework.response import Response
from .bitrixMethods import updateDataBitrix
from .newClient import AddNewClient
from .getClient import GetClientClass

class GetCurrentClient(APIView):
    def post(self, request):
        serializer = DataCustomerBotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = CurrentClient(idDeal=request.data['idDeal'],idManager=request.data['idManager'],nickname=request.data['nickname'],chatId=request.data['chatId'])
        link = data.getLinkTelegramManager()
        if link.find('t.me') != -1:
            updateBitrix = updateDataBitrix(id=request.data['idDeal'], nickname=request.data['nickname'], chatId=request.data['chatId'])
            updateBitrix()
        return Response(link)


class NewClient(APIView):
    def post(self, request):
        serializer = DataNewClietnBotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = AddNewClient(phone=request.data['phone'],nickname=request.data['nickname'],chatId=request.data['chatId'],idGroup=request.data['idGroup'])
        data()
        return Response(data.link)


class GetClient(APIView):
    def post(self, request):
        serializer = GetClietnBotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = GetClientClass(nick=request.data)
        return Response(client.defineEntity())