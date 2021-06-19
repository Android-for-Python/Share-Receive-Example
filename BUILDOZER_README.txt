

# VideoPlayer depends on ffpyplayer
requirements = python3, kivy==2.0.0, ffpyplayer

# Required only for devices with api < 29
android.permissions = READ_EXTERNAL_STORAGE

android.api = 30

# Add Intent filter
android.manifest.intent_filters = intent_filter.xml

android.add_src = storage_src
