from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, OneSensorSerializer


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MakeMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get('sensor') is None or request.data.get('temperature') is None:
            return Response({'message': 'must be sensor and temperature data'})
        else:
            sensor = request.data['sensor']
            temp = request.data['temperature']
            if Measurement.objects.filter(sensor_id_id=sensor).exists():
                measurement_result = Measurement.objects.create(temperature=temp, sensor_id_id=sensor)
                return Response({'sensor': measurement_result.sensor_id_id,
                                 'temperature': measurement_result.temperature,
                                 'created_at': measurement_result.created_at
                                 })
            else:
                return Response({'status': 'wrong sensor id'})


class OneSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = OneSensorSerializer
