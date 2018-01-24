import sys
import time
import copy
from app.Workers.Worker import Worker
from multiprocessing import Process


def main(name):
    worker = Worker(name)
    worker.run()

if __name__ == '__main__':
    processes = {}

    for i in range(5):
        worker_name = 'enterprise_work' + str(i+1)
        p = Process(target=main, args=(worker_name,))
        p.start()
        print(p.pid)
        processes[worker_name] = p

    while len(processes) > 0:
        task_list = copy.deepcopy(list(processes.keys()))
        # print(task_list)
        for task in task_list:
            p = processes[task]
            time.sleep(1)
            if p.exitcode is None:
                if not p.is_alive():
                    p_re = Process(target=main, args=(task,))
                    p_re.start()
                    processes[worker_name] = p_re
                    print('not alive restart', task, p_re.pid, p_re.name)
                else:
                    continue
                    # print(task, 'still alive...')

            elif p.exitcode == 0:
                print(task, 'finished', p.pid, p.exitcode, not p.is_alive)
                p.join()
                del processes[task]

            else:
                p_re = Process(target=main, args=(task,))
                p_re.start()
                processes[worker_name] = p_re
                print('err exit and restart', task, p_re.pid, p_re.name)





