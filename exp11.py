class BankersAlgorithm:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        
        # Initialize data structures
        self.available = []
        self.maximum = []
        self.allocation = []
        self.need = []
        self.process_sequence = []
    
    def input_data(self):
        """Get all necessary input from user"""
        # Get available resources
        print("\nEnter the available resources:")
        self.available = list(map(int, input().split()))
        
        # Get maximum resource need for each process
        print("\nEnter the maximum resource need for each process:")
        print("(Enter values for each resource type separated by space)")
        for i in range(self.num_processes):
            print(f"For Process {i}:")
            self.maximum.append(list(map(int, input().split())))
        
        # Get current resource allocation for each process
        print("\nEnter the current resource allocation for each process:")
        print("(Enter values for each resource type separated by space)")
        for i in range(self.num_processes):
            print(f"For Process {i}:")
            self.allocation.append(list(map(int, input().split())))
        
        # Calculate need matrix
        self.calculate_need()
    
    def calculate_need(self):
        """Calculate the need matrix"""
        self.need = []
        for i in range(self.num_processes):
            process_need = []
            for j in range(self.num_resources):
                process_need.append(self.maximum[i][j] - self.allocation[i][j])
            self.need.append(process_need)
    
    def is_safe_state(self):
        """Check if the system is in safe state and find safe sequence"""
        # Initialize work and finish arrays
        work = self.available.copy()
        finish = [False] * self.num_processes
        self.process_sequence = []
        
        while True:
            # Find a process that can be executed
            found = False
            for i in range(self.num_processes):
                if not finish[i] and self.can_allocate(i, work):
                    # Process can be executed
                    found = True
                    finish[i] = True
                    self.process_sequence.append(i)
                    
                    # Add allocated resources back to work
                    for j in range(self.num_resources):
                        work[j] += self.allocation[i][j]
                    break
            
            if not found:
                # No process can be executed
                break
        
        # Check if all processes are finished
        return all(finish)
    
    def can_allocate(self, process_id, work):
        """Check if resources can be allocated to a process"""
        for j in range(self.num_resources):
            if self.need[process_id][j] > work[j]:
                return False
        return True
    
    def request_resources(self, process_id, request):
        """Handle resource request from a process"""
        # Check if request is valid
        for i in range(self.num_resources):
            if request[i] > self.need[process_id][i]:
                return False, "Error: Request exceeds maximum need"
            if request[i] > self.available[i]:
                return False, "Error: Resources not available"
        
        # Try to allocate resources
        # Save current state
        old_available = self.available.copy()
        old_allocation = [row[:] for row in self.allocation]
        old_need = [row[:] for row in self.need]
        
        # Allocate resources temporarily
        for i in range(self.num_resources):
            self.available[i] -= request[i]
            self.allocation[process_id][i] += request[i]
            self.need[process_id][i] -= request[i]
        
        # Check if resulting state is safe
        if self.is_safe_state():
            return True, "Resources allocated successfully"
        else:
            # Restore old state
            self.available = old_available
            self.allocation = old_allocation
            self.need = old_need
            return False, "Error: Resource allocation would lead to unsafe state"
    
    def print_state(self):
        """Print current state of the system"""
        print("\nCurrent System State:")
        print("\nAvailable Resources:", self.available)
        
        print("\nMaximum Resource Need:")
        for i in range(self.num_processes):
            print(f"Process {i}:", self.maximum[i])
        
        print("\nCurrent Resource Allocation:")
        for i in range(self.num_processes):
            print(f"Process {i}:", self.allocation[i])
        
        print("\nRemaining Resource Need:")
        for i in range(self.num_processes):
            print(f"Process {i}:", self.need[i])

def main():
    print("Banker's Algorithm for Deadlock Avoidance")
    print("----------------------------------------")
    
    # Get number of processes and resources
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resource types: "))
    
    # Create Banker's Algorithm instance
    banker = BankersAlgorithm(num_processes, num_resources)
    
    # Get initial state
    banker.input_data()
    
    while True:
        print("\nOptions:")
        print("1. Check system safety")
        print("2. Request resources")
        print("3. Print current state")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            if banker.is_safe_state():
                print("\nSystem is in safe state!")
                print("Safe sequence is:", ' → '.join(map(str, banker.process_sequence)))
            else:
                print("\nSystem is in unsafe state!")
        
        elif choice == '2':
            process_id = int(input("\nEnter process ID requesting resources: "))
            print("Enter resource request (space-separated values):")
            request = list(map(int, input().split()))
            
            success, message = banker.request_resources(process_id, request)
            print("\n" + message)
        
        elif choice == '3':
            banker.print_state()
        
        elif choice == '4':
            print("\nExiting program...")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()