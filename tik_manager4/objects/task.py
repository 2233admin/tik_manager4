import os
from glob import glob
from tik_manager4.core.settings import Settings
from tik_manager4.objects.entity import Entity


class Task(Settings, Entity):
    def __init__(self, absolute_path,
                 name=None,
                 category=None,
                 path=None
                 ):
        super(Task, self).__init__()
        self.settings_file = absolute_path

        self._name = self.get_property("name") or name
        self._creator = self.get_property("creator") or self._guard.user
        self._category = self.get_property("category") or category
        # self._dcc = self.get_property("dcc") or self._guard.dcc
        self._works = []
        self._publishes = []
        self._task_id = self.get_property("task_id") or self.id
        self._relative_path = self.get_property("path") or path


    def scan_works(self, all_dcc=False):
        """
        Scan the task for all work objects.
        Args:
            all_dcc: (bool) If True, scans for all dcc versions

        Returns:

        """
        self._works.clear()

        # override the all_dcc flag if its standalone
        if self._guard.dcc == "Standalone":
            all_dcc = True

        if not all_dcc:
            _search_dir = self.get_abs_database_path(self._guard.dcc)  # this is DCC specific directory
            _work_paths = glob(os.path.join(_search_dir, '{0}.twork'.format(self.name)))
        else:
            _search_dir = self.get_abs_database_path()
            _work_paths = [y for x in os.walk(_search_dir) for y in glob(os.path.join(x[0], '{0}.twork'.format(self.name)))]
        print(_search_dir)
        print("***")
        print("***")
        print("***")
        print("***")
        print(_work_paths)
        print("***")
        print("***")
        print("***")
        print("***")
        # for b_path in _base_scene_paths:
        #     self._versions.append(Task(b_path))

    def scan_publishes(self, all_dcc=False):
        """
        Scan the task for publishes.
        Args:
            all_dcc:

        Returns: (bool) If True
        """
        self._publishes.clear()

        # override the all_dcc flag if its standalone
        if self._guard.dcc == "Standalone":
            all_dcc = True

        if not all_dcc:
            _search_dir = self.get_abs_database_path(self._guard.dcc)
            _work_paths = glob(os.path.join(_search_dir, '{0}.tpub'.format(self.name)))
        else:
            _search_dir = self.get_abs_database_path()
            _work_paths = [y for x in os.walk(_search_dir) for y in glob(os.path.join(x[0], '{0}.tpub'.format(self.name)))]


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val
        self.add_property("name", val)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, val):
        self._creator = val
        self.add_property("creator", val)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        self._category = val
        self.add_property("category", val)

    # @property
    # def path(self):
    #     return self._path

    # @path.setter
    # def path(self, val):
    #     self._path = val
    #     self.add_property("path", val)

    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, val):
        self._works = val
        self.add_property("versions", val)

    @property
    def publishes(self):
        return self._publishes

    @publishes.setter
    def publishes(self, val):
        self._publishes = val
        self.add_property("publishes", val)

    @property
    def reference_id(self):
        return self._task_id

    @reference_id.setter
    def reference_id(self, val):
        self.reference_id = val
        self.add_property("referenceID", val)
