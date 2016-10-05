from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter(name="dollars")        
def prepend_dollars(dollars):
    """
        Format the integer field `dollar_amount` as `$NNN,NNN.NN`.
    """
    if dollars:
        dollars = round(float(dollars), 2)
        return "${}{}".format(intcomma(int(dollars)), "{:0.2f}".format(dollars)[-3:])
    else:
        return ''