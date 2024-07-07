class Emergency:

    OCCURED = 0
    NOT_OCCURED = 1
    SKIPPED = 2
    SKIPPED_AFTER_OCCURRENCE = 3

    def __init__(
            self, name: str, check: callable, action: callable,
            step: int = 1, stop_if_occured: bool = False, skip_after_occurrence: int = 0, throttle_after_occurrence: int = 0,
            **kwargs
        ) -> None:

        self.__name = name

        self.__check = check
        self.__action = action

        self.__step = step

        self.__stop_if_occured = stop_if_occured

        self.__skip_after_occurrence = skip_after_occurrence
        self.__throttle_after_occurrence = throttle_after_occurrence

        self.__counter = step

        self.__steps_after_occurrence_left = 0

        self.__kwargs = kwargs

    def run(self, data: dict) -> None:

        if self.__counter == self.__step:

            if self.__steps_after_occurrence_left == 0:

                if self.__check(data, **self.__kwargs):

                    self.__action(data, **self.__kwargs)

                    self.__steps_after_occurrence_left = self.__skip_after_occurrence

                    status = Emergency.OCCURED

                else:
                    status = Emergency.NOT_OCCURED

            else:

                self.__steps_after_occurrence_left -= 1

                status = Emergency.SKIPPED_AFTER_OCCURRENCE

            self.__counter = 1

        else:

            self.__counter += 1

            status = Emergency.SKIPPED

        return status
    
    def stop_if_occured(self):
        return self.__stop_if_occured

    def get_throttle_after_occurrence(self) -> int:
        return self.__throttle_after_occurrence

    def __str__(self) -> str:
        return self.__name
