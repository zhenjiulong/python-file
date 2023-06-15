# shopping_list = []
# shopping_list.append("键盘")
# shopping_list.append("键帽")
# shopping_list.append("电竞椅")
# shopping_list.append("鼠标")
# print(shopping_list)
# print(len(shopping_list))
# shopping_list.remove("键帽")
# print(shopping_list)
class ShoppingList:
    """初始化购物清单ShoppingList是一个字典类型，包含商品名和对应的价格
    eg:{"牙刷":7,"毛巾":10,"电池":3}"""
    def __init__(self,shoppinglist):
        self.shoppinglist = shoppinglist

        """返回清单上有多少商品"""
    def get_item_count(self):
        return len(self.shoppinglist)

    """返回购物清单商品总额"""
    def get_total_price(self):
        total_price=0
        for price in self.shoppinglist.values():
            total_price += price
        return total_price


