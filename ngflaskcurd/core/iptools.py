#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

import requests


class Ip(object):
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.country = kwargs.get('country')
        self.area = kwargs.get('area')
        self.region = kwargs.get('region')
        self.city = kwargs.get('city')
        self.county = kwargs.get('county')
        self.isp = kwargs.get('isp')
        self.country_id = kwargs.get('country_id')
        self.area_id = kwargs.get('area_id')
        self.region_id = kwargs.get('region_id')
        self.county_id = kwargs.get('county_id')
        self.isp_id = kwargs.get('isp_id')

    def to_string(self, format=''):
        """XX国 xx省 xx市 xx县 运营商"""
        # TODO: 支持自定义格式
        return '%s %s %s %s %s' % (self.country, self.region, self.city, self.county, self.isp)


class IpParser(object):
    TAOBAO_IP_API = 'http://ip.taobao.com/service/getIpInfo.php'

    def __init__(self):
        pass

    def get_ip(self, ip):
        response = requests.get(self.TAOBAO_IP_API, params={'ip': ip})
        content = response.json()
        if content.get('code', 1) == 1:
            return
        return Ip(**content.get('data'))


def get_ip_info(ip):
    ip_parser = IpParser()
    return ip_parser.get_ip(ip)


if __name__ == '__main__':
    testing_ip = '121.33.113.220'
    ip = get_ip_info(testing_ip)
    print ip
    print ip.to_string()