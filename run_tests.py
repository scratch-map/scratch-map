import os
import sys

import pytest


if __name__ == "__main__":
    os.environ['APP_SETTINGS'] = 'TestingConfig'
    exitcode = pytest.main()
    sys.exit(exitcode)
