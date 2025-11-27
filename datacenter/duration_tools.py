from datetime import datetime


def get_duration(visit):
    """
    Возвращает продолжительность визита в секундах.
    Если человек все еще в хранилище (leaved_at нет), берём текущее время.
    """
    entered_at = visit.entered_at
    leaved_at = visit.leaved_at if visit.leaved_at else datetime.now(entered_at.tzinfo)
    duration = (leaved_at - entered_at).total_seconds()
    return duration


def format_duration(duration):
    """
    Форматирует длительность (секунды) в строку ЧЧ:ММ:СС
    """
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}:{minutes:02}:{seconds:02}'
    

def is_visit_long(visit, threshold_seconds=3600):
    """
    Проверяет, длится ли визит дольше порога (по умолчанию 1 час — 3600 сек)
    """
    return get_duration(visit) > threshold_seconds