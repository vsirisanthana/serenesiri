from djangorestframework import status
from djangorestframework.mixins import (
    ModelMixin as DrfModelMixin,
    ReadModelMixin as DrfReadModelMixin,
    CreateModelMixin as DrfCreateModelMixin,
    PaginatorMixin as DrfPaginatorMixin,
)
from djangorestframework.response import ErrorResponse, Response
from enhancedurlobject import EnhancedURLObject


class ReadModelMixin(DrfReadModelMixin):

    def get(self, request, *args, **kwargs):
        instance = super(ReadModelMixin, self).get(request, *args, **kwargs)
        return Response(content=instance, headers={'Last-Modified':instance.last_modified})


class UpdateModelMixin(DrfModelMixin):
    """
    Behavior to update a `model` instance on PUT requests
    """
    def put(self, request, *args, **kwargs):
        model = self.resource.model
        try:
            self.model_instance = self.get_object(*args, **kwargs)
            for (key, val) in self.CONTENT.items():
                setattr(self.model_instance, key, val)
        except model.DoesNotExist:
            raise ErrorResponse(status.HTTP_404_NOT_FOUND)
        self.model_instance.save()
        return self.model_instance


class UpdateOrCreateModelMixin(DrfModelMixin):
    """
    Behavior to update or create a `model` instance on PUT requests
    """
    def put(self, request, *args, **kwargs):
        model = self.resource.model
        try:
            self.model_instance = self.get_object(*args, **kwargs)
            for (key, val) in self.CONTENT.items():
                setattr(self.model_instance, key, val)
        except model.DoesNotExist:
            self.model_instance = model(**self.get_instance_data(model, self.CONTENT, *args, **kwargs))
            self.model_instance.save()
            return Response(status.HTTP_201_CREATED, self.model_instance)
        self.model_instance.save()
        return self.model_instance


class CreateModelMixin(DrfCreateModelMixin):

    def post(self, request, *args, **kwargs):
        response = super(CreateModelMixin, self).post(request, *args, **kwargs)
        response.headers.update({
            'Content-Location': self.resource(self).url(response.raw_content)
        })
        return response


class PaginatorMixin(DrfPaginatorMixin):

    def first(self, page):
        """
        Returns a url to the first page of results
        """
        return self.url_with_page_number(1)

    def last(self, page):
        """
        Returns a url to the last page of results
        """
        return self.url_with_page_number(page.paginator.num_pages)

    def url_with_page_number(self, page_number):
        """
        Constructs a url used for getting the next/previous urls,
        replacing page & limit with updated number
        """
        url = EnhancedURLObject.parse(self.request.build_absolute_uri())

        if page_number != 1:
            url |= 'page', page_number
        else:
            url -= 'page'

        limit = self.get_limit()
        if limit != self.limit:
            url |= 'limit', limit

        return url

    def serialize_page_info(self, page):
        """
        This is some useful information that is added to the response
        """
        links = {'self': {'href': self.request.build_absolute_uri(), 'rel': 'self'}}

        next_page = self.next(page)
        if next_page:
            links['next'] = {'href': next_page, 'rel': 'next'}

        previous_page = self.previous(page)
        if previous_page:
            links['previous'] = {'href': previous_page, 'rel': 'previous'}

        first_page = self.first(page)
        if first_page:
            links['first'] = {'href': first_page, 'rel': 'first'}

        last_page = self.last(page)
        if last_page:
            links['last'] = {'href': last_page, 'rel': 'last'}

        return {
            'links': links,
            'page': page.number,
            'pages': page.paginator.num_pages,
            'per_page': self.get_limit(),
            'total': page.paginator.count,
        }
