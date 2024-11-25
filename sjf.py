class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

# Function to perform SJF scheduling (non-preemptive)
def sjf_scheduling(processes):
    n = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    gantt_chart = []
    completed_processes = 0
    visited = [False] * n

    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)
    
    while completed_processes < n:
        # Get all processes that have arrived up to current time and are not completed
        available_processes = [p for p in processes if p.arrival_time <= current_time and not visited[processes.index(p)]]

        if available_processes:
            # Select process with the shortest burst time
            next_process = min(available_processes, key=lambda p: p.burst_time)
            idx = processes.index(next_process)
            visited[idx] = True

            # Update completion, turnaround, and waiting times
            next_process.completion_time = current_time + next_process.burst_time
            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.burst_time

            # Update total waiting and turnaround times
            total_waiting_time += next_process.waiting_time
            total_turnaround_time += next_process.turnaround_time

            # Add to Gantt chart
            gantt_chart.append((next_process.pid, current_time, next_process.completion_time))
            current_time = next_process.completion_time

            # Increment completed process count
            completed_processes += 1
        else:
            # If no process is available, increment time (CPU idle)
            current_time += 1

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return gantt_chart, avg_waiting_time, avg_turnaround_time

def main():
    # User input for process IDs, burst times, and arrival times
    process_ids = list(map(int, input("Enter process IDs as space-separated values: ").split()))
    burst_times = list(map(int, input("Enter burst times as space-separated values: ").split()))
    arrival_times = list(map(int, input("Enter arrival times as space-separated values: ").split()))
    
    n = len(process_ids)
    processes = [Process(process_ids[i], burst_times[i], arrival_times[i]) for i in range(n)]

    # Perform SJF scheduling
    gantt_chart, avg_waiting_time, avg_turnaround_time = sjf_scheduling(processes)

    # Output Gantt Chart
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: Start time = {entry[1]}, End time = {entry[2]}")

    # Output average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

if __name__ == "__main__":
    main()