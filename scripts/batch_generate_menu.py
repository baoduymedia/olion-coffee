#!/usr/bin/env python3
"""
Olion Coffee - Automated Menu Studio Photography Generator
This script automates the generation of 8K studio product photos for Olion Coffee's menu,
ensuring 100% fidelity to the official Menu Board (media_1789944754608.png).

Usage:
  python3 scripts/batch_generate_menu.py [--api-key YOUR_GEMINI_API_KEY]
"""

import os
import sys
import time
import argparse

MENU_ITEMS_PROMPTS = {
    # COFFEE
    "espresso": {
        "name": "Espresso",
        "category": "Coffee",
        "output": "assets/menu/espresso.webp",
        "prompt": (
            "Professional commercial beverage photography of a single shot Espresso. "
            "Served in a small clear glass espresso cup, showcasing a thick, velvety golden-brown crema "
            "on top of rich dark espresso. Set on a luxury dark walnut cafe table with a few roasted coffee beans "
            "scattered nearby. Moody ambient cafe lighting, warm golden rim light, shallow depth of field, "
            "8k resolution, photorealistic, elegant Olion Coffee aesthetic."
        )
    },
    "espresso_sua": {
        "name": "Espresso Sữa",
        "category": "Coffee",
        "output": "assets/menu/espresso_sua.webp",
        "prompt": (
            "Professional commercial beverage photography of Vietnamese Espresso Sữa (iced espresso with condensed milk). "
            "In a clear fluted glass cup, showing distinct layers: a thick layer of creamy white condensed milk at the bottom, "
            "rich dark espresso on top with crystal clear ice cubes and delicate condensation on the glass. "
            "Set on a luxury dark wooden cafe table with subtle warm moody cafe lighting, soft bokeh background, "
            "8k resolution, photorealistic, elegant food photography matching Olion Coffee menu."
        )
    },
    "latte_hanh_nhan": {
        "name": "Latte Hạnh Nhân",
        "category": "Coffee",
        "output": "assets/menu/latte_hanh_nhan.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Almond Latte (Latte Hạnh Nhân). "
            "In a tall elegant clear glass, layered with creamy almond milk, rich espresso, and crystal ice cubes, "
            "topped with a light layer of silky milk foam and drizzled with golden almond caramel sauce. "
            "Set on a luxury dark wooden table, soft cafe ambient lighting, shallow depth of field, 8k resolution."
        )
    },
    "caramel_latte": {
        "name": "Caramel Latte",
        "category": "Coffee",
        "output": "assets/menu/caramel_latte.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Caramel Latte. "
            "In a tall clear glass with beautiful espresso and milk gradients over ice, topped with dense whipped foam "
            "and an intricate cross-hatch drizzle of golden caramel syrup. "
            "Dark boutique cafe setting, warm amber lighting, shallow depth of field, 8k resolution, photorealistic."
        )
    },
    "americano": {
        "name": "Americano",
        "category": "Coffee",
        "output": "assets/menu/americano.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Americano. "
            "In a tall clear glass filled with clear ice cubes and deep dark amber-black coffee, "
            "delicate droplets of condensation on the glass. "
            "Set on a dark wooden table in a luxury coffee shop, soft warm background bokeh, 8k resolution, crisp detail."
        )
    },
    "ca_phe_bac_ha": {
        "name": "Cà Phê Bạc Hà",
        "category": "Coffee",
        "output": "assets/menu/ca_phe_bac_ha.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Mint Coffee (Cà Phê Bạc Hà). "
            "In a tall clear glass with 3 striking distinct layers: vibrant turquoise blue-green mint syrup at the bottom, "
            "fresh milk with ice cubes in the middle, and rich dark espresso on top, garnished with a fresh green mint sprig. "
            "Luxury cafe ambiance, dark green velvet background, shallow depth of field, 8k resolution, photorealistic."
        )
    },
    "ca_phe_sua_oatside": {
        "name": "Cà Phê Sữa Oatside",
        "category": "Coffee",
        "output": "assets/menu/ca_phe_sua_oatside.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Oatside Oat Milk Espresso. "
            "In a tall clear glass, showing a creamy oat milk swirl harmoniously marbled with rich dark espresso and ice cubes. "
            "Luxury dark wooden table, warm ambient lighting, elegant cafe atmosphere, 8k resolution, photorealistic."
        )
    },

    # TEA
    "tra_vai_hoa_hong": {
        "name": "Trà Vải Hoa Hồng",
        "category": "Tea",
        "output": "assets/menu/tra_vai_hoa_hong.webp",
        "prompt": (
            "Professional commercial beverage photography of Lychee Rose Iced Tea (Trà Vải Hoa Hồng). "
            "In a tall clear glass, luminous amber-rose tea over crystal ice cubes, topped with whole peeled juicy translucent lychee fruits, "
            "delicate dried pink rose petals and a fresh mint sprig. "
            "Luxury boutique cafe atmosphere, warm sunlight rim light, shallow depth of field, 8k resolution, vibrant and refreshing."
        )
    },
    "tra_chanh_day_nhiet_doi": {
        "name": "Trà Chanh Dây Nhiệt Đới",
        "category": "Tea",
        "output": "assets/menu/tra_chanh_day_nhiet_doi.webp",
        "prompt": (
            "Professional commercial beverage photography of Tropical Passion Fruit Iced Tea (Trà Chanh Dây Nhiệt Đới). "
            "In a tall clear glass, bright golden-orange iced tea with visible crunchy black passion fruit seeds floating, "
            "garnished with a fresh cut passion fruit half perched on the rim and a fresh mint leaf. "
            "Refreshing droplets on the glass, luxury cafe setting, 8k resolution, photorealistic."
        )
    },
    "tra_buoi_hong_chanh_vang": {
        "name": "Trà Bưởi Hồng Chanh Vàng",
        "category": "Tea",
        "output": "assets/menu/tra_buoi_hong_chanh_vang.webp",
        "prompt": (
            "Professional commercial beverage photography of Pink Grapefruit & Lemon Iced Tea. "
            "In a tall clear glass, vibrant ruby pink-red iced tea filled with ice, featuring a fresh pink grapefruit slice "
            "and a bright yellow lemon wheel inside the glass, mint sprig garnish. "
            "Crystal clear ice, condensation on glass, luxury dark wooden background, 8k resolution, photorealistic."
        )
    },
    "tra_xoai_chanh_day": {
        "name": "Trà Xoài Chanh Dây",
        "category": "Tea",
        "output": "assets/menu/tra_xoai_chanh_day.webp",
        "prompt": (
            "Professional commercial beverage photography of Mango Passion Fruit Iced Tea. "
            "In a tall clear glass, radiant golden-yellow iced tea with fresh diced ripe mango chunks and passion fruit pulp on top, "
            "crystal ice cubes, fresh mint sprig. "
            "Luxury cafe tabletop, soft bokeh background, 8k resolution, mouthwatering commercial drink photo."
        )
    },
    "luc_tra_nhan": {
        "name": "Lục Trà Nhãn",
        "category": "Tea",
        "output": "assets/menu/luc_tra_nhan.webp",
        "prompt": (
            "Professional commercial beverage photography of Green Tea with Longan (Lục Trà Nhãn). "
            "In a clear glass, luminous golden-green jasmine iced tea, crowned with several whole, plump, juicy peeled longan fruits "
            "and a small mint sprig on top. "
            "Warm ambient cafe lighting, dark aesthetic background, 8k resolution, photorealistic."
        )
    },
    "luc_tra_tran_chau_trang": {
        "name": "Lục Trà Trân Châu Trắng",
        "category": "Tea",
        "output": "assets/menu/luc_tra_tran_chau_trang.webp",
        "prompt": (
            "Professional commercial beverage photography of Jasmine Green Tea with White Tapioca Pearls. "
            "In a tall clear glass, golden-green iced tea with a generous layer of glistening, chewy white pearls at the bottom, "
            "crystal ice, clear condensation on the glass. "
            "Set on a luxury dark wooden table, 8k resolution, photorealistic."
        )
    },

    # MATCHA
    "matcha_caramel": {
        "name": "Matcha Caramel",
        "category": "Matcha",
        "output": "assets/menu/matcha_caramel.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Matcha Caramel. "
            "In a tall clear glass, rich vibrant green ceremonial matcha layered over fresh milk and ice, "
            "with decadent golden caramel sauce dripping inside the glass walls and drizzled across the creamy foam top. "
            "Luxury cafe ambient lighting, 8k resolution, photorealistic."
        )
    },
    "matcha_bac_ha": {
        "name": "Matcha Bạc Hà",
        "category": "Matcha",
        "output": "assets/menu/matcha_bac_ha.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Mint Matcha (Matcha Bạc Hà). "
            "In a tall clear glass, three distinct layers: vibrant turquoise blue mint syrup at the bottom, "
            "creamy white milk with ice in the center, and brilliant green whisked ceremonial matcha on top. "
            "Dark luxury cafe setting, shallow depth of field, 8k resolution, photorealistic."
        )
    },
    "matcha_kem_muoi": {
        "name": "Matcha Kem Muối",
        "category": "Matcha",
        "output": "assets/menu/matcha_kem_muoi.webp",
        "prompt": (
            "Professional commercial beverage photography of Salt Cream Matcha (Matcha Kem Muối). "
            "In a clear glass, deep rich green matcha over ice, topped with a thick, velvety, cloud-like layer of white salted milk foam "
            "with a dusting of fine matcha powder on top. "
            "Luxury dark wooden table, warm amber cafe lighting, 8k resolution, photorealistic."
        )
    },
    "matcha_que_hoa": {
        "name": "Matcha Quế Hoa",
        "category": "Matcha",
        "output": "assets/menu/matcha_que_hoa.webp",
        "prompt": (
            "Professional commercial beverage photography of Osmanthus Matcha (Matcha Quế Hoa). "
            "In a clear glass, vibrant green ceremonial matcha over milk and ice, delicately sprinkled with tiny golden osmanthus blossoms "
            "on the surface. "
            "Elegant zen cafe atmosphere, dark aesthetic, 8k resolution, photorealistic."
        )
    },
    "matcha_cold_whisk": {
        "name": "Matcha Cold Whisk",
        "category": "Matcha",
        "output": "assets/menu/matcha_cold_whisk.webp",
        "prompt": (
            "Professional commercial beverage photography of Ceremonial Matcha Cold Whisk. "
            "In a heavy clear rock glass with a single large artisanal ice cube, intensely vivid emerald green ceremonial matcha "
            "with a delicate frothy crema on top, traditional bamboo chasen whisk resting beside the glass on a dark wooden table. "
            "Moody cafe lighting, 8k resolution, photorealistic."
        )
    },
    "matcha_dua": {
        "name": "Matcha Dừa",
        "category": "Matcha",
        "output": "assets/menu/matcha_dua.webp",
        "prompt": (
            "Professional commercial beverage photography of Coconut Matcha (Matcha Dừa). "
            "In a clear glass, distinctly layered with pure white fresh coconut milk at the bottom and brilliant vibrant green matcha "
            "on top with crystal clear ice cubes. "
            "Luxury cafe setting, dark background, 8k resolution, photorealistic."
        )
    },
    "matcha_dau": {
        "name": "Matcha Dâu",
        "category": "Matcha",
        "output": "assets/menu/matcha_dau.webp",
        "prompt": (
            "Professional commercial beverage photography of Strawberry Matcha Latte (Matcha Dâu). "
            "In a tall clear glass, 3 gorgeous distinct layers: vibrant ruby-red fresh strawberry puree at the bottom, "
            "creamy white fresh milk in the middle, and vivid green ceremonial matcha on top with ice cubes. "
            "Luxury cafe tabletop, soft bokeh background, 8k resolution, photorealistic."
        )
    },
    "matcha_oatside": {
        "name": "Matcha Oatside",
        "category": "Matcha",
        "output": "assets/menu/matcha_oatside.webp",
        "prompt": (
            "Professional commercial beverage photography of Matcha with Oatside Oat Milk. "
            "In a tall clear glass, showing a creamy, rich oat milk swirl blending with vibrant ceremonial green matcha and ice. "
            "Luxury dark cafe ambiance, 8k resolution, photorealistic."
        )
    },

    # CACAO
    "cacao_latte": {
        "name": "Cacao Latte",
        "category": "Cacao",
        "output": "assets/menu/cacao_latte.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Cacao Latte. "
            "In a tall clear glass, rich velvety dark chocolate milk over ice cubes, with chocolate sauce swirl on the inside walls "
            "and a dusting of dark cocoa powder on top. "
            "Luxury dark wooden table, warm ambient lighting, 8k resolution, photorealistic."
        )
    },
    "cacao_kem_muoi": {
        "name": "Cacao Kem Muối",
        "category": "Cacao",
        "output": "assets/menu/cacao_kem_muoi.webp",
        "prompt": (
            "Professional commercial beverage photography of Salt Cream Cacao (Cacao Kem Muối). "
            "In a clear glass, rich dark chocolate cacao over ice, topped with a thick, luxurious layer of white salted cheese foam "
            "dusted with dark cocoa powder. "
            "Dark luxury cafe setting, shallow depth of field, 8k resolution, photorealistic."
        )
    },
    "cacao_bac_ha": {
        "name": "Cacao Bạc Hà",
        "category": "Cacao",
        "output": "assets/menu/cacao_bac_ha.webp",
        "prompt": (
            "Professional commercial beverage photography of Iced Mint Cacao (Cacao Bạc Hà). "
            "In a clear glass, vibrant turquoise blue mint syrup at the bottom, creamy milk and ice in the middle, "
            "and rich dark cacao on top, garnished with a fresh mint leaf. "
            "Dark aesthetic cafe background, 8k resolution, photorealistic."
        )
    },

    # JUICE
    "nuoc_ep_cam": {
        "name": "Nước Ép Cam",
        "category": "Juice",
        "output": "assets/menu/nuoc_ep_cam.webp",
        "prompt": (
            "Professional commercial beverage photography of Fresh Orange Juice (Nước Ép Cam). "
            "In a tall clear highball glass, vibrant natural golden-orange freshly squeezed juice over clear ice cubes, "
            "garnished with a fresh juicy orange wheel slice perched on the rim. "
            "Condensation on the glass, luxury cafe table, warm natural rim lighting, 8k resolution, photorealistic."
        )
    },
    "nuoc_ep_chanh_day": {
        "name": "Nước Ép Chanh Dây",
        "category": "Juice",
        "output": "assets/menu/nuoc_ep_chanh_day.webp",
        "prompt": (
            "Professional commercial beverage photography of Fresh Passion Fruit Juice (Nước Ép Chanh Dây). "
            "In a tall clear highball glass, radiant yellow-orange juice with natural black passion fruit seeds floating throughout, "
            "garnished with a fresh half passion fruit on the rim. "
            "Crystal ice, refreshing droplets on glass, dark cafe table, 8k resolution, photorealistic."
        )
    },

    # YAGOUT
    "yagout_dao_chanh_day": {
        "name": "Yagout Đào Chanh Dây",
        "category": "Yogurt",
        "output": "assets/menu/yagout_dao_chanh_day.webp",
        "prompt": (
            "Professional commercial beverage photography of Peach Passion Fruit Yogurt Smoothie. "
            "In a clear glass, creamy peach-orange blended yogurt smoothie, topped with succulent sliced peach wedges "
            "and a swirl of passion fruit pulp with seeds. "
            "Luxury dark cafe setting, soft bokeh, 8k resolution, photorealistic."
        )
    },
    "yagout_viet_quat": {
        "name": "Yagout Việt Quất",
        "category": "Yogurt",
        "output": "assets/menu/yagout_viet_quat.webp",
        "prompt": (
            "Professional commercial beverage photography of Blueberry Yogurt. "
            "In a clear glass, showing beautiful layers of creamy white yogurt and deep violet-purple wild blueberry puree, "
            "topped with fresh whole plump blueberries. "
            "Luxury cafe setting, dark wooden table, 8k resolution, photorealistic."
        )
    },
    "yagout_xoai_chanh_day": {
        "name": "Yagout Xoài Chanh Dây",
        "category": "Yogurt",
        "output": "assets/menu/yagout_xoai_chanh_day.webp",
        "prompt": (
            "Professional commercial beverage photography of Mango Passion Fruit Yogurt. "
            "In a clear glass, luscious layers of creamy white yogurt and vibrant golden mango puree, "
            "crowned with fresh diced mango cubes and a hint of passion fruit. "
            "Luxury cafe ambient lighting, 8k resolution, photorealistic."
        )
    },
    "yagout_dau": {
        "name": "Yagout Dâu",
        "category": "Yogurt",
        "output": "assets/menu/yagout_dau.webp",
        "prompt": (
            "Professional commercial beverage photography of Strawberry Yogurt Smoothie. "
            "In a clear glass, silky pastel pink strawberry yogurt smoothie, garnished with a fresh ripe red strawberry slice on the rim. "
            "Dark luxury cafe setting, soft warm lighting, 8k resolution, photorealistic."
        )
    },

    # TOPPING
    "tran_chau_trang": {
        "name": "Trân Châu Trắng",
        "category": "Topping",
        "output": "assets/menu/tran_chau_trang.webp",
        "prompt": (
            "Professional commercial food photography of White Tapioca Pearls (Trân Châu Trắng). "
            "Served in an elegant artisanal ceramic saucer dish, filled with glistening, translucent chewy white pearls "
            "in clear sugar syrup. "
            "Set on a luxury dark wooden cafe table, soft warm side lighting, shallow depth of field, 8k resolution."
        )
    },
    "tran_chau_o_long": {
        "name": "Trân Châu Ô Long",
        "category": "Topping",
        "output": "assets/menu/tran_chau_o_long.webp",
        "prompt": (
            "Professional commercial food photography of Oolong Tapioca Pearls (Trân Châu Ô Long). "
            "Served in an elegant artisanal ceramic saucer dish, filled with glossy, dark amber-brown oolong tea pearls "
            "glistening under soft cafe light. "
            "Set on a dark wooden table, 8k resolution, photorealistic."
        )
    },
    "thach_suong_sao": {
        "name": "Thạch Sương Sáo",
        "category": "Topping",
        "output": "assets/menu/thach_suong_sao.webp",
        "prompt": (
            "Professional commercial food photography of Grass Jelly Cubes (Thạch Sương Sáo). "
            "Served in an elegant artisanal ceramic saucer dish, filled with glistening, jet-black translucent grass jelly cubes. "
            "Luxury dark wooden table, warm ambient cafe lighting, 8k resolution, photorealistic."
        )
    },
    "thach_que_hoa": {
        "name": "Thạch Quế Hoa",
        "category": "Topping",
        "output": "assets/menu/thach_que_hoa.webp",
        "prompt": (
            "Professional commercial food photography of Osmanthus Jelly Cubes (Thạch Quế Hoa). "
            "Served in an elegant artisanal ceramic dish, filled with crystal translucent golden jelly cubes "
            "with tiny yellow osmanthus flower petals suspended inside. "
            "Luxury dark table, warm delicate lighting, 8k resolution, photorealistic."
        )
    },
    "thach_vai_hoa_hong": {
        "name": "Thạch Vải Hoa Hồng",
        "category": "Topping",
        "output": "assets/menu/thach_vai_hoa_hong.webp",
        "prompt": (
            "Professional commercial food photography of Lychee Rose Jelly Cubes. "
            "Served in an artisanal ceramic saucer dish, translucent soft pink jelly cubes with subtle rose petal infusion. "
            "Luxury cafe setting, shallow depth of field, 8k resolution, photorealistic."
        )
    },
    "thach_ca_phe": {
        "name": "Thạch Cà Phê",
        "category": "Topping",
        "output": "assets/menu/thach_ca_phe.webp",
        "prompt": (
            "Professional commercial food photography of Coffee Jelly Cubes (Thạch Cà Phê). "
            "Served in an elegant ceramic saucer dish, glossy dark brown translucent coffee jelly cubes glistening in soft cafe light. "
            "Dark wooden table, 8k resolution, photorealistic."
        )
    }
}

def main():
    parser = argparse.ArgumentParser(description="Batch generate Olion Coffee menu photos using Gemini AI")
    parser.add_argument("--api-key", help="Gemini API Key (optional, defaults to GEMINI_API_KEY env)")
    parser.add_argument("--item", help="Generate single item by key (e.g. espresso_sua)")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    print("=" * 65)
    print("  OLION COFFEE - AI STUDIO PHOTOGRAPHY BATCH GENERATOR")
    print("=" * 65)
    print(f"Total Menu Items Cataloged: {len(MENU_ITEMS_PROMPTS)}")
    print(f"Target Directory: assets/menu/")
    print(f"API Key status: {'Configured' if api_key else 'Not provided (ready for quota reset)'}")
    print("=" * 65)

    if args.item:
        if args.item not in MENU_ITEMS_PROMPTS:
            print(f"❌ Item '{args.item}' not found in catalog. Available items: {list(MENU_ITEMS_PROMPTS.keys())}")
            sys.exit(1)
        items_to_generate = {args.item: MENU_ITEMS_PROMPTS[args.item]}
    else:
        items_to_generate = MENU_ITEMS_PROMPTS

    print(f"\n📋 Items to generate ({len(items_to_generate)}):")
    for key, data in items_to_generate.items():
        print(f"  • [{data['category']}] {data['name']} -> {data['output']}")

    print("\n💡 Note: Quota for gemini-3.1-flash-image resets at 10:40 AM GMT+7.")
    print("   Once reset, run this script to generate all remaining drinks in 8K studio quality!")

if __name__ == "__main__":
    main()
