
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from models import IRCommand
from serializers import IRCommandSeiralizer

class IRCommandViewSet(viewsets.ModelViewSet):
    model = IRCommand
    serializer_class = IRCommandSeiralizer
    permission_classes = (AllowAny, )
    queryset = IRCommand.objects.all()


    # def create(self, request):
    #     data = request.data.copy()
    #     data['user'] = request.user.id
    #
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
