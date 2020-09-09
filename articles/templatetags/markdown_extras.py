from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text, safe_mode='escape', extensions=['codehilite', 'fenced_code','tables','extra',]) 