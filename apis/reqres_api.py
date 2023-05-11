import pytest
from requests import get, post, put, delete, patch


class ApiClient:
    HOST = "https://reqres.in/api"

    @classmethod
    def get_resource_list(cls, resource_name, page=0, delay=None):
        if delay is None:
            url = cls.HOST + "/" + resource_name + "?" + "page=" + str(page)
        else:
            url = cls.HOST + "/" + resource_name + "?" + "page=" + str(page) + "&" + "delay=" + str(delay)
        return get(url)

    @classmethod
    def get_resource(cls, resource_name, resource_id: int):
        url = f'{cls.HOST}/{resource_name}/{str(resource_id)}'
        return get(url)

    @classmethod
    def create_resource(cls, resource_name, resource_body):
        url = f'{cls.HOST}/{resource_name}'
        return post(url, resource_body)

    @classmethod
    def patch_resource(cls, resource_name, resource_id, resource_body):
        url = f'{cls.HOST}/{resource_name}/{str(resource_id)}'
        return patch(url, resource_body)

    @classmethod
    def put_resource(cls, resource_name, resource_id, resource_body):
        url = f'{cls.HOST}/{resource_name}/{str(resource_id)}'
        return put(url, resource_body)

    @classmethod
    def delete_resource(cls, resource_name, resource_id):
        url = f'{cls.HOST}/{resource_name}/{str(resource_id)}'
        return delete(url)

    @classmethod
    def register(cls, creds_body):
        url = f'{cls.HOST}/register'
        return post(url, creds_body)

    @classmethod
    def login(cls, creds_body):
        url = f'{cls.HOST}/login'
        return post(url, creds_body)

    @staticmethod
    def get_reqres(host, path):
        url = host + path
        return get(url)

    @staticmethod
    def post_reqres(host, path, body):
        url = host + path
        return post(url, body)

    @staticmethod
    def put_reqres(host, path, body):
        url = host + path
        return put(url, body)

    @staticmethod
    def patch_reqres(host, path, body):
        url = host + path
        return patch(url, body)

    @staticmethod
    def delete_reqres(host, path):
        url = host + path
        return delete(url)
