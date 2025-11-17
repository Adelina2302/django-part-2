import os
import django
from django.utils import timezone
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':
    # Все визиты без времени выхода
    unclosed_visits = Visit.objects.filter(leaved_at=None)

    for visit in unclosed_visits:
        entered_at_local = localtime(visit.entered_at)  # Переводим время в Москву
        time_spent = timezone.now() - visit.entered_at  # Сколько прошло времени

        print(f'Посетитель: {visit.passcard.owner_name}')
        print(f'Зашёл в хранилище: {entered_at_local}')
        print(f'Находится в хранилище: {time_spent}')
        print('---')
