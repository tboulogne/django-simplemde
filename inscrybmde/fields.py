from django.db.models import TextField
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from .widgets import InscrybMDEEditor


class InscrybMDEField(TextField):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('inscrybmde_options', {})
        self.widget = InscrybMDEEditor(
            inscrybmde_options=options,
        )
        super(InscrybMDEField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = self.widget
        return super(InscrybMDEField, self).formfield(**defaults)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^inscrybmde\.fields\.InscrybMDEField"])
