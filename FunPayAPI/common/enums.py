from __future__ import annotations
from enum import Enum


class MessageTypes(Enum):
    """
    Типы сообщений.
    """
    NON_SYSTEM = 0
    """Несистемное сообщение."""

    ORDER_PURCHASED = 1
    """Покупатель X оплатил заказ #Y. Лот. X, не забудьте потом нажать кнопку «Подтвердить выполнение заказа»."""

    ORDER_CONFIRMED = 2
    """Покупатель X подтвердил успешное выполнение заказа #Y и отправил деньги продавцу Z."""

    NEW_FEEDBACK = 3
    """Покупатель X написал отзыв к заказу #Y."""

    FEEDBACK_CHANGED = 4
    """Покупатель X изменил отзыв к заказу #Y."""

    FEEDBACK_DELETED = 5
    """Покупатель X удалил отзыв к заказу #Y."""

    NEW_FEEDBACK_ANSWER = 6
    """Продавец Z ответил на отзыв к заказу #Y."""

    FEEDBACK_ANSWER_CHANGED = 7
    """Продавец Z изменил ответ на отзыв к заказу #Y."""

    FEEDBACK_ANSWER_DELETED = 8
    """Продавец Z удалил ответ на отзыв к заказу #Y."""

    ORDER_REOPENED = 9
    """Заказ #Y открыт повторно."""

    REFUND = 10
    """Продавец Z вернул деньги покупателю X по заказу #Y."""

    PARTIAL_REFUND = 11
    """Часть средств по заказу #Y возвращена покупателю."""

    ORDER_CONFIRMED_BY_ADMIN = 12
    """Администратор A подтвердил успешное выполнение заказа #Y и отправил деньги продавцу Z."""

    DISCORD = 13
    """Вы можете перейти в Discord. Внимание: общение за пределами сервера FunPay считается нарушением правил."""


class OrderStatuses(Enum):
    """
    Состояния заказов.
    """
    PAID = 0
    """Заказ оплачен и ожидает выполнения."""
    CLOSED = 1
    """Заказ закрыт."""
    REFUNDED = 2
    """Средства по заказу возвращены."""


class SubCategoryTypes(Enum):
    """
    Типы подкатегорий.
    """
    COMMON = 0
    """Подкатегория со стандартными лотами."""
    CURRENCY = 1
    """Подкатегория с лотами игровой валюты (их нельзя поднимать)."""


class Currency(Enum):
    """
    Типы валют.
    """
    USD = 0
    """Доллар"""
    RUB = 1
    """Рубль"""
    EUR = 2
    """Евро"""


class Wallet(Enum):
    """Кошельки для вывода."""
    QIWI = 0
    BINANCE = 2
    TRC = 3
    CARD = 4
    WEBMONEY = 5
    YOUMONEY = 6
