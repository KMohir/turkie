from django import template
from django.utils.translation import get_language

register = template.Library()

UZBEK_MONTHS = {
    "january": "yanvar",
    "february": "fevral",
    "march": "mart",
    "april": "aprel",
    "may": "may",
    "june": "iyun",
    "july": "iyul",
    "august": "avgust",
    "september": "sentyabr",
    "october": "oktyabr",
    "november": "noyabr",
    "december": "dekabr",
}

RUSSIAN_MONTHS = {
    "january": "январь",
    "february": "февраль",
    "march": "март",
    "april": "апрель",
    "may": "май",
    "june": "июнь",
    "july": "июль",
    "august": "август",
    "september": "сентябрь",
    "october": "октябрь",
    "november": "ноябрь",
    "december": "декабрь",
}

@register.filter
def uzbek_date_format(value):
    if not value:
        return ""
    current_language = get_language()
    year = value.strftime("%Y")
    day = value.strftime("%d")
    month = value.strftime("%B").lower()  # e.g., "march"

    if current_language == 'ru':
        month_name = RUSSIAN_MONTHS.get(month, month)
        return f"{year} год {day}-{month_name}"
    else:
        month_name = UZBEK_MONTHS.get(month, month)
        return f"{year}-yil {day}-{month_name} kuni"