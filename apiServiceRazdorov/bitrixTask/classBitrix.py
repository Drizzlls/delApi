from bitrix24 import *


class Bitrix24Data:
    WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/apnjml2qrh1s0tn1/"
    """ Тестовый """
    # WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/cpr67qfdl69mk1db/"
    B = Bitrix24(WEBHOOK)

class Bitrix24DataTgBot:
    WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/hyxr1ri1iil9gk66/"
    B = Bitrix24(WEBHOOK)

class Bitrix24DataTgInfoBot:
    WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/gjcab40r26ej26ag/"
    B = Bitrix24(WEBHOOK)