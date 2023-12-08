from django_filters import FilterSet
from .models import Instrument


class InstrumentFilter(FilterSet):
    class Meta:
        model = Instrument
        fields = ["name", "model", "brand", "color", "status"]