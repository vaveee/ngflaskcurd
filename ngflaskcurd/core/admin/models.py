# coding : utf -8

from flask.ext.admin.contrib.fileadmin import FileAdmin as _FileAdmin
from flask.ext.admin.babel import gettext, ngettext
from flask.ext.admin import AdminIndexView
from flask.ext.admin import BaseView as AdminBaseView
from flask.ext.admin.actions import action
from flask.ext.admin import helpers as h
from flask.ext.security import current_user
from flask.ext.security.utils import url_for_security
from flask import redirect, flash, url_for, Response, current_app

from flask.ext.htmlbuilder import html


class Roled(object):
    def is_accessible(self):
        roles_accepted = getattr(self, 'roles_accepted', None)
        if roles_accepted:
            accessible = any(
                [current_user.has_role(role) for role in roles_accepted]
            )
            return accessible
        return True

    def _handle_view(self, name, *args, **kwargs):
        if not current_user.is_authenticated():
            return redirect(url_for_security('login', next="/admin"))
        if not self.is_accessible():
            return self.render("admin/denied.html")


def format_datetime(self, request, obj, fieldname, *args, **kwargs):
    return html.div(style='min-width:130px;')(
        getattr(obj, fieldname).strftime(self.get_datetime_format())
    )


def view_on_site(self, request, obj, fieldname, *args, **kwargs):
    endpoint = kwargs.pop('endpoint', 'detail')
    return html.a(
        href=obj.get_absolute_url(endpoint),
        target='_blank',
    )(html.i(class_="icon icon-eye-open", style="margin-right: 5px;")(),
      _l('View on site'))


def format_ul(self, request, obj, fieldname, *args, **kwars):
    field = getattr(obj, fieldname)
    column_formatters_args = getattr(self, 'column_formatters_args', {})
    _args = column_formatters_args.get('ul', {}).get(fieldname, {})
    ul = html.ul(style=_args.get('style', "min-width:200px;max-width:300px;"))
    placeholder = _args.get('placeholder', u"{i}")
    lis = [html.li(placeholder.format(item=item)) for item in field]
    return ul(*lis)


def format_status(self, request, obj, fieldname, *args, **kwargs):
    status = getattr(obj, fieldname)
    column_formatters_args = getattr(self, 'column_formatters_args', {})
    _args = column_formatters_args.get('status', {}).get(fieldname, {})
    labels = _args.get('labels', {})
    return html.span(
        class_="label label-{0}".format(labels.get(status, 'default')),
        style=_args.get('style', 'min-height:18px;')
    )(status)


def get_url(self, request, obj, fieldname, *args, **kwargs):
    column_formatters_args = getattr(self, 'column_formatters_args', {})
    _args = column_formatters_args.get('get_url', {}).get(fieldname, {})
    attribute = _args.get('attribute', None)
    method = _args.get('method', 'get_absolute_url')
    text = getattr(obj, fieldname, '')
    if attribute:
        target = getattr(obj, attribute, None)
    else:
        target = obj

    url = getattr(target, method, lambda: '#')()

    return html.a(href=url)(text if text not in [None, 'None'] else '')


class FileAdmin(Roled, _FileAdmin):
    def __init__(self, *args, **kwargs):
        self.roles_accepted = kwargs.pop('roles_accepted')
        super(FileAdmin, self).__init__(*args, **kwargs)




class BaseIndexView(Roled, AdminIndexView):
    pass


class BaseView(Roled, AdminBaseView):
    pass


