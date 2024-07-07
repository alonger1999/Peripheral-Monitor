from abc import ABC

from drivers import Driver
from emergencies import Emergency


class Monitor(ABC):

    RUN = 0
    SKiPPED = 1
    THROTTLED = 2

    def __init__(self, name: str, driver: Driver, emergencies: list[Emergency] = None, step: int = 1, **kwargs) -> None:

        self.__name = name

        self.__driver = driver

        self.__emergencies = [] if emergencies is None else emergencies

        self.__step = step

        self.kwargs = kwargs

        self.__counter = step

        self.__throttled_steps_left = 0

    def pre_check(self) -> None:
        pass

    def check(self) -> None:

        emergency_run_statuses = {}

        if self.__counter == self.__step:

            if self.__throttled_steps_left == 0:

                self.pre_check()
                
                data = self.__driver.get_data()

                for emergency in self.__emergencies:

                    emergency_run_status = emergency.run(data)

                    emergency_run_statuses[str(emergency)] = emergency_run_status

                    if emergency_run_status == Emergency.OCCURED:

                        throttle_after_occurrence = emergency.get_throttle_after_occurrence()

                        self.__throttled_steps_left = throttle_after_occurrence

                        if emergency.stop_if_occured() or throttle_after_occurrence:
                            break

                self.post_check()

                status = Monitor.RUN

            else:

                self.__throttled_steps_left -= 1

                status = Monitor.THROTTLED

            self.__counter = 1

        else:

            self.__counter += 1

            status = Monitor.SKiPPED

        return status, emergency_run_statuses

    def post_check(self) -> None:
        pass

    def __str__(self) -> str:
        return self.__name
