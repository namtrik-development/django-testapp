from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Poll, Choice

User = get_user_model()

class ChoiceInLine(admin.StackedInline):
  model = Choice
  fields = ['choice_text']
  extra = 3

class PollAdmin(admin.ModelAdmin):
  inlines = [ChoiceInLine]
  list_display = ('owner', 'question', 'pub_date', 'was_published_recently')
  search_fields = ['question']

  def was_published_recently(self, obj):
    """Muestra en el listado si la encuesta es reciente."""
    return obj.was_published_recently()

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'owner':
      kwargs['queryset'] = User.objects.filter(Q(groups__permissions__codename='add_poll') \
        | Q(user_permissions__codename='add_poll')).distinct()
    return super().formfield_for_foreignkey(db_field, request, **kwargs)

  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = _('Published recently?')

admin.site.register(Poll, PollAdmin)
