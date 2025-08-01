[app]
title = RSS Reader
package.name = rssreader
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,feedparser,plyer,cython,pyjnius==2.1.0
orientation = portrait
fullscreen = 0

# Permissions for internet and notifications
android.permissions = INTERNET,RECEIVE_BOOT_COMPLETED,VIBRATE,WAKE_LOCK

# Entry point
entrypoint = main.py

# (Optional) Icon
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.ndk = 25b
android.arch = armeabi-v7a
android.minapi = 21
sdk_path = /home/runner/.buildozer/android/platform/android-sdk
build_tools_version = 34.0.0
