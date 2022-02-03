from datetime import datetime


def profiler(f):
    """
        Time spent by function f
    """
    def inner_f(*args, **kwrgs):
        start_time = datetime.now()
        result = f(*args, **kwrgs)
        end_time = datetime.now()
        run_time = end_time - start_time
        print("-" * 40)
        print(f"Time spent by {f.__name__}: {run_time}")
        print("-" * 40)
        return result

    return inner_f