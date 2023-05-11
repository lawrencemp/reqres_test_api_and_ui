import pytest

name_job_list = [
    {
        "name": "morpheus",
        "job": "leader"
    },
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]

partial_name_job_list = [
    {
        "name": "Konstantin"
    },
    {
        "job": "Autotester"
    }
]

register_data_list = [
    {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    },
    pytest.param({"email": "sydney@fife"}, marks=pytest.mark.xfail)

]

login_data_list = [
    {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    },
    pytest.param({"email": "peter@klaven"}, marks=pytest.mark.xfail)
]
