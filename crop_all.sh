#!/bin/bash
SRC="/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0/.user_uploaded/media_1789917213060.png"
OUT_DIR="/Users/thanhduy/Documents/olion-coffee/assets/menu"

mkdir -p "$OUT_DIR"

crop_item() {
  local name="$1"
  local x="$2"
  local y="$3"
  local w="${4:-86}"
  local h="${5:-84}"
  sips --cropToHeightWidth "$h" "$w" --cropOffset "$y" "$x" "$SRC" --out "$OUT_DIR/$name.png" > /dev/null
}

# Row 1 (y: 158)
crop_item "espresso" 20 158
crop_item "espresso_sua" 118 158
crop_item "bac_xiu" 216 158
crop_item "tra_vai_hoa_hong" 314 158
crop_item "tra_buoi_hong_chanh_vang" 412 158
crop_item "matcha_latte" 510 158
crop_item "matcha_caramel" 607 158
crop_item "matcha_bac_ha" 705 158
crop_item "tran_chau_trang" 810 158
crop_item "tran_chau_o_long" 908 158

# Row 2 (y: 276)
crop_item "latte_hanh_nhan" 20 276
crop_item "caramel_latte" 118 276
crop_item "americano" 216 276
crop_item "tra_chanh_day_nhiet_doi" 314 276
crop_item "tra_xoai_chanh_day" 412 276
crop_item "matcha_kem_muoi" 510 276
crop_item "matcha_que_hoa" 607 276
crop_item "matcha_cold_whisk" 705 276
crop_item "thach_suong_sao" 810 276
crop_item "thach_que_hoa" 908 276

# Row 3 (y: 398)
crop_item "ca_phe_muoi" 20 398
crop_item "ca_phe_bac_ha" 118 398
crop_item "ca_phe_sua_oatside" 216 398
crop_item "luc_tra_nhan" 314 398
crop_item "luc_tra_tran_chau_trang" 412 398
crop_item "matcha_dua" 510 398
crop_item "matcha_dau" 607 398
crop_item "matcha_oatside" 705 398
crop_item "thach_vai_hoa_hong" 810 398
crop_item "thach_ca_phe" 908 398

# Row 4 (y: 578)
crop_item "cacao_latte" 20 578
crop_item "cacao_kem_muoi" 118 578
crop_item "cacao_bac_ha" 216 578
crop_item "nuoc_ep_cam" 362 578
crop_item "nuoc_ep_chanh_day" 460 578
crop_item "yagout_dao_chanh_day" 618 578
crop_item "yagout_viet_quat" 715 578
crop_item "yagout_xoai_chanh_day" 812 578
crop_item "yagout_dau" 910 578

echo "Fine-tuned crop completed for all 39 items!"
