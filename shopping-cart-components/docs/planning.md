# Uruz Alışveriş Sepeti Bileşeni - Gereksinimlerin Tanımı Belgesi


Bir alışveriş sepeti üç temel parçadan oluşur:
- **Ürünler** (sepet listesindeki öğeler)
- **Sepet listesi**
- **Kuponlar** (isteğe bağlı - MVP'de (Minimum Viable Product) yer almayacak.)

---

## Ürün Yapısı (`CartItem`)
Bir e-ticaret uygulamasında sepete eklenen ürünü temsil eder.
Sepete eklenecek ürünün: ürün adı, fiyatı, bağlantısı, miktarı ve
indirim oranı bilgilerini tutar.

**Sepetteki her ürün için gerekli nitelikler:**
- Ürünün adı veya ID
- Ürünün birim fiyatı (indirimsiz)
- Sepete eklenen adet sayısı (varsayılan: 1)
- Ürünün sayfasına ait link bilgisi (varsayılan: "")
- ürüne ait indirim bilgisi (varsayılan: %0)

**Ürün üzerinde yapılabilecek işlemler:**
- Ürün bilgisini okuma.
    - `__str__()`
- Sepete eklenen miktarı dikkate alarak indirimsiz toplam fiyatı bulma.
    - `@property, total_price()`
- Sepete eklenen miktarı dikkate alarak indirimli toplam fiyatı bulma.
    - `@property, discount_price()`

---

## Sepet Özellikleri (`ShoppingCart`)

**Sepetteki her ürün için gerekli nitelikler:**
- Sepete eklenen ürünlerin tutulduğu bir liste (varsayılan: [ ]) 

**Sepet üzerinde yapılabilecek işlemler:**
- Sepetteki ürünlerin bilgilerini okuma.
    - `__str__()`
- Sepetteki ürünleri listeleme.
    - `...`
- Ürün ekleme, eğer ürün zaten sepette mevcutsa ürüne ait miktar niteliğini günceller.
    - `add_item()`
- Ürün çıkarma
    - `remove_item()`
- Sepeti temizleme
    - `clear_shopping_list()`
- Ürün adedini artırma/azaltma
    - `update_item_amount()`
- Sepetteki ürünlerin indirimsiz toplam fiyatını hesaplama
    - `total_price()`
- Sepetteki ürünlerin indirimli toplam fiyatını hesaplama
    - `discount_total_price()`

---

## Kuponlar (`Coupon`, İsteğe Bağlı)
- Kupon kodu ekleme
- İndirim oranı veya tutarı uygulama
- Kupon geçerlilik kontrolü

---

## Deneme Sürümü için Mini Uygulama Arayüzü (Temsili)
```TXT
-------------------------------------------------------------------------------
Uruz - Shopping Cart Test Panel                                         [-][X]
-------------------------------------------------------------------------------

Test Panel - Products
-------------------------------------------------------------------------------
ürün-1 | 100.05 | [ Add ][ Remove ]
ürün-2 | 900.38 | [ Add ][ Remove ]
ürün-3 | 400.46 | [ Add ][ Remove ]
-------------------------------------------------------------------------------

Test Panel - Shopping Cart
-------------------------------------------------------------------------------
[+][-] |    1 |    ürün-1 |  10000.40 | [ Delete ]
[+][-] |    1 |    ürün-3 |   2000.36 | [ Delete ]
-------------------------------------------------------------------------------
Total Amount to be Paid   |  12000.76 | [ Payment ]
-------------------------------------------------------------------------------         
```
