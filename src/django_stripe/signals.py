# from django.dispatch import Signal
#
# webhook_signal = Signal()

# signals_registry.py

from django.dispatch import Signal


# Dictionary to hold all dynamically created signals
dynamic_signals = {}


def get_signal(event_type):
    if event_type not in dynamic_signals:
        dynamic_signals[event_type] = Signal()
    return dynamic_signals[event_type]
