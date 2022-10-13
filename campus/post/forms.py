from main import models
from django import forms
from mdeditor.fields import MDTextFormField  # +


class PostArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['category', 'title', 'avatar', 'tag', 'summary', 'body', 'file']

    avatar = forms.ImageField(required=False)  # required=Ture表示必填项。
    category = forms.ModelChoiceField(label="Category", queryset=models.SubCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Make more keywords!"}))
    tag = forms.CharField(label="Tag", widget=forms.TextInput(attrs={'class': 'form-control'}),
                          required=True)
    summary = forms.CharField(label="Summary", widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = MDTextFormField()
    # 支持多文件上传
    file = forms.FileField(required=False, label='Please choose files',
                           widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise forms.ValidationError("Your title is too long!")
        return title

    def clean_tag(self):
        tag = self.cleaned_data.get('tag')
        if len(tag) > 150:
            raise forms.ValidationError("Your tag is too long!")
        return tag

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) > 150:
            raise forms.ValidationError("Your summary is too long!")
        return summary


class PostFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['description']

    description = forms.CharField(label='Description', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "ex: Firmware for visiblelight"}))
    file = forms.FileField(required=True, label='Please choose files',
                           widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PostLinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['name', 'url', 'description']

    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "ZKTeco official website"}))
    description = forms.CharField(label='Description', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "ZKTeco official website"}))
    url = forms.URLField(label='URL',
                         widget=forms.URLInput(
                             attrs={'class': 'form-control', 'placeholder': "https://www.zkteco.com/en/"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 100:
            raise forms.ValidationError("Your Link name is too long!")
        return name
