from django import forms

from .models import Brand,Category


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, brand_category):
        return "%s" % brand_category.category

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['brand_category','title','brand_images','discription']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a New Category'}),
            'discription' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a Category Discription'})
        }        
        brand_category = CustomMMCF(
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )