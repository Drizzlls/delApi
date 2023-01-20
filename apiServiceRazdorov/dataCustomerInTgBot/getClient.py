from bitrixTask.classBitrix import Bitrix24DataTgBot as Bitrix24Data
import pprint

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
            return self.getDeal(deal)
        getLead = Bitrix24Data.B.callMethod('crm.lead.list',filter={"UF_CRM_1673529241": self.nickname})
        if getLead != []:
            return {"lead": getLead}
        return 'Такого никнейма нет в Битриксе'

    # def getData(self):
    #     data = self.defineEntity()
    #     if isinstance(data[0], list):
    #         if data.get('deal', False):
    #             print('Я в сделке')
    #             deal = self.getDeal(data)
    #             return deal
    #         elif data.get('lead', False):
    #             lead = self.getLead(data)
    #             return lead
    #     return 'Такого никнейма нет в Битриксе (getData)'


    # def getLead(self,data):
    #     """ Получаем лид """
    #     return {'ID': data[0]['ID'],
    #             'ASSIGNED_BY_ID': data[0]['ASSIGNED_BY_ID'],
    #             'Source': data[0]['UF_CRM_5F3BE0484AC8C'],
    #             'Name': data[0]['NAME'],
    #             'Last_Name': contact['LAST_NAME'],
    #             'Second_name': contact['SECOND_NAME'],
    #             'Type': 'Лид'}

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
                'ASSIGNED_BY_ID': data[0]['ASSIGNED_BY_ID'],
                'Date':data[0]['UF_CRM_62DAB2BE1B9C0'][:-15] if data[0]['UF_CRM_62DAB2BE1B9C0'] else 'Нет',
                'Number':data[0]['UF_CRM_6059A855ED8BE'] if data[0]['UF_CRM_6059A855ED8BE'] else 'Нет',
                'Source': data[0]['UF_CRM_5F3BE0484AC8C'],
                'Name':contact['NAME'],
                'Last_Name':contact['LAST_NAME'],
                'Second_name':contact['SECOND_NAME'],
                'Type': 'Сделка'}


    def getContact(self, id):
        contact = Bitrix24Data.B.callMethod('crm.contact.get', id=id)
        return {'NAME': contact['NAME'] if contact['NAME'] else '',
                'LAST_NAME':contact['LAST_NAME'] if contact['LAST_NAME'] else '',
                'SECOND_NAME':contact['SECOND_NAME'] if contact['SECOND_NAME'] else ''}
