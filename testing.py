# list_search.py - Using a Hashmap to find the indices of two numbers that add up to a target.

# 1. Setup the Problem
number_list = [4, 1, 9, 15, 7, 11]
target = 22 # We are looking for two numbers that add up to 22 (e.g., 7 + 15)
print("--- List and Target ---")
print(f"List: {number_list}")
print(f"Target: {target}")

# 2. The Hashmap (Dictionary)
# We use this hashmap to store numbers we have seen and their index (position) in the list.
# Structure: {number: index}
seen_numbers = {} 
print(f"Starting Hashmap: {seen_numbers}")

# 3. The Fast Search Loop
# We loop through the list exactly one time.
for current_index, current_number in enumerate(number_list):
    
    # Calculate the 'Complement' (The number we need to complete the pair)
    # Complement = Target - Current Number
    complement = target - current_number
    
    print(f"\nProcessing index {current_index} (Number: {current_number}).")
    print(f"Need Complement: {complement}")

    # The Hashmap Check (The O(1) step!)
    # We instantly check if the complement needed is already stored as a key in our hashmap.
    if complement in seen_numbers:
        
        # Success! We found the pair.
        # The index of the first number is stored in the hashmap (seen_numbers[complement]).
        # The index of the second number is the current_index.
        first_index = seen_numbers[complement]
        
        print("🎉 Match Found!")
        print(f"Target {target} is the sum of: {complement} (at index {first_index}) and {current_number} (at index {current_index}).")
        
        # We stop and print the result.
        break 
        
    else:
        # If the complement is NOT found, we add the current number to the hashmap
        # so it can be used as a complement for a future number.
        seen_numbers[current_number] = current_index
        print(f"Adding {current_number} (index {current_index}) to hashmap.")
        print(f"Current Hashmap: {seen_numbers}")