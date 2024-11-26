import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.0f}s")
        return result
    return wrapper

def counter(lst, elem):
    count = 0
    for item in lst:
        if isinstance(item, list):  
            count += counter(item, elem)  
        elif item == elem:  
            count += 1
    return count

timer(counter)([1, 'a', 2, ['3', 1, 1], 5, [1, [1]]], 1)

