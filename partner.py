def calculate_new_hours(current_average, hours_streamed, new_viewers, new_average):
    # Solve for new hours
    new_hours = ((current_average * hours_streamed) - (new_average * hours_streamed)) / (new_average - new_viewers)
    
    return new_hours

# Example inputs
current_average = float(input("Enter current average viewers: "))
hours_streamed = float(input("Enter hours streamed so far: "))
new_viewers = float(input("Enter new viewers: "))
new_average = float(input("Enter target new average viewers: "))

new_hours = calculate_new_hours(current_average, hours_streamed, new_viewers, new_average)
print(f"Oats needs to stream {new_hours:.2f} more hours to reach the target average.")
