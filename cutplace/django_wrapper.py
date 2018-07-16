try:
    from django.utils.translation import ugettext
except ImportError:
    def ugettext(untranslated):
        # NoOP in case Django isn't available
        return untranslated
