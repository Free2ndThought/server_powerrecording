import time
from collections import deque
from math import ceil

# If we perform a RabbitMQ Transaction for *every* sample, we overload the Disk I/O.
# samples_per_second = 7 Hz * nr_of_plugs
# We merge the individual samples into a list, and generate the list in timely regularly spaced repetitions


# We compress the json, therefore limiting the size of the messages is not really needed anymore
# Periodically run this function
def round_robin_pooling_size_limited(q_list):
    pool_deq = deque()  # deque instead of list for O(1) append

    #  if all allnet-queues are sufficently filled, 
    #  we still want to limit the rabbitMQ-message size to 100kB
    #  100kB is a good message size for RabbitMQ. 1 Message = 324 Bytes
    #  https://www.rabbitmq.com/blog/2012/04/25/rabbitmq-performance-measurements-part-2/
    n_iter = ceil(100*1024/324 / len(q_list))

    for i in range(n_iter):
        if all((q.empty() for q in q_list)):
            print("All Allnet Queues are empty")
            break
        else:
            samples = [q.get() for q in q_list if not q.empty()]
            [pool_deq.append(sample) for sample in samples]
        if i == n_iter-1:
            print("Warning Allnet-Queues are not yet emptied and round_robin_pooling_stopped") 

    return pool_deq


def round_robin_pooling(q_list):
    batch = []
    while any((not q.empty() for q in q_list)):
        samples = [q.get() for q in q_list if not q.empty()]
        batch.extend(samples)
    return batch


def blocking_delay_generator(T=1.0):
    """This generator tries to proceed at a regular time intervall T.
    If the generator's consumer is slower than T, the generator immediately proceeds.
    The generator yields the timepoints in unixtime at which the generator proceeds.
    The blocking iteration ensures that round_robin_pooling() is executed sequentially
    instead of async-concurrently"""
    next_call = time.time()
    while True:
        yield time.time()
        next_call = next_call + T
        sleep_length = next_call - time.time()
        if sleep_length > 0:
            time.sleep(sleep_length)


# unused
#def periodically_run(f=lambda : print(time.time()), T=1.0, *args, **kwargs):
#    next_call = time.time()
#    while True:
#        f(*args, **kwargs)
#        next_call = next_call + T
#        time.sleep(next_call - time.time())
#
#timerThread = threading.Thread(target=periodically_run, 
#                               kwargs={'f':round_robin_pooling, 'T':1.0, 'q_list':[]}, 
#                               daemon=True)
#timerThread.start()


if __name__ == "__main__":
    from AllnetPoll import AllnetPoll
    from local_config import SETUP_NR, DEVICE_LIST
    from queue import SimpleQueue

    devices = ["BLADL_0%d_0%02d" % (SETUP_NR, i) for i in DEVICE_LIST[SETUP_NR]]
    assert len(devices)
    q_list = [SimpleQueue() for device in devices]
    thread_list = [AllnetPoll(dev, q) for dev, q in zip(devices, q_list)]
    [thread.start() for thread in thread_list]

    for timestamp in blocking_delay_generator(10):
        x = round_robin_pooling(q_list)
        print(timestamp, '\t', len(x))
