class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time  # For SRTF

def non_preemptive_sjf(processes):
    """
    Implementation of non-preemptive Shortest Job First scheduling
    """
    n = len(processes)
    completed_processes = []
    current_time = 0
    remaining_processes = processes.copy()
    
    print("\nNon-Preemptive SJF Scheduling:")
    print("=" * 70)
    
    while remaining_processes:
        # Get available processes at current time
        available_processes = [p for p in remaining_processes 
                             if p.arrival_time <= current_time]
        
        if not available_processes:
            # No process available, move time to next arrival
            current_time = min(p.arrival_time for p in remaining_processes)
            continue
        
        # Select process with shortest burst time
        next_process = min(available_processes, 
                         key=lambda p: (p.burst_time, p.arrival_time))
        
        # Update process times
        next_process.start_time = current_time
        current_time += next_process.burst_time
        next_process.completion_time = current_time
        next_process.turnaround_time = (next_process.completion_time - 
                                      next_process.arrival_time)
        next_process.waiting_time = (next_process.turnaround_time - 
                                   next_process.burst_time)
        
        # Move process to completed list
        completed_processes.append(next_process)
        remaining_processes.remove(next_process)
    
    display_results(completed_processes, "Non-Preemptive SJF")

def preemptive_sjf(processes):
    """
    Implementation of preemptive Shortest Job First scheduling (SRTF)
    """
    n = len(processes)
    completed_processes = []
    current_time = 0
    remaining_processes = [Process(p.pid, p.arrival_time, p.burst_time) 
                         for p in processes]
    
    print("\nPreemptive SJF (SRTF) Scheduling:")
    print("=" * 70)
    
    gantt_chart = []
    prev_process = None
    
    while len(completed_processes) < n:
        # Get available processes at current time
        available_processes = [p for p in remaining_processes 
                             if p.arrival_time <= current_time]
        
        if not available_processes:
            # No process available, move time to next arrival
            current_time = min(p.arrival_time for p in remaining_processes)
            continue
        
        # Select process with shortest remaining time
        current_process = min(available_processes, 
                            key=lambda p: (p.remaining_time, p.arrival_time))
        
        # Record for Gantt chart if process changes
        if prev_process != current_process:
            gantt_chart.append((current_time, current_process.pid))
            if not hasattr(current_process, 'first_start'):
                current_process.first_start = current_time
            prev_process = current_process
        
        # Execute for 1 time unit
        current_process.remaining_time -= 1
        current_time += 1
        
        # Check if process is completed
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            current_process.turnaround_time = (current_process.completion_time - 
                                             current_process.arrival_time)
            current_process.waiting_time = (current_process.turnaround_time - 
                                          current_process.burst_time)
            current_process.start_time = current_process.first_start
            completed_processes.append(current_process)
            remaining_processes.remove(current_process)
            prev_process = None
    
    # Print Gantt chart
    print("\nGantt Chart:")
    print("-" * 50)
    for i in range(len(gantt_chart)):
        if i < len(gantt_chart) - 1:
            print(f"|P{gantt_chart[i][1]} ({gantt_chart[i][0]}-{gantt_chart[i+1][0]})", end="")
        else:
            print(f"|P{gantt_chart[i][1]} ({gantt_chart[i][0]}-{current_time})|")
    print("-" * 50)
    
    display_results(completed_processes, "Preemptive SJF (SRTF)")

def display_results(processes, algorithm_name):
    """
    Display scheduling results in a formatted table
    """
    print(f"\n{algorithm_name} Results:")
    print("=" * 75)
    print(f"{'Process':8} {'Arrival':8} {'Burst':8} {'Start':8} {'Finish':8} {'Wait':8} {'TAT':8}")
    print("-" * 75)
    
    total_waiting = 0
    total_turnaround = 0
    
    for process in sorted(processes, key=lambda p: p.pid):
        print(f"P{process.pid:<7} {process.arrival_time:<8} {process.burst_time:<8} "
              f"{process.start_time:<8} {process.completion_time:<8} "
              f"{process.waiting_time:<8} {process.turnaround_time:<8}")
        total_waiting += process.waiting_time
        total_turnaround += process.turnaround_time
    
    n = len(processes)
    print("=" * 75)
    print(f"\nAverage Waiting Time: {total_waiting/n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround/n:.2f}")

def main():
    # Get number of processes
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
    
    # Input process details
    for i in range(n):
        while True:
            try:
                print(f"\nFor Process P{i+1}:")
                arrival_time = int(input("Enter arrival time: "))
                if arrival_time < 0:
                    print("Arrival time cannot be negative.")
                    continue
                    
                burst_time = int(input("Enter burst time: "))
                if burst_time <= 0:
                    print("Burst time must be positive.")
                    continue
                
                processes.append(Process(i+1, arrival_time, burst_time))
                break
            except ValueError:
                print("Please enter valid numbers.")
    
    # Run both scheduling algorithms
    non_preemptive_sjf(processes)
    preemptive_sjf(processes)

if __name__ == "__main__":
    main()