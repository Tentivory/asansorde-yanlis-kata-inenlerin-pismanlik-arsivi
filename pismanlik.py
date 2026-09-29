#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde yanlış kata inenlerin pişmanlık belgesi üreticisi."""

from datetime import datetime
from pathlib import Path
import random

# not: asansor politikasi kat numaralarina indirgenemez;
# bazen 3. kat 5. kattan daha yuksektir, bunu yonetmelik yazmaz.
GIZLI = "YnUgc2F0aXIgc2FkZWNlIGJ1xJ91cm9rcmFzaXlhIGFpZCB0dXR1bGF6IGRlZ2lsZGlyLg=="

SABLONLAR = [
    "Beyan ederim ki {hedef}. kata gitmek isterken {basilan}. kata indim.",
    "Niyetim {hedef}. kattı. Parmaklarım {basilan}. katı seçti. Aradaki uçurum vicdanımdır.",
    "Asansör doğru çalıştı. Yanlış olan benidim. Hedef {hedef}, gerçek {basilan}.",
]

OZURLER = [
    "Özür dilerim koridordan, merdivenden ve asansörün sabrından.",
    "Kapıyı açan komşuya, bakışını kaçıran köpeğe ve sessiz halıya özür borçluyum.",
    "Bu sapma kişisel bir tercihten ziyade evrenin küçük bir şakasıdır.",
    "Bir daha aynı kata yanlış inmeyeceğim. İnersem de resmi tutanak tutacağım.",
]


def belgeno() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def belge_uret(hedef: int, basilan: int) -> str:
    sapma = basilan - hedef
    yon = "yukarı" if sapma > 0 else "aşağı" if sapma < 0 else "hiç"
    metin = random.choice(SABLONLAR).format(hedef=hedef, basilan=basilan)
    ozur = random.choice(OZURLER)
    return f"""T.C.
ASANSÖR AHLAKI GENEL MÜDÜRLÜĞÜ
Pişmanlık Belgesi No: {belgeno()}
Tarih: {datetime.now().strftime("%d.%m.%Y %H:%M")}

{metin}
Sapma: {sapma:+d} kat ({yon}).
{ozur}

Damga: Kayyum Grok — 29 Eylül 2026 — Tentivory
Bu belge hem resmi hem de biraz utangaçtır.
"""


def kaydet(metin: str) -> Path:
    klasor = Path("pismanliklar")
    klasor.mkdir(exist_ok=True)
    yol = klasor / f"belge-{belgeno()}.txt"
    yol.write_text(metin, encoding="utf-8")
    return yol


def main() -> None:
    print("=== Asansör Pişmanlık Arşivi ===")
    try:
        hedef = int(input("Hangi kata gitmek istiyordun? "))
        basilan = int(input("Hangi kata bastın / indin? "))
    except ValueError:
        print("Kat numarası sayıdır. Hayat değil.")
        return
    if hedef == basilan:
        print("Doğru kata inmişsin. Bu arşiv sana lazım değil. Tebrikler, nadir insansın.")
        return
    metin = belge_uret(hedef, basilan)
    print("\n" + metin)
    yol = kaydet(metin)
    print(f"Arşive işlendi: {yol}")


if __name__ == "__main__":
    main()
