from django import forms

from reviews.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content' ]
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
        }

    def clean_content(self):
        content = self.cleaned_data['content']

        if not content.strip():
            raise forms.ValidationError('Comment cannot be empty.')

        if len(content.strip()) < 3:
            raise forms.ValidationError('Comment must be at least 3 characters long.')

        return content

