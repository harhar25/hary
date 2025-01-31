import time

# Function to simulate FCFS Scheduling for food orders
def fcfs_food_orders(orders):
    print("\n Fast-Food Order Processing (FCFS) \n")
    
    current_time = 0  # Track the total cooking time
    completion_times = {}  # Store completion times of orders
    
    print(f"{'Order':<8}{'Customer':<10}{'Arrival':<12}{'Prep Time':<12}{'Start Time':<12}{'End Time':<12}")
    print("=" * 70)
    
    for order_id, customer, arrival_time, prep_time in orders:
        # Ensure the order starts at or after its arrival time
        start_time = max(current_time, arrival_time)
        end_time = start_time + prep_time  # When the order is completed
        
        print(f"{order_id:<8}{customer:<10}{arrival_time:<12}{prep_time:<12}{start_time:<12}{end_time:<12}")
        time.sleep(1)  # Simulating real-time processing
        
        completion_times[order_id] = end_time  # Store completion time
        current_time = end_time  # Move current time forward

    return completion_times


# Example Orders: (Order ID, Customer Name, Arrival Time, Preparation Time in minutes)
food_orders = [
    (101, "Alice", 0, 5),
    (102, "Bob", 2, 3),
    (103, "Charlie", 5, 8),
]

# Run the simulation
completion_times = fcfs_food_orders(food_orders)

# Display Final Completion Times
print("\n Final Order Completion Times ")
for order_id, completion_time in completion_times.items():
    print(f" Order {order_id} completed at {completion_time} minutes")

