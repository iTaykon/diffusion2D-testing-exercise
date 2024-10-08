# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/RSE-102/Lecture-Material/blob/main/04_testing/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

======================================= test session starts ========================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/pillerls/Documents/courses/2024_RSE102/diffusion2D-testing-exercise
collected 5 items                                                                                  

tests/integration/test_diffusion2d.py ..                                                     [ 40%]
tests/unit/test_diffusion2d_functions.py ...                                                 [100%]

======================================== 5 passed in 0.42s =========================================

### unittest log

tests/unit/test_diffusion2d_functions.py
Fdt = 0.0025000000000000005
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestSolveDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/pillerls/Documents/courses/2024_RSE102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 32, in test_initialize_domain
    self.assertAlmostEqual(solver.nx, nx, places=5)
AssertionError: 25 != 75 within 5 places (50 difference)

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestSolveDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/pillerls/Documents/courses/2024_RSE102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 58, in test_initialize_physical_parameters
    self.assertAlmostEqual(solver.dt, dt, places=5)
AssertionError: 0.0025000000000000005 != 0.00125 within 5 places (0.0012500000000000005 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestSolveDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/pillerls/Documents/courses/2024_RSE102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 93, in test_set_initial_condition
    assert np.allclose(u_actual, u_expected)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
