from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin.utils import label_for_field
from django.db.models import Sum
from django.db.models.fields import FieldDoesNotExist


class TotalsumAdmin(admin.ModelAdmin):
    change_list_template = 'totalsum_change_list.html'

    totalsum_list = ()
    unit_of_measure = ''
    totalsum_decimal_places = 2

    def changelist_view(self, request, extra_context=None):
        response = super(TotalsumAdmin, self).changelist_view(request, extra_context)
        if not hasattr(response, 'context_data') or 'cl' not in response.context_data:
            return response
        filtered_query_set = response.context_data["cl"].queryset
        extra_context = extra_context or {}
        extra_context['totals'] = {}
        extra_context['unit_of_measure'] = self.unit_of_measure

        for elem in self.totalsum_list:
            try:
                self.model._meta.get_field(elem)  # Checking if elem is a field
                total = filtered_query_set.aggregate(totalsum_field=Sum(elem))['totalsum_field']
                if total is not None:
                    extra_context['totals'][label_for_field(elem, self.model, self)] = round(
                        total, self.totalsum_decimal_places)
            except FieldDoesNotExist:  # maybe it's a property
                if hasattr(self.model, elem):
                    total = 0
                    for f in filtered_query_set:
                        total += getattr(f, elem, 0)
                    extra_context['totals'][label_for_field(elem, self.model, self)] = round(
                        total, self.totalsum_decimal_places)

        response.context_data.update(extra_context)
        return response
