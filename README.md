# Doğum Günü Sürprizi

Sevdiğin birine hazırlayabileceğin, animasyonlu ve interaktif bir doğum günü sayfası. Tek bir HTML dosyası, kurulum gerektirmez. Telefonda da bilgisayarda da çalışır.

## Neler var

Sayfa sekiz sahneden oluşuyor:

1. **Giriş kapısı.** "Doğum günün hangi gün?" sorusu. Yanlış cevapta ipuçları doğum tarihinden kendiliğinden oluşur.
2. **Hediye kutusu.** Üç dokunuşta açılır. Altından canlı bir sayaç çıkar: dünyada geçirilen saniyeler, Dünya'nın güneş etrafındaki tur sayısı, uzayda alınan yol, görülen dolunaylar ve doğulan günün hangi gün olduğu.
3. **Pasta ve dilek feneri.** Yaşı kadar mum üflenir, sonra yazılan dilek bir fenerle gökyüzüne yükselir. Dilek hiçbir yere gönderilmez.
4. **Deniz kabukları.** Her kabuğun altında bir inci ve bir iltifat var.
5. **Kazı kazan.** Altından bir hediye kuponu çıkar.
6. **Şişedeki mesaj.** Dalgaların arasından gelen şişeden harf harf yazılan bir mektup çıkar.
7. **"Ne zaman ihtiyacın olursa aç" zarfları.** Dönen kartlarda destek veren kısa mesajlar.
8. **Final.** Havai fişekler. "Gökyüzüne bak" denince yıldızlar birleşip adı yazar, ardından gün doğumu ve açan bir çiçek buketi gelir.

Gizli bir sürpriz de var: Sol üstteki aya beş kez dokununca doğduğu gecenin ay evresi gösterilir.

Müzik ve ses efektleri tarayıcıda üretilir (Web Audio), dışarıdan dosya yüklenmez.

## Kişiselleştirme

Her şey `index.html` içindeki `CONFIG` nesnesinden ayarlanır:

| Alan | Ne işe yarar |
|---|---|
| `name` | Adı. Yıldızlar bu adı yazar (Türk alfabesinin bütün harfleri desteklenir). |
| `birth` | Doğum tarihi. Giriş sorusu, ipuçları, sayaç ve ay evresi buna göre hesaplanır. |
| `age`, `candles` | Boş bırakılırsa bu yılki yaş ve o kadar mum kullanılır. |
| `star` | Finalde gösterilen yıldız. Yaşına yakın uzaklıkta (ışık yılı) bir yıldız seçersen "doğduğun gün yola çıkan ışık şimdi ulaşıyor" mesajı anlamlı olur. |
| `reasons` | Deniz kabuklarından çıkan cümleler. |
| `coupon` | Kazı kazandan çıkan kupon. |
| `letter` | Mektup. `null` bırakılırsa örnek mektup kullanılır. |
| `openWhen` | "Ne zaman ihtiyacın olursa aç" zarfları. |
| `signature` | Mektubun imzası. |

En güzel sonuç, mektuba ve kabuklara kendi cümlelerini yazınca çıkar.

## Yayınlama

Dosyayı doğrudan tarayıcıda açabilirsin. Paylaşmak için GitHub Pages kullanabilirsin:

1. Bu depoyu kendi hesabına fork'la.
2. **Settings → Pages** bölümünde kaynak olarak `main` dalını seç.
3. Birkaç dakika sonra sayfan `https://kullanici-adin.github.io/dogum-gunu-surprizi/` adresinde yayında olur.

> **Gizlilik:** Açık bir depoya gerçek isim, doğum tarihi ya da kişisel bir mektup koyarsan bunları herkes görebilir. Kişisel sürümünü gizli (private) bir depoda tut ya da başka bir yerde yayınla.

## Kalp şeklinde QR kod

`tools/kalp-qr.py` sitenin adresini kalp şeklinde bir QR koda dönüştürür. QR kod 45 derece döndürülür, iki üst kenarına yuvarlak "kulaklar" eklenir. En yüksek hata düzeltme seviyesi kullanıldığı için okunabilir kalır.

```bash
pip install qrcode pillow
python3 tools/kalp-qr.py https://site-adresin -o kalp-qr.png -t "Ada için"
```

Basarken en az 5 cm genişlik ve açık renkli bir kağıt kullan.

## Lisans

[MIT](LICENSE)
