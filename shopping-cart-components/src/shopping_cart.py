from cart_item import CartItem 


class ShoppingCart:
    """
    """
    def __init__(self, item_list: list[CartItem] = []):
        self.item_list = item_list


    def __str__(self) -> str:
        """
        Sepetteki tüm ürünlerin bilgilerini okunabilir biçimde döndürür.
        """
        # Her öğe için string üret, sonra join ile birleştir.
        return "\n".join(item.__str__() for item in self.item_list)


    def add_item(self) -> None:
        pass


    def remove_item(self) -> None:
        pass


    def update_item_amount(self) -> None:
        pass


    def total_price(self) -> float:
        pass


    def discount_total_price(self) -> float:
        pass


# example use:
if __name__ == "__main__":
     # Bu blok yalnızca dosya doğrudan çalıştırıldığında çalışır.
    # Başka modüller bu sınıfı import etse bile buradaki kodlar çalışmaz.

    item_1 = CartItem(
        name="Hero-XPulse 200 4V",
        price=184574.00,
        link="https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/",
        discount=0.1,
    )
    item_2 = CartItem(
        name="TVS-Raider 125",
        price=149400.00,
        link="https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr",
        discount=0.15,
    )
    item_3 = CartItem(
        name="RKS-Racing R 250",
        price=205000.00,
        link="https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/",
        discount=0.2,
    )

    item_4 = CartItem(
        name="QJMotor-SRK 250 RC",
        price=180000.00,
        link="https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/",
        discount=0.2,
    )

    shopping_cart = ShoppingCart([item_1, item_2, item_3])
    print("\nSpetteki Ürünlerin Bilgileri:", shopping_cart)
