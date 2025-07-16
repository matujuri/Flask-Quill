from wtforms import HiddenField

class QuillField(HiddenField):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)