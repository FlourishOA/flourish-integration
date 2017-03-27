from abc import ABCMeta, abstractmethod
import re


class BaseScraper:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_entries(self):
        pass


class BaseJournalScraper(BaseScraper):
    __metaclass__ = ABCMeta
    COL_NAMES = ("pub_name", "journal_name", "date", "journal_type", "issn", "apc")
    PRICE_PATT = re.compile("\$\d[,|\d*]\d*")
    ISSN_PATT = re.compile("\d{4}-\d{3}[\dxX]")

    REPLS = {
        "\xca": " ", "\r\xa0": "", "\x96": "n",
        "\x97": "o", "\x87": "a", "\x8b": "a",
        "\x92": "i", "\x8e": "e", "\x8f": "e",
        "\xd5": "'", "\xea": "I", "\x9f": "u",
        "\x8a": "a", "\x8d": "c", "\x91": "i",
        "\x85": "O", "\x9a": "o", "\xd0": "",
        "\xa7": "B", " fee not payable by author": ""
    }

    @staticmethod
    def to_unicode_item(item):
        try:
            return unicode(item, errors="replace")
        except TypeError:
            return item

    @staticmethod
    def to_unicode_row(row):
        return [BaseJournalScraper.to_unicode_item(i) for i in row]
