"""
    장고 스케줄링 파일
    등록 종료 일자로 부터 자동 삭제
    
    설정 명령어
    python manage.py crontab add
    
    해제 명령어
    python manage.py crontab remove
    
    윈도우에서 fcntl 모듈을 설치할 수 없다는 결론
"""

"""from datetime import timedelta
from django.utils import timezone
from contents.models import Content


def delete_expired_data():
    # 현재 날짜
    current_date = timezone.now().date()
    # 14일 이전 날짜
    expiration_date = current_date - timedelta(days=14)
    # 등록 종료 일자가 14일 이전인 데이터 삭제
    Content.objects.filter(enroll_end_date__lte=expiration_date).delete()"""
