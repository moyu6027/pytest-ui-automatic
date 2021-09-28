# -*- coding: utf-8 -*-
# @Author  : sean
# @File    : api_helper.py
from utils.api_helper.api_abilities import ApiAbilities


def authenticate(base_url: str, user) -> None:
    _data = user
    _url = f'/Account/v1/Login'

    response = ApiAbilities().requests(host=base_url, url=_url, method='POST', data=_data)

    if response.status_code == 200:
        return response.json()


