from appium.webdriver.common.appiumby import AppiumBy


class HymnPageLocators:

    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/titleHymn"
    )

    PREVIOUS_HYMN_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/nextHymnsBefore"
    )

    NEXT_HYMN_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/nextHymnsAfter"
    )

    FAVORITE_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/favoriteFloatButton"
    )

    PLAY_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/playFloatButton"
    )

    ADD_TO_LIST_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/addListHymns"
    )

    KNOWN_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/knowFloatButton"
    )

    MUSIC_PLAYER_CONTAINER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/musicPlayerLayout"
    )

    CURRENT_TIME = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tvCurrent"
    )

    DURATION_TIME = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tvDuration"
    )

    SEEK_BAR = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/seekBar"
    )

    REWIND_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnRewind"
    )

    PLAY_PAUSE_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnPlayPause"
    )

    FORWARD_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btnForward"
    )

    HYMN_CONTAINER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/hymn"
    )

    VERSE_TEXTS = (
        AppiumBy.XPATH,
        "//android.widget.LinearLayout[@resource-id='com.pentecostal.himnarioprincipal:id/hymn']//android.widget.TextView"
    )
