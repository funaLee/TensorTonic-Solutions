def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps):
        dx = (2* x0 * a) + b
        x0 -= lr * dx

    return x0