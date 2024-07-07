from monitors import Monitor
from emergencies import Emergency
from utils import Logger


MONITORS_STATUS_LOG_CONFIG = {
    Monitor.RUN: {
        'function': Logger.success,
        'message_template': "Monitor \"{{ monitor }}\" has been run."
    },
    Monitor.THROTTLED: {
        'function': Logger.warning,
        'message_template': "Monitor \"{{ monitor }}\" has been throttled."
    },
    Monitor.SKiPPED: {
        'function': Logger.info,
        'message_template': "Monitor \"{{ monitor }}\" has been skipped."
    }
}

EMERGENCIES_STATUS_LOG_CONFIG = {
    Emergency.OCCURED: {
        'function': Logger.error,
        'message_template': "Emergency \"{{ emergency }}\" has occurred."
    },
    Emergency.NOT_OCCURED: {
        'function': Logger.success,
        'message_template': "Emergency \"{{ emergency }}\" has not occurred."
    },
    Emergency.SKIPPED: {
        'function': Logger.info,
        'message_template': "Emergency \"{{ emergency }}\" has been skipped."
    },
    Emergency.SKIPPED_AFTER_OCCURRENCE: {
        'function': Logger.warning,
        'message_template': "Emergency \"{{ emergency }}\" has been skipped after occurrence."
    }
}
