import pytest
import montyhallsim

def test_run_simulation1():
    """First test usage of the run_simulation() method."""
    with pytest.raises(Exception):
        montyhallsim.run_simulation(10)
