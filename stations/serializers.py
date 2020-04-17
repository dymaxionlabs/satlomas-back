from rest_framework import serializers

from .models import Place, Station


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    place_name = serializers.ReadOnlyField()

    class Meta:
        model = Station
        fields = '__all__'


class MeasurementSummarySerializer(serializers.Serializer):
    station = serializers.IntegerField()
    parameter = serializers.CharField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    grouping_interval = serializers.ChoiceField(
        choices=['hour', 'day', 'week', 'month', 'year'], default='day')
    aggregation_func = serializers.ChoiceField(
        choices=['avg', 'sum', 'count', 'min', 'max'], default='avg')


class AllMeasurementSummarySerializer(serializers.Serializer):
    station = serializers.IntegerField()
    parameter = serializers.ListField(child = serializers.CharField())
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    grouping_interval = serializers.ChoiceField(
        choices=['hour', 'day', 'week', 'month', 'year'], default='day')
    aggregation_func = serializers.ChoiceField(
        choices=['avg', 'sum', 'count', 'min', 'max'], default='avg')
