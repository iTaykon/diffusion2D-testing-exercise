"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # fixture
    w = 10.
    h = 5.
    dx = 0.1
    dy = 0.2
    d = 3.
    T_cold = 60.
    T_hot = 200.

    # expected result
    dt = pytest.approx(1/750, rel=1e-5)

    solver = SolveDiffusion2D()
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert solver.dt == dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # fixture
    h = 1.
    w = 1.
    T_cold = 40.
    T_hot = 100.
    d = 2.
    dx = 0.2
    dy = 0.2

    # expected result
    u_expected = np.array([[40., 40., 40., 40., 40.],
                            [40., 40., 40., 40., 40.],
                            [40., 40., 100., 100., 40.],
                            [40., 40., 100., 100., 40.],
                            [40., 40., 40., 40., 40.]])
    
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    u_actual = solver.set_initial_condition()

    assert np.allclose(u_actual, u_expected)
