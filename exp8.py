def round_robin_scheduling():
    # Get number of processes
    n = int(input("Enter the number of processes: "))
    # Initialize process details
    processes = []
    for i in range(n):
        print(f"\nProcess {i+1}")
        arrival_time = int(input(f"Enter arrival time for P{i+1}: "))
        burst_time = int(input(f"Enter burst time for P{i+1}: "))
        processes.append({
            'pid': i+1,
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'remaining_time': burst_time,
            'completion_time': 0,
            'turnaround_time': 0,
            'waiting_time': 0
        })
    # Get time quantum
    time_quantum = int(input("\nEnter time quantum: "))
    # Initialize variables
    current_time = 0
    completed = 0
    queue = []
    time_chart = []
    # Continue until all processes are completed
    while completed != n:
        # Add newly arrived processes to queue
        for process in processes:
            if process['arrival_time'] <= current_time and process['remaining_time'] > 0:
                if process['pid'] not in [p['pid'] for p in queue]:
                    queue.append(process)
        if not queue:
            current_time += 1
            continue
        # Get current process from queue
        current_process = queue.pop(0)
        # Calculate execution time for this quantum
        execution_time = min(time_quantum, current_process['remaining_time'])
        # Update time chart
        time_chart.append({
            'pid': current_process['pid'],
            'start_time': current_time,
            'end_time': current_time + execution_time
        })
        # Update process times
        current_process['remaining_time'] -= execution_time
        current_time += execution_time
        # If process is completed
        if current_process['remaining_time'] == 0:
            completed += 1
            current_process['completion_time'] = current_time
            current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
            current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
        else:
            queue.append(current_process)
    # Print results
    print("\nProcess Execution Order:")
    print("Process | Start Time | End Time")
    print("-" * 35)
    for entry in time_chart:
        print(f"P{entry['pid']:6d} | {entry['start_time']:10d} | {entry['end_time']:8d}")
    print("\nProcess Details:")
    print("Process | Arrival | Burst | Completion | Turnaround | Waiting")
    print("-" * 65)
    for process in processes:
        print(f"P{process['pid']:6d} | {process['arrival_time']:7d} | {process['burst_time']:5d} | "
              f"{process['completion_time']:10d} | {process['turnaround_time']:10d} | {process['waiting_time']:7d}")
    # Calculate and print averages
    avg_turnaround = sum(p['turnaround_time'] for p in processes) / n
    avg_waiting = sum(p['waiting_time'] for p in processes) / n
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")
# Example usage
if __name__ == "__main__":
    print("Round Robin CPU Scheduling Algorithm")
    print("===================================")
    round_robin_scheduling()