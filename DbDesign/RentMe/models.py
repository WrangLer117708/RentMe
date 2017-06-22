from django.db import models
import django.utils.timezone as timezone
import datetime
# Create your models here.
class model_info(models.Model):
    CarTypes = (
        (0, u'SUV'),
        (1, u'商务车'),
    )
    stateChoices = (
        (u'Sing',u'单天窗'),
        (u'all',u'全景天窗'),
        (u'else',u'其他'),
        (u'N',u'无'),
    )
    DvdChoices = (
        (u'D',u'DVD'),
        (u'C',u'CD'),
        (u'S',u'其他'),
    )
    car_model_id = models.CharField(max_length=40,primary_key=True,verbose_name='品牌/车系/年代款/配置款')
    car_type = models.IntegerField(choices=CarTypes,null=True,verbose_name='车型')
    car_brand = models.CharField(max_length=20,default='奔驰')
    car_series= models.CharField(max_length=20,default='X3')
    car_issue_date = models.CharField(max_length=4,default='2017')
    car_config_model = models.CharField(max_length=10,default='悦动型')
    car_seats_num = models.IntegerField(null=True)
    car_doors = models.IntegerField(null=True)
    car_fuel_type = models.CharField(max_length=5,null=True,verbose_name='燃料类型')
    car_gearbox_type = models.CharField(max_length=5,null=True,verbose_name='变速箱类型')
    car_displacement = models.IntegerField(null=True,verbose_name='排量')
    car_fuel_num = models.CharField(max_length=10,null=True,verbose_name='使用燃油编号')
    car_drive_way = models.CharField(max_length=5,null=True,verbose_name='驱动方式')
    car_engine_intake = models.CharField(max_length=10,null=True,verbose_name='发动机进气方式')
    car_skylight = models.CharField(max_length=5,choices=stateChoices,default='无',verbose_name='天窗')
    car_tank_capa = models.IntegerField(null=True,verbose_name='邮箱容量')
    car_voicebox = models.IntegerField(null=True,verbose_name='音箱')
    car_seats_type = models.CharField(max_length=10,null=True,verbose_name='座椅')
    car_reverse_radar = models.CharField(max_length=4,choices=stateChoices,default='无',verbose_name='倒车雷达')
    car_airbag = models.CharField(max_length=4,null=True,verbose_name='气囊')
    car_dvd = models.CharField(max_length=4,choices=DvdChoices,default='DVD')
    car_gps = models.CharField(max_length=5,choices=stateChoices,default='无',verbose_name='GPS导航')
    car_deposit = models.IntegerField(default=5000,verbose_name='押金')
    car_day_price = models.IntegerField(default=1000,verbose_name='日租金')
    car_time_out_price = models.IntegerField(default=150,verbose_name='超时费用(元/天)')
    car_over_kilo_price = models.FloatField(default=0.5,verbose_name='超公里费用(元/公里)')

    def __str__(self):
        return self.car_model_id
    class Meta:
        verbose_name = '车型'
        verbose_name_plural = '车型'

class car_info(models.Model):
    ColorChoices = (
        (u'red',u'红色'),
        (u'bla',u'黑色'),
        (u'sli',u'银色'),
    )
    statusChoices = (
        (u'N',u'未租'),
        (u'R',u'已租'),
        (u'F',u'维修'),
    )
    car_num = models.CharField(max_length=10,primary_key=True)
    car_model_id = models.ForeignKey(model_info,related_name='car_model')
    car_color = models.CharField(max_length=4,choices=ColorChoices,default='黑色',verbose_name='颜色')
    car_engine_num = models.CharField(max_length=10,null=True,verbose_name='发动机号')
    car_frame_num = models.CharField(max_length=20,null=True,verbose_name='车架编号')
    car_buy_date = models.CharField(max_length=4,null=True,verbose_name='购车年份')
    car_retailer = models.CharField(max_length=20,null=True,verbose_name='销售商')
    car_status = models.CharField(max_length=4,choices=statusChoices,default='未租',verbose_name='车辆状态')
    car_ins_num = models.CharField(max_length=50,null=True,verbose_name='保单编号')

    def __str__(self):
        return self.car_num
    class Meta:
        verbose_name = '车辆信息'
        verbose_name_plural = '车辆信息'
class admin_info(models.Model):
    GenderChoices = (
        (u'F', u'女'),
        (u'M', u'男'),
    )
    AdminChoices = (
        (0,u'大中华地区管理员'),
        (1,u'门店管理员'),
        (2,u'违章处理管理员'),
    )
    admin_num = models.CharField(max_length=15,primary_key=True)
    admin_name = models.CharField(max_length=10,null=True,verbose_name='管理员姓名')
    admin_sex = models.CharField(max_length=2,choices=GenderChoices,null=True,verbose_name='管理员性别')
    admin_age = models.CharField(max_length=3,null=True,verbose_name='管理员年龄')
    admin_ident = models.CharField(max_length=18,null=True,verbose_name='管理员身份证')
    admin_tel = models.CharField(max_length=20,null=True,verbose_name='管理员电话')
    admin_email = models.CharField(max_length=50,null=True,verbose_name='管理员EMAIL')
    admin_type = models.IntegerField(default='门店管理员',choices=AdminChoices,verbose_name='管理员类型')

    def __str__(self):
        return self.admin_name
    class Meta:
        verbose_name = '管理员信息'
        verbose_name_plural = '管理员信息'

class store_info(models.Model):
    store_num = models.AutoField(max_length=10,primary_key=True)
    store_addr = models.CharField(max_length=50,null=True,verbose_name='门店地址')
    store_tel = models.CharField(max_length=20,null=True,verbose_name='门店联系方式')
    store_start_time = models.CharField(max_length=20,null=True,verbose_name='门店营业时间')
    store_admin = models.ForeignKey(admin_info,related_name='store_manage',verbose_name='门店管理员')

    def __str__(self):
        return self.store_num
    class Meta:
        verbose_name = '门店信息'
        verbose_name_plural = '门店信息'

class user_info(models.Model):
    GenderChoices = (
        (u'F',u'女'),
        (u'M',u'男'),
    )
    user_num = models.CharField(max_length=15,primary_key=True)
    user_name = models.CharField(max_length=10)
    user_sex = models.CharField(max_length=2,choices=GenderChoices,verbose_name='性别')
    user_age = models.CharField(max_length=3,null=True,verbose_name='年龄')
    user_ident = models.CharField(max_length=18,null=True,verbose_name='身份证号')
    user_tel = models.CharField(max_length=15,null=True,verbose_name='电话')
    user_office = models.CharField(max_length=50,null=True,verbose_name='工作单位')
    user_addr = models.CharField(max_length=50,null=True,verbose_name='地址')
    user_post = models.CharField(max_length=6,null=True,verbose_name='邮编')
    user_email = models.CharField(max_length=50,null=True,verbose_name='EMAIL')

    def __str__(self):
        return self.user_name
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

class rent_order(models.Model):
    order_num = models.CharField(max_length=20,primary_key=True)
    user_num = models.ForeignKey(user_info,related_name='user_rent',verbose_name='租车用户')
    car_num = models.ForeignKey(car_info,related_name='rent_car',verbose_name='车牌')
    user_drive = models.CharField(max_length=12,null=True,verbose_name='驾驶证编号')
    pick_addr = models.ForeignKey(store_info,related_name='pick_store',verbose_name='取车门店')
    #drop_addr = models.ForeignKey(store_info,related_name='drop_store',verbose_name='还车门店')
    pick_time = models.DateField(null=True,verbose_name='取车时间')
    initial_drop_time = models.DateField(null=True,verbose_name='还车时间')
    relet_day = models.IntegerField(default=0,verbose_name='续租天数')
    illegal_info = models.TextField(null=True,verbose_name='违章信息')
    breaken_bill = models.IntegerField(null=True,verbose_name='维修费用')
    illegal_bill = models.IntegerField(null=True,verbose_name='违章费用')

    def __str__(self):
        return self.order_num
    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'

class relet_record(models.Model):
    relet_id = models.AutoField(max_length=10,primary_key=True)
    order_num = models.ForeignKey(rent_order,related_name='relet_order')
    relet_day = models.IntegerField(null=True,verbose_name='续租天数')
    relet_apply_day = models.DateField(auto_now_add=True)
    #重租记录被创建时记录时间

    def __str__(self):
        return self.relet_id
    class Meta:
        verbose_name = '续租信息'
        verbose_name_plural = '续租信息'


class illegal_record(models.Model):
    illegal_id = models.AutoField(primary_key=True)
    illegal_car_num = models.ForeignKey(car_info,related_name='illegal_car',verbose_name='违章车辆车牌')
    illegal_date = models.DateField(null=True,verbose_name='违章时间')
    illegal_bill = models.IntegerField(null=True,verbose_name='违章金额/元')
    illegal_info = models.TextField(null=True,verbose_name='违章信息')
    def __str__(self):
        return self.illegal_id
    class Meta:
        verbose_name = '违章记录'
        verbose_name_plural = '违章记录'
