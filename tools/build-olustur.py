#!/usr/bin/env python3
"""olustur/index.html dosyasını üretir: tools/olustur.src.html içindeki __SABLON__ yerine
kökteki index.html (şablon) gömülür. Şablon değişince bunu yeniden çalıştır.

    python3 tools/build-olustur.py
"""
import json
import pathlib

kok = pathlib.Path(__file__).resolve().parent.parent
sablon = (kok / "index.html").read_text(encoding="utf-8")
kaynak = (kok / "tools" / "olustur.src.html").read_text(encoding="utf-8")

# "<" karakterini kaçır: gömülü metindeki <script>, </script> ve <!-- dizileri sayfayı bozmasın
gomulu = json.dumps(sablon, ensure_ascii=False).replace("<", "\\u003c")
isaret = '/*__SABLON__*/""'
assert kaynak.count(isaret) == 1, "olustur.src.html içinde yer tutucu bulunamadı"

cikti = kok / "olustur" / "index.html"
cikti.parent.mkdir(exist_ok=True)
cikti.write_text(kaynak.replace(isaret, gomulu), encoding="utf-8")
print(f"{cikti.relative_to(kok)} yazıldı ({cikti.stat().st_size // 1024} KB)")
