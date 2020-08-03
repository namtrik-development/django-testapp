from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import ROOT_SCHEMA

urlpatterns = [
  path('', GraphQLView.as_view(graphiql=settings.DEBUG, schema=ROOT_SCHEMA), name='apis.graphql')
]
