from src import CartItem, ShoppingCart, UpdateAmountAction


def demo_cart_items() -> list[CartItem]:
    print("\n=== DEMO: CART ITEMS ===")

    items = [
        CartItem(
            name="Hero-XPulse 200 4V",
            price=184574.00,
            link="https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/",
            discount=0.0,
        ),
        CartItem(
            name="TVS-Raider 125",
            price=149400.00,
            link="https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr",
            discount=0.1,
        ),
        CartItem(
            name="RKS-Racing R 250",
            price=205000.00,
            link="https://www.rksmotor.com.tr/model/r250.html",
            discount=0.15,
        ),
        CartItem(
            name="QJMotor-SRK 250 RC",
            price=180000.00,
            link="https://tr.qjmotor.com/products_details/69.html",
            discount=0.2,
        ),
    ]

    for item in items:
        print(item)  # '__str__' metodu çalışır.

    return items


def demo_single_item(item: CartItem):
    print("\n=== DEMO: SINGLE ITEM ===")

    print(item)  # '__str__' metodu çalışır.
    print(f"\n>>> Toplam (indirimsiz): {item.total_price:.2f}")
    print(f">>> Toplam (indirimli) : {item.discount_price:.2f}")


def demo_shopping_cart(items: list[CartItem]) -> ShoppingCart:
    print("\n=== DEMO: SHOPPING CART ===")

    cart = ShoppingCart(items)
    print(cart)  # '__str__' metodu çalışır.
    print(f"\n>>> Sepet toplam (indirimsiz): {cart.total_price:.2f}")
    print(f">>> Sepet toplam (indirimli) : {cart.discount_total_price:.2f}")

    print(79*"-")

    # Örnek işlemler
    cart.remove_item(items[3])
    print("\n-> QJMotor çıkarıldı")
    print(cart)

    print(79*"-")

    cart.add_item(items[0])
    print("\n-> Hero-XPulse eklendi")
    print(cart)

    print(79*"-")

    cart.update_item_amount(items[0], UpdateAmountAction.INCREASE)
    print("\n-> Hero-XPulse adedi artırıldı")
    print(cart)


if __name__ == "__main__":
    items = demo_cart_items()
    demo_single_item(items[0])  # Hero-XPulse 200 4V
    demo_shopping_cart(items)


### OUTPUT ###
"""
=== DEMO: CART ITEMS ===

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

- QJMotor-SRK 250 RC
- 180000.00 TL
- %20 indirim
- 1 adet
- https://tr.qjmotor.com/products_details/69.html
 
=== DEMO: SINGLE ITEM ===

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

>>> Toplam (indirimsiz): 184574.00
>>> Toplam (indirimli) : 184574.00

=== DEMO: SHOPPING CART ===

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

- QJMotor-SRK 250 RC
- 180000.00 TL
- %20 indirim
- 1 adet
- https://tr.qjmotor.com/products_details/69.html

>>> Sepet toplam (indirimsiz): 718974.00
>>> Sepet toplam (indirimli) : 637284.00
-------------------------------------------------------------------------------

-> QJMotor çıkarıldı

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html
-------------------------------------------------------------------------------

-> Hero-XPulse eklendi

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 2 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html
-------------------------------------------------------------------------------

-> Hero-XPulse adedi artırıldı

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 3 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html
"""
