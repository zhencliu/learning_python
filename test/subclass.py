#!/usr/bin/env python3


class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

class UnknownEvent(Event):
    """A type of event that cannot be identified from its data"""
    pass

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )

class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data
    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)


from abc import ABC


class CVMRes(ABC):
    def __init__(self):
        self.id = None

    def to_specs(self):
        pass


class SEVCommRes(CVMRes):
    def __init__(self):
        super().__init__()
        self.cbitpos = None
        self.phys_reduced_bit = None
        self.sev_dev = '/dev/sev'

    def to_specs(self):
        pass

class SEVRes(SEVCommRes):
    def __init__(self):
        super().__init__()
        pass

    def to_specs(self):
        pass


class SNPRes(SEVCommRes):
    def __init__(self):
        super().__init__()
        pass

    def to_specs(self):
        pass


class TDXRes(CVMRes):
    def __init__(self):
        super().__init__()
        pass

    def to_specs(self):
        pass

class LaunchSecurity(object):
    @staticmethod
    def run():
        for cls in CVMResMgr.__subclasses__():
            if cls.meet_conditions():
                return cls


if __name__ == '__main__':
    obj = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print(obj.identify_event().__class__.__name__)
    CVMResGenerator.gen()
    obj = CVMRes()

