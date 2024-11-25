# FCFS Scheduling with Arrival Time

# Get the number of processes from the user
num_processes = int(input("Enter the number of processes: "))

# Initialize lists to store arrival and burst times
arrival_times = []
burst_times = []

# Get arrival and burst times for each process
for i in range(num_processes):
    arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
    burst_time = int(input(f"Enter burst time for process {i+1}: "))
    arrival_times.append(arrival_time)
    burst_times.append(burst_time)

# Sorting processes by arrival time
processes = list(zip(arrival_times, burst_times))
processes.sort()

# Initialize variables for calculating times
completion_times = [0] * num_processes
waiting_times = [0] * num_processes
turnaround_times = [0] * num_processes

# Calculate completion, turnaround, and waiting times
for i, (arrival, burst) in enumerate(processes):
    if i == 0:
        completion_times[i] = arrival + burst
    else:
        # Check if the CPU is idle
        if arrival > completion_times[i - 1]:
            completion_times[i] = arrival + burst
        else:
            completion_times[i] = completion_times[i - 1] + burst
    turnaround_times[i] = completion_times[i] - arrival
    waiting_times[i] = turnaround_times[i] - burst

# Calculate average turnaround time and waiting time
avg_turnaround_time = sum(turnaround_times) / num_processes
avg_waiting_time = sum(waiting_times) / num_processes

print(f"Average Turnaround Time: {avg_turnaround_time}")
print(f"Average Waiting Time: {avg_waiting_time}")
