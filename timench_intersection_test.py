import random
from timench import Timench

# Setup
a3 = [v for v in range(0, 3)]
b3 = [v for v in range(0, 3)]
a1000 = [v for v in range(0, 1000)]
b1000 = [v for v in range(0, 1000)]
ar3 = [random.randint(0, 3) for _ in range(0, 3)]
br3 = [random.randint(0, 3) for _ in range(0, 3)]
ar1000 = [random.randint(0, 1000) for _ in range(0, 1000)]
br1000 = [random.randint(0, 1000) for _ in range(0, 1000)]

tmnch = Timench()
repeats = 100


def get_intersection(a, b):
    a = set(a)
    b = set(b)
    c = sorted(list(a&b))
    return c

def get_list_difference(a, b):
    l = []
    for i in a:
        if i in b:
            l.append(i)
    return l

# Benchmark
funcs_dict = {
    get_intersection.__name__ + '_3': get_intersection,
    get_list_difference.__name__ + '_3': get_list_difference,
    get_intersection.__name__ + '_1000': get_intersection,
    get_list_difference.__name__ + '_1000': get_list_difference,
    get_intersection.__name__ + '_random3': get_intersection,
    get_list_difference.__name__ + '_random3': get_list_difference,
    get_intersection.__name__ + '_random1000': get_intersection,
    get_list_difference.__name__ + '_random1000': get_list_difference,
}
env_args = {  # dict structure: {case_name: [args, kwargs] of function func(*args, **kwargs), }
    get_intersection.__name__ + '_3': [[a3, b3], None],
    get_list_difference.__name__ + '_3': [[a3, b3], None],
    get_intersection.__name__ + '_1000': [[a1000, b1000], None],
    get_list_difference.__name__ + '_1000': [[a1000, b1000], None],
    get_intersection.__name__ + '_random3': [[ar3, br3], None],
    get_list_difference.__name__ + '_random3': [[ar3, br3], None],
    get_intersection.__name__ + '_random1000': [[ar1000, br1000], None],
    get_list_difference.__name__ + '_random1000': [[ar1000, br1000], None],
}

for case_name in funcs_dict:  # # Add functions to benchmark list
    tmnch.add_func(case_name, funcs_dict[case_name])

tmnch.multiple_run(repeats, env_args)  # Run multiple benchmarks

for case_name in env_args:
    print(tmnch.get_report(case_name))  # Print to terminal all reports

#tmnch.write_reports('example_6_report.txt')  # Write all reports to txt-file

"""
Case: get_intersection_3
---
Function: get_intersection
Total time = 0.000258142 sec
Best loop time = 2.257e-06 sec
Average loop time = 2.58142e-06 sec
Repeats = 100

Case: get_list_difference_3
---
Function: get_list_difference
Total time = 0.000146501 sec
Best loop time = 1.44e-06 sec
Average loop time = 1.46501e-06 sec
Repeats = 100

Case: get_intersection_1000
---
Function: get_intersection
Total time = 0.0201919 sec
Best loop time = 0.00017029 sec
Average loop time = 0.000201919 sec
Repeats = 100

Case: get_list_difference_1000
---
Function: get_list_difference
Total time = 1.75355 sec
Best loop time = 0.0138173 sec
Average loop time = 0.0175355 sec
Repeats = 100

Case: get_intersection_random3
---
Function: get_intersection
Total time = 0.000226242 sec
Best loop time = 2.164e-06 sec
Average loop time = 2.26242e-06 sec
Repeats = 100

Case: get_list_difference_random3
---
Function: get_list_difference
Total time = 0.000126137 sec
Best loop time = 1.245e-06 sec
Average loop time = 1.26137e-06 sec
Repeats = 100

Case: get_intersection_random1000
---
Function: get_intersection
Total time = 0.0189411 sec
Best loop time = 0.00017441 sec
Average loop time = 0.000189411 sec
Repeats = 100

Case: get_list_difference_random1000
---
Function: get_list_difference
Total time = 2.21987 sec
Best loop time = 0.0198208 sec
Average loop time = 0.0221987 sec
Repeats = 100


Process finished with exit code 0

"""