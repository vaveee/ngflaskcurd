# -*- coding:utf-8 -*-

from __future__ import absolute_import
import random
import hashlib
import uuid
import xml.etree.ElementTree as ET

def get_range_items_from_header(headers):
    """
    Header: "Range: items=start-stop"
    """
    range_str = headers.get('Range')
    if range_str and 'items' in range_str:
        _ = range_str.split('=')
        return [max(0, int(x) - 1) for x in _[1].split('-')]
    return 0, 10


def generate_range_items_for_header(start, stop):
    return {"Range": "items=%s-%s" % (start, stop)}


def generate_content_range_items_for_header(start, stop, count):
    return {'Content-Range': 'items %s-%s/%s' % (start, stop, count)}


def get_current_page_from_header(headers):
    content_range = headers.get('Content-Range')
    if not content_range:
        return
    start, stop = [int(x) for x in content_range.split(' ')[1].split('/')[0].split('-')]
    assert stop > start
    return start / (stop - start) + 1


def get_count_from_header(headers):
    content_range = headers.get('Content-Range')
    if not content_range:
        return
    count = int(content_range.split(' ')[1].split('/')[1])
    return count


def random_string_only_with_number(length):
    _ = str(random.randint(10 ** length, 10 ** (length + 1)))
    return _[0:length]


def md5sum(string):
    return hashlib.md5(string).hexdigest()


def sha1sum(string):
    return hashlib.sha1(string).hexdigest()


def get_really_ip(request):
    x_forwarded_for = request.headers.get('x_forwarded_for')
    if not x_forwarded_for:
        return request.remote_addr
    return x_forwarded_for.split(',')[0]


def gen_sn():
    return uuid.uuid1().get_hex()

def xml_to_dict(xml_str):
    root = ET.fromstring(xml_str)
    child = list(root)
    dict_params = {}
    for i in child:
        dict_params[i.tag] = i.text
    return dict_params