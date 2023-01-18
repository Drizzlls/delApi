from rest_framework import serializers

class DataCustomerBotSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()
    idManager = serializers.IntegerField()
    nickname = serializers.CharField()
    chatId = serializers.IntegerField()


class DataNewClietnBotSerializer(serializers.Serializer):
    phone = serializers.CharField()
    nickname = serializers.CharField()
    chatId = serializers.IntegerField()
    idGroup = serializers.IntegerField()

class GetClietnBotSerializer(serializers.Serializer):
    nickname = serializers.CharField()
