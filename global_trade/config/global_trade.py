from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Global Trade Settings",
                    "label": _("Global Trade Settings"),
                    "description": _("Global Trade Settings")
                }
            ]
        }
    ]