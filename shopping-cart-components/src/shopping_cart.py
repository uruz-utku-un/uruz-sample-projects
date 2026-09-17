# created 2026-09-15, by Utku Ün (Uruz)


# Notlar:
# @property Python’da bir özellik (property) tanımlamak için kullanılan
# bir dekoratördür.
# Normalde bir sınıf metodunu çağırmak için () kullanırsın,
# ama @property sayesinde o metod bir nitelik (attribute) gibi davranır.


from enum import Enum
from .cart_item import CartItem


class UpdateAmountAction(Enum):
    INCREASE = "increase"
    DECREASE = "decrease"


class ShoppingCart:
    """
    Bir e-ticaret uyuglamasında sepeti temsil eder.
    """


    def __init__(self, item_list: list[CartItem] | None = None) -> None:
        """
        ShoppingCart nesnesi oluşturur.

        Args:
            item_list (list[CartItem] | None): Başlangıçta sepete eklenecek
            ürünler.
        """
        self.item_list = item_list or []


    def __str__(self) -> str:
        """
        Sepetteki tüm ürünlerin bilgilerini okunabilir biçimde döndürür.

        Returns:
            str: Sepetteki ürünlerin string temsili.
        """
        # Her öğe için string üret, sonra join ile birleştir.
        return "\n".join(item.__str__() for item in self.item_list)


    def add_item(self, new_item: CartItem) -> None:
        """
        Ürün sepette zaten varsa miktarını artırır, yoksa sepete ekler.

        Args:
            new_item (CartItem): Sepete eklenecek ürün.
        """
        # ürün zaten sepette mevcutsa:
        for item in self.item_list:
            # ürün adı üzerinden kontrol (ileride id kullanılabilir.)
            if item.name == new_item.name:
                item.quantity += 1
                return

        # ürün sepette mevcut değilse:
        self.item_list.append(new_item)


    def remove_item(self, remove_item: CartItem) -> None:
        """
        Ürünü sepetten çıkarır.

        Args:
            remove_item (CartItem): Sepetten çıkarılacak ürün.
        """
        # Listeyei yeniden oluştur, kaldırılacak ürünü listeye dahil etme.
        self.item_list = [
            item for item in self.item_list if item != remove_item
        ]


    def update_item_amount(
            self,
            target_item: CartItem,
            action: UpdateAmountAction
    ) -> None:
        """
        Sepetteki ürün miktarını 1 birim artırır veya azaltır.

        Args:
            target_item (CartItem): Güncellenecek ürün.
            action (UpdateAmountAction): INCREASE veya DECREASE.

        Raises:
            ValueError: Ürün sepette yoksa.
        """
        for item in self.item_list:
            if item.name == target_item.name:
                if action == UpdateAmountAction.INCREASE:
                    item.quantity = max(100, item.quantity + 1)
                elif action == UpdateAmountAction.DECREASE:
                    item.quantity = max(0, item.quantity - 1)
                return

        raise ValueError(f"{target_item.name} sepette bulunamadı.")


    @property
    def total_price(self) -> float:
        """
        Sepetteki ürünlerin indirimsiz toplam fiyatını döndürür.

        Returns:
            float: İndirimsiz toplam fiyat.
        """
        return sum(item.total_price for item in self.item_list)


    @property
    def discount_total_price(self) -> float:
        """
        Sepetteki ürünlerin indirim uygulanmış toplam fiyatını döndürür.

        Returns:
            float: İndirimli toplam fiyat.
        """
        return sum(item.discount_price for item in self.item_list)
