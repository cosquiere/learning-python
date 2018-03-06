# -*- coding: utf-8 -*-

from django.conf import settings


# LICENSES:
COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)


#GET FROM PROJECT SETTINGS LICENSES IF NOT FOUND SET DEFAULT LICENSES
LICENSES = getattr(settings,'LICENSES',DEFAULT_LICENSES)


#By default not badwords validators
BADWORDS = getattr(settings,'PROJECT_BADWORDS',[])