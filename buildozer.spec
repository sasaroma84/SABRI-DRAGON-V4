[app]
title = SABRI DRAGON V4
package.name = sabridragon
package.domain = com.sabri.dragon
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0
android.permissions = INTERNET,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.ndk = 25b
android.sdk = 33
android.api = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
