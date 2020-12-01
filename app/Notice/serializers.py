from rest_framework import serializers
from .models import NoticeTbl


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeTbl
        fields = ('id', 'title', 'description', 'created_at', 'file_name')