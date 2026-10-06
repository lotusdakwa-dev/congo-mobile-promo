from django.core.management.base import BaseCommand
from core.models import Product
import re
import unicodedata


PHONES_TEXT = r"""
--- A SERIES ---
- A05 (6/128GB) - Prix : $52 - Photo : [Insérer le lien ici]
- A14 2SIM (6/128GB) - Prix : $52 - Photo : [Insérer le lien ici]
- A05S (8/128GB) - Prix : $59 - Photo : [Insérer le lien ici]
- A06 (6/128GB) - Prix : $59 - Photo : [Insérer le lien ici]
- A07 (4/128GB) - Prix : $63 - Photo : [Insérer le lien ici]
- A13 5G (6/128GB) - Prix : $63 - Photo : [Insérer le lien ici]
- A15 2SIM (6/128GB) - Prix : $73 - Photo : [Insérer le lien ici]
- A15 KOREAN (6/128GB) - Prix : $97 - Photo : [Insérer le lien ici]
- A16 (6/128GB) - Prix : $74 - Photo : [Insérer le lien ici]
- A16 KOREAN (6/128GB) - Prix : $108 - Photo : [Insérer le lien ici]
- A17 (128GB) - Prix : $82 - Photo : [Insérer le lien ici]
- A31 (8/128GB) - Prix : $64 - Photo : [Insérer le lien ici]
- A32 4G (8/128GB) - Prix : $75 - Photo : [Insérer le lien ici]
- A32 5G JAPAN (4/64GB) - Prix : $73 - Photo : [Insérer le lien ici]
- A32 5G KOREAN (4/128GB) - Prix : $89 - Photo : [Insérer le lien ici]
- A33 5G KOREAN (6/128GB) - Prix : $111 - Photo : [Insérer le lien ici]
- A34 5G KOREAN (6/128GB) - Prix : $115 - Photo : [Insérer le lien ici]
- A22 5G KOREAN (6/128GB) - Prix : $75 - Photo : [Insérer le lien ici]
- A23 (6/128GB) - Prix : $64 - Photo : [Insérer le lien ici]
- A23 5G KOREAN (6/128GB) - Prix : $86 - Photo : [Insérer le lien ici]
- A24 KOREAN (4/128GB) - Prix : $86 - Photo : [Insérer le lien ici]
- A25 (8/256GB) - Prix : $78 - Photo : [Insérer le lien ici]
- A25 KOREAN (6/128GB) - Prix : $112 - Photo : [Insérer le lien ici]
- A26 (8/256GB) - Prix : $85 - Photo : [Insérer le lien ici]
- A50 (6/128GB) - Prix : $55 - Photo : [Insérer le lien ici]
- A51 4G 2SIM (6/128GB) - Prix : $73 - Photo : [Insérer le lien ici]
- A51 5G (8/128GB) - Prix : $75 - Photo : [Insérer le lien ici]
- A52 5G 2SIM (6/128GB) - Prix : $96 - Photo : [Insérer le lien ici]
- A53 5G JAPAN (6/128GB) - Prix : $115 - Photo : [Insérer le lien ici]
- A54 JAPAN (6/128GB) - Prix : $133 - Photo : [Insérer le lien ici]
- A71 4G 2SIM (6/128GB) - Prix : $0 - Photo : [Insérer le lien ici]
- A71 5G (8/128GB) - Prix : $89 - Photo : [Insérer le lien ici]
- A90 (6/128GB) - Prix : $81 - Photo : [Insérer le lien ici]

--- APPLE SERIES ---
- XR (64GB) - Prix : $127 - Photo : [Insérer le lien ici]
- XR (128GB) - Prix : $141 - Photo : [Insérer le lien ici]
- X (64GB) - Prix : $115 - Photo : [Insérer le lien ici]
- X (256GB) - Prix : $123 - Photo : [Insérer le lien ici]
- XS MAX (256GB) - Prix : $153 - Photo : [Insérer le lien ici]
- 11 (64GB) - Prix : $164 - Photo : [Insérer le lien ici]
- 11 (128GB) - Prix : $178 - Photo : [Insérer le lien ici]
- 11 PRO (64GB) - Prix : $200 - Photo : [Insérer le lien ici]
- 11 PRO (256GB) - Prix : $215 - Photo : [Insérer le lien ici]
- 11 PRO MAX (64GB) - Prix : $216 - Photo : [Insérer le lien ici]
- 11 PRO MAX (256GB) - Prix : $225 - Photo : [Insérer le lien ici]
- 12 (64GB) - Prix : $178 - Photo : [Insérer le lien ici]
- 12 (128GB) - Prix : $189 - Photo : [Insérer le lien ici]
- 12 PRO (128GB) - Prix : $247 - Photo : [Insérer le lien ici]
- 12 PRO (256GB) - Prix : $266 - Photo : [Insérer le lien ici]
- 12 PRO MAX (128GB) - Prix : $263 - Photo : [Insérer le lien ici]
- 12 PRO MAX (256GB) - Prix : $290 - Photo : [Insérer le lien ici]
- 13 (128GB) - Prix : $255 - Photo : [Insérer le lien ici]
- 13 PRO (128GB) - Prix : $41 - Photo : [Insérer le lien ici]
- 13 PRO (256GB) - Prix : $362 - Photo : [Insérer le lien ici]
- 13 PRO MAX (128GB) - Prix : $377 - Photo : [Insérer le lien ici]
- 13 PRO MAX (256GB) - Prix : $407 - Photo : [Insérer le lien ici]
- 14 (128GB) - Prix : $301 - Photo : [Insérer le lien ici]
- 14 (256GB) - Prix : $332 - Photo : [Insérer le lien ici]
- 14 PLUS (128GB) - Prix : $288 - Photo : [Insérer le lien ici]
- 14 PLUS (256GB) - Prix : $315 - Photo : [Insérer le lien ici]
- 14 PRO (128GB) - Prix : $392 - Photo : [Insérer le lien ici]
- 14 PRO (256GB) - Prix : $419 - Photo : [Insérer le lien ici]
- 14 PRO MAX (128GB) - Prix : $433 - Photo : [Insérer le lien ici]
- 14 PRO MAX (256GB) - Prix : $463 - Photo : [Insérer le lien ici]
- 15 (128GB) - Prix : $378 - Photo : [Insérer le lien ici]
- 15 (256GB) - Prix : $405 - Photo : [Insérer le lien ici]
- 15 PLUS (128GB) - Prix : $422 - Photo : [Insérer le lien ici]
- 15 PLUS (256GB) - Prix : $447 - Photo : [Insérer le lien ici]
- 15 PRO (128GB) - Prix : $466 - Photo : [Insérer le lien ici]
- 15 PRO (256GB) - Prix : $479 - Photo : [Insérer le lien ici]
- 15 PRO MAX (256GB) - Prix : $548 - Photo : [Insérer le lien ici]
- 16 (256GB) - Prix : $581 - Photo : [Insérer le lien ici]
- 16 PLUS (128GB) - Prix : $584 - Photo : [Insérer le lien ici]
- 16 PLUS (256GB) - Prix : $611 - Photo : [Insérer le lien ici]
- 16 PRO MAX (256GB) - Prix : $740 - Photo : [Insérer le lien ici]
- 17 PRO MAX (256GB) - Prix : $1156 - Photo : [Insérer le lien ici]

--- F SERIES ---
- F16 (128GB) - Prix : $79 - Photo : [Insérer le lien ici]
- F15 (128GB) - Prix : $78 - Photo : [Insérer le lien ici]
- F17 (6/128GB) - Prix : $82 - Photo : [Insérer le lien ici]

--- FLIP SERIES ---
- Z FLIP 3 USA (8/128GB) - Prix : $152 - Photo : [Insérer le lien ici]
- Z FLIP 3 KOREAN (8/256GB) - Prix : $162 - Photo : [Insérer le lien ici]
- Z FLIP 4 JAPAN (8/128GB) - Prix : $171 - Photo : [Insérer le lien ici]
- Z FLIP 4 USA (8/256GB) - Prix : $178 - Photo : [Insérer le lien ici]
- ZFLIP 5 KOREAN (8/512GB) - Prix : $236 - Photo : [Insérer le lien ici]
- ZFLIP 6 KOREAN (12/256GB) - Prix : $348 - Photo : [Insérer le lien ici]

--- FOLD SERIES ---
- ZFOLD 2 (12/256GB) - Prix : $325 - Photo : [Insérer le lien ici]
- ZFOLD 3 (12/256GB) - Prix : $352 - Photo : [Insérer le lien ici]
- ZFOLD 3 (12/512GB) - Prix : $359 - Photo : [Insérer le lien ici]
- ZFOLD 4 (12/256GB) - Prix : $396 - Photo : [Insérer le lien ici]
- Z FOLD 5 (12/512GB) - Prix : $458 - Photo : [Insérer le lien ici]
- ZFOLD 6 (12/256GB) - Prix : $671 - Photo : [Insérer le lien ici]

--- M SERIES ---
- M13 5G (6/128GB) - Prix : $62 - Photo : [Insérer le lien ici]
- M14 5G (6/128GB) - Prix : $58 - Photo : [Insérer le lien ici]
- M15 5G (6/128GB) - Prix : $81 - Photo : [Insérer le lien ici]
- M16 (6/128GB) - Prix : $85 - Photo : [Insérer le lien ici]
- M16 KOREAN (6/128GB) - Prix : $112 - Photo : [Insérer le lien ici]
- M17 (128GB) - Prix : $86 - Photo : [Insérer le lien ici]
- M05 (128GB) - Prix : $52 - Photo : [Insérer le lien ici]
- M06 (128GB) - Prix : $59 - Photo : [Insérer le lien ici]
- M23 5G KOREAN (4/128GB) - Prix : $82 - Photo : [Insérer le lien ici]
- M33 5G KOREAN (6/128GB) - Prix : $85 - Photo : [Insérer le lien ici]
- M44 5G KOREAN (6/128GB) - Prix : $85 - Photo : [Insérer le lien ici]
- M53 KOREAN (8/128GB) - Prix : $97 - Photo : [Insérer le lien ici]

--- NOTE SERIES ---
- NOTE 10 (8/256GB) - Prix : $126 - Photo : [Insérer le lien ici]
- NOTE 10 PLUS (12/256GB) - Prix : $173 - Photo : [Insérer le lien ici]
- NOTE 20 (8/128GB) - Prix : $125 - Photo : [Insérer le lien ici]
- NOTE 20 (8/256GB) - Prix : $127 - Photo : [Insérer le lien ici]
- NOTE 20 ULTRA (12/128GB) - Prix : $233 - Photo : [Insérer le lien ici]
- NOTE 20 ULTRA 2SIM (12/256GB) - Prix : $244 - Photo : [Insérer le lien ici]

--- S SERIES ---
- S8 (4/64GB) - Prix : $75 - Photo : [Insérer le lien ici]
- S9 (4/64GB) - Prix : $78 - Photo : [Insérer le lien ici]
- S8 PLUS (4/64GB) - Prix : $88 - Photo : [Insérer le lien ici]
- S9 PLUS (4/64GB) - Prix : $89 - Photo : [Insérer le lien ici]
- S10E (6/128GB) - Prix : $103 - Photo : [Insérer le lien ici]
- S10 (8/128GB) - Prix : $123 - Photo : [Insérer le lien ici]
- S10 PLUS (8/128GB) - Prix : $144 - Photo : [Insérer le lien ici]
- S10 5G (8/256GB) - Prix : $147 - Photo : [Insérer le lien ici]
- S20 (8/128GB) - Prix : $118 - Photo : [Insérer le lien ici]
- S20 FE (6/128GB) - Prix : $105 - Photo : [Insérer le lien ici]
- S20 PLUS (12/128GB) - Prix : $121 - Photo : [Insérer le lien ici]
- S20 PLUS (12/256GB) - Prix : $125 - Photo : [Insérer le lien ici]
- S20 PLUS 2SIM (12/256GB) - Prix : $127 - Photo : [Insérer le lien ici]
- S20 ULTRA (12/128GB) - Prix : $151 - Photo : [Insérer le lien ici]
- S20 ULTRA (12/256GB) - Prix : $160 - Photo : [Insérer le lien ici]
- S21 (8/128GB) - Prix : $133 - Photo : [Insérer le lien ici]
- S21 (8/256GB) - Prix : $145 - Photo : [Insérer le lien ici]
- S21FE (6/128GB) - Prix : $116 - Photo : [Insérer le lien ici]
- S21 PLUS (12/128GB) - Prix : $140 - Photo : [Insérer le lien ici]
- S21 PLUS (12/256GB) - Prix : $145 - Photo : [Insérer le lien ici]
- S21 ULTRA (12/128GB) - Prix : $189 - Photo : [Insérer le lien ici]
- S21 ULTRA (12/256GB) - Prix : $238 - Photo : [Insérer le lien ici]
- S21 ULTRA 2SIM (12/256GB) - Prix : $244 - Photo : [Insérer le lien ici]
- S21 ULTRA (12/512GB) - Prix : $245 - Photo : [Insérer le lien ici]
- S22 (8/256GB) - Prix : $174 - Photo : [Insérer le lien ici]
- S22 PLUS (8/128GB) - Prix : $197 - Photo : [Insérer le lien ici]
- S22 ULTRA (8/128GB) - Prix : $249 - Photo : [Insérer le lien ici]
- S22 ULTRA (12/256GB) - Prix : $301 - Photo : [Insérer le lien ici]
- S22 ULTRA KOREA (12/256GB) - Prix : $342 - Photo : [Insérer le lien ici]
- S22 ULTRA (12/512GB) - Prix : $308 - Photo : [Insérer le lien ici]
- S23 (8/128GB) - Prix : $225 - Photo : [Insérer le lien ici]
- S23 JAPPAN (8/256GB) - Prix : $233 - Photo : [Insérer le lien ici]
- S23FE (8/128GB) - Prix : $208 - Photo : [Insérer le lien ici]
- S23FE (8/256GB) - Prix : $225 - Photo : [Insérer le lien ici]
- S23PLUS (8/256GB) - Prix : $315 - Photo : [Insérer le lien ici]
- S23PLUS (8/512GB) - Prix : $329 - Photo : [Insérer le lien ici]
- S23 ULTRA USA (8/256GB) - Prix : $337 - Photo : [Insérer le lien ici]
- S23 ULTRA KOREA (12/256GB) - Prix : $452 - Photo : [Insérer le lien ici]
- S23 ULTRA USA (8/512GB) - Prix : $384 - Photo : [Insérer le lien ici]
- S24 (8/256GB) - Prix : $351 - Photo : [Insérer le lien ici]
- S24FE 2SIM (8/128GB) - Prix : $282 - Photo : [Insérer le lien ici]
- S24 PLUS (8/256GB) - Prix : $359 - Photo : [Insérer le lien ici]
- S24 ULTRA USA (12/256GB) - Prix : $556 - Photo : [Insérer le lien ici]
- S24 ULTRA KOREA (12/256GB) - Prix : $575 - Photo : [Insérer le lien ici]
- S24 ULTRA KOREAN (12/512GB) - Prix : $608 - Photo : [Insérer le lien ici]
- S25 ULTRA (12/256GB) - Prix : $748 - Photo : [Insérer le lien ici]
- S25 ULTRA (12/512GB) - Prix : $773 - Photo : [Insérer le lien ici]
- S26 ULTRA (12/256GB) - Prix : $1022 - Photo : [Insérer le lien ici]
"""


def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r"[^a-zA-Z0-9\\s-]", '', text)
    text = text.strip().lower()
    text = re.sub(r"[\\s]+", '-', text)
    return text


class Command(BaseCommand):
    help = 'Importe la liste fournie de téléphones et crée des produits (image_url -> /static/images/phones/<slug>.jpg)'

    def handle(self, *args, **options):
        lines = PHONES_TEXT.splitlines()
        current_series = 'Unknown'
        created = 0

        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            if line.startswith('---') and line.endswith('---'):
                # extract series name
                current_series = line.strip('- ').strip()
                continue
            if line.startswith('- '):
                # parse model and price
                try:
                    # left and right split
                    parts = line[2:].split(' - Prix : ')
                    if len(parts) < 2:
                        continue
                    name_part = parts[0].strip()
                    price_part = parts[1]
                    m = re.search(r"\\$([0-9]+)", price_part)
                    price = float(m.group(1)) if m else 0.0

                    name = name_part
                    brand = current_series.title()
                    category = 'apple' if 'APPLE' in current_series.upper() else 'accessoire'
                    slug = slugify(name)
                    image_url = f"/static/images/phones/{slug}.jpg"

                    Product.objects.create(
                        name=name,
                        category=category,
                        brand=brand,
                        price_usd=price,
                        description=f"Importé depuis liste — série: {current_series}",
                        image_url=image_url,
                        is_featured=False,
                    )
                    created += 1
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Skipped line due to error: {line} -> {e}"))

        self.stdout.write(self.style.SUCCESS(f"Import terminé : {created} produits ajoutés."))
