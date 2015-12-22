import blinker


namespace = blinker.Namespace()

pre_allocate_ids = namespace.signal('pre-allocate-ids')
post_allocate_ids = namespace.signal('post-allocate-ids')

pre_delete = namespace.signal('pre-delete')
post_delete = namespace.signal('post-delete')

pre_get = namespace.signal('pre-get')
post_get = namespace.signal('post-get')

pre_put = namespace.signal('pre-put')
post_put = namespace.signal('post-put')


class _SignalsMixin(object):
    @classmethod
    def _pre_allocate_ids_hook(cls, size, max, parent):
        pre_allocate_ids.send(cls, size=size, max=max, parent=parent)

    @classmethod
    def _post_allocate_ids_hook(cls, size, max, parent, future):
        post_allocate_ids.send(
            cls, size=size, max=max, parent=parent, future=future)

    @classmethod
    def _pre_delete_hook(cls, key):
        pre_delete.send(cls, key=key)

    @classmethod
    def _post_delete_hook(cls, key, future):
        post_delete.send(cls, key=key, future=future)

    @classmethod
    def _pre_get_hook(cls, key):
        pre_get.send(cls, key=key)

    @classmethod
    def _post_get_hook(cls, key, future):
        post_get.send(cls, key=key, future=future)

    def _pre_put_hook(self):
        pre_put.send(self.__class__, instance=self)

    def _post_put_hook(self, future):
        post_put.send(self.__class__, instance=self, future=future)


