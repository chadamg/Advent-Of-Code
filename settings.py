try:
  from settings_local import *
except ImportError:
  SESSION_COOKIE = "YOUR-SESSION-COOKIE-HERE"