# main.py
from concurrent.futures import ThreadPoolExecutor
from lens_sensor_simulator.Utilities import mymean_ignored_args

def main():
    """Entry point for the application.

    Creates a ThreadPoolExecutor with 5 workers and executes the `mymean_ignored_args` function 100 times.
    Prints the list of results to the console.
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(mymean_ignored_args, [None]*100))
        print(results)

if __name__ == "__main__":
    main()