"""Const for the Alarmdotcom integration."""
from __future__ import annotations

from homeassistant.const import CONF_PIN
from pyalarmdotcomajax.devices import Sensor as pyadcSensor

INTEGRATION_NAME = "Alarm.com"
DOMAIN = "alarmdotcom"
ISSUE_URL = ""
STARTUP_MESSAGE = f"""
===================================================================
{DOMAIN}
This is a custom component
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
===================================================================
"""

STATE_MALFUNCTION = "Malfunction"

DEBUG_REQ_EVENT = "alarmdotcom_debug_request"

MIGRATE_MSG_ALERT = (
    "The Alarm.com integration is now configured exclusively via Home Assistant's"
    " integrations page. Please delete the Alarm.com entry from configuration.yaml."
    " Your existing settings have already been migrated."
)

# #
# CONFIGURATION
# #

# Configuration
CONF_USERNAME = "username"
CONF_PASSWORD = "password"  # nosec
CONF_2FA_COOKIE = "2fa_cookie"
CONF_OTP = "otp"

CONF_UPDATE_INTERVAL = "update_interval"
CONF_ARM_HOME = "arm_home_options"
CONF_ARM_AWAY = "arm_away_options"
CONF_ARM_NIGHT = "arm_night_options"

CONF_UPDATE_INTERVAL_DEFAULT = 30
CONF_ARM_MODE_OPTIONS = {
    "bypass": "Force Bypass",
    "silent": "Arm Silently",
    "delay": "Arming Delay",
}

CONF_OPTIONS_DEFAULT = {
    CONF_PIN: "",
    CONF_ARM_HOME: ["bypass"],
    CONF_ARM_AWAY: ["bypass", "delay"],
    CONF_ARM_NIGHT: ["bypass"],
    CONF_UPDATE_INTERVAL: CONF_UPDATE_INTERVAL_DEFAULT,
}

SENSOR_SUBTYPE_BLACKLIST = [
    pyadcSensor.Subtype.MOBILE_PHONE,  # No purpose
    pyadcSensor.Subtype.PANEL_IMAGE_SENSOR,  # No support yet
]
