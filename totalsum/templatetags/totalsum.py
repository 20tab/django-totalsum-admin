"""
Contains some common filter as utilities
"""
from django.template import Library
from django.contrib.admin.templatetags.admin_list import result_headers, result_hidden_fields, results, admin_actions


register = Library()

admin_actions = admin_actions

@register.inclusion_tag("totalsum_change_list_results.html")
def totalsum_result_list(cl, totals, unit_of_measure):
    """
    Displays the headers and data list together
    """
    pagination_required = (not cl.show_all or not cl.can_show_all) and cl.multi_page
    headers = list(result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    return {
        'cl': cl,
        'totals': totals,
        'unit_of_measure': unit_of_measure,
        'result_hidden_fields': list(result_hidden_fields(cl)),
        'result_headers': headers,
        'num_sorted_fields': num_sorted_fields,
        'results': list(results(cl)),
        'pagination_required': pagination_required
    }


@register.filter
def get_total(totals, column):
    if column.lower() in totals.keys():
        return totals[column.lower()]
    return ''