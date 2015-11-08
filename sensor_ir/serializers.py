from models import IRCommand
from rest_framework import serializers


class IRCommandSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = IRCommand
