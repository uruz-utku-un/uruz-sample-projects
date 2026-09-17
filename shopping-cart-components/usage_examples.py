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
    print(79*"-")
    print(f"Toplam (indirimsiz): {item.total_price:.2f}")
    print(f"Toplam (indirimli) : {item.discount_price:.2f}")


def demo_shopping_cart(items: list[CartItem]) -> ShoppingCart:
    print("\n=== DEMO: SHOPPING CART ===")

    cart = ShoppingCart(items)
    print(cart)  # '__str__' metodu çalışır.
    print(79*"-")
    print(f"Sepet toplam (indirimsiz): {cart.total_price:.2f}")
    print(f"Sepet toplam (indirimli) : {cart.discount_total_price:.2f}")

    # Örnek işlemler
    cart.remove_item(items[3])
    print(79*"-")
    print("-> QJMotor çıkarıldı")
    print(cart)

    cart.add_item(items[0])
    print(79*"-")
    print("-> Hero-XPulse eklendi")
    print(cart)

    cart.update_item_amount(items[0], UpdateAmountAction.INCREASE)
    print(79*"-")
    print("-> Hero-XPulse adedi artırıldı")
    print(cart)


if __name__ == "__main__":
    items = demo_cart_items()
    demo_single_item(items[0])  # Hero-XPulse 200 4V
    demo_shopping_cart(items)
