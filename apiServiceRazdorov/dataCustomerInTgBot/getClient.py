from bitrixTask.classBitrix import Bitrix24DataTgBot as Bitrix24Data
import pprint
from .models import AllManagers, SourceDeal, SourceLead

"""
1) ФИО
2) Номер телефона
3) Менеджер
4) Группа
5) Дата заключения - UF_CRM_62DAB2BE1B9C0
6) Номер дела
7) Источник
"""
class GetClientClass:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sourceId = {
            ""
        }

    def defineEntity(self):
        deal = Bitrix24Data.B.callMethod('crm.deal.list',filter={"UF_CRM_1671012335": self.nickname}, select=['CONTACT_ID','ASSIGNED_BY_ID','UF_CRM_62DAB2BE1B9C0','UF_CRM_6059A855ED8BE','UF_CRM_5F3BE0484AC8C','STAGE_ID','UF_CRM_1671012335','CATEGORY_ID'])
        if deal != []:
            return self.getDeal(deal),
        lead = Bitrix24Data.B.callMethod('crm.lead.list',filter={"UF_CRM_1673529241": self.nickname},select=['ID','ASSIGNED_BY_ID','UF_CRM_1597759307071','NAME','LAST_NAME','SECOND_NAME'])
        if lead != []:
            return self.getLead(lead)
        return 'Такого никнейма нет в Битриксе'


    def getLead(self,data):
        """ Получаем лид """
        return {'ID': data[0]['ID'],
                'ASSIGNED_BY_ID': self.getManager(data[0]['ASSIGNED_BY_ID']),
                'Source': self.getSource(data[0]['UF_CRM_1597759307071'],entity='lead'),
                'Name': data[0]['NAME'],
                'Last_Name': data[0]['LAST_NAME'],
                'Second_name': data[0]['SECOND_NAME'],
                'Type': 'Лид',
                'Group':self.getGroup(id=data[0]['ASSIGNED_BY_ID'])}

    def getDeal(self, data):
        """ Получаем сделку """
        if len(data) > 1:
            for deal in data:
                if deal["UF_CRM_1671012335"] != self.nickname:
                    data.remove(deal)
                    continue
                if deal['STAGE_ID'] == 'C14:WON' or deal['CATEGORY_ID'] == '0':
                    data.remove(deal)
        contact = self.getContact(data[0]['CONTACT_ID'])
        return {'ID': data[0]['ID'],
                'ASSIGNED_BY_ID': self.getManager(data[0]['ASSIGNED_BY_ID']),
                'Date':data[0]['UF_CRM_62DAB2BE1B9C0'][:-15] if data[0]['UF_CRM_62DAB2BE1B9C0'] else 'Нет',
                'Number':data[0]['UF_CRM_6059A855ED8BE'] if data[0]['UF_CRM_6059A855ED8BE'] else 'Нет',
                'Source': self.getSource(id=data[0]['UF_CRM_5F3BE0484AC8C'],entity='deal'),
                'Name':contact['NAME'],
                'Last_Name':contact['LAST_NAME'],
                'Second_name':contact['SECOND_NAME'],
                'Type': 'Сделка',
                'Group': self.getGroup(data[0]['ASSIGNED_BY_ID'])}


    def getContact(self, id):
        contact = Bitrix24Data.B.callMethod('crm.contact.get', id=id)
        return {'NAME': contact['NAME'] if contact['NAME'] else '',
                'LAST_NAME':contact['LAST_NAME'] if contact['LAST_NAME'] else '',
                'SECOND_NAME':contact['SECOND_NAME'] if contact['SECOND_NAME'] else ''}

    def getManager(self,id):
        try:
            manager = AllManagers.objects.get(idManager=id).name
            return manager
        except:
            return id

    def getSource(self,id,entity):
        if entity == 'lead':
            try:
                source = SourceLead.objects.get(idFromBitrix=id).title
                return source
            except:
                return id
        else:
            try:
                source = SourceDeal.objects.get(idFromBitrix=id).title
                return source
            except:
                return id

    def getGroup(self,id):
        departamentManager = Bitrix24Data.B.callMethod('user.get', id=id)
        dictGroup = {
            80: 'Группа Филиной',
            82: 'Группа Власенко',
            84: 'Группа Саркисян',
            88: 'Группа Арсеньева',
            90: 'Группа Шмелева'
        }
        for group in departamentManager[0]['UF_DEPARTMENT']:
            if group in dictGroup.keys():
                return dictGroup[group]
        return 'Сотрудник вне рабочей группы'

