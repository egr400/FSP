# import example.py, the file we created at the start
# import example_cy

# example.test(5)

import timeit

# cy = timeit.timeit('program_broken_cy', setup='import program_broken_cy', number=100)
py = timeit.timeit('program_break', setup='import program_break', number=100)
py_1 = timeit.timeit('program', setup='import program', number=100)


# print(cy, py)
print(py, py_1)
# print('Cython is {} times faster'.format(py/cy))
print('Speed is {} times faster'.format(py_1/ py))