@hotlink @shop
  Feature: As a new user,
    I want to be order a t-shirt,
    In order to buy a t-shirt, I must register my account

    Background:
      Given Sean 打开网站首页

    Scenario: 我按照购物流程进行下单, 新用户注册等操作
      Given Sean 打开了T-shirt 分类
      And Sean 选了一件T-shirt加入购物车并进行下一步
      And Sean 作为新用户需要注册
      And Sean 完成了下单
      When Sean 查看个人资料订单页面
      Then Sean 发现订单显示丢失


      Scenario: 进入首页后, 查看附件数量
        Then 发现附件数量异常