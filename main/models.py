

# Create your models here.
from django.db import models

class BusinessInfo(models.Model):
    business_hours = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # 新增前端介绍内容字段
    hero_title = models.CharField(max_length=200, default="FREIGHT SOLUTIONSEXPRESS PTY LTD", verbose_name="首页标题")
    hero_subtitle = models.TextField(default="Need fast and reliable shipping for your goods? Whether it's air, road, or sea - we've got you covered!", verbose_name="首页副标题")
    about_us = models.TextField(default="默认公司介绍内容...", verbose_name="公司介绍")
    cta_text = models.TextField(default="Avoid the stress and complexity of international shipping!", verbose_name="联系区域文本")
        # 便于后台显示
    def __str__(self):
        return "网站基础信息设置"
    class Meta:
        verbose_name = "网站基础信息"
        verbose_name_plural = "网站基础信息"    

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)  # 保留姓名
    company = models.CharField(max_length=100)  # 保留公司
    phone_email = models.CharField(max_length=100, verbose_name="Phone / Email", default="")  # 设为空字符串默认值
    pickup_location = models.CharField(max_length=200, verbose_name="Pickup Location", default="")
    dropoff_location = models.CharField(max_length=200, verbose_name="Dropoff Location", default="")  # 解决第一个错误
    load_size = models.CharField(max_length=100, verbose_name="Load Size", default="")  # 解决第二个错误
    load_weight = models.CharField(max_length=50, verbose_name="Load Weight (approx)", default="")  # 解决第三个错误
    preferred_datetime = models.CharField(max_length=100, verbose_name="Preferred Date/Time", default="")
    additional_notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")  # 允许为空
    submission_time = models.DateTimeField(auto_now_add=True)