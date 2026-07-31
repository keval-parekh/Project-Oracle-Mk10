import numpy as np
import pytest


@pytest.fixture
def rgb_frame():
    rng = np.random.default_rng(0)
    return (rng.random((32, 32, 3)) * 255).astype(np.uint8)
