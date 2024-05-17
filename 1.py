import time

# Initialize variables
work_time = 50  # seconds
break_time = 10  # seconds
cycle_count = 0

# Infinite loop to run work-break cycles
while True:
    # Work time
    print(f"Work Time {cycle_count + 1}: {work_time} seconds")
    time.sleep(work_time)
    
    # Break time
    print(f"Break Time {cycle_count + 1}: {break_time} seconds")
    time.sleep(break_time)
    
    # Increment cycle count
    cycle_count += 1

    # Check if 50 cycles are completed
    if cycle_count == 50:
        break

# Calculate and print total work and break time
total_work_time = cycle_count * work_time
total_break_time = cycle_count * break_time
print(f"Total Work Time: {total_work_time} seconds")
print(f"Total Break Time: {total_break_time} seconds")
