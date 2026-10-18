class Texts:
    
    URL_PART_FORGOT_PASSWORD = "/forgot-password"
    URL_PART_FEED = "/feed"
    URL_PART_ACCOUNT_PROFILE = "/account/profile"
    URL_PART_ACCOUNT_ORDER_HISTORY = "/account/order-history"

    PASSWORD_TYPE_VISIBLE = "text"

    # Заглушка, которая появляется в модалке до прихода реального номера
    ORDER_NUMBER_PLACEHOLDER = "9999"


class RecoveryData:

    EMAIL = "recovery_test@yandex.ru"


class Timeouts:

    DEFAULT = 10
    LONG = 15
    POLL_INTERVAL = 2


class IngredientDelta:

    BUN = 2          # булочка = верх + низ
    SAUCE = 1
    MEAT = 1