from atexit import register
from django import template
from notes.models import Tag

register = template.Library()

@register.filter(name='show_tags')
# @register.inclusion_tag("sidebar.html", takes_context=True)
def show_tags(request):
	# user_id = request.user.id
	# tags = Tag.objects.filter(user_id=user_id)
	tags = Tag.objects.all()
	context = {'tags': tags}
	return context
