try:
    from django.core.exceptions import ImproperlyConfigured
    from django.utils.translation import ugettext as _ugettext

    def ugettext(untranslated):
        try:
            return _ugettext(untranslated)
        except (ImproperlyConfigured, ModuleNotFoundError):
            return untranslated
except ImportError:
    def ugettext(untranslated):
        # NoOP in case Django isn't available
        return untranslated
