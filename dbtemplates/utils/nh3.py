
try:
    from django_nh3.models import Nh3TextField
except ImportError:
    NH3_INSTALLED = False
else:
    NH3_INSTALLED = True
