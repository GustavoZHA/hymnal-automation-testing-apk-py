from appium.webdriver.common.appiumby import AppiumBy


class SettingsLocators:
    THEME_SWITCH = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/switch_theme"
    )

    INCREASE_FONT_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btn_font_increase"
    )

    DECREASE_FONT_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btn_font_decrease"
    )

    VISIBLE_MUSIC_SWITCH = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/switch_music"
    )

    SETTINGS_TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tv_settings_title"
    )
