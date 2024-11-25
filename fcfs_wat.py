# FCFS Scheduling without Arrival Time (all processes arrive at time 0)

# Get the number of processes from the user
num_processes = int(input("Enter the number of processes: "))

# Initialize a list to store burst times
burst_times = []

# Get burst times for each process
for i in range(num_processes):
    burst_time = int(input(f"Enter burst time for process {i+1}: "))
    burst_times.append(burst_time)

# Initialize variables for calculating times
waiting_times = [0] * num_processes
turnaround_times = [0] * num_processes

# Calculate waiting time for each process
for i in range(1, num_processes):
    waiting_times[i] = waiting_times[i - 1] + burst_times[i - 1]

# Calculate turnaround time for each process
for i in range(num_processes):
    turnaround_times[i] = waiting_times[i] + burst_times[i]

# Calculate average turnaround time and waiting time
avg_turnaround_time = sum(turnaround_times) / num_processes
avg_waiting_time = sum(waiting_times) / num_processes

print(f"Average Turnaround Time: {avg_turnaround_time}")
print(f"Average Waiting Time: {avg_waiting_time}")
