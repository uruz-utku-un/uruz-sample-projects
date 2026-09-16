# Notlar:
# @property Python’da bir özellik (property) tanımlamak için kullanılan
# bir dekoratördür.
# Normalde bir sınıf metodunu çağırmak için () kullanırsın,
# ama @property sayesinde o metod bir nitelik (attribute) gibi davranır.


class CartItem:
    """
    Bir e-ticaret uygulamasında sepete eklenen ürünü temsil eder.
    Ürün adı, fiyatı, bağlantısı, miktarı ve indirim oranı bilgilerini tutar.
    """

    
    def __init__(self, name: str, price: float, link: str = "", quantity: int = 1, discount: float = 0.0):
        """
        CartItem nesnesi oluşturur.

        Args:
            name (str): Ürün adı.
            price (float): Ürün birim fiyatı.
            link (str, optional): Ürün bağlantısı. Varsayılan "".
            quantity (int, optional): Ürün miktarı. Varsayılan 1.
            discount (float, optional): İndirim oranı (0–1 arası). Varsayılan 0.0.
        """
        self.name = name
        self.price = price
        self.link = link
        self.quantity = quantity
        self.discount = discount


    def __str__(self) -> str:
        """
        Ürün bilgilerini okunabilir string formatında döndürür.

        Returns:
            str: Ürün adı, fiyatı, indirim oranı, miktarı ve bağlantısını
                 içeren string.
        """
        msg_1 = f"\n- {self.name}\n- {self.price:.2f} TL"
        msg_2 = f"\n- %{self.discount * 100:.0f} indirim\n- {self.quantity} adet"
        msg_3 = f"\n- {self.link}"
        return msg_1 + msg_2 + msg_3


    @property
    def total_price(self) -> float:
        """
        İndirimsiz toplam fiyatı döndürür.

        Returns:
            float: Ürün miktarı ile birim fiyatın çarpımı.
        """
        return self.price * self.quantity


    @property
    def discount_price(self) -> float:
        """
        İndirim uygulanmış toplam fiyatı döndürür.

        Returns:
            float: İndirimsiz toplam fiyattan indirim miktarı çıkarılarak
                   hesaplanan fiyat.
        """
        discount_amount = self.price * self.discount
        return self.total_price - discount_amount
