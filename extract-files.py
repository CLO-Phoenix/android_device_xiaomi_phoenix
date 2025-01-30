#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
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
    'hardware/xiaomi',
    'vendor/qcom/common/vendor/adreno-5xx',
    'vendor/qcom/common/vendor/adreno-r',
    'vendor/qcom/common/vendor/adreno-s',
    'vendor/qcom/common/vendor/adreno-t',
    'vendor/qcom/common/vendor/adreno-u',
    'vendor/qcom/common/vendor/media/5.4',
    'vendor/qcom/common/vendor/perf',
    'vendor/xiaomi/sm6150-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/init.mi_thermald.rc': blob_fixup()
        .regex_replace(' +seclabel u:r:mi_thermald:s0\n', ''),
    'vendor/lib64/libgoodixhwfingerprint.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so'),    
    'vendor/lib64/camera/components/com.qti.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    ('vendor/lib64/hw/camera.qcom.so', 'vendor/lib64/libFaceDetectpp-0.5.2.so', 'vendor/lib64/libfacedet.so'): blob_fixup()
        .binary_regex_replace(b'libmegface.so', b'libfacedet.so')
        .binary_regex_replace(b'libMegviiFacepp-0.5.2.so', b'libFaceDetectpp-0.5.2.so')
        .binary_regex_replace(b'megviifacepp_0_5_2_model', b'facedetectpp_0_5_2_model'),
}  # fmt: skip

module = ExtractUtilsModule(
    'phoenix',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6150-common', module.vendor
    )
    utils.run()
