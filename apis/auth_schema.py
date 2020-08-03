from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphql_jwt.relay import ObtainJSONWebToken, Verify, Refresh

UserModel = get_user_model()

class User(DjangoObjectType):
  class Meta:
    model = UserModel
    filter_fields = '__all__'
    interfaces = (relay.Node,)

class Mutation(ObjectType):
  token_auth = ObtainJSONWebToken.Field()
  verify_token = Verify.Field()
  refresh_token = Refresh.Field()
