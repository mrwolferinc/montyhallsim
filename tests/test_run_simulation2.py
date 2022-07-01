import pytest
import montyhallsim

def test_run_simulation2():
    """Second test usage of the run_simulation() method."""
    with pytest.raises(Exception):
        montyhallsim.run_simulation(15, False)
