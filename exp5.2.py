class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid          # Process ID
        self.arrival = arrival  # Arrival time
        self.burst = burst      # Burst time
        self.start_time = 0     # Time when process starts execution
        self.completion_time = 0 # Time when process completes execution
        self.waiting_time = 0   # Time process waits in ready queue
        self.turnaround_time = 0 # Total time from arrival to completion

def sort_by_arrival(processes):
    return sorted(processes, key=lambda x: (x.arrival, x.pid))

def fcfs_scheduling_with_arrival(processes):
    n = len(processes)
    current_time = 0
    
    # Process each job in order
    for process in processes:
        # If there's a gap between current time and process arrival
        if current_time < process.arrival:
            current_time = process.arrival
            
        # Record start time
        process.start_time = current_time
        
        # Update current time with burst duration
        current_time += process.burst
        
        # Calculate completion time
        process.completion_time = current_time
        
        # Calculate turnaround time (completion - arrival)
        process.turnaround_time = process.completion_time - process.arrival
        
        # Calculate waiting time (turnaround - burst)
        process.waiting_time = process.turnaround_time - process.burst

    # Calculate averages
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / n
    avg_waiting_time = sum(p.waiting_time for p in processes) / n
    
    # Display results with table formatting
    print("\nFCFS Scheduling Results:")
    print("=" * 65)
    print(f"{'Process':8} {'Arrival':8} {'Burst':8} {'Start':8} {'Finish':8} {'Wait':8} {'TAT':8}")
    print("-" * 65)
    
    for process in processes:
        print(f"P{process.pid:<7} {process.arrival:<8} {process.burst:<8} "
              f"{process.start_time:<8} {process.completion_time:<8} "
              f"{process.waiting_time:<8} {process.turnaround_time:<8}")
    
    print("=" * 65)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

def main():
    while True:
        try:
            n = int(input("\nEnter the number of processes: "))
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    processes = []
    
    # Input process details with validation
    for i in range(n):
        while True:
            try:
                print(f"\nFor Process P{i+1}:")
                arrival = int(input("Enter arrival time: "))
                if arrival < 0:
                    print("Arrival time cannot be negative.")
                    continue
                    
                burst = int(input("Enter burst time: "))
                if burst <= 0:
                    print("Burst time must be positive.")
                    continue
                    
                processes.append(Process(i+1, arrival, burst))
                break
            except ValueError:
                print("Please enter valid numbers.")
    
    # Sort processes by arrival time and PID
    processes = sort_by_arrival(processes)
    
    # Run FCFS Scheduling
    fcfs_scheduling_with_arrival(processes)

if __name__ == "__main__":
    main()
