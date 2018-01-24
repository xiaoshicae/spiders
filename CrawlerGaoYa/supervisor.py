# --*-- coding=utf-8 --*--
import sys
import time
import random
import logging
import importlib
from copy import deepcopy
from multiprocessing import Process


def supervise(target, arguments, process_num, process_check_frequency, log_name, tag):
    """
    arguments: tuple or list of args(ex: (arg1, arg2), [arg1, arg2])
    """
    if not isinstance(arguments, (tuple, list)):
        raise TypeError("Arguments is not a tuple or list")

    if (not isinstance(process_num, int)) or process_num < 0:
        raise TypeError("Process number must be positive integer")

    if process_check_frequency <= 0:
        raise ValueError("Process check frequency be positive")

    arguments = tuple(arguments)
    init_log(log_name)
    logger = logging.getLogger(log_name)
    processes = {}

    for i in range(process_num):
        process_name = 'Process_' + str(i + 1)
        p = Process(target=target, args=arguments)
        p.start()
        processes[process_name] = p
        logger.info('[%s]-[%s]-[%s] has been started' % (log_name, tag, process_name))

    while len(processes) > 0:
        time.sleep(process_check_frequency)

        process_list = deepcopy(list(processes.keys()))
        for process_name in process_list:
            p = processes[process_name]
            if p.exitcode is None:
                if not p.is_alive():
                    p_restart = Process(target=target, args=arguments)
                    p_restart.start()
                    processes[process_name] = p_restart
                    logger.error('[%s]-[%s]-[%s] aborted with exitcode None and has been restarted' % (
                        log_name, tag, process_name))
                else:
                    # logger.info('[%s] - [%s] running ok' % (log_name, process_name))
                    continue  # no error and loop continue

            elif p.exitcode == 0:
                logger.info('[%s]-[%s]-[%s] has been finished' % (log_name, tag, process_name))
                p.join()
                del processes[process_name]

            else:
                p_restart = Process(target=target, args=arguments)
                p_restart.start()
                processes[process_name] = p_restart
                logger.error(
                    '[%s]-[%s]-[%s] aborted with exitcode %s and has been restarted' % (
                        log_name, tag, process_name, p.exitcode))

    logger.info('All [%s] processes have been finished' % tag)


def supervisor(target, arguments=None, process_num=3, process_check_frequency=10, log_name='supervisor', tag='tag'):
    args = [target, arguments, process_num, process_check_frequency, log_name, tag]
    p = Process(target=supervise, args=args)
    p.start()


def test(test_arg):
    begin = time.time()
    while True:
        print(test_arg)
        time.sleep(random.randint(1, 20))
        current = time.time()
        if current - begin > 50:
            sys.exit(0)


def init_log(log_name):
    config = importlib.import_module('config')
    config.init_log(log_name)


if __name__ == '__main__':
    init_log('supervisor_test')
    supervise(test, ["zz"], 2, 10, 'supervisor_test')
