from jinja2 import Template

from emergencies import Emergency
from utils.telegram import send_message
from config.custom import TELEGRAM_BOT_TOKEN, TELEGRAM_RECEIVERS, SEND_MESSAGE_MAX_RETRIES, CPU_CONFIG, RAM_CONFIG, DRIVE_TEMPERATURE_THRESHOLDS, DRIVE_CONFIG


def get_emergency_functions(threshold, metric, parameters=None):

    def check(data, **kwargs):
        return data[metric]['raw'] >= threshold['value']
    
    def action(data, **kwargs):

        if parameters is None:
            message = Template(threshold['message_template']).render(data=data)
        else:
            message = Template(threshold['message_template']).render(data=data, **parameters)

        success = False
        attempts = 0

        while not success and attempts < SEND_MESSAGE_MAX_RETRIES:
            success = send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_RECEIVERS, message)
            attempts += 1
    
    return {
        'check': check,
        'action': action
    }


def get_cpu_emergencies(metric):

    parameters = CPU_CONFIG[metric]['parameters'] if 'parameters' in CPU_CONFIG[metric] else None

    emergencies = []

    for threshold in CPU_CONFIG[metric]['thresholds']:
        emergencies.append(
            Emergency(
                f"{metric.title()} over {threshold['value']}",
                get_emergency_functions(threshold, metric, parameters)['check'], get_emergency_functions(threshold, metric, parameters)['action'],
                stop_if_occured=True, throttle_after_occurrence=59
            )
        )

    return emergencies


def get_ram_emergencies(metric):

    parameters = RAM_CONFIG[metric]['parameters'] if 'parameters' in RAM_CONFIG[metric] else None

    emergencies = []

    for threshold in RAM_CONFIG[metric]['thresholds']:
        emergencies.append(
            Emergency(
                f"Usage over {threshold['value']}",
                get_emergency_functions(threshold, metric, parameters)['check'], get_emergency_functions(threshold, metric, parameters)['action'],
                stop_if_occured=True, throttle_after_occurrence=59
            )
        )

    return emergencies


def get_drive_emergencies():

    emergencies = []

    for threshold in DRIVE_TEMPERATURE_THRESHOLDS:
        emergencies.append(
            Emergency(
                f"Temperature over {threshold['value']}",
                get_emergency_functions(threshold, 'temperature')['check'], get_emergency_functions(threshold, 'temperature')['action'],
                stop_if_occured=True, throttle_after_occurrence=59
            )
        )

    return emergencies
