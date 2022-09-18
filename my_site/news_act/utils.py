
class MyMixin(object):
    mixin_prop = ''

    def get_upper(self, s: str) -> str:
        self.mixin_prop = s
        return s.upper()
