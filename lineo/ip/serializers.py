from rest_framework import serializers

from lineo.ip.models import Visit


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('ip_address', 'time')