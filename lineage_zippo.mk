#
# Copyright (C) 2019-2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_p.mk)

# Inherit from zippo device
$(call inherit-product, device/lenovo/zippo/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Device identifier. This must come after all inclusions.
PRODUCT_BRAND := Lenovo
PRODUCT_DEVICE := zippo
PRODUCT_MANUFACTURER := Lenovo
PRODUCT_MODEL := Lenovo L78051
PRODUCT_NAME := lineage_zippo

PRODUCT_GMS_CLIENTID_BASE := android-lenovo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="zippo_row-user 9 PKQ1.190110.001 11.0.405_191210 release-keys" \
    BuildFingerprint=Lenovo/zippo_row/zippo:9/PKQ1.190110.001/11.0.405_191210:user/release-keys \
    DeviceProduct=zippo
