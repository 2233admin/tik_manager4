"""Tests for UI translation helpers."""

import pytest

pytest.importorskip("PyQt5")

from tik_manager4.ui import i18n
from tik_manager4.ui.Qt import QtWidgets


def test_translate_text_lookup():
    """Chinese translations should resolve from the dictionary."""
    assert i18n.translate_text("File", language="zh_CN") == "文件"
    assert i18n.translate_text("Status | Ready", language="zh_CN") == "状态 | 就绪"
    assert i18n.translate_text("File", language="en") == "File"


def test_localize_widget_tree_round_trip(qtbot):
    """Widgets should translate to Chinese and back to English."""
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(widget)
    button = QtWidgets.QPushButton("&Save New Work")
    label = QtWidgets.QLabel("User Name:")

    layout.addWidget(button)
    layout.addWidget(label)
    qtbot.addWidget(widget)

    i18n.set_language("zh_CN")
    i18n.localize_widget_tree(widget)
    assert button.text() == "&保存新工作文件"
    assert label.text() == "用户名："

    i18n.set_language("en")
    i18n.localize_widget_tree(widget)
    assert button.text() == "&Save New Work"
    assert label.text() == "User Name:"


def test_combo_box_items_translate_only_when_opted_in(qtbot):
    """Combo items should translate only for opt-in display-only combos."""
    combo_box = QtWidgets.QComboBox()
    combo_box.addItems(["Observer", "Generic"])
    qtbot.addWidget(combo_box)

    i18n.set_language("zh_CN")
    i18n.localize_widget_tree(combo_box)
    assert combo_box.itemText(0) == "Observer"

    combo_box.setProperty("i18n_translate_items", True)
    i18n.localize_widget_tree(combo_box)
    assert combo_box.itemText(0) == "观察者"

    i18n.set_language("en")
    i18n.localize_widget_tree(combo_box)
    assert combo_box.itemText(0) == "Observer"
