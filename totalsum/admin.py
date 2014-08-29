from __future__ import unicode_literals
from django.contrib import admin
from django.db.models import Sum
from django.db.models.fields import FieldDoesNotExist


class TotalsumAdmin(admin.ModelAdmin):
    change_list_template = 'totalsum_change_list.html'

    totalsum_list = ()
    unit_of_measure = ''
    totalsum_decimal_places = 2

    def changelist_view(self, request, extra_context=None):
        response = super(TotalsumAdmin, self).changelist_view(request, extra_context)
        filtered_query_set = response.context_data["cl"].queryset
        extra_context = extra_context or {}
        extra_context['totals'] = {}
        extra_context['unit_of_measure'] = self.unit_of_measure

        for elem in self.totalsum_list:
            try:
                self.model._meta.get_field_by_name(elem)  # Checking if elem is a field
                total = filtered_query_set.aggregate(totalsum_field=Sum(elem))['totalsum_field']
                if total is not None:
                    extra_context['totals'][elem] = round(total, self.totalsum_decimal_places)
            except FieldDoesNotExist:  # maybe it's a property
                if hasattr(self.model, elem):
                    total = 0
                    for f in filtered_query_set:
                        total += getattr(f, elem, 0)
                    extra_context['totals'][elem] = round(total, self.totalsum_decimal_places)

        response.context_data.update(extra_context)
        return response


