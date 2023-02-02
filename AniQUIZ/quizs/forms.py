from . import models
from django.forms import ModelForm, Textarea, ChoiceField, ModelChoiceField


class QuizForm(ModelForm):
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.id = None

    class Meta:
        model = models.Quiz

        fields = ['title', 'imageScreensaver', 'category']


class questionForm(ModelForm):
    class Meta:
        model = models.questions

        fields = ['question', 'image', 'quiz']


class answerForm(ModelForm):
    class Meta:
        model = models.answers

        fields = ['answer', 'correct', 'questions']