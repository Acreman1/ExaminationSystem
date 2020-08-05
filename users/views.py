from django.shortcuts import redirect
from rest_framework import generics,views,viewsets,authentication,mixins
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework_jwt.authentication import jwt_decode_handler
from utils.peimissions import IsOwnerReadOnly
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password,check_password
from email_send import send_register_email
from .models import EmailVerifyRecord,VerifyCode
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import CreateModelMixin
import re,random
from yunpian import YunPian
from ExaminationSystem.settings import APIKEY
# from rest_framework_jwt.authentication import jwt_decode_handler
# Create your views here.
User = get_user_model()

class CustomBackend(ModelBackend):
    # 自定义用户验证
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserPutView(viewsets.ReadOnlyModelViewSet,generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    return {
        'token': token,
        'user': UserSerializers(user, context={'request': request}).data
    }


#验证码
class CodeViewset(views.APIView):
    def post(self,request):
        mobile = request.POST.get('username','')
        if mobile:
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 生成手机验证码
                code = VerifyCode()
                code.mobile = mobile
                c = random.randint(1000, 9999)
                code.code = str(c)
                code.save()
                code = VerifyCode.objects.filter(mobile=mobile).first().code
                yunpian = YunPian(APIKEY)
                yunpian.send_sms(code=code, mobile=mobile)
                res = {
                    'msg': '验证码已发送'
                }
                return Response(res)
            else:
                res = {
                    'msg':'请输入有效手机号码!'
                }
                return Response(res)
        else:
            res = {
                'msg': '手机号不能为空！'
            }
            return Response(res)




#手机注册
class PhoneViewset(CreateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        return serializer.save(password=make_password(self.request.data['password']),mobile=self.request.data['username'])


#邮箱注册
class UserViewset(generics.CreateAPIView,viewsets.GenericViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    def perform_create(self, serializer):
        return serializer.save(password=make_password(self.request.data['password']),email=self.request.data['username'],is_active=0)



#发送
class SendMailViewset(views.APIView):
    def post(self,request):
        email = request.POST.get('email')
        send_register_email(email,send_type='register')
        res = {
            'status':200
        }
        return Response(res)


#激活
class ActiveViewset(views.APIView):
    def get(self,request,code):
        all_record = EmailVerifyRecord.objects.filter(code=code)
        if all_record:
            for record in all_record:
                email = record.email
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
            return redirect('http://127.0.0.1:5500/templates/web/index.html#')
        else:
            return Response('激活失败')


#忘记密码
class ForgetViewset(views.APIView):
    def post(self,request):
        email = self.request.data['email']
        send_register_email(email,send_type='forget')
        res = {
            'status':200
        }
        return Response(res)


#登录邮箱
class ResetViewset(views.APIView):
    def get(self,request,code):
        all_record = EmailVerifyRecord.objects.filter(code=code)
        if all_record:
            return redirect('http://127.0.0.1:5500/templates/web/reset.html')
        else:
            return Response('登录邮箱失败')


#重置密码
class ModifyPwdView(views.APIView):
    def post(self,request):
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        if pwd1 == pwd2:
            obj = User.objects.get(email=email)
            obj.password = make_password(pwd2)
            obj.save()
            res = {
                'status': 200
            }
            return Response(res)
        else:
            res = {
                'msg': '修改密码失败'
            }
            return Response(res)




















