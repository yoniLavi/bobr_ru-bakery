from filebrowser.templatetags.fb_tags import register as fb_register
from django.utils.safestring import mark_safe


@fb_register.simple_tag(takes_context=True)
def get_file_extensions(context, qs):
    extensions = []
    # TODO: refactor the original tag
    return mark_safe(extensions)
