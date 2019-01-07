import on_activated_testcase.plugin as module

import sublime
from unittesting import DeferrableTestCase


class TestActivatedCallback(DeferrableTestCase):
    @classmethod
    def setUpClass(cls):
        sublime.run_command("new_window")
        cls.window = sublime.active_window()
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    @classmethod
    def tearDownClass(self):
        self.window.run_command('close_window')

    def test_a(self):
        module.activated_views.clear()
        module.async_activated_views.clear()

        view = self.window.new_file()
        print('--> created new view', view.id())
        view.set_scratch(True)
        self.addCleanup(view.close)

        yield 1000

        self.assertTrue(len(module.activated_views) > 0)
        self.assertTrue(view.id() in module.activated_views)
        self.assertTrue(len(module.async_activated_views) > 0)
        self.assertTrue(view.id() in module.async_activated_views)
