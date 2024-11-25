import threading
import random
import time
from threading import Semaphore

class DiningPhilosophers:
    def __init__(self, number_of_philosophers):
        self.number_of_philosophers = number_of_philosophers
        self.forks = [Semaphore(1) for _ in range(number_of_philosophers)]
        self.dining_lock = Semaphore(number_of_philosophers - 1)  # Deadlock prevention
        self.philosopher_states = ['thinking'] * number_of_philosophers
        self.state_lock = threading.Lock()
        
    def print_state(self):
        """Print the current state of all philosophers"""
        with self.state_lock:
            states = ' | '.join(f'Philosopher {i}: {state}' 
                              for i, state in enumerate(self.philosopher_states))
            print(states)
            print('-' * 50)

    def get_forks(self, philosopher_id):
        """Try to acquire both forks for a philosopher"""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.number_of_philosophers
        
        self.dining_lock.acquire()  # Prevent deadlock
        
        self.forks[left_fork].acquire()
        print(f'Philosopher {philosopher_id} picked up left fork {left_fork}')
        
        self.forks[right_fork].acquire()
        print(f'Philosopher {philosopher_id} picked up right fork {right_fork}')
    
    def put_forks(self, philosopher_id):
        """Release both forks after eating"""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.number_of_philosophers
        
        self.forks[left_fork].release()
        print(f'Philosopher {philosopher_id} put down left fork {left_fork}')
        
        self.forks[right_fork].release()
        print(f'Philosopher {philosopher_id} put down right fork {right_fork}')
        
        self.dining_lock.release()
    
    def think(self, philosopher_id):
        """Philosopher thinks for a random amount of time"""
        with self.state_lock:
            self.philosopher_states[philosopher_id] = 'thinking'
        self.print_state()
        time.sleep(random.uniform(1, 3))
    
    def eat(self, philosopher_id):
        """Philosopher eats for a random amount of time"""
        with self.state_lock:
            self.philosopher_states[philosopher_id] = 'eating'
        self.print_state()
        time.sleep(random.uniform(1, 3))
    
    def philosopher(self, philosopher_id):
        """Simulate the lifecycle of a philosopher"""
        while True:
            self.think(philosopher_id)
            
            print(f'Philosopher {philosopher_id} is hungry')
            self.get_forks(philosopher_id)
            
            self.eat(philosopher_id)
            
            self.put_forks(philosopher_id)

def main():
    # Get user input
    num_philosophers = int(input("Enter the number of philosophers (minimum 3): "))
    if num_philosophers < 3:
        print("Number of philosophers must be at least 3")
        return
    
    simulation_time = float(input("Enter simulation time in seconds: "))
    
    # Create and start the simulation
    dining = DiningPhilosophers(num_philosophers)
    
    # Create and start philosopher threads
    philosophers = []
    for i in range(num_philosophers):
        philosopher = threading.Thread(target=dining.philosopher, args=(i,))
        philosopher.daemon = True  # Set as daemon thread
        philosophers.append(philosopher)
        philosopher.start()
    
    # Run simulation for specified time
    try:
        time.sleep(simulation_time)
        print("\nSimulation completed!")
    except KeyboardInterrupt:
        print("\nSimulation stopped by user!")

if __name__ == "__main__":
    main()