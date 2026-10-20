# Performance timing
from time import perf_counter
import httpx
from functools import wraps

def time_it(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f"Duration is {duration}")
        return result
    return wrapper

@time_it
def hello_world():
    print("hello")

# Retry
def retry(max_attempt, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempt:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"Attempt {attempt}/{max_attempt} failed: '{e}'. Retrying in {delay}s...")
                    sleep(delay)
        return wrapper
    return decorator

    
@retry(2)
@time_it
def fetch_data():
    response = httpx.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code:
        print(response.text)


fetch_data()