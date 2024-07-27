import logging

class ConversionData:
    def __init__(self: list, source: list, destination: list, origin: list, changed: list, cost: list):
        self.source = source
        self.destination = destination
        self.origin = origin
        self.changed = changed
        self.cost = cost


class ConversionExecutor:
    def __init__(self, conversion_data):
        self.conversion_data = conversion_data

    """ 
    Check input is a valid array and input is not empty
    """
    def _checkinput(self, inp: list, name="input"):
        msg = ""
        if not inp:
            msg = "Invalid {}. {} array must not be empty.".format(name, name)
        
        if msg != "":
            raise ValueError(msg)

    """
    Execute conversion logic
    """
    def execute(self) -> float:
        # validate input of source destination origin and changed are arrays
        try:
            for attrs in dir(self.conversion_data):
                if not attrs.startswith("__"):
                    self._checkinput(getattr(self.conversion_data, attrs), attrs)
        except ValueError as e:
            logging.error(repr(e))
            raise e

        logging.info("Conversion data: {}, {}, {}, {}, {}".format(self.conversion_data.source, self.conversion_data.destination, self.conversion_data.origin, self.conversion_data.changed, self.conversion_data.cost))
        # Example conversion logic
        result = self.conversion_data.origin[0] + self.conversion_data.changed[0]

        return result