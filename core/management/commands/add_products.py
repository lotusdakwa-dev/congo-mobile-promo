from django.core.management.base import BaseCommand
from core.models import Product  # Remplace 'core' par le nom de ton app si nécessaire

class Command(BaseCommand):
    help = 'Ajoute 20 produits high-tech de démonstration au catalogue'

    def handle(self, *args, **kwargs):
        products_data = [
            # --- 5 MODÈLES iPHONE ---
            {
                "name": "iPhone 17 Pro Max", "brand": "Apple", "price_usd": 1399.00,
                "description": "Le summum de la technologie Apple avec une puce ultra-rapide et un titane aérospatial.",
                "image_url": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "iPhone 17 Pro", "brand": "Apple", "price_usd": 1199.00,
                "description": "Performances professionnelles dans un format compact et élégant.",
                "image_url": "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "iPhone 16 Plus", "brand": "Apple", "price_usd": 999.00,
                "description": "Grand écran Super Retina XDR et autonomie record pour tenir toute la journée.",
                "image_url": "https://images.unsplash.com/photo-1695048065075-291773d4fc6a?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },
            {
                "name": "iPhone 16", "brand": "Apple", "price_usd": 899.00,
                "description": "Le dernier né d'Apple doté du contrôle de l'appareil photo et de l'intelligence artificielle.",
                "image_url": "https://images.unsplash.com/photo-1695048132959-46c5963973c7?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "iPhone 15 Pro", "brand": "Apple", "price_usd": 849.00,
                "description": "Châssis en titane léger, bouton Action personnalisable et puce A17 Pro.",
                "image_url": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },

            # --- 5 MODÈLES SAMSUNG ---
            {
                "name": "Samsung Galaxy S26 Ultra", "brand": "Samsung", "price_usd": 1349.00,
                "description": "Intégration Galaxy AI poussée à son maximum avec un capteur photo de 200 MP.",
                "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "Samsung Galaxy S26+", "brand": "Samsung", "price_usd": 1099.00,
                "description": "Grand écran dynamique fluide et design épuré en armure d'aluminium.",
                "image_url": "https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },
            {
                "name": "Samsung Galaxy Z Fold 7", "brand": "Samsung", "price_usd": 1799.00,
                "description": "Le smartphone pliable de référence qui se transforme en véritable tablette tactile.",
                "image_url": "https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "Samsung Galaxy S25 Ultra", "brand": "Samsung", "price_usd": 1199.00,
                "description": "Puissance brute, stylet S-Pen intégré et finitions haut de gamme.",
                "image_url": "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },
            {
                "name": "Samsung Galaxy Z Flip 6", "brand": "Samsung", "price_usd": 999.00,
                "description": "Design compact à clapet avec écran externe intelligent et photos sublimes.",
                "image_url": "https://images.unsplash.com/photo-1537589376225-5405c60a5bd8?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },

            # --- 3 MODÈLES HP ---
            {
                "name": "HP Spectre x360 14", "brand": "HP", "price_usd": 1499.00,
                "description": "Ultrabook convertible tactile OLED haut de gamme pour les professionnels exigeants.",
                "image_url": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "HP Omen Transcend 16", "brand": "HP", "price_usd": 1799.00,
                "description": "PC portable gamer surpuissant avec écran haute fréquence et carte graphique dédiée.",
                "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },
            {
                "name": "HP Envy 17", "brand": "HP", "price_usd": 1149.00,
                "description": "Grand espace de travail, processeur Intel Core i7 et finitions en aluminium élégantes.",
                "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },

            # --- 2 MODÈLES DELL ---
            {
                "name": "Dell XPS 14 OLED", "brand": "Dell", "price_usd": 1699.00,
                "description": "Design futuriste, clavier sans bordure et écran InfinityEdge OLED époustouflant.",
                "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "Dell Latitude 7450 Ultra", "brand": "Dell", "price_usd": 1399.00,
                "description": "PC professionnel ultra-sécurisé, léger, fiable et taillé pour la productivité.",
                "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=80", "is_featured": False
            },

            # --- 2 MODÈLES MACBOOK ---
            {
                "name": "MacBook Pro 16 M3 Max", "brand": "Apple", "price_usd": 2499.00,
                "description": "La station de travail ultime pour développeurs, monteurs vidéo et créateurs de contenu.",
                "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80", "is_featured": True
            },
            {
                "name": "MacBook Air 15 M3", "brand": "Apple", "price_usd": 1499.00,
                "description": "Finesse extraordinaire, silence absolu (sans ventilateur) et autonomie de 18 heures.",
                "image_url": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?auto=format&fit=crop&w=800&q=80", "is_featured": True
            }
        ]

        count = 0
        for item in products_data:
            Product.objects.create(
                name=item["name"],
                brand=item["brand"],
                price_usd=item["price_usd"],
                description=item["description"],
                image_url=item["image_url"],
                is_featured=item["is_featured"]
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Succès ! {count} produits haut de gamme ont été ajoutés à la base de données."))