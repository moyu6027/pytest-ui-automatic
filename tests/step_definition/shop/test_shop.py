# encoding: utf-8
"""As a new user, I want to be order a t-shirt feature tests."""

import allure
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from page_objects.registation.registration_object import RegistrationPage
from page_objects.shop.shop_object import ShopPage
from utils.bdd_helper import BddHelper

feature_path = BddHelper.get_feature_path("shop/shop_order_t_shirt.feature")


@scenario(feature_path, '我按照购物流程进行下单, 新用户注册等操作')
def test_shop_order_t_shirt():
    """我按照购物流程进行下单, 新用户注册等操作."""
    pass


@scenario(feature_path, '进入首页后, 查看附件数量')
def test_shop_attachment_count():
    pass


@given('Sean 作为新用户需要注册')
def register_account(page):
    """Sean 作为新用户需要注册."""
    ShopPage(page).go_to_the_second_cart_step()
    RegistrationPage(page).register_account()


@given('Sean 完成了下单')
def finish_order_after_registration(page):
    """Sean 完成了下单."""
    ShopPage(page).finish_order_after_registration()


@given('Sean 打开了T-shirt 分类')
def open_t_shirt_category(page):
    """Sean 打开了T-shirt 分类."""
    ShopPage(page).open_t_shirt_category()


@given('Sean 打开网站首页')
def open_site(page):
    """Sean 打开网站首页."""
    ShopPage(page).open_site()


@given('Sean 选了一件T-shirt加入购物车并进行下一步')
def add_item_to_cart_and_proceed(page):
    """Sean 选了一件T-shirt加入购物车并进行下一步."""
    ShopPage(page).add_item_to_cart_and_proceed()


@when('Sean 查看个人资料订单页面')
def open_profile_order_page(page):
    """Sean 查看个人资料订单页面."""
    ShopPage(page).open_profile_order_page()


@then('Sean 发现订单显示丢失')
def is_order_present(page):
    """Sean 发现订单显示丢失."""
    assert ShopPage(page).is_order_present(), 'Order missed'


@then('发现附件数量异常')
def is_attachments_count(page):
    assert False
