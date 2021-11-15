
from os import getlogin as getusername
import uuid
RESULT_COUNT = 5

# length of different elements in video list
TITLE_LENGTH = 40
DURATION_LENGTH = 6
CHANNEL_LENGTH = 15

TERMINAL = f'alacritty --class="YT#{str(uuid.uuid4()).split("-")[0]}"'

API_KEY_PATH = f"/home/{getusername()}/.config/apikeys/youtube"

API_KEY = "AIzaSyBx_QEW4FvK-HtKn_MDLO8y1q6X4sgXlQg"
