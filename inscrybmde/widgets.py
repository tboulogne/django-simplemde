from __future__ import unicode_literals
import uuid
from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.conf import settings

try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy

from .utils import json_dumps


GLOBAL_OPTIONS = getattr(settings, 'INSCRYBMDE_OPTIONS', {})


class InscrybMDEEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        self.custom_options = kwargs.pop('inscrybmde_options', {})
        super(InscrybMDEEditor, self).__init__(*args, **kwargs)

    @property
    def options(self):
        options = GLOBAL_OPTIONS.copy()
        if 'autosave' in options and options['autosave'].get('enabled', False):
            options['autosave']['uniqueId'] = str(uuid.uuid4())
        options.update(self.custom_options)
        return options

    def render(self, name, value, attrs=None):
        if 'class' not in attrs.keys():
            attrs['class'] = ''

        attrs['class'] += ' inscrybmde-box'

        attrs['data-inscrybmde-options'] = json_dumps(self.options)

        html = super(InscrybMDEEditor, self).render(name, value, attrs)

        return mark_safe(html)

    def _media(self):
        js = (
            'inscrybmde/inscrybmde.min.js',
            'inscrybmde/inscrybmde.init.js'
        )

        css = {
            'all': (
                'inscrybmde/inscrybmde.min.css',
            )
        }
        return forms.Media(css=css, js=js)
    media = property(_media)
