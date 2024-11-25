import threading
import time
from threading import Semaphore, Lock
class ReaderWriter:
    def __init__(self):
        self.read_count = 0
        self.read_count_lock = Lock()
        self.resource_lock = Semaphore(1)  # Controls access to the resource
        self.shared_resource = 0  # The shared resource/data
    def reader(self, reader_id):
        while True:
            # Entry section
            self.read_count_lock.acquire()
            self.read_count += 1
            if self.read_count == 1:  # First reader
                self.resource_lock.acquire()  # Lock the resource for writers
            self.read_count_lock.release()
            # Critical section (reading)
            print(f"Reader {reader_id} is reading. Shared Resource = {self.shared_resource}")
            time.sleep(1)  # Simulate reading
            # Exit section
            self.read_count_lock.acquire()
            self.read_count -= 1
            if self.read_count == 0:  # Last reader
                self.resource_lock.release()  # Release for writers
            self.read_count_lock.release()
            time.sleep(0.1)  # Reader takes a break
    def writer(self, writer_id):
        while True:
            # Entry section
            self.resource_lock.acquire()
            # Critical section (writing)
            self.shared_resource += 1
            print(f"Writer {writer_id} is writing. Updated Shared Resource = {self.shared_resource}")
            time.sleep(1)  # Simulate writing
            # Exit section
            self.resource_lock.release()
            time.sleep(0.1)  # Writer takes a break
def main():
    # Get user input
    num_readers = int(input("Enter the number of readers: "))
    num_writers = int(input("Enter the number of writers: "))
    # Create ReaderWriter instance
    rw = ReaderWriter()
    # Create and start reader threads
    reader_threads = []
    for i in range(num_readers):
        reader_thread = threading.Thread(target=rw.reader, args=(i+1,))
        reader_thread.daemon = True  # Set as daemon thread so it exits when main program exits
        reader_threads.append(reader_thread)
        reader_thread.start()
    # Create and start writer threads
    writer_threads = []
    for i in range(num_writers):
        writer_thread = threading.Thread(target=rw.writer, args=(i+1,))
        writer_thread.daemon = True  # Set as daemon thread so it exits when main program exits
        writer_threads.append(writer_thread)
        writer_thread.start()
    # Let the simulation run for a specified time
    try:
        time.sleep(float(input("Enter simulation time in seconds: ")))
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")
if __name__ == "__main__":
    main()