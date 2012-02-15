from djangorestframework.resources import ModelResource


class BaseModelResource(ModelResource):
    exclude = ()
    include = ('links',)

    def links(self, instance):
        return [{
            'href': self.url(instance),
            'rel': 'self',
        }]