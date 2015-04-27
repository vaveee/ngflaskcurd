# -*- coding: utf-8 -*-
import requests
from hashlib import md5
from .excep import MissingParameter
from .excep import ParameterValueError
import six
from tornado.escape import utf8
import urllib
import xml.etree.ElementTree as ET
from ...utils.hashcompat import md5_constructor

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

def encode_dict(params):
    return {k:six.u(v).encode('utf-8') if isinstance(v, str) else v.encode('utf-8') if isinstance(v, six.string_types) else v for k, v in six.iteritems(params)}

class Alipay(object):

    GATEWAY_URL = 'https://mapi.alipay.com/gateway.do'
    SQ_TOKEN = "http://wappaygw.alipay.com/service/rest.htm"

    def __init__(self, pid, key, seller_email):
        self.key = key
        self.pid = pid
        self.seller_email = seller_email
        self.default_params = {'_input_charset': 'utf-8',
                               'partner': pid,
                               'seller_email': seller_email,
                               'payment_type': '1'}

    def _generate_sign(self, params):
        src = '&'.join(['%s=%s' % (key, value) for key, 
                        value in sorted(params.items())]) + self.key
        return md5(src.encode('utf-8')).hexdigest()

    def _check_params(self, params, names):
        if not all(k in params for k in names):
            raise MissingParameter('missing parameters')
        return

    def _build_url(self, service, **kw):
        params = self.default_params.copy()
        params['service'] = service
        params.update(kw)
        params.update({'sign_type': 'MD5',
                       'sign': self._generate_sign(params)})

        return '%s?%s' % (self.GATEWAY_URL, urlencode(encode_dict(params)))

    def create_direct_pay_by_user_url(self, **kw):
        '''即时到帐'''
        self._check_params(kw, ['out_trade_no', 'subject'])

        if not kw.get('total_fee') and \
           not (kw.get('price') and kw.get('quantity')):
            raise ParameterValueError('total_fee or (price && quantiry)\
             must have one')

        url = self._build_url('create_direct_pay_by_user', **kw)
        return url

        # 获取授权令牌
    def phone_wap_pay_by_buyuer_url(self, **kw):
        kw["seller_account_name"] = self.seller_email
        
        strs = "<direct_trade_create_req>"
        for k, v in kw.items():
            strs += "<" + str(k) + ">" + str(v) + "</" + str(k) + ">";
        strs += "</direct_trade_create_req>"
        
        pasas = {
                 "req_id":kw.get("out_trade_no"), 
                 "req_data":strs.decode("utf-8")
                 }
        url = self._phonewap_url('alipay.wap.trade.create.direct', **pasas)
        
        urls = urllib.urlopen(url)
        readto = urllib.unquote(urls.read())
        req = readto.split("&")
        dicreq = {}
        for i in req:
            itemvk = i.split("=", 1)
            dicreq[itemvk[0]] = itemvk[1]
    
        xda = dicreq.get("res_data") or dicreq.get("res_error")
        # 读取返回的数据
        if xda and str(dicreq.get("req_id")) == str(pasas.get("req_id")):
            xda = xda.replace("+", " ")
            
            root = ET.fromstring(xda)
            child = list(root)
            rev = {}
            for i in child:
                rev[i.tag] = i.text
            if rev.get('request_token'):
                su_token = rev.get('request_token')
                print '---本次token为---', su_token
                return su_token
            if rev.get('code'):
                return u'发生错误'
                
        return u'发生错误'
    
    def phone_jiaoyi_url(self, **kw):
        '''手机网站交易'''
        token = self.phone_wap_pay_by_buyuer_url(**kw)
        if token.find(u"错误") > -1:
            return '---------发生错误-----------'
        tostr = "<auth_and_execute_req><request_token>" + token + "</request_token></auth_and_execute_req>"
        jy = {
              'req_data':tostr,
              "req_id":kw.get("out_trade_no")
              }
        url = self._phonewap_url('alipay.wap.auth.authAndExecute', **jy)
        return url
    
    def _phonewap_url(self, service, **kw):
        params = self.default_params.copy()
        params['service'] = service
        params["format"] = "xml"
        params["v"] = "2.0"
        params['sec_id'] = 'MD5'
        params.update(kw)
        params.update({'sign': self._generate_sign(params)})
        return '?'.join([self.SQ_TOKEN, urlencode(encode_dict(params))])

    def create_partner_trade_by_buyer_url(self, **kw):
        '''担保交易'''
        names = ['out_trade_no', 'subject', 'logistics_type',
                 'logistics_fee', 'logistics_payment', 'price', 'quantity']
        self._check_params(kw, names)
        url = self._build_url('create_partner_trade_by_buyer', **kw)
        return url

    def trade_create_by_buyer_url(self, **kw):
        '''标准双接口'''
        names = ['out_trade_no', 'subject', 'logistics_type',
                 'logistics_fee', 'logistics_payment', 'price', 'quantity']
        self._check_params(kw, names)

        url = self._build_url('trade_create_by_buyer', **kw)
        return url
    
    def send_goods_confirm_by_platform(self, **kw):
        '''确认发货接口'''
        names = ['trade_no', 'logistics_name', 'invoice_no']
        self._check_params(kw, names)

        url = self._build_url('send_goods_confirm_by_platform', **kw)
        return url

    def verify_notify(self, **kw):
#        sign = kw.pop('sign')
#        kw.pop('sign_type')
#        if self._generate_sign(kw) == sign:
#            return requests.get("https://mapi.alipay.com/gateway.do?service=notify_verify&partner=%s&notify_id=%s" % (self.pid, kw['notify_id'])).text == 'true'
#        else:
#            return False
#  
        notify_id = kw.pop('notify_id')
        if notify_id:
            params = {}
            params['partner'] = self.pid
            params['notify_id'] = notify_id
            if 'http' == 'https':
                params['service'] = 'notify_verify'
                gateway = 'https://mapi.alipay.com/gateway.do'
            else:
                gateway = 'http://notify.alipay.com/trade/notify_query.do'
            verify_url = "%s?%s" % (gateway, urllib.urlencode(params))
            
            return urllib.urlopen(verify_url).read()
        return False

    'add 2015-1-30'
    def build_mysign(self, prestr, key):
        sign_type = "MD5"
        if sign_type == "MD5":
            return md5_constructor(prestr+key).hexdigest()
        return ""

    def fixed_params_filter(self,params):
        """sort the params dict and exclude "sign, sign_type", and enmpty keys
        """
        ks = params.keys()
        new_params = {}
        for k in ks:
            v = params[k]
            if k not in ("sign", "sign_type") and v != '':
                new_params[k] = utf8(v)
        prestr = "service=%s&v=%s&sec_id=%s&notify_data=%s" % (
            new_params["service"],
            new_params["v"],
            new_params["sec_id"],
            new_params["notify_data"])
        return new_params, prestr

