#!/usr/bin/env python3
"""olustur/index.html dosyasını üretir: tools/olustur.src.html içindeki __SABLON__ yerine
kökteki index.html (şablon) gömülür. Şablon değişince bunu yeniden çalıştır.

    python3 tools/build-olustur.py
    python3 tools/build-olustur.py --check
"""
import argparse
import json
import pathlib
import sys

kok = pathlib.Path(__file__).resolve().parent.parent
sablon = (kok / "index.html").read_text(encoding="utf-8")
kaynak = (kok / "tools" / "olustur.src.html").read_text(encoding="utf-8")

# "<" karakterini kaçır: gömülü metindeki <script>, </script> ve <!-- dizileri sayfayı bozmasın
gomulu = json.dumps(sablon, ensure_ascii=False).replace("<", "\\u003c")
isaret = '/*__SABLON__*/""'
assert kaynak.count(isaret) == 1, "olustur.src.html içinde yer tutucu bulunamadı"

cikti = kok / "olustur" / "index.html"
uretilen = kaynak.replace(isaret, gomulu)


def main():
    parser = argparse.ArgumentParser(
        description="olustur/index.html dosyasını kökteki index.html şablonundan üretir."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="dosyayı yazmadan üretilmesi gereken içerikle karşılaştır; "
        "eksik veya eskiyse sıfır dışı kodla çık.",
    )
    args = parser.parse_args()

    if args.check:
        if not cikti.exists():
            print(
                f"{cikti.relative_to(kok)} yok; python3 tools/build-olustur.py çalıştırılmalı.",
                file=sys.stderr,
            )
            return 1
        if cikti.read_text(encoding="utf-8") != uretilen:
            print(
                f"{cikti.relative_to(kok)} güncel değil; python3 tools/build-olustur.py çalıştırılmalı.",
                file=sys.stderr,
            )
            return 1
        print(f"{cikti.relative_to(kok)} güncel.")
        return 0

    cikti.parent.mkdir(exist_ok=True)
    cikti.write_text(uretilen, encoding="utf-8")
    print(f"{cikti.relative_to(kok)} yazıldı ({cikti.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
