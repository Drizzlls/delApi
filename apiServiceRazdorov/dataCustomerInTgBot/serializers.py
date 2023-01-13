from rest_framework import serializers

class DataCustomerBotSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()
    idManager = serializers.IntegerField()
    nickname = serializers.CharField()
    chatId = serializers.IntegerField()
