from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    measurements = SensorSerializer(many=True, read_only=True)

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'measurements']


def testsens():
    queryset = Sensor.objects.all()
    ser = SensorSerializer(queryset, many=True)
    return ser.data


def testmeas():
    queryset = Measurement.objects.all()
    ser = MeasurementSerializer(queryset, many=True)
    return ser.data
