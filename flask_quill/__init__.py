from markupsafe import Markup

class Quill:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.globals['quill'] = self

    def load(self):
        return Markup('''
<link href="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.js"></script>
''')

    def create_editor(self, field_id):
        return Markup(f'''
<div id="editor"></div>
<input type="hidden" name="{field_id}" id="{field_id}">
<script>
  let quill;
  document.addEventListener('DOMContentLoaded', function () {{
    quill = new Quill('#editor', {{ theme: 'snow' }});
    document.querySelector('form').onsubmit = function() {{
      document.querySelector('#{field_id}').value = quill.root.innerHTML;
    }};
  }});
</script>
''')