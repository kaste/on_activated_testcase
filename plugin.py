
import sublime_plugin


activated_views = set()
async_activated_views = set()


class ActivatedListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        activated_views.add(view.id())

    def on_activated_async(self, view):
        async_activated_views.add(view.id())
