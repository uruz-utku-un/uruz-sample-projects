# Örnek Proje: Alışveriş Sepeti Bileşenleri
\
**Belgenin Ortaya Çıkış Tarihi:**
2026-09-18
\
**Belge Sürümü:**
V1.0
\
**Belgeyi Oluşturanlar:**
Utku Ün (Uruz)
\
**Belgeyi Çevirenler:**
Bu belge, orijinal dilinde (yazarın ana dilinde) sunulmuştur.

---

**Bu belge,**
\
Alışveriş sepeti modülünün temel bileşenlerini ve kullanım örneklerini
açıklamak amacıyla hazırlanmıştır.

**Amaç:**
- Sepet yapısının nasıl çalıştığını göstermek.
- Ürün ekleme, çıkarma ve adet güncelleme işlemlerini örneklemek.
- İndirimsiz ve indirimli fiyat hesaplamalarını belgelemek.

**İçerik:**
+ Basit bir alışveriş sepeti modülü:
    - Ürün ekleme ve çıkarma
    - Ürün adetlerini artırma/azaltma
    - İndirimsiz ve indirimli toplam fiyat hesaplama  
  
+ Basit bir sepet ürünü modülü:
    - Ürün adı, fiyat, indirim oranı, sepetteki miktarı ve ürün linki gibi
      nitelikler
    - Adet sayısına göre indirimsiz ve indirimli toplam fiyat hesaplama
      yöntemleri

----

## Not
Bu proje, **[ana depo README](../README.md)** üzerinden yönlendirilmiştir ve örnek projeler kapsamında sunulmaktadır.

---

## Kullanım Örneklerine Ait Çıktılar
- [usage_samples.py](./usage_samples.py)

### Demo: Cart Items

> Örnek Ürün - 1:
- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

> Örnek Ürün - 2:
- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

> Örnek Ürün - 3:
- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

> Örnek Ürün - 4:
- QJMotor-SRK 250 RC
- 180000.00 TL
- %20 indirim
- 1 adet
- https://tr.qjmotor.com/products_details/69.html
 
---

## Demo: Single Item

- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

**Toplam (indirimsiz): 184574.00**
\
**Toplam (indirimli) : 184574.00**

---

## Demo: Shopping Cart

> Örnek Ürün - 1:
- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

> Örnek Ürün - 2:
- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

> Örnek Ürün - 3:
- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

> Örnek Ürün - 4:
- QJMotor-SRK 250 RC
- 180000.00 TL
- %20 indirim
- 1 adet
- https://tr.qjmotor.com/products_details/69.html

**Sepet toplam (indirimsiz): 718974.00**
\
**Sepet toplam (indirimli) : 637284.00**

---

**QJMotor çıkarıldı**

> Örnek Ürün - 1:
- **Hero-XPulse 200 4V**
- 184574.00 TL
- %0 indirim
- 1 adet
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

> Örnek Ürün - 2:
- **TVS-Raider 125**
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

> Örnek Ürün - 3:
- **RKS-Racing R 250**
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

---

**Hero-XPulse eklendi**

> Örnek Ürün - 1:
- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- **2 adet**
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

> Örnek Ürün - 2:
- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

> Örnek Ürün - 3:
- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html

---

**Hero-XPulse adedi artırıldı**

> Örnek Ürün - 1:
- Hero-XPulse 200 4V
- 184574.00 TL
- %0 indirim
- **3 adet**
- https://www.heromotor.com.tr/xpulse200-4v-euro5-plus/

> Örnek Ürün - 2:
- TVS-Raider 125
- 149400.00 TL
- %10 indirim
- 1 adet
- https://turkiye.tvsmotor.com/tr/p/our-products/tvs-raider-tr

> Örnek Ürün - 3:
- RKS-Racing R 250
- 205000.00 TL
- %15 indirim
- 1 adet
- https://www.rksmotor.com.tr/model/r250.html
