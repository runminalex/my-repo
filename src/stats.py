"""Statistics module with descriptive statistical operations."""

import math
from collections import Counter
from typing import Sequence


class Statistics:
    """A class providing descriptive statistical operations on data sets."""

    def mean(self, data: Sequence[float]) -> float:
        """Return the arithmetic mean of the data set.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute mean of an empty data set")
        return sum(data) / len(data)

    def median(self, data: Sequence[float]) -> float:
        """Return the median value of the data set.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute median of an empty data set")

        sorted_data = sorted(data)
        n = len(sorted_data)

        if n % 2 == 1:
            return float(sorted_data[n // 2])
        else:
            mid_left = sorted_data[n // 2 - 1]
            mid_right = sorted_data[n // 2]
            return (mid_left + mid_right) / 2.0

    def mode(self, data: Sequence[float]) -> list[float]:
        """Return the mode(s) of the data set (most frequent value(s)).

        If multiple values have the same highest frequency, all are returned.
        Returns an empty list if the data set is empty.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute mode of an empty data set")

        counter = Counter(data)
        max_count = max(counter.values())

        return sorted([value for value, count in counter.items() if count == max_count])

    def variance(self, data: Sequence[float], ddof: int = 0) -> float:
        """Return the variance of the data set.

        Args:
            data: The data set.
            ddof: Delta degrees of freedom. Use 0 for population variance,
                  use 1 for sample variance.

        Raises:
            ValueError: If the data set has fewer elements than ddof + 1.
        """
        n = len(data)
        if n <= ddof:
            raise ValueError(
                f"Cannot compute variance with ddof={ddof} on a data set of size {n}"
            )

        μ = self.mean(data)
        return sum((x - μ) ** 2 for x in data) / (n - ddof)

    def standard_deviation(self, data: Sequence[float], ddof: int = 0) -> float:
        """Return the standard deviation of the data set.

        Args:
            data: The data set.
            ddof: Delta degrees of freedom. Use 0 for population std,
                  use 1 for sample std.

        Raises:
            ValueError: If the data set has fewer elements than ddof + 1.
        """
        return math.sqrt(self.variance(data, ddof=ddof))

    def min(self, data: Sequence[float]) -> float:
        """Return the minimum value of the data set.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute min of an empty data set")
        return float(min(data))

    def max(self, data: Sequence[float]) -> float:
        """Return the maximum value of the data set.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute max of an empty data set")
        return float(max(data))

    def range(self, data: Sequence[float]) -> float:
        """Return the range (max - min) of the data set.

        Raises:
            ValueError: If the data set is empty.
        """
        if not data:
            raise ValueError("Cannot compute range of an empty data set")
        return self.max(data) - self.min(data)

    def quartiles(self, data: Sequence[float]) -> dict[str, float]:
        """Return Q1, Q2 (median), and Q3 quartiles of the data set.

        Uses the inclusive method (Tukey hinges).

        Raises:
            ValueError: If the data set has fewer than 2 elements.
        """
        if len(data) < 2:
            raise ValueError("Cannot compute quartiles of a data set with fewer than 2 elements")

        sorted_data = sorted(data)
        n = len(sorted_data)

        # Q2 is the median
        q2 = self.median(sorted_data)

        # Split into lower and upper halves (inclusive of median)
        if n % 2 == 1:
            # Odd count: exclude the median from both halves
            lower = sorted_data[: n // 2]
            upper = sorted_data[n // 2 + 1 :]
        else:
            # Even count: split evenly
            lower = sorted_data[: n // 2]
            upper = sorted_data[n // 2 :]

        q1 = self.median(lower)
        q3 = self.median(upper)

        return {"Q1": q1, "Q2": q2, "Q3": q3}

    def iqr(self, data: Sequence[float]) -> float:
        """Return the interquartile range (Q3 - Q1) of the data set.

        Raises:
            ValueError: If the data set has fewer than 2 elements.
        """
        q = self.quartiles(data)
        return q["Q3"] - q["Q1"]
