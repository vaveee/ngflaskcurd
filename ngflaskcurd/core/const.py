# -*- coding: utf-8 -*-


ITEMS_PER_PAGE = 10

STATUS_NEW = 90
STATUS_PUBLISH = 1
STATUS_UNPUBLISH = 98
STATUS_DELETEED = 99

STATUS = {
          STATUS_NEW: u'新增',
          STATUS_PUBLISH: u'已发布',
          STATUS_UNPUBLISH: u'已下线',
#          STATUS_DELETEED: u'已删除',
          }


GENDER_FEMALE = 1
GENDER_MALE = 2
GENDER = {
          GENDER_FEMALE: u'女士',
          GENDER_MALE: u'男士',
          }

BIRTHDATE_GREGORIAN = 1
BIRTHDATE_LUNAR =2
BIRTHDATE_LUNAR_LEAP_MONTH = 3
BIRTHDATE = {
          BIRTHDATE_GREGORIAN: u'阳历',
          BIRTHDATE_LUNAR: u'阴历',
          BIRTHDATE_LUNAR_LEAP_MONTH: u'阴历闰月',
          }


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

FATE_TYPE_BEFORE = 1
FATE_TYPE_AFTER = 2
FATE_TYPE = {
          FATE_TYPE_BEFORE: u'前运',
          FATE_TYPE_AFTER: u'后运',
          }


ORDER_STATUS_NEW = 2
ORDER_STATUS_PENDING = 3
ORDER_STATUS_CHECKOUT = 4
ORDER_STATUS_COMMIT = 5 #已经支付
ORDER_STATUS_FATE_BEFORE = 6
ORDER_STATUS_FATE_BEFORE_REPLY = 8
ORDER_STATUS_INTERACTION = 9
ORDER_STATUS_FATE_PREREFUND = 10
ORDER_STATUS_FATE_REFUND = 12
ORDER_STATUS_FATE_COMMIT_AFTER = 13
ORDER_STATUS_FATE_AFTER = 14
ORDER_STATUS_FATE_CANCELED = 16

ORDER_STATUS = {
                ORDER_STATUS_NEW : u'待付款',
                ORDER_STATUS_PENDING : u'待付款',
                ORDER_STATUS_CHECKOUT : u'已提交支付',
                ORDER_STATUS_COMMIT : u'已提交预约', #已经支付完成
                ORDER_STATUS_FATE_BEFORE : u'已算前运',
                ORDER_STATUS_FATE_BEFORE_REPLY : u'已反馈前运',
                ORDER_STATUS_INTERACTION : u'交互校正',
                ORDER_STATUS_FATE_PREREFUND : u'已申请退款',
                ORDER_STATUS_FATE_REFUND : u'退款成功',
                ORDER_STATUS_FATE_COMMIT_AFTER : u'待算后运',
                ORDER_STATUS_FATE_AFTER : u'已算后运',
                ORDER_STATUS_FATE_CANCELED : u'用户已取消',
          }

PROVINCE = (u"北京",u"天津",u"河北",u"山西",u"内蒙古",u"辽宁",u"吉林",u"黑龙江",u"上海",u"江苏",u"浙江",u"安徽",u"福建",u"江西",u"山东",u"河南",u"湖北",u"湖南",u"广东",u"广西",u"海南",u"重庆",u"四川",u"贵州",u"云南",u"西藏",u"陕西",u"甘肃",u"青海",u"宁夏",u"新疆",u"香港",u"澳门")

PROMO_CODE_STATUS_NEW = 0
PROMO_CODE_STATUS_USED = 2
PROMO_CODE_STATUS_INVALID = 4
PROMO_CODE_STATUS = {
                     PROMO_CODE_STATUS_NEW:'',
                     PROMO_CODE_STATUS_USED:'',
                     PROMO_CODE_STATUS_INVALID:'',
                     }

SIT_AMOUNT_KEY_PRE = 'sit_amount_key_pre'
SIT_VALUE_KEY_PRE = 'sit_value_key_pre'


ZAN_STATUS_YES = 1
ZAN_STATUS_NO = 0