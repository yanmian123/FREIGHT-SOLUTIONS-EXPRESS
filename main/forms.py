# from django import forms
# from .models import ContactSubmission

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactSubmission
#         fields = [
#             'name', 
#             'company', 
#             'phone_email', 
#             'pickup_location', 
#             'dropoff_location', 
#             'load_size', 
#             'load_weight', 
#             'preferred_datetime', 
#             'additional_notes'
#         ]
#         # 可选：添加字段提示文本
#         widgets = {
#             'phone_email': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
#             'load_weight': forms.TextInput(attrs={'placeholder': 'e.g. 500kg'}),
#             'preferred_datetime': forms.TextInput(attrs={'placeholder': 'e.g. 2024-06-30 14:00'}),
#         }
        
# # 在现有ContactForm下方添加
# class QuickInquiryForm(forms.ModelForm):
#     class Meta:
#         model = ContactSubmission  # 假设使用相同的数据模型
#         fields = [
#             'name', 
#             'phone_email', 
#             'additional_notes'  # 用于咨询内容
#         ]
#         widgets = {
#             'phone_email': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
#             'additional_notes': forms.Textarea(attrs={'placeholder': 'Your inquiry details...', 'rows': 4}),
#         }



from django import forms

# 移除对ContactSubmission模型的依赖
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    phone_email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone or Email'}))
    pickup_location = forms.CharField(max_length=200)
    dropoff_location = forms.CharField(max_length=200)
    load_size = forms.CharField(max_length=100)
    load_weight = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'e.g. 500kg'}), required=False)
    preferred_datetime = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'e.g. 2024-06-30 14:00'}), required=False)
    additional_notes = forms.CharField(widget=forms.Textarea, required=False)

class QuickInquiryForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone or Email'}))
    additional_notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your inquiry details...', 'rows': 4}))