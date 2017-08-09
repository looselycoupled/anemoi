
# fix working directory when testing objects that have relative paths from root
import os
os.chdir(os.path.join(os.getcwd(), '..'))

import logging
logging.disable(logging.CRITICAL)
