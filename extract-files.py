#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so'): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .add_needed('libcomparetf2_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'zippo',
    'lenovo',
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8150-common', module.vendor
    )
    utils.run()
