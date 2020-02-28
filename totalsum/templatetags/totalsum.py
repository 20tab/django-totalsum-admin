"""
Contains some common filter as utilities
"""
from django.contrib.admin.templatetags.admin_list import (
    admin_actions,
    result_headers,
    result_hidden_fields,
    results,
)
from django.template import Library, loader

register = Library()

admin_actions = admin_actions


@register.simple_tag(takes_context=True)
def totalsum_result_list(
    context,
    cl,
    totals,
    unit_of_measure,
    template_name="totalsum_change_list_results.html",
):

    pagination_required = (not cl.show_all or not cl.can_show_all) and cl.multi_page
    headers = list(result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h["sortable"] and h["sorted"]:
            num_sorted_fields += 1
    c = {
        "cl": cl,
        "totals": totals,
        "unit_of_measure": unit_of_measure,
        "result_hidden_fields": list(result_hidden_fields(cl)),
        "result_headers": headers,
        "num_sorted_fields": num_sorted_fields,
        "results": list(results(cl)),
        "pagination_required": pagination_required,
    }

    t = loader.get_template(template_name)
    return t.render(c)


@register.filter
def get_total(totals, column):
    if column in totals.keys():
        return totals[column]
    return ""
