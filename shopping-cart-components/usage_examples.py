from src import CartItem, ShoppingCart


print("\nEXAMPLE ITEMS\n----------")

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


print("\nEXAMPLE: CART ITEM\n----------")

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


print("\nEXAMPLE: SHOPPING CART\n----------")

shopping_cart = ShoppingCart([item_1, item_2, item_3])
print("Spetteki Ürünlerin Bilgileri:", shopping_cart)














