from .models import (Genre,
                     Person,
                     PersonFilmwork,
                     Filmwork,
                     GenreFilmwork)
from django.db.models.signals import (post_save,
                                      post_delete)
from django.dispatch import receiver
import logging

logger = logging.getLogger('django')


@receiver(post_save, sender=Genre)
@receiver(post_save, sender=Person)
@receiver(post_save, sender=PersonFilmwork)
@receiver(post_save, sender=Filmwork)
@receiver(post_save, sender=GenreFilmwork)
def log_create_or_update(sender, instance, created, **kwargs):
    model_name = sender.__name__
    if created:
        logger.info('New record created in %s: %s', model_name, instance)
    else:
        logger.info('Record updated in %s: %s', model_name, instance)


@receiver(post_delete, sender=Genre)
@receiver(post_delete, sender=Person)
@receiver(post_delete, sender=PersonFilmwork)
@receiver(post_delete, sender=Filmwork)
@receiver(post_delete, sender=GenreFilmwork)
def log_delete(sender, instance, **kwargs):
    model_name = sender.__name__
    logger.info('Record deleted in %s: %s', model_name, instance)
