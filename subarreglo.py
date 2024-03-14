def encontrar_sublista_suma_mayor(lista):
    largest_sum = float('-inf')  # Initializes the largest sum with negative infinity.
    start_sublist = 0  # Index of the start of the sublist with the largest sum.
    end_sublist = 0  # Index of the end of the sublist with the largest sum.
    current_sum = 0  # Current sum of the sublist under consideration.
    best_sublist_start = 0  # Index of the start of the best sublist found so far.

    for i, number in enumerate(lista):  # Iterates through the list of numbers.
        current_sum += number  # Adds the current number to the current sum.

        if current_sum > largest_sum:  # Compares the current sum with the largest sum.
            largest_sum = current_sum
            start_sublist = best_sublist_start  # Updates the start of the sublist.
            end_sublist = i

        if current_sum < 0:  # Resets the current sum if it becomes negative.
            current_sum = 0
            best_sublist_start = i + 1

    return lista[start_sublist:end_sublist + 1]  # Returns the sublist with the largest sum.

