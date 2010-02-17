import django.template
import django.http

def template(template_name):
	def renderer(func):
		def wrapper(request, *args, **kw):
			context_dict = func(request, *args, **kw)
			if not isinstance(context_dict, dict):
				return context_dict
			context = django.template.RequestContext(request, context_dict)
			template = django.template.loader.get_template(template_name)
			return django.http.HttpResponse(template.render(context))
		return wrapper
	return renderer
