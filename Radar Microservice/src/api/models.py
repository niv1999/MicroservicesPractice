from django.db.models import Model, DecimalField, DateTimeField
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.serializers import ModelSerializer

class AttackModel(Model):

    latitude = DecimalField(max_digits = 8, decimal_places = 6, validators = [MinValueValidator(-90), MaxValueValidator(90)])
    longitude = DecimalField(max_digits = 9, decimal_places = 6, validators = [MinValueValidator(-180), MaxValueValidator(180)])
    attack_time = DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "attacks"


class AttackSerializer(ModelSerializer):

    class Meta:
        model = AttackModel
        fields = "__all__"

