
from ngflaskcurd.utils.routing import expose
from .models import BaseIndexView 


class IndexView(BaseIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


