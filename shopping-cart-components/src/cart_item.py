# Notlar:
# @property Python’da bir özellik (property) tanımlamak için kullanılan
# bir dekoratördür.
# Normalde bir sınıf metodunu çağırmak için () kullanırsın,
# ama @property sayesinde o metod bir nitelik (attribute) gibi davranır.


class CartItem:
    """
    Bir e-ticaret uygulamasında sepete eklenen ürünü temsil eder.
    Sepete eklenecek ürünün: ürün adı, fiyatı, bağlantısı,
    miktarı ve indirim oranı bilgilerini tutar.
    """
    def __init__(self, name: str, price: float, link: str = "", quantity: int = 1, discount: float = 0.0):
        self.name = name
        self.price = price
        self.link = link
        self.quantity = quantity
        self.discount = discount


    def __str__(self) -> str:
        """
        Ürün bilgilerini okunabilir string formatında döndürür.
        """
        msg_1 = f"\n- {self.name}\n- {self.price:.2f} TL"
        msg_2 = f"\n- %{self.discount * 100:.0f} indirim\n- {self.quantity} adet"
        msg_3 = f"\n- {self.link}"
        return msg_1 + msg_2 + msg_3


    @property
    def total_price(self) -> float:
        """
        İndirimsiz toplam fiyatı döndürür.
        """
        return self.price * self.quantity


    @property
    def discount_price(self) -> float:
        """
        İndirim uygulanmış toplam fiyatı döndürür.
        """
        discount_amount = self.price * self.discount
        return self.total_price - discount_amount


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

    print("Ürün Bilgileri:", item_1)  # __str__ sayesinde otomatik bilgi gösterir.
    print(f"Ürünlerin Toplam Fiyatı (İndirimsiz)    : {item_1.total_price:.2f}")
    print(f"Ürünlerin Toplam Fiyatı (İndirimli)     : {item_1.discount_price:.2f}")
    item_1.quantity += 1
    print(f"Aynı üründen 1 adet daha eklendi.")
    print(f"Ürünlerin Toplam Fiyatı (İndirimsiz)    : {item_1.total_price:.2f}")
    print(f"Ürünlerin Toplam Fiyatı (İndirimli)     : {item_1.discount_price:.2f}")


# output:
# Product Informations: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %10 discount
# - 1 piece
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
# Total Price of Products (Not Discounted)      : 184574.00
# Total Price of Products (Discounted)          : 166116.60
# One more of the same product has been added.
# Total Price of Products (Not Discounted)      : 369148.00
# Total Price of Products (Discounted)          : 350690.60
