#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common AxionAOSP stuff
$(call inherit-product, vendor/neoteric/target/product/neoteric-target.mk)

# Inherit from r5x device
$(call inherit-product, device/xiaomi/phoenix/device.mk)

PRODUCT_BRAND := Redmi
PRODUCT_DEVICE := phoenix
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_NAME := phoenix
PRODUCT_MODEL := Redmi K30

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# Boot animation resolution.
TARGET_BOOT_ANIMATION_RES := 720

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="phoenix-user 11 RKQ1.200826.002 21.9.28 release-keys" \
    BuildFingerprint=Redmi/phoenix/phoenix:11/RKQ1.200826.002/21.9.28:user/release-keys