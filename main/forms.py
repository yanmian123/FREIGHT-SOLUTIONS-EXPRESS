from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = [
            'name', 
            'company', 
            'phone_email', 
            'pickup_location', 
            'dropoff_location', 
            'load_size', 
            'load_weight', 
            'preferred_datetime', 
            'additional_notes'
        ]
        # 可选：添加字段提示文本
        widgets = {
            'phone_email': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
            'load_weight': forms.TextInput(attrs={'placeholder': 'e.g. 500kg'}),
            'preferred_datetime': forms.TextInput(attrs={'placeholder': 'e.g. 2024-06-30 14:00'}),
        }
        
# 在现有ContactForm下方添加
class QuickInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission  # 假设使用相同的数据模型
        fields = [
            'name', 
            'phone_email', 
            'additional_notes'  # 用于咨询内容
        ]
        widgets = {
            'phone_email': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
            'additional_notes': forms.Textarea(attrs={'placeholder': 'Your inquiry details...', 'rows': 4}),
        }