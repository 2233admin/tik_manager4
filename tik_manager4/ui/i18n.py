"""Lightweight runtime UI translation helpers."""

from __future__ import annotations

from tik_manager4.ui.Qt import QtCore, QtWidgets

DEFAULT_LANGUAGE = "en"
SIMPLIFIED_CHINESE = "zh_CN"

SUPPORTED_LANGUAGES = {
    DEFAULT_LANGUAGE: "English",
    SIMPLIFIED_CHINESE: "简体中文",
}

_LANGUAGE = DEFAULT_LANGUAGE
_FILTER = None
_COMBO_ITEM_SOURCE_ROLE = (
    QtCore.Qt.UserRole if hasattr(QtCore.Qt, "UserRole") else 32
) + 2048

TRANSLATIONS = {
    SIMPLIFIED_CHINESE: {
        "Info": "信息",
        "Question": "问题",
        "Warning": "警告",
        "Error": "错误",
        "Confirmation": "确认",
        "OK": "确定",
        "Cancel": "取消",
        "Yes": "是",
        "No": "否",
        "Save": "保存",
        "Open": "打开",
        "Close": "关闭",
        "Continue": "继续",
        "Discard": "放弃",
        "Apply": "应用",
        "Reset": "重置",
        "Restore Defaults": "恢复默认值",
        "Help": "帮助",
        "Save All": "全部保存",
        "Ignore": "忽略",
        "Abort": "中止",
        "Retry": "重试",
        "File": "文件",
        "UI Elements": "界面元素",
        "Purgatory": "回收站",
        "Language": "语言",
        "English": "English",
        "Simplified Chinese": "简体中文",
        "Create New Project": "创建新项目",
        "Set Project": "设置项目",
        "Set Project Template": "设置项目模板",
        "Add New User": "新增用户",
        "Save File as Work": "将文件保存为工作文件",
        "Save Folder as Work": "将文件夹保存为工作文件",
        "Export Selection as Work": "导出选中内容为工作文件",
        "Save New Work": "保存新工作文件",
        "Create Work From Template": "从模板创建工作文件",
        "Work from Template": "从模板创建工作文件",
        "Increment Version": "递增版本",
        "Ingest Version": "导入版本",
        "Publish Scene": "发布场景",
        "Publish Snapshot": "发布快照",
        "Load Item": "加载项目",
        "Import Item": "导入项目",
        "Settings": "设置",
        "User": "用户",
        "User Settings": "用户设置",
        "Change Password": "修改密码",
        "Change User Password": "修改用户密码",
        "Localization": "本地缓存",
        "Executables": "可执行程序",
        "Apply": "应用",
        "User Login": "用户登录",
        "Exit": "退出",
        "Project": "项目",
        "Buttons": "按钮",
        "Purge Local Purgatory": "清理本地回收站",
        "Purge Project Purgatory": "清理项目回收站",
        "Show Deleted Items": "显示已删除项目",
        "Issues & Feature Requests": "问题与功能请求",
        "Online Documentation": "在线文档",
        "Check for Updates": "检查更新",
        "Support Tik Manager": "支持 Tik Manager",
        "Status | Ready": "状态 | 就绪",
        "Create New User": "创建新用户",
        "Set Project": "设置项目",
        "Cannot set project": "无法设置项目",
        "No project selected.\nPlease select a project from                 the folders or bookmarks and press 'Set'": "未选择项目。\n请从文件夹或书签中选择一个项目，然后点击“设置”。",
        "Look in:": "当前位置：",
        "Recent": "最近",
        "Recent projects": "最近项目",
        "Filter": "筛选",
        "Create New Project": "创建新项目",
        "Root Properties": "根属性",
        "Projects Root :": "项目根目录：",
        "Root for the projects": "项目根目录",
        "Project Name :": "项目名称：",
        "Name of the Project": "项目名称",
        "Template :": "模板：",
        "Set Project Template": "设置项目模板",
        "Edit Subproject": "编辑子项目",
        "Main Properties": "主要属性",
        "Inherited Properties": "继承属性",
        "New Properties": "新属性",
        "New Subproject": "新建子项目",
        "Name :": "名称：",
        "Name": "名称",
        "Parent :": "父级：",
        "Parent": "父级",
        "Old Password :": "旧密码：",
        "New Password :": "新密码：",
        "New Password Again :": "再次输入新密码：",
        "Change user password of {user}": "修改 {user} 的用户密码",
        "Common Folder :": "公共目录：",
        "User Templates Directory :": "用户模板目录：",
        "Alembic Viewer :": "Alembic 查看器：",
        "USD Viewer :": "USD 查看器：",
        "FBX Viewer :": "FBX 查看器：",
        "Image Viewer :": "图片查看器：",
        "Sequence Viewer :": "序列查看器：",
        "Video Viewer :": "视频查看器：",
        "Enabled": "启用",
        "Local Cache Folder": "本地缓存目录",
        "Cache Work Files": "缓存工作文件",
        "Cache Publish Files": "缓存发布文件",
        "The folder where the common data for all projects is stored.": "存放所有项目公共数据的目录。",
        "The folder where all user template files stored for all Dccs. Supports flags.": "存放所有 DCC 用户模板文件的目录，支持附加参数。",
        "The path to the Alembic Viewer executable. Supports flags.": "Alembic 查看器可执行文件路径，支持附加参数。",
        "The path to the USD Viewer executable. Supports flags.": "USD 查看器可执行文件路径，支持附加参数。",
        "The path to the FBX Viewer executable. Supports flags.": "FBX 查看器可执行文件路径，支持附加参数。",
        "The path to the Image Viewer executable. Supports flags.": "图片查看器可执行文件路径，支持附加参数。",
        "The path to the Sequence Viewer executable. Supports flags.": "序列查看器可执行文件路径，支持附加参数。",
        "The path to the Video Player executable. Supports flags.": "视频播放器可执行文件路径，支持附加参数。",
        "Local folder to store cache files.": "用于存放缓存文件的本地目录。",
        "If enabled, work files will be stored in the cache folder and won't be accessible for other users until its synced.": "启用后，工作文件会先保存到缓存目录，在同步前其他用户无法访问。",
        "If enabled, publish files will be stored in the cache folder and won't be accessible for other users until its synced.": "启用后，发布文件会先保存到缓存目录，在同步前其他用户无法访问。",
        "User Name:": "用户名：",
        "Initials :": "缩写：",
        "Email :": "邮箱：",
        "Permission Level :": "权限级别：",
        "Password :": "密码：",
        "Password Again :": "再次输入密码：",
        "User :": "用户：",
        "Remember :": "记住登录：",
        "If checked, remember this user until logout": "勾选后将记住该用户，直到注销",
        "Login": "登录",
        "Observer": "观察者",
        "Generic": "普通用户",
        "Experienced": "高级用户",
        "Admin": "管理员",
        "User Creation Error": "用户创建错误",
        "Paswords not matching": "密码不匹配",
        "Passwords entered don't match": "两次输入的密码不一致",
        "Type the confirmation word to proceed:": "请输入确认词后继续：",
        "Type confirmation word here": "在此输入确认词",
        "Please type the project name to confirm.": "请输入项目名称以确认。",
        "New Work": "新建工作文件",
        "Create New Work File": "创建新的工作文件",
        "Path cannot be resolved": "无法解析路径",
        "Name cannot be resolved": "无法解析名称",
        "Invalid name": "名称无效",
        "Notes:": "备注：",
        "Notes: ": "备注：",
        "Create Work": "创建工作文件",
        "Sub-project": "子项目",
        "Task": "任务",
        "Category": "分类",
        "Label": "标签",
        "(Optional)": "（可选）",
        "Path of the sub-project": "子项目路径",
        "Name of the Task": "任务名称",
        "Category of the work file": "工作文件分类",
        "Name of the work file that will be added as a label tag.": "工作文件名称，会作为标签写入。",
        "File Format": "文件格式",
        "File format of the work file": "工作文件的文件格式",
        "New Version": "新建版本",
        "Create New Version": "创建新版本",
        "Could not create version. Check the script editor for details.": "无法创建版本，请检查脚本编辑器了解详情。",
        "Create Work From Template": "从模板创建工作文件",
        "Template": "模板",
        "Template file to create the work from": "用于创建工作文件的模板文件",
        "Save Any File or Folder": "保存任意文件或文件夹",
        "Saving: {path}": "正在保存：{path}",
        "Direct Publish": "直接发布",
        "If checked, the file will be published directly.": "勾选后将直接发布该文件。",
        "Publish File": "发布文件",
        "DCC override": "DCC 覆盖",
        "DCC to use for the work file": "此工作文件使用的 DCC",
        "Name of the work file": "工作文件名称",
        "Export Selection as Work": "导出选择为工作文件",
        "Purge Failed": "清理失败",
        "Local Purgatory Purged": "本地回收站已清理",
        "Project Purgatory Purged": "项目回收站已清理",
        "The project name does not match. Purge failed.": "项目名称不匹配，清理失败。",
        "Are you sure you want to purge the local purgatory?": "确定要清理本地回收站吗？",
        "Are you sure you want to purge the project purgatory?": "确定要清理项目回收站吗？",
        "Connecting to {platform}...": "正在连接到 {platform}...",
        "Authentication Failed": "认证失败",
        "Authentication failed while connecting to {platform}\n\n{message}": "连接到 {platform} 时认证失败\n\n{message}",
        "Connected to {platform} successfully.": "已成功连接到 {platform}。",
        "Restart Required": "需要重启",
        "Changing the common folder requires a restart of the application.": "更改公共目录需要重启应用程序。",
        "Set Commons Directory": "设置公共目录",
        "Commons Directory is not defined. Press Continue to select Commons Directory": "未定义公共目录。点击继续以选择公共目录。",
        "Commons Directory does not exist": "公共目录不存在",
        "Defined Commons Directory does not exist. \n{path}Do you want to define a new Commons Directory?": "已配置的公共目录不存在。\n{path}\n是否要重新设置公共目录？",
        "Commons Directory is not valid": "公共目录无效",
        "Commons Directory doesn't contain all of the necessary files and it is write protected.\nDo you want to define a new Commons Directory?": "公共目录缺少必要文件，且当前为只读状态。\n是否要重新设置公共目录？",
        "Language switched to {language}.": "界面语言已切换为 {language}。",
    }
}


def normalize_language(language):
    """Normalize language identifiers to supported values."""
    if not language:
        return DEFAULT_LANGUAGE
    normalized = str(language).replace("-", "_")
    lowered = normalized.lower()
    if lowered.startswith("zh"):
        return SIMPLIFIED_CHINESE
    return DEFAULT_LANGUAGE


def get_language():
    """Return the active UI language."""
    return _LANGUAGE


def set_language(language):
    """Set the active UI language."""
    global _LANGUAGE
    _LANGUAGE = normalize_language(language)
    return _LANGUAGE


def get_language_name(language=None):
    """Return the display name for a language."""
    return SUPPORTED_LANGUAGES.get(normalize_language(language or _LANGUAGE), "English")


def _clean_text(text):
    """Strip Qt accelerator markers and padding for dictionary lookup."""
    if text is None:
        return ""
    cleaned = str(text).replace("&&", "__AMP__").replace("&", "")
    cleaned = cleaned.replace("__AMP__", "&").rstrip()
    return cleaned


def translate_text(text, language=None, **kwargs):
    """Translate text using the active language dictionary."""
    if text is None:
        return None
    source = str(text)
    lang = normalize_language(language or _LANGUAGE)
    if lang == DEFAULT_LANGUAGE:
        translated = source
    else:
        translation_map = TRANSLATIONS.get(lang, {})
        translated = translation_map.get(source)
        if translated is None:
            translated = translation_map.get(_clean_text(source), source)
        if source.startswith("&") and not translated.startswith("&"):
            translated = f"&{translated}"
        trailing_spaces = len(source) - len(source.rstrip(" "))
        if trailing_spaces and not translated.endswith(" " * trailing_spaces):
            translated = translated.rstrip() + (" " * trailing_spaces)
    if kwargs:
        return translated.format(**kwargs)
    return translated


def _property_name(attr_name):
    return f"_i18n_source_{attr_name}"


def _remember_source(obj, attr_name, current_value):
    property_name = _property_name(attr_name)
    source_value = obj.property(property_name)
    if source_value is None:
        obj.setProperty(property_name, current_value)
        return current_value
    return source_value


def _translate_accessor(obj, getter_name, setter_name, attr_name):
    getter = getattr(obj, getter_name, None)
    setter = getattr(obj, setter_name, None)
    if not getter or not setter:
        return
    try:
        current_value = getter()
    except TypeError:
        return
    if not isinstance(current_value, str) or not current_value:
        return
    source_value = _remember_source(obj, attr_name, current_value)
    setter(translate_text(source_value))


def _translate_tab_widget(tab_widget):
    for index in range(tab_widget.count()):
        source_text = tab_widget.tabBar().tabData(index)
        if source_text is None:
            source_text = tab_widget.tabText(index)
            tab_widget.tabBar().setTabData(index, source_text)
        tab_widget.setTabText(index, translate_text(source_text))


def _translate_combo_items(combo_box):
    if not combo_box.property("i18n_translate_items"):
        return
    for index in range(combo_box.count()):
        source_text = combo_box.itemData(index, _COMBO_ITEM_SOURCE_ROLE)
        if source_text is None:
            source_text = combo_box.itemText(index)
            combo_box.setItemData(index, source_text, _COMBO_ITEM_SOURCE_ROLE)
        combo_box.setItemText(index, translate_text(source_text))


def localize_action(action):
    """Translate a QAction in-place."""
    _translate_accessor(action, "text", "setText", "text")
    _translate_accessor(action, "toolTip", "setToolTip", "toolTip")
    _translate_accessor(action, "statusTip", "setStatusTip", "statusTip")


def localize_widget(widget):
    """Translate a single widget in-place."""
    if widget is None:
        return

    for getter_name, setter_name, attr_name in (
        ("windowTitle", "setWindowTitle", "windowTitle"),
        ("text", "setText", "text"),
        ("title", "setTitle", "title"),
        ("placeholderText", "setPlaceholderText", "placeholderText"),
        ("toolTip", "setToolTip", "toolTip"),
        ("statusTip", "setStatusTip", "statusTip"),
        ("whatsThis", "setWhatsThis", "whatsThis"),
    ):
        _translate_accessor(widget, getter_name, setter_name, attr_name)

    if isinstance(widget, QtWidgets.QComboBox):
        _translate_combo_items(widget)
    if isinstance(widget, QtWidgets.QTabWidget):
        _translate_tab_widget(widget)

    for action in widget.actions():
        localize_action(action)


def localize_widget_tree(root):
    """Translate a widget and all of its children."""
    if root is None:
        return
    localize_widget(root)
    for child in root.findChildren(QtWidgets.QWidget):
        localize_widget(child)


class _UiTranslationFilter(QtCore.QObject):
    """Translate widgets lazily as they are shown."""

    def eventFilter(self, obj, event):  # pylint: disable=invalid-name
        if isinstance(obj, QtWidgets.QWidget):
            if event.type() in (QtCore.QEvent.Show, QtCore.QEvent.Polish):
                localize_widget_tree(obj)
        return super().eventFilter(obj, event)


def ensure_translator(app=None):
    """Install the UI translation event filter once."""
    global _FILTER
    app = app or QtWidgets.QApplication.instance()
    if not app or _FILTER:
        return _FILTER
    _FILTER = _UiTranslationFilter(app)
    app.installEventFilter(_FILTER)
    return _FILTER
