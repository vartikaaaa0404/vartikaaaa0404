# Structure to represent a process
class Process:
    def __init__(self, pid, burst):
        self.pid = pid       # Process ID
        self.burst = burst   # Burst time

def fcfs_scheduling(n, processes):
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # FCFS Scheduling without Arrival Time
    for i in range(n):
        waiting_time[i] = current_time  # Process starts as soon as the previous one finishes
        current_time += processes[i].burst  # Update current_time based on burst time
        turnaround_time[i] = waiting_time[i] + processes[i].burst

    # Calculate sum of waiting and turnaround times
    sum_waiting_time = sum(waiting_time)
    sum_turnaround_time = sum(turnaround_time)

    # Calculate averages
    avg_waiting_time = sum_waiting_time / n
    avg_turnaround_time = sum_turnaround_time / n

    # Display results
    print("\nProcess\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"P{processes[i].pid}\t{processes[i].burst}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Turnaround Time = {avg_turnaround_time}")
    print(f"Average Waiting Time = {avg_waiting_time}")

if __name__ == "__main__":
    # Input number of processes
    n = int(input("Enter the number of processes: "))
    processes = []

    # Input burst time for each process
    for i in range(n):
        burst = int(input(f"Enter the burst time for process {i+1}: "))
        processes.append(Process(i+1, burst))

    # Run FCFS Scheduling
    fcfs_scheduling(n, processes)
