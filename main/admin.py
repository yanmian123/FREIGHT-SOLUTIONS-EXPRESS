# from django.contrib import admin
# from .models import BusinessInfo, ContactSubmission

# @admin.register(BusinessInfo)
# class BusinessInfoAdmin(admin.ModelAdmin):
#     # 后台编辑页显示的字段顺序
#     fields = [
#         'phone_number', 
#         'business_hours', 
#         'hero_title', 
#         'hero_subtitle', 
#         'about_us', 
#         'cta_text'
#     ]
#     # 列表页显示的字段（因为通常只需要一条基础信息记录）
#     list_display = ['phone_number', 'business_hours']

# @admin.register(ContactSubmission)
# class ContactSubmissionAdmin(admin.ModelAdmin):
#     # 联系人提交记录的列表页显示字段
#     list_display = ['name', 'phone', 'email', 'submission_time']
#     # 可搜索字段
#     search_fields = ['name', 'email', 'company']
#     # 过滤字段
#     list_filter = ['submission_time']