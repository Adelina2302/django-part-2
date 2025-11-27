from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    """Сколько длился визит на данный момент"""
    start = localtime(visit.entered_at)
    end = localtime()  # сейчас
    return end - start


def format_duration(duration):
    """Переводим timedelta в строку ЧЧ:ММ"""
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"


def storage_information_view(request):
    # Получаем все незакрытые визиты
    unclosed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in unclosed_visits:
        duration = get_duration(visit)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
