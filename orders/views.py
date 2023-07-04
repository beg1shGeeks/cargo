from rest_framework.response import Response
from rest_framework import pagination, status
from.models import(
    Orders
)
from .serializers import(
    OrdersSerializer,
    OrderValidateSerialiser,
)
from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class Paginator(pagination.PageNumberPagination):
    page_size = 10

class OrdersListCreateAPIView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    pagination_class = Paginator

    def post(self, request, *args, **kwargs):
        serializer = OrderValidateSerialiser(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        cargo_name = serializer.validated_data.get('cargo_name')
        cargo_weight = serializer.validated_data.get('cargo_weight')
        cargo_value = serializer.validated_data.get('cargo_value')
        sending_date = serializer.validated_data.get('sending_date')
        loading_location = serializer.validated_data.get('loading_location')
        loading_time = serializer.validated_data.get('loading_time')
        unloading_place = serializer.validated_data.get('unloading_place')
        unloading_time = serializer.validated_data.get('unloading_time')
        car_box = serializer.validated_data.get('car_box')
        loading_car = serializer.validated_data.get('loading_car')
        unloading_car = serializer.validated_data.get('unloading_car')
        price = serializer.validated_data.get('price')
        order = Orders.objects.create(
            cargo_name=cargo_name,
            cargo_weight=cargo_weight,
            cargo_value=cargo_value,
            sending_date=sending_date,
            loading_location=loading_location,
            loading_time=loading_time,
            unloading_place=unloading_place,
            unloading_time=unloading_time,
            car_box=car_box,
            loading_car=loading_car,
            unloading_car=unloading_car,
            price=price
        )
        return Response(status=status.HTTP_201_CREATED, data=OrdersSerializer(order).data)

class OrderDateilAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            item = Orders.objects.get(id=kwargs['id'])
        except Orders.DoesNotExist:
            return Response(data={'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderValidateSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.cargo_name = serializer.validated_data.get('cargo_name')
        item.cargo_weight = serializer.validated_data.get('cargo_weight')
        item.cargo_value = serializer.validated_data.get('cargo_value')
        item.sending_date = serializer.validated_data.get('sending_date')
        item.loading_location = serializer.validated_data.get('loading_location')
        item.loading_time = serializer.validated_data.get('loading_time')
        item.unloading_place = serializer.validated_data.get('unloading_place')
        item.unloading_time = serializer.validated_data.get('unloading_time')
        item.car_box = serializer.validated_data.get('car_box')
        item.loading_car = serializer.validated_data.get('loading_car')
        item.unloading_car = serializer.validated_data.get('unloading_car')
        item.price = serializer.validated_data.get('price')
        item.save()
        return Response(data=OrdersSerializer(item).data)
