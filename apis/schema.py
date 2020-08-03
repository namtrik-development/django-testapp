from graphene import Field, ObjectType, Schema
from .polls_schema import Query as PollQuery, Mutation as PollMutation
from .auth_schema import User, Mutation as AuthMutation

class Query(PollQuery, ObjectType):
  pass

class Mutation(PollMutation, AuthMutation, ObjectType):
  pass

ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)
