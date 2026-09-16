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
