"""
Herramientas y utilidades para el despliegue en AWS Elastic Beanstalk.
https://docs.aws.amazon.com/elastic-beanstalk/index.html
"""

LOG_PATH = '/opt/python/log/'

def get_instance_ip():
  """
  Retorna la IP de la instancia para resolver el error de verificación de estado del entorno.

  El servicio de AWS Elastic Load Balancer (AWSELB) verifica el estado de 'salud' del entorno a
  través de una solicitud HTTP al sistema, pero no fija el nombre del host, en su lugar, intenta
  conectarse directamente usando la dirección IP de la instancia. Esto provoca que el entorno muestre
  el estado 'Grave'.

  Esta función retorna la dirección privada de la instancia para que sea agregada a la variable
  ALLOWED_HOSTS y permitir que se realice la verificación de estado del entorno.
  """
  import requests
  try:
    instance_ip = requests.get('http://instance-data/latest/meta-data/local-ipv4').text
  except requests.exceptions.ConnectionError:
    return None
  else:
    del requests
    return instance_ip
