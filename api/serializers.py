from rest_framework import serializers
from classes.models import Classroom

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
                'subject',
                'year',
                'teacher',]


class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
                'subject',
                'year',
                'teacher',]

class ClassUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
                'subject',
                'year',
                'teacher',]

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']