import time

class IDWorker(object):
    def __init__(self, worker_id, data_center_id):
        self.worker_id = worker_id
        self.data_center_id = data_center_id

        # stats
        self.ids_generated = 0
        self.current_timestamp = 1318323746000

        self.sequence = 0L
        self.worker_id_bits = 5L
        self.data_center_id_bits = 5L
        self.max_worker_id = -1L ^ (-1L << self.worker_id_bits)
        self.max_data_center_id = -1L ^ (-1L << self.data_center_id_bits)
        self.sequence_bits = 12L

        self.worker_id_shift = self.sequence_bits #12
        self.data_center_id_shift = self.sequence_bits + self.worker_id_bits #5
        self.timestamp_left_shift = self.sequence_bits + self.worker_id_bits + self.data_center_id_bits
        self.sequence_mask = -1L ^ (-1L << self.sequence_bits) # 4095

        self.last_timestamp = -1L

    def _time_gen(self, timestamp=None):
        t = timestamp if timestamp else time.time()
        return long(int(t * 1000))

    def _till_next_millis(self, last_timestamp, timestamp=None):
        timestamp = self._time_gen(timestamp)
        while last_timestamp == timestamp:
            timestamp = self._time_gen(timestamp)
        return timestamp

    def _next_id(self, timestamp=None):
        timestamp = self._time_gen(timestamp)

        if self.last_timestamp > timestamp:
            raise 'invalid system lock'

        if self.last_timestamp == timestamp:
            self.sequence = (self.sequence + 1) & self.sequence_mask
            if self.sequence == 0:
                timestamp = self._till_next_millis(self.last_timestamp, timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = ((timestamp - self.current_timestamp) << self.timestamp_left_shift) | (self.data_center_id << self.data_center_id_shift) | (self.worker_id << self.worker_id_shift) | self.sequence
        return new_id

    def get_id(self, timestamp=None):
        new_id = self._next_id(timestamp)
        return new_id

if __name__ == '__main__':
    idworker = IDWorker(1, 1)
    print idworker.get_id()
    # for i in range(3):
    #     print idworker.get_id()