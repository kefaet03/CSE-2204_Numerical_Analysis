# Lagrange Interpolation Formula Implementation

def lagrange_interpolation(x_values, y_values, x):
    """
    Function to calculate interpolated value using Lagrange Interpolation Formula.

    Parameters:
    x_values (list): Known x-coordinates.
    y_values (list): Known y-coordinates.
    x (float): Point at which interpolation is to be done.

    Returns:
    float: Interpolated value of y at the given x.
    """
    n = len(x_values)
    result = 0

    for i in range(n):
        # Calculate L_i(x) for i-th term
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


# Example Usage
x_points = [2, 2.5, 3]  # Known x values
y_points = [0.69315, 0.91629, 1.09861]  # Corresponding y values

x_to_interpolate = 2.7  # The x value where interpolation is needed
y_result = lagrange_interpolation(x_points, y_points, x_to_interpolate)

print(f"The interpolated value at x = {x_to_interpolate} is y = {y_result:.4f}")
