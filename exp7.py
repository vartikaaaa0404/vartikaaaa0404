class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
def priority_scheduling(processes):
    # Sort processes based on priority (lower number means higher priority)
    processes.sort(key=lambda x: x.priority)
    # Calculate waiting time and turnaround time
    current_time = 0
    for process in processes:
        process.waiting_time = current_time
        process.turnaround_time = current_time + process.burst_time
        current_time += process.burst_time
    # Calculate averages
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    return avg_waiting_time, avg_turnaround_time
def main():
    # Get number of processes from user
    n = int(input("Enter the number of processes: "))
    processes = []
    # Get process details from user
    for i in range(n):
        print(f"\nProcess {i+1}")
        burst_time = int(input(f"Enter burst time for Process {i+1}: "))
        priority = int(input(f"Enter priority for Process {i+1} (lower number means higher priority): "))
        processes.append(Process(i+1, burst_time, priority))
    # Run priority scheduling algorithm
    avg_waiting_time, avg_turnaround_time = priority_scheduling(processes)
    # Display results
    print("\nProcess Execution Order:")
    print("Process ID\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    print("-" * 75)
    for process in processes:
        print(f"P{process.pid}\t\t{process.priority}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
if __name__ == "__main__":
    main()