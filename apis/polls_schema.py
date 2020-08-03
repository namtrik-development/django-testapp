from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import relay, ObjectType
from polls.models import Choice as ChoiceModel, Poll as PollModel
from polls.forms import ChoiceForm, PollForm

class Poll(DjangoObjectType):
  class Meta:
    model = PollModel
    filter_fields = '__all__'
    interfaces = (relay.Node,)

class Choice(DjangoObjectType):
  class Meta:
    model = ChoiceModel
    filter_fields = '__all__'
    interfaces = (relay.Node,)

class Query(ObjectType):
  poll = relay.Node.Field(Poll)
  polls = DjangoFilterConnectionField(Poll)

class PollMutation(DjangoModelFormMutation):
  class Meta:
    form_class = PollForm

class ChoiceMutation(DjangoModelFormMutation):
  class Meta:
    form_class = ChoiceForm

class Mutation(ObjectType):
  poll = PollMutation.Field()
  choice = ChoiceMutation.Field()
