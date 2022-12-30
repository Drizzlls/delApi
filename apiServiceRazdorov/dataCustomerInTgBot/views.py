import pprint
from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from bitrixTask.classBitrix import Bitrix24Data
import json
from .serializers import DataCustomerBotSerializer
from pytz import timezone



class TaskAPIView(APIView):

    def post(self, request):
        serializer = DataCustomerBotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)





class TreatmentDataCustomer:

    def __init__(self, idDeal, idManager, nickname, chatId):
        self.idDeal = idDeal
        self.idManager = idManager
        self.nickname = nickname
        self.chatId = chatId
        self.allUsersData = self.allUsers()
        self.dictDepartament= [80, 82, 84, 88, 90]


    def allUsers(self):
        getAllUsers = Bitrix24Data.B.callMethod('user.get')
        return getAllUsers

    def getLinkTelegramManager(self):
        """ Получаем Рабочий Telegram канал сотрудника """
        link = ''
        for user in self.allUsersData:
            if user['ID'] == self.idManager:
                link == user['UF_USR_1672311069106']
                return link
        if link != '':
            return link
        else:
            return False

    def getSubdivisionManager(self):
        truesubdivision = ''
        for division in self.allUsersData:
            if division['UF_DEPARTMENT'] in self.dictDepartament:
                truesubdivision = division
                return truesubdivision
        return False



