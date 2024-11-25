def lru_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0

    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)  # Remove least recently used (front of the list)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)  # Mark page as most recently used
        print(f"Current memory: {memory}")

    return page_faults

def fifo_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0

    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)  # Remove the first-in page
                memory.append(page)
        print(f"Current memory: {memory}")

    return page_faults

def optimal_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0

    for i in range(len(reference_string)):
        page = reference_string[i]
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                # Find the page to replace
                future_uses = []
                for m_page in memory:
                    if m_page in reference_string[i + 1:]:
                        future_uses.append(reference_string[i + 1:].index(m_page))
                    else:
                        future_uses.append(float('inf'))

                page_to_replace = future_uses.index(max(future_uses))
                memory[page_to_replace] = page
        print(f"Current memory: {memory}")

    return page_faults

def main():
    print("Page Replacement Policies: LRU, FIFO, Optimal")
    policy = input("Choose a policy (lru/fifo/optimal): ").strip().lower()
    frames = int(input("Enter the number of frames: "))
    reference_string = list(map(int, input("Enter the reference string (space-separated): ").split()))

    if policy == 'lru':
        page_faults = lru_page_replacement(frames, reference_string)
        print(f"Total page faults using LRU: {page_faults}")
    elif policy == 'fifo':
        page_faults = fifo_page_replacement(frames, reference_string)
        print(f"Total page faults using FIFO: {page_faults}")
    elif policy == 'optimal':
        page_faults = optimal_page_replacement(frames, reference_string)
        print(f"Total page faults using Optimal: {page_faults}")
    else:
        print("Invalid policy choice!")

if __name__ == "__main__":
    main()
