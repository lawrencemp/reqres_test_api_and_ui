import pytest
from utils.data import name_job_list, partial_name_job_list, login_data_list, register_data_list


@pytest.mark.api_test
class TestApi:
    @pytest.mark.parametrize("page", [pytest.param(0, marks=pytest.mark.xfail), 1, 2])
    def test_get_list_of_users(self, api_calling, page):
        response = api_calling.get_resource_list("users", page)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert page == response_body["page"], f'Должна быть {page} страница. получена {response_body["page"]}'

    @pytest.mark.parametrize("user_id", [2, pytest.param(23, marks=pytest.mark.xfail)])
    def test_get_single_user(self, api_calling, user_id):
        response = api_calling.get_resource("users", user_id)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert response_body["data"] is not None, "Нет данных юзера в ответе"

    @pytest.mark.parametrize("resource_id", [2, pytest.param(23, marks=pytest.mark.xfail)])
    def test_get_single_resource(self, api_calling, resource_id):
        response = api_calling.get_resource("unknown", resource_id)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert response_body["data"] is not None, "Нет данных об этом ресурсе в ответе"

    @pytest.mark.parametrize("user_json", name_job_list)
    def test_create_new_user(self, api_calling, user_json):
        response = api_calling.create_resource("users", user_json)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 201)
        assert response_body["name"] == user_json["name"] and response_body["job"] == user_json["job"], "Не совпадают" \
                                                                                                        " поля тела"

    @pytest.mark.parametrize("user_json", name_job_list)
    def test_put_user(self, api_calling, user_json):
        response = api_calling.put_resource("users", 2, user_json)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert response_body["name"] == user_json["name"] and response_body["job"] == user_json["job"], "Не совпадают" \
                                                                                                        " поля тела"

    @pytest.mark.parametrize("part_of_user_json", partial_name_job_list)
    def test_patch_user(self, api_calling, part_of_user_json):
        response = api_calling.patch_resource("users", 2, part_of_user_json)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        if 'name' in part_of_user_json:
            assert response_body["name"] == part_of_user_json["name"], "Не совпадают поля тела"
        else:
            assert response_body["job"] == part_of_user_json["job"], "Не совпадают поля тела"

    @pytest.mark.parametrize("user_delete_id", [12, 20])
    def test_delete_user(self, api_calling, user_delete_id):
        response = api_calling.delete_resource("users", user_delete_id)
        api_calling.is_response_code_correct(response, 204)

    @pytest.mark.parametrize("creds_json", register_data_list)
    def test_register_user(self, api_calling, creds_json):
        response = api_calling.register(creds_json)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert response_body["token"] is not None, "В теле ответа пришла ошибка"

    @pytest.mark.parametrize("creds_json", login_data_list)
    def test_login_user(self, api_calling, creds_json):
        response = api_calling.login(creds_json)
        response_body = response.json()
        api_calling.is_response_code_correct(response, 200)
        assert response_body["token"] is not None, "В теле ответа пришла ошибка"

    @pytest.mark.parametrize("delay", [0, 3])
    def test_get_with_delay(self, api_calling, delay):
        response = api_calling.get_resource_list("users", 2, delay)
        api_calling.is_response_code_correct(response, 200)
