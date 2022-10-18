# add context_processors for displaying tag objects without views and url
# in sidebar.html

def tags(request):
	from notes.models import Tag
	user_id = request.user.id
	tags = Tag.objects.filter(user_id=user_id)
	# tags = Tag.objects.all()
	context = {'tags': tags}
	return context