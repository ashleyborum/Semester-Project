import re
from typing import (TextIO, Iterator, List, Tuple)


def parse_raw_temps(original_temps: TextIO, step_size: int = 30) -> Iterator[Tuple[float, List[float]]]:
    """
    Take an input file and time-step size and parse all core temps.

    Per T.K.:
    Args:
        original_temps: an input file
        step_size: time-step in seconds
    Yields:
        A tuple containing the next time step and a List containing _n_ core
        temps as floating point values (where _n_ is the number of CPU cores)
    """

    split_re = re.compile(r"[^0-9]*\s+|[^0-9]*$")

    for step, line in enumerate(original_temps):
        yield (step * step_size), \
              [float(entry) for entry in split_re.split(line) if len(entry) > 0]