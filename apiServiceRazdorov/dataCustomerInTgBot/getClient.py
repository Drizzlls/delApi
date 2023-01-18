from bitrixTask.classBitrix import Bitrix24DataTgBot as Bitrix24Data
import pprint


class GetClientClass:
    def __init__(self, nick):
        self.nick = nick

    def defineEntity(self):
        getDeal = Bitrix24Data.B.callMethod('crm.deal.list',filter={"UF_CRM_1671012335": self.nick})
        if getDeal != []:
            return {"deal": getDeal}
        getLead = Bitrix24Data.B.callMethod('crm.lead.list',filter={"UF_CRM_1673529241": self.nick})
        if getLead != []:
            return {"lead": getLead}
        return False

    def getData(self):
        data = self.defineEntity()
        if data:
            if data.get('deal'):
                pass


    def getContact(self,id):
        contact = Bitrix24Data.B.callMethod('crm.contact.get', id=id)
        return contact
