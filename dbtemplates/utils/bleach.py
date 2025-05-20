
try:
    from django_bleach.models import BleachField
except ImportError:
    BLEACH_INSTALLED = False
else:
    BLEACH_INSTALLED = True
