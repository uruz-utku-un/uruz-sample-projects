from src import CartItem, ShoppingCart, UpdateAmountAction


print("\nEXAMPLE CART ITEMS\n----------")

item_1 = CartItem(
    name="Hero-XPulse 200 4V",
    price=184574.00,
    link="https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/",
    discount=0.0,
)
item_2 = CartItem(
    name="TVS-Raider 125",
    price=149400.00,
    link="https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr",
    discount=0.1,
)
item_3 = CartItem(
    name="RKS-Racing R 250",
    price=205000.00,
    link="https://www.rksmotor.com.tr/model/r250.html",
    discount=0.15,
)
item_4 = CartItem(
    name="QJMotor-SRK 250 RC",
    price=180000.00,
    link="https://tr.qjmotor.com/products_details/69.html",
    discount=0.2,
)

item_list = [item_1, item_2, item_3, item_4]
print("Ürünler:", "\n".join(str(item) for item in item_list))

### output ###
# EXAMPLE CART ITEMS
# ----------
# Products: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 1 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

# - TVS-Raider 125
# - 149400.00 TL
# - %10 indirim
# - 1 adet
# - https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

# - RKS-Racing R 250
# - 205000.00 TL
# - %15 indirim
# - 1 adet
# - https://www.rksmotor.com.tr/model/r250.html

# - QJMotor-SRK 250 RC
# - 180000.00 TL
# - %20 indirim
# - 1 adet
# - https://tr.qjmotor.com/products_details/69.html


print("\nEXAMPLE: CART ITEM\n----------")

print("Ürün Bilgileri:", item_1, "\n")  # __str__ sayesinde otomatik bilgi gösterir.
print(f"Ürünlerin Toplam Fiyatı (İndirimsiz)    : {item_1.total_price:.2f}")
print(f"Ürünlerin Toplam Fiyatı (İndirimli)     : {item_1.discount_price:.2f}")

### output ###
# EXAMPLE: CART ITEM
# ----------
# Product Informations: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 discount
# - 1 piece
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
#
# Total Price of Products (Not Discounted)      : 184574.00
# Total Price of Products (Discounted)          : 184574.00
# One more of the same product has been added.
# Total Price of Products (Not Discounted)      : 369148.00
# Total Price of Products (Discounted)          : 369148.00


print("\nEXAMPLE: SHOPPING CART\n----------")

shopping_cart = ShoppingCart(item_list)
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.remove_item(item_4)
print("\n4. Ürün (QJMotor-SRK 250 RC) sepetten Çıkarıldı.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.remove_item(item_2)
print("\n2. Ürün (TVS-Raider 125) sepetten Çıkarıldı.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.remove_item(item_3)
print("\n3. Ürün (RKS-Racing R 250) sepetten Çıkarıldı.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.add_item(item_1)
print("\n1. Ürün (Hero-XPulse 200 4V) sepete eklendi.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.add_item(item_1)
print("\n1. Ürün (Hero-XPulse 200 4V) sepete eklendi.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.update_item_amount(item_1, UpdateAmountAction.INCREASE)
print("\n1. Ürün (Hero-XPulse 200 4V) adedi 1 artırıldı.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.update_item_amount(item_1, UpdateAmountAction.DECREASE)
shopping_cart.update_item_amount(item_1, UpdateAmountAction.DECREASE)
shopping_cart.update_item_amount(item_1, UpdateAmountAction.DECREASE)
shopping_cart.update_item_amount(item_1, UpdateAmountAction.DECREASE)
print("\n1. Ürün (Hero-XPulse 200 4V) adedi 4 azaltıldıdı.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

shopping_cart.add_item(item_3)
print("\n3. Ürün (RKS-Racing R 250) sepete eklendi.\n")
print("Spetteki Ürünlerin Bilgileri:", shopping_cart, "\n")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : {shopping_cart.total_price:.2f}")
print(f"Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : {shopping_cart.discount_total_price:.2f}")

### output ###
# EXAMPLE: SHOPPING CART
# ----------
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 1 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
#
# - TVS-Raider 125
# - 149400.00 TL
# - %10 indirim
# - 1 adet
# - https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr
#
# - RKS-Racing R 250
# - 205000.00 TL
# - %15 indirim
# - 1 adet
# - https://www.rksmotor.com.tr/model/r250.html
#
# - QJMotor-SRK 250 RC
# - 180000.00 TL
# - %20 indirim
# - 1 adet
# - https://tr.qjmotor.com/products_details/69.html 
# 
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 718974.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 637284.00
# 
# 4. Ürün (QJMotor-SRK 250 RC) sepetten Çıkarıldı.
#
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 1 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
# 
# - TVS-Raider 125
# - 149400.00 TL
# - %10 indirim
# - 1 adet
# - https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr
# 
# - RKS-Racing R 250
# - 205000.00 TL
# - %15 indirim
# - 1 adet
# - https://www.rksmotor.com.tr/model/r250.html 
# 
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 538974.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 493284.00
# 
# 2. Ürün (TVS-Raider 125) sepetten Çıkarıldı.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 1 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
# 
# - RKS-Racing R 250
# - 205000.00 TL
# - %15 indirim
# - 1 adet
# - https://www.rksmotor.com.tr/model/r250.html 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 389574.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 358824.00
# 
# 3. Ürün (RKS-Racing R 250) sepetten Çıkarıldı.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 1 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/ 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 184574.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 184574.00
# 
# 1. Ürün (Hero-XPulse 200 4V) sepete eklendi.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 2 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/ 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 369148.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 369148.00

# 1. Ürün (Hero-XPulse 200 4V) sepete eklendi.

# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 3 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/ 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 553722.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 553722.00
#
# 1. Ürün (Hero-XPulse 200 4V) adedi 1 artırıldı.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 4 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/ 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 738296.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 738296.00
#
# 1. Ürün (Hero-XPulse 200 4V) adedi 4 azaltıldıdı.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 0 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/ 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 0.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 0.00
# 
# 3. Ürün (RKS-Racing R 250) sepete eklendi.
# 
# Spetteki Ürünlerin Bilgileri: 
# - Hero-XPulse 200 4V
# - 184574.00 TL
# - %0 indirim
# - 0 adet
# - https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/
# 
# - RKS-Racing R 250
# - 205000.00 TL
# - %15 indirim
# - 1 adet
# - https://www.rksmotor.com.tr/model/r250.html 
#
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimsiz)  : 205000.00
# Sepetteki Ürünlerin Toplam Fiyatı (İndirimli)   : 174250.00
