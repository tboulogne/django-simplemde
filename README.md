# A markdown editor(with preview) for Django
Use markdown editor https://github.com/NextStepWebs/inscrybmde-markdown-editor in django project, this project is inspired by https://github.com/douglasmiranda/django-wysiwyg-redactor/ 

# Getting started
* install django-inscrybmde
```
pip install django-inscrybmde
```

* add 'inscrybmde' to INSTALLED_APPS.

```python
INSTALLED_APPS = (
    # ...
    'inscrybmde',
    # ...
)
```

# Using in models
```python
from django.db import models
from inscrybmde.fields import InscrybMDEField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = InscrybMDEField(verbose_name=u'mardown content')
```

# InscrybMDE options
You could set InscrybMDE options in settings.py like this:

```python
INSCRYBMDE_OPTIONS = {
    'placeholder': 'haha',
    'status': False,
    'autosave': {
        'enabled': True
    }
}
```

Right now this plugin supports [InscrybMDE Configurations](https://github.com/NextStepWebs/inscrybmde-markdown-editor#configuration), but only the static ones(don't support js configurations like ```previewRender```)

***for autosave option, you dont need to set it, this plugin will generate uniqueId with python's uuid.uuid4 automatically***

# Get InscrybMDE instance from DOM

After InscrybMDE initialized, you could get InscrybMDE instance from dom element like this:

```javascript
$('.inscrybmde-box')[0].InscrybMDE
```