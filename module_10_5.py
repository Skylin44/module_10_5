import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f'0:00:{(time.time() - start_time):.6f} (линейный)')

    # Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f'0:00:{(time.time() - start_time):.6f} (многопроцессный)')
