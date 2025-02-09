from .rest import RestSession, StrOrDict

__all__ = ['ApiChild']


class ApiChild:
    """
    Base class for child APIs of :class:`WebexSimpleApi`
    """

    def __init__(self, session: RestSession):
        #: REST session
        self.session = session

    def __init_subclass__(cls, base: str, **kwargs):
        """
        Subclass registration hook. Each APIChild has a specific endpoint prefix which we gather at subclass
        registration time-

        :param base: APIChild specific URL path
        :param kwargs:
        """
        super().__init_subclass__(**kwargs)
        # save endpoint prefix
        cls.base = base

    def ep(self, path: str = None):
        """
        endpoint URL for given path

        :param path: path after APIChild subclass specific endpoint URI prefix
        :type path: str
        :return: endpoint URL
        :rtype: str
        """
        path = path and f'/{path}' or ''
        return self.session.ep(f'{self.base}{path}')

    def get(self, *args, **kwargs) -> StrOrDict:
        """
        GET request

        :param args:
        :param kwargs:
        :return:
        """
        return self.session.rest_get(*args, **kwargs)

    def post(self, *args, **kwargs) -> StrOrDict:
        """
        POST request

        :param args:
        :param kwargs:
        :return:
        """
        return self.session.rest_post(*args, **kwargs)

    def put(self, *args, **kwargs) -> StrOrDict:
        """
        PUT request

        :param args:
        :param kwargs:
        :return:
        """
        return self.session.rest_put(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        """
        DELETE request

        :param args:
        :param kwargs:
        """
        self.session.rest_delete(*args, **kwargs)
