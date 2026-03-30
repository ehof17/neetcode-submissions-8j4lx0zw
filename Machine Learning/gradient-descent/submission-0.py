class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimize = init
        for x in range(iterations):
            derivative = 2 * minimize
            minimize = minimize - learning_rate * derivative

        return round(minimize, 5)

    