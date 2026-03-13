"""Configuration for pytest."""
import os
import stat
import shutil
from pathlib import Path
import pytest

@pytest.fixture(scope='function')
def tik(tmp_path):
    """Initialize tik_manager4 for testing."""
    print("\n")
    print("----------------------------")
    print("Preparing Mockup Common and User Folders...")
    print("----------------------------")
    mockup_commons_path = Path(tmp_path / "mockup_common")
    mockup_commons_path.mkdir(parents=True, exist_ok=True)
    original_home = os.environ.get("HOME")
    original_userprofile = os.environ.get("USERPROFILE")
    sandbox_home = tmp_path / "home"
    sandbox_home.mkdir(parents=True, exist_ok=True)
    os.environ["HOME"] = str(sandbox_home)
    os.environ["USERPROFILE"] = str(sandbox_home)
    user_path = sandbox_home / "TikManager4"
    user_path.mkdir(parents=True, exist_ok=True)
    import tik_manager4
    try:
        yield tik_manager4.initialize("Standalone", common_folder=str(mockup_commons_path))
    finally:
        if original_home is None:
            os.environ.pop("HOME", None)
        else:
            os.environ["HOME"] = original_home
        if original_userprofile is None:
            os.environ.pop("USERPROFILE", None)
        else:
            os.environ["USERPROFILE"] = original_userprofile


@pytest.fixture(scope='session', autouse=True)
def files():
    """Fixture to handle files."""
    return Files()


class Files:
    def _onerror_handler(self, func, path, exc_info):
        """
        Error handler for shutil.rmtree to handle read-only files.
        """

        # If the error is due to a permission error and the file is read-only
        if issubclass(exc_info[0], PermissionError):
            os.chmod(path, stat.S_IWRITE)  # Give write permission
            func(path)  # Retry the original function
        else:
            raise  # Re-raise the original exception if it's not a permission error

    def force_remove_directory(self, directory_path):
        """
        Forcefully remove a directory along with read-only files.
        """
        try:
            shutil.rmtree(str(directory_path), onerror=self._onerror_handler)
            print(f"Successfully removed {directory_path}.")
        except Exception as e:
            print(f"Error removing {directory_path}: {e}")
