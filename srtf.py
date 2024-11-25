class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time  # Remaining time for SRTF
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

# Function to perform SRTF scheduling (preemptive)
def srtf_scheduling(processes):
    n = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    completed_processes = 0
    gantt_chart = []

    # To track the current shortest remaining time process
    ready_queue = []
    processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time

    while completed_processes < n:
        # Add all processes that have arrived by the current time to the ready queue
        for process in processes:
            if process.arrival_time <= current_time and process not in ready_queue and process.remaining_time > 0:
                ready_queue.append(process)

        if ready_queue:
            # Select the process with the shortest remaining burst time
            ready_queue.sort(key=lambda p: p.remaining_time)
            current_process = ready_queue[0]

            # Execute the current process for 1 unit of time
            current_process.remaining_time -= 1
            gantt_chart.append((current_process.pid, current_time, current_time + 1))

            # If the current process finishes, update its completion and turnaround times
            if current_process.remaining_time == 0:
                current_process.completion_time = current_time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                total_waiting_time += current_process.waiting_time
                total_turnaround_time += current_process.turnaround_time
                completed_processes += 1
                ready_queue.remove(current_process)

        current_time += 1  # Increment the current time after each unit of execution

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

    # Perform SRTF scheduling
    gantt_chart, avg_waiting_time, avg_turnaround_time = srtf_scheduling(processes)

    # Output Gantt Chart
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: Start time = {entry[1]}, End time = {entry[2]}")

    # Output average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

if __name__ == "__main__":
    main()