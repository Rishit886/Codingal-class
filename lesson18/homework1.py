def process_number_range(start, end):
    # Find the square values of numbers in the given range (inclusive of 'end')
    squares = [n ** 2 for n in range(start, end + 1)]
    
    # Filter odd and even square values
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    # Print the results
    print(f"Original Range: {start} to {end}")
    print(f"Square Values: {squares}")
    print(f"Even Square Values: {even_squares}")
    print(f"Odd Square Values: {odd_squares}")

# Example usage:
process_number_range(1, 5)

