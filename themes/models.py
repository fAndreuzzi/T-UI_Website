from django.db import models

class Theme(models.Model):
    navigationbar_color = models.TextField()
    app_uninstalled_color = models.TextField()
    storage_color = models.TextField()
    battery_color_high = models.TextField()
    battery_color_low = models.TextField()
    battery_color_medium = models.TextField()
    ram_color = models.TextField()
    output_color = models.TextField()
    input_color = models.TextField()
    bg_color = models.TextField()
    statusbar_color = models.TextField()
    enter_color = models.TextField()
    time_color = models.TextField()
    toolbar_bg = models.TextField()
    alias_content_color = models.TextField()
    app_installed_color = models.TextField()
    device_color = models.TextField()
    toolbar_color = models.TextField()
    alias_text_color = models.TextField()
    song_bg_color = models.TextField()
    cmd_bg_color = models.TextField()
    song_text_color = models.TextField()
    file_bg_color = models.TextField()
    contact_text_color = models.TextField()
    enabled = models.BooleanField()
    contact_bg_color = models.TextField()
    apps_bg_color = models.TextField()
    transparent = models.BooleanField()
    cmd_text_color = models.TextField()
    default_text_color = models.TextField()
    apps_text_color = models.TextField()
    file_text_color = models.TextField()
    alias_bg_color = models.TextField()
    default_bg_color = models.TextField()
    name = models.TextField()
    downloads = models.IntegerField()
    author = models.TextField()