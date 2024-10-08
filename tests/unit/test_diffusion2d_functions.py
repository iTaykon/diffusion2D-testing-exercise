"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import unittest

class TestSolveDiffusion2D(unittest.TestCase):
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # fixture
        w=15.
        h=5.
        dx=0.2
        dy=0.05

        # expected result
        nx = 75
        ny = 100


        solver = SolveDiffusion2D()
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

        self.assertEqual(solver.w, w)
        self.assertEqual(solver.h, h)
        self.assertEqual(solver.dx, dx)
        self.assertEqual(solver.dy, dy)
        self.assertAlmostEqual(solver.nx, nx, places=5)
        self.assertAlmostEqual(solver.ny, ny, places=5)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # fixture
        d = 2.
        T_cold = 450.
        T_hot = 1000.
        dx = 0.1
        dy = 0.1

        # expected result
        dt = 0.00125

        solver = SolveDiffusion2D()
        solver.dx = dx
        solver.dy = dy
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

        self.assertEqual(solver.D, d)
        self.assertEqual(solver.T_cold, T_cold)
        self.assertEqual(solver.T_hot, T_hot)
        self.assertAlmostEqual(solver.dt, dt, places=5)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # fixture
        nx = 5
        ny = 5
        h = 1.
        w = 1.
        T_cold = 40.
        T_hot = 100.
        dx = 0.2
        dy = 0.2

        # expected result
        u_expected = np.array([[40., 40., 40., 40., 40.],
                                [40., 40., 40., 40., 40.],
                                [40., 40., 100., 100., 40.],
                                [40., 40., 100., 100., 40.],
                                [40., 40., 40., 40., 40.]])

        solver = SolveDiffusion2D()
        solver.nx = nx
        solver.ny = ny
        solver.h = h
        solver.w = w
        solver.T_cold = T_cold
        solver.T_hot = T_hot
        solver.dx = dx
        solver.dy = dy
        u_actual = solver.set_initial_condition()

        assert np.allclose(u_actual, u_expected)