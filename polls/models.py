import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def limit_owner_choices():
  """Filtra y valida los usuarios que tienen el permiso de ser propietario de una encuesta."""
  return {'groups__permissions__codename': 'add_poll'}

class Poll(models.Model):
  """
  Las encuestas le permiten a los usuarios elegir una de varias opciones basado en la elección de los
  votantes.
  """
  question = models.CharField(_('pregunta'), max_length=250)
  pub_date = models.DateTimeField(_('fecha de publicación'))
  owner = models.ForeignKey(User, limit_choices_to=limit_owner_choices, on_delete=models.CASCADE,
    verbose_name=_('propietario'))

  class Meta:
    verbose_name = _('encuesta')
    verbose_name_plural = _('encuestas')

  def was_published_recently(self):
    """True si la encuesta es reciente, False si ha pasado más de un día de su publicación"""
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
    return self.question

class Choice(models.Model):
  """
  Las opciones son las posibles respuestas de las cuales los usuarios pueden hacer su votación.
  """
  poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name=_('encuesta'))
  choice_text = models.CharField(_('texto de la opción'), max_length=250)
  votes = models.IntegerField('votos', default=0)

  class Meta:
    verbose_name = _('opción')
    verbose_name_plural = _('opciones')

  def __str__(self):
    return self.choice_text
