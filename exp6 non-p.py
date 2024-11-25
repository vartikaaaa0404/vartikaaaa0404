# Function to calculate average waiting time and turnaround time using Non-preemptive SJF
def sjf_non_preemptive(n, processes):
    # Sort processes by burst time first (secondary) and arrival time (primary)
    processes.sort(key=lambda x: (x[1], x[2]))
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0

    for i in range(n):
        pid, arrival, burst = processes[i]

        if current_time < arrival:
            current_time = arrival  # CPU is idle until the process arrives

        waiting_time[i] = current_time - arrival
        current_time += burst
        turnaround_time[i] = waiting_time[i] + burst

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

# Input
n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    arrival = int(input(f"Enter arrival time for process {i+1}: "))
    burst = int(input(f"Enter burst time for process {i+1}: "))
    processes.append((i+1, arrival, burst))

# Calculate using Non-preemptive SJF
waiting_time, turnaround_time, avg_wt, avg_tat = sjf_non_preemptive(n, processes)

print("\nNon-preemptive SJF Scheduling:")
print("Process\tArrival\tBurst\tWaiting\tTurnaround")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_time[i]}\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")