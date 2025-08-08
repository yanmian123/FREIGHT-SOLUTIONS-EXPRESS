# from django.shortcuts import render
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse
# from .models import BusinessInfo, ContactSubmission
# from .forms import ContactForm, QuickInquiryForm  # 导入新的表单类

# def index(request):
#     business_info = BusinessInfo.objects.first()
#         # 初始化两个表单
#     contact_form = ContactForm()
#     inquiry_form = QuickInquiryForm()
#     if request.method == 'POST':
#                 # 判断是哪个表单提交
#         if 'inquiry_submit' in request.POST:
#             form = QuickInquiryForm(request.POST)
#             form_type = "inquiry"
#         else:
#             form = ContactForm(request.POST)
#             form_type = "quote"
#         if form.is_valid():
#             form.save()
#                  # 发送邮件
#             try:
#                 # 根据表单类型构建邮件内容
#                 if form_type == "inquiry":
#                     subject = 'New Inquiry'
#                     message = f'Name: {form.cleaned_data["name"]}\n' \
#                               f'Phone/Email: {form.cleaned_data["phone_email"]}\n' \
#                               f'Inquiry: {form.cleaned_data["additional_notes"]}'
#                 else:
#                     subject = 'New Quote Request'
#                     message = f'Name: {form.cleaned_data["name"]}\n' \
#                               f'Company: {form.cleaned_data["company"]}\n' \
#                               f'Phone/Email: {form.cleaned_data["phone_email"]}\n' \
#                               f'Pickup Location: {form.cleaned_data["pickup_location"]}\n' \
#                               f'Dropoff Location: {form.cleaned_data["dropoff_location"]}\n' \
#                               f'Load Size: {form.cleaned_data["load_size"]}\n' \
#                               f'Load Weight: {form.cleaned_data["load_weight"]}\n' \
#                               f'Preferred Date/Time: {form.cleaned_data["preferred_datetime"]}\n' \
#                               f'Additional Notes: {form.cleaned_data["additional_notes"]}'
#                 send_mail(
#                     subject,
#                     message,
#                     'freightsol.express@gmail.com',
#                     ['freightsol.express@gmail.com'],
#                     fail_silently=False,
#                 )
#                 return HttpResponse('<script>alert("Request submitted successfully! We\'ll contact you shortly."); window.history.back();</script>')
#                 # return HttpResponse("request submitted successfully! We'll contact you shortly.")
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             except Exception as e:
#                 # return HttpResponse("Your request was saved, but we couldn't send the email. Please contact us directly.")
#                 print(f"reason：{str(e)}")  # 在控制台查看
#                 # return HttpResponse(f"Your request was saved, but email failed. Error: {str(e)}")
#                 return HttpResponse('<script>alert("Your request was saved, but we couldnt send the email. Please contact us directly"); window.history.back();</script>')
#     else:
#         form = ContactForm()
#     return render(request, 'index.html', {        
#         'business_info': business_info, 
#         'form': contact_form,
#         'inquiry_form': inquiry_form})


from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm, QuickInquiryForm

def index(request):
    # 硬编码业务信息（替代从数据库查询的BusinessInfo）
    business_info = {
        'phone_number': '+61:0449 704 140',
        'business_hours': 'Monday-Friday: 7:00 AM - 6:00 PM',
        'hero_title': 'FREIGHT SOLUTIONS EXPRESS',
        'hero_subtitle': 'Reliable Freight Transport Across Sydney & Beyond',
        'about_us': 'Freight Solutions Express is a Sydney-based, Australian-owned freight transport company offering reliable and efficient delivery services across local and interstate routes. With a skilled team, modern fleet, and customer-first mindset, we move goods with precision, safety, and accountability.',
        'cta_text': 'Avoid the stress of freight transport — let us handle it!'
    }

    # 初始化表单
    contact_form = ContactForm()
    inquiry_form = QuickInquiryForm()

    if request.method == 'POST':
        # 判断表单类型
        if 'inquiry_submit' in request.POST:
            form = QuickInquiryForm(request.POST)
            form_type = "inquiry"
        else:
            form = ContactForm(request.POST)
            form_type = "quote"

        if form.is_valid():
            # 移除form.save()（不再保存到数据库）
            try:
                # 构建邮件内容（使用表单清洁数据）
                if form_type == "inquiry":
                    subject = 'New Inquiry'
                    message = f'Name: {form.cleaned_data["name"]}\n' \
                              f'Phone/Email: {form.cleaned_data["phone_email"]}\n' \
                              f'Inquiry: {form.cleaned_data["additional_notes"]}'
                else:
                    subject = 'New Quote Request'
                    message = f'Name: {form.cleaned_data["name"]}\n' \
                              f'Company: {form.cleaned_data["company"]}\n' \
                              f'Phone/Email: {form.cleaned_data["phone_email"]}\n' \
                              f'Pickup Location: {form.cleaned_data["pickup_location"]}\n' \
                              f'Dropoff Location: {form.cleaned_data["dropoff_location"]}\n' \
                              f'Load Size: {form.cleaned_data["load_size"]}\n' \
                              f'Load Weight: {form.cleaned_data["load_weight"]}\n' \
                              f'Preferred Date/Time: {form.cleaned_data["preferred_datetime"]}\n' \
                              f'Additional Notes: {form.cleaned_data["additional_notes"]}'

                send_mail(
                    subject,
                    message,
                    'freightsol.express@gmail.com',
                    ['freightsol.express@gmail.com'],
                    fail_silently=False,
                )
                return HttpResponse('<script>alert("Request submitted successfully! We\'ll contact you shortly."); window.history.back();</script>')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                print(f"Email error: {str(e)}")
                return HttpResponse('<script>alert("Your request was received, but we couldn\'t send the email. Please contact us directly."); window.history.back();</script>')

    return render(request, 'index.html', {        
        'business_info': business_info,  # 传入硬编码的业务信息
        'form': contact_form,
        'inquiry_form': inquiry_form
    })