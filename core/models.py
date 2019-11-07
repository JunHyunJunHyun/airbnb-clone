from django.db import models


class AbstractTimeStamped(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # model이지만 데이터베이스에는 나타나지 않는 추상 모델 (확장용)
