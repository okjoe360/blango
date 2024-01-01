from django import template


register = template.Library()

@register.simple_tag
def row():
  return format_html('<div class="row">')


@register.simple_tag
def endrow():
  return format_html("</div>")