from appium.webdriver.common.appiumby import AppiumBy


class SettingsLocators:
    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/title"
    )

    SCREEN_CONFIG = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/screenConfig"
    )

    SWITCH_MUSIC = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/switchMusic"
    )

    LAYOUT_MODE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/layoutMode"
    )

    MODE_LIGHT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/modeLight"
    )

    MODE_DARK = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/modeDark"
    )

    INCREASE_FONT_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/increaseTextId"
    )

    DECREASE_FONT_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/decreaseTextId"
    )

    PREVIEW_TEXT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/textEg"
    )

    PREVIEW_VERSE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/verseEg"
    )

    BTN_EXPORT_BACKUP = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnExportBackup"
    )

    BTN_IMPORT_BACKUP = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnImportBackup"
    )

    BTN_DOWNLOAD_ALL_AUDIO = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnDownloadAllAudio"
    )

    # Export Dialog
    EXPORT_DIALOG_TITLE = (
        AppiumBy.ID,
        "android:id/alertTitle"
    )

    EXPORT_CB_FAVORITES = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/cbFavorites"
    )

    EXPORT_CB_KNOWN = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/cbKnown"
    )

    EXPORT_RV_CUSTOM_LISTS = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/rvCustomLists"
    )

    EXPORT_CB_LIST_NAME = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/cbListName"
    )

    EXPORT_BTN_SHARE = (
        AppiumBy.ID,
        "android:id/button1"
    )

    EXPORT_BTN_CANCEL = (
        AppiumBy.ID,
        "android:id/button2"
    )

    EXPORT_BTN_SAVE = (
        AppiumBy.ID,
        "android:id/button3"
    )

    # Document / File Picker
    FILE_TITLE = (
        AppiumBy.ID,
        "android:id/title"
    )

    @staticmethod
    def file_by_name(filename: str):
        return (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='android:id/title' and @text='{filename}']"
        )
