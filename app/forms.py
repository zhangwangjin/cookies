# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators,BooleanField
from wtforms.validators import DataRequired,InputRequired,EqualTo

class RegisterForm(Form):
    email=StringField(u'邮箱账号', [DataRequired(message=u"请填入邮箱"),validators.email(message=u"邮箱地址不是正确的")])
    password=PasswordField(u'密    码', [InputRequired(message=u"请输入密码"), EqualTo('rpassword', message=u'两次输入密码不同'),validators.length(min=6,max=16,message=u"密码长度在6~16位")])
    rpassword=PasswordField(u'确认密码', [InputRequired(message=u"请再次输入密码"),validators.length(min=6,max=16,message=u"密码长度在6~16位")])
    accept_tos = BooleanField(u'协议',[validators.DataRequired()])