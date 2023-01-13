import pprint
from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from bitrixTask.classBitrix import Bitrix24DataTgBot as Bitrix24Data
import json
from .serializers import DataCustomerBotSerializer
from pytz import timezone
from random import randint

class TaskAPIView(APIView):
    def post(self, request):
        serializer = DataCustomerBotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = TreatmentDataCustomer(idDeal=request.data['idDeal'],idManager=request.data['idManager'],nickname=request.data['nickname'],chatId=request.data['chatId'])
        if data.getLinkTelegramManager().find('t.me') != -1:
            updateBitrix = updateDataBitrix(id=request.data['idDeal'], nickname=request.data['nickname'], chatId=request.data['chatId'])
            updateBitrix()
        return Response(data.getLinkTelegramManager())


class TreatmentDataCustomer:
    def __init__(self, idDeal, idManager, nickname, chatId):
        self.idDeal = idDeal
        self.idManager = idManager
        self.nickname = nickname
        self.chatId = chatId
        self.allUsersData = self.allUsers()
        self.dictDepartament = [80, 82, 84, 88, 90]

    def allUsers(self):
        """ Получаем все данные сотрудников """
        getAllUsers = Bitrix24Data.B.callMethod('user.get')
        return getAllUsers

    def getLinkTelegramManager(self):
        """ Получаем Рабочий Telegram канал сотрудника """
        for user in self.allUsersData:
            if user['ID'] == self.idManager:
                return user['UF_USR_1672311069106']
        return self.getLinkTelegramSubdivision()

    def getSubdivisionManager(self):
        """ Получаем подрозделение сотрудника """
        truesubdivision = ''
        for user in self.allUsersData:
            if user['ID'] == str(self.idManager):
                if self.trueDepartament(user['UF_DEPARTMENT']) in self.dictDepartament:
                    return self.trueDepartament(user['UF_DEPARTMENT'])
        return self.randLink()

    def getLinkTelegramSubdivision(self):
        """ Получаем ссылку на тг канал, если у ответственного менеджера своего канала нет """
        division = self.getSubdivisionManager()
        if isinstance(division, int):
            for user in self.allUsersData:
                if division in user['UF_DEPARTMENT']:
                    if user['UF_USR_1672311069106']:
                        return user['UF_USR_1672311069106']
        else:
            return division

    def trueDepartament(self, listDepartament: list):
        """ Определяем нужный департамент """
        for departament in listDepartament:
            if departament in self.dictDepartament:
                return departament
        return False

    def randLink(self):
        """ Получаем рандомные ссылки """
        allLink = []
        for link in self.allUsersData:
            if link['UF_USR_1672311069106']:
                allLink.append(link['UF_USR_1672311069106'])
        return allLink[randint(0,len(allLink)-1)]



class updateDataBitrix:
    def __init__(self, id, nickname, chatId):
        self.nickname = nickname
        self.id = id
        self.chadId = chatId
        self.fieldLead = {
            'UF_CRM_1673529241': self.nickname,
            'UF_CRM_1673599207' : self.chadId,
        }
        self.fieldDeal = {
            'UF_CRM_1671012335': self.nickname,
            'UF_CRM_63C1194BD233D': self.chadId,
        }
        self.essence = ''



    def defineEssence(self) -> str:
        """ Определям сущность по id """
        try:
            get = Bitrix24Data.B.callMethod('crm.deal.get', ID=self.id)
            self.essence = 'deal'
        except:
            get = Bitrix24Data.B.callMethod('crm.lead.get', ID=self.id)
            self.essence = 'lead'
        return self.essence


    def updateDealOrLead(self):
        """ Обновляем сущность """
        try:
            if self.essence == "lead":
                update = Bitrix24Data.B.callMethod(f'crm.{self.essence}.update', ID=self.id,
                                                   fields=self.fieldLead)
            else:
                update = Bitrix24Data.B.callMethod(f'crm.{self.essence}.update', ID=self.id,
                                                   fields=self.fieldDeal)
            return True
        except Exception as e:
            print(f'Ошибка — {e}')
            return e

    def __call__(self, *args, **kwargs):
        self.defineEssence()
        self.updateDealOrLead()
        return True

