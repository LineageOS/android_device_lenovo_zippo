#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/lenovo/sm8150-common',
    'hardware/qcom-caf/sm8150',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so'): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .add_needed('libcomparetf2_shim.so'),
    'vendor/lib64/libsnpe_adsp.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    ('vendor/lib64/libsnpe_dsp_domains.so', 'vendor/lib64/libsnpe_dsp_domains_v2.so'): blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
        .clear_symbol_version('remote_register_dma_handle'),
    (
        'vendor/lib64/hw/android.hardware.camera.provider@2.4-impl.so',
        'vendor/lib64/android.hardware.camera.provider@2.4-external.so',
        'vendor/lib64/camera.device@3.4-external-impl.so',
        'vendor/lib64/camera.device@3.5-external-impl.so',
        'vendor/lib64/camera.device@3.6-external-impl.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so')
}  # fmt: skip

module = ExtractUtilsModule(
    'zippo',
    'lenovo',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8150-common', module.vendor
    )
    utils.run()
