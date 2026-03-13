"""Tests for the UI elements."""
import os
import pytest

pytest.importorskip("PyQt5")

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
if IN_GITHUB_ACTIONS:
    pytest.skip("Skipping UI tests in GitHub Actions", allow_module_level=True)

from pathlib import Path
import sys
from tik_manager4.core import utils

from tik_manager4.ui import main
from tik_manager4.ui import i18n
from tik_manager4.ui.Qt import QtWidgets
from tik_manager4.ui import pick
from tik_manager4.ui.dialog.work_dialog import NewVersionDialog
from tik_manager4.ui.dialog.preview_dialog import PreviewDialog
from tik_manager4.ui.dialog.project_dialog import SetProjectDialog, NewProjectDialog
from tik_manager4.ui.dialog.subproject_dialog import NewSubprojectDialog, EditSubprojectDialog
from tik_manager4.ui.dialog.publish_dialog import PublishSceneDialog
from tik_manager4.ui.dialog.settings_dialog import SettingsDialog
from tik_manager4.ui.dialog.user_dialog import NewUserDialog
from tik_manager4.ui.dialog.work_dialog import NewWorkDialog
from tik_manager4.ui.dialog.feedback import Feedback
from tik_manager4.ui.widgets import common

class TestUI:
    """Test UI."""

    @pytest.fixture(scope='function')
    def main_object(self, tik, files):
        project_path = Path(utils.get_home_dir(), "t4_UI_test_project_DO_NOT_USE")
        if project_path.exists():
            files.force_remove_directory(project_path)
        tik.user.set("Admin", "1234")
        tik.user.ui_language = "en"
        tik.user.resume.apply_settings()
        tik.create_project(str(project_path), structure_template="empty")
        return tik

    def _kill_modules(self):
        kill_list = []
        for name, _module in sys.modules.items():
            if name.startswith("tik_manager4"):
                kill_list.append(name)
        for x in kill_list:
            sys.modules.pop(x)

    def test_launch_main_ui(self, qtbot, main_object):
        m = main.launch(dcc="Standalone")
        qtbot.addWidget(m)
        assert m.windowTitle() == f"{main.WINDOW_NAME} - Standalone"
        assert m.objectName() == f"{main.WINDOW_NAME} - Standalone"

    def test_launch_ui_with_wrong_dcc(self, qtbot):
        # make sure all the modules are reloaded
        self._kill_modules()

        with pytest.raises(ImportError) as e_info:
            main.launch(dcc="Maya")
            assert e_info == "cannot import name 'cmds' from 'maya' (unknown location)"

    def test_launch_ui_manually(self, qtbot, main_object):
        parent = main_object.dcc.get_main_window()
        m = main.MainUI(main_object, parent=parent)
        m.show()
        qtbot.addWidget(m)
        assert m.windowTitle() == main.WINDOW_NAME
        assert m.objectName() == main.WINDOW_NAME

    def test_main_ui_language_switch(self, qtbot, main_object):
        m = main.launch(dcc="Standalone")
        m.show()
        qtbot.addWidget(m)

        m.set_ui_language("zh_CN")
        menu_texts = [_action.text().replace("&", "").strip() for _action in m.menu_bar.actions()]
        assert "文件" in menu_texts
        assert "语言" in menu_texts
        assert m.tik.user.ui_language == "zh_CN"

        m.set_ui_language("en")
        menu_texts = [_action.text().replace("&", "").strip() for _action in m.menu_bar.actions()]
        assert "File" in menu_texts
        assert "Language" in menu_texts
        assert i18n.get_language() == "en"

    def test_launch_respects_persisted_language(self, qtbot, main_object):
        main_object.user.ui_language = "zh_CN"
        main_object.user.resume.apply_settings()
        i18n.set_language("en")

        m = main.launch(dcc="Standalone")
        m.show()
        qtbot.addWidget(m)

        menu_texts = [_action.text().replace("&", "").strip() for _action in m.menu_bar.actions()]
        assert "文件" in menu_texts
        assert i18n.get_language() == "zh_CN"

        m.set_ui_language("en")

    def test_project_dialog_uses_active_language(self, qtbot, main_object):
        i18n.ensure_translator()
        i18n.set_language("zh_CN")

        dialog = SetProjectDialog(main_object)
        dialog.show()
        qtbot.addWidget(dialog)

        assert dialog.windowTitle() == "设置项目"

    def test_open_dialog_updates_when_language_switches(self, qtbot, main_object):
        m = main.launch(dcc="Standalone")
        m.show()
        qtbot.addWidget(m)

        dialog = SettingsDialog(main_object)
        dialog.show()
        qtbot.addWidget(dialog)

        m.set_ui_language("zh_CN")
        assert dialog.windowTitle() == "设置"

        m.set_ui_language("en")
        assert dialog.windowTitle() == "Settings"

    def test_main_ui_buttons(self, qtbot, main_object, monkeypatch):
        self._kill_modules()
        m = main.launch(dcc="Standalone")
        m.show()
        qtbot.addWidget(m)

        # Test buttons
        # get all the buttons under work_buttons_layout
        buttons_layout = m.work_buttons_layout
        widget_count = buttons_layout.count()
        for nmb in range(widget_count):
            button = buttons_layout.itemAt(nmb).widget()
            if button:
                button_text = button.text()
                monkeypatch.setattr(m.feedback, "pop_info", lambda *args, **kwargs: None)
                monkeypatch.setattr(NewWorkDialog, "exec_", lambda *args: QtWidgets.QMessageBox.Yes)
                monkeypatch.setattr(Feedback, "pop_info", lambda *args, **kwargs: None)

                if button_text == "Save New Work":
                    button.click()
                elif button_text == "Increment Version":
                    # monkeypatch the pop_info method of m.feedback to return None
                    button.click()
                elif button_text == "Ingest Version":
                    # monkeypatch the pop_info method of m.feedback to return None
                    button.click()
                elif button_text == "Publish":
                    button.click()

    def test_feedback_pop_ups(self, qtbot, monkeypatch):
        """Test the feedback module"""

        feedback = Feedback()
        monkeypatch.setattr(common.TikMessageBox, "exec_", lambda *args: QtWidgets.QMessageBox.Yes)
        feedback.pop_info(title="Test", text="Test", details="Test", critical=False, button_label="Test", modal=False)
        feedback.pop_info(title="Test", text="Test", details="Test", critical=True, button_label="Test", modal=True)
        feedback.pop_question(title="Test", text="Test", details="Test", buttons=["yes", "no", "cancel"], modal=False)
        feedback.pop_question(title="Test", text="Test", details="Test", buttons=["save", "continue", "ok"], modal=True)

    def test_preview_dialog(self, qtbot, main_object):
        # create a new work
        main_object.project.scan_tasks()
        work = main_object.project.tasks["main"].categories["Model"].create_work("test_work")
        dialog = PreviewDialog(work, 1)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_project_dialog(self, qtbot, main_object):
        dialog = SetProjectDialog(main_object)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_new_project_dialog(self, qtbot, main_object):
        dialog = NewProjectDialog(main_object)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_new_subproject_dialog(self, qtbot, main_object):
        dialog = NewSubprojectDialog(main_object.project)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_edit_subproject_dialog(self, qtbot, main_object):
        dialog = EditSubprojectDialog(main_object.project)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_publish_dialog(self, qtbot, monkeypatch, main_object):
        # create a new work
        main_object.project.scan_tasks()
        work = main_object.project.tasks["main"].categories["Model"].create_work("test_work")
        monkeypatch.setattr(main_object.project, "get_current_work", lambda: (work, 1))
        main_object.project.publisher.resolve()
        dialog = PublishSceneDialog(main_object.project)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_settings_dialog(self, qtbot, main_object):
        dialog = SettingsDialog(main_object)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_user_dialog(self, qtbot, main_object):
        dialog = NewUserDialog(main_object.user)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_create_new_work_dialog(self, qtbot, main_object):
        dialog = NewWorkDialog(main_object)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_create_new_version_dialog(self, qtbot, main_object):
        main_object.project.scan_tasks()
        work = main_object.project.tasks["main"].categories["Model"].create_work("test_work")
        dialog = NewVersionDialog(work, ingest=False)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_create_new_version_dialog_ingest(self, qtbot, main_object):
        main_object.project.scan_tasks()
        work = main_object.project.tasks["main"].categories["Model"].create_work("test_work")
        dialog = NewVersionDialog(work, ingest=True)
        qtbot.addWidget(dialog)
        style_file = pick.style_file()
        dialog.setStyleSheet(str(style_file.readAll(), "utf-8"))
        dialog.show()
        # qtbot.stop()

    def test_applying_stylesheet(self, qtbot, tmp_path):
        """Test applying stylesheet."""
        # test applying stylesheet
        _stylesheet = tmp_path / "test_stylesheet.qss"
        with open(_stylesheet, "w") as f:
            f.write("test")
        _widget = QtWidgets.QWidget()
        qtbot.addWidget(_widget)
        assert utils.apply_stylesheet(str(_stylesheet), _widget) == True
        assert utils.apply_stylesheet(str(tmp_path / "test_stylesheet.NA"), _widget) == False


class TestPySide6Compatibility:
    """Tests for PySide6.8.3 compatibility improvements.

    These tests verify that custom layout classes are now proper QWidget subclasses
    with correct parent-child relationships to prevent crashes during shutdown.
    """

    def test_collapsible_layout_is_qwidget(self, qtbot):
        """Test that CollapsibleLayout is a QWidget subclass."""
        from tik_manager4.ui.layouts.collapsible_layout import CollapsibleLayout
        assert issubclass(CollapsibleLayout, QtWidgets.QWidget)

        # Create instance and verify widget hierarchy
        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = CollapsibleLayout("Test", expanded=True, parent=parent)
        assert layout.parent() == parent
        assert isinstance(layout.frame, QtWidgets.QFrame)
        assert isinstance(layout.contents_widget, QtWidgets.QWidget)

    def test_tik_subproject_layout_is_qwidget(self, qtbot, main_object):
        """Test that TikSubProjectLayout is a QWidget subclass."""
        from tik_manager4.ui.mcv.subproject_mcv import TikSubProjectWidget
        assert issubclass(TikSubProjectWidget, QtWidgets.QWidget)

        # Create instance and verify widget hierarchy
        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = TikSubProjectWidget(main_object.project, parent=parent)
        assert layout.parent() == parent
        assert isinstance(layout.sub_view, QtWidgets.QTreeView)
        assert isinstance(layout.refresh_btn, QtWidgets.QPushButton)

    def test_tik_task_layout_is_qwidget(self, qtbot):
        """Test that TikTaskLayout is a QWidget subclass."""
        from tik_manager4.ui.mcv.task_mcv import TikTaskWidget
        assert issubclass(TikTaskWidget, QtWidgets.QWidget)

        # Create instance and verify widget hierarchy
        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = TikTaskWidget(parent=parent)
        assert layout.parent() == parent
        assert isinstance(layout.task_view, QtWidgets.QTreeView)
        assert isinstance(layout.refresh_btn, QtWidgets.QPushButton)

    def test_tik_category_layout_is_qwidget(self, qtbot):
        """Test that TikCategoryLayout is a QWidget subclass."""
        from tik_manager4.ui.mcv.category_mcv import TikCategoryWidget
        assert issubclass(TikCategoryWidget, QtWidgets.QWidget)

        # Create instance and verify widget hierarchy
        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = TikCategoryWidget(parent=parent)
        assert layout.parent() == parent
        assert isinstance(layout.work_tree_view, QtWidgets.QTreeView)
        assert isinstance(layout.refresh_btn, QtWidgets.QPushButton)

    def test_tik_version_layout_is_qwidget(self, qtbot, main_object):
        """Test that TikVersionLayout is a QWidget subclass."""
        from tik_manager4.ui.mcv.version_mcv import TikVersionWidget
        assert issubclass(TikVersionWidget, QtWidgets.QWidget)

        # Create instance and verify widget hierarchy
        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = TikVersionWidget(main_object.project, parent=parent)
        assert layout.parent() == parent

    def test_collapsible_layout_signal_connections(self, qtbot):
        """Test that CollapsibleLayout signal connections work correctly."""
        from tik_manager4.ui.layouts.collapsible_layout import CollapsibleLayout

        parent = QtWidgets.QWidget()
        qtbot.addWidget(parent)
        layout = CollapsibleLayout("Test", expanded=False, parent=parent)
        parent.show()

        # Verify initial state
        assert layout._expanded == False

        # Test toggle via button click
        with qtbot.waitSignal(layout.expand_toggled, timeout=1000):
            layout.expand_button.click()

        assert layout._expanded == True

        # Test toggle back
        with qtbot.waitSignal(layout.expand_toggled, timeout=1000):
            layout.expand_button.click()

        assert layout._expanded == False

    @pytest.fixture(scope='function')
    def main_object(self, tik, files):
        """Create a test project for compatibility tests."""
        project_path = Path(utils.get_home_dir(), "t4_pyside6_compat_test_DO_NOT_USE")
        if project_path.exists():
            files.force_remove_directory(project_path)
        tik.user.set("Admin", "1234")
        tik.create_project(str(project_path), structure_template="empty")
        return tik


