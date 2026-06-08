"""Statistics module with descriptive statistical operations and correlation/regression analysis."""

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

        If multiple values have the same highest frequency, all are returned
        as a sorted list.

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

        mu = self.mean(data)
        return sum((x - mu) ** 2 for x in data) / (n - ddof)

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

        # Split into lower and upper halves (exclusive of median for odd n)
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

    # ── Correlation & Regression ──────────────────────────────────────

    def covariance(self, x: Sequence[float], y: Sequence[float], ddof: int = 0) -> float:
        """Return the covariance between two data sets.

        Args:
            x: The first data set.
            y: The second data set.
            ddof: Delta degrees of freedom. Use 0 for population covariance,
                  use 1 for sample covariance.

        Raises:
            ValueError: If x and y have different lengths, or are too small for ddof.
        """
        if len(x) != len(y):
            raise ValueError("Cannot compute covariance of data sets with different lengths")
        n = len(x)
        if n <= ddof:
            raise ValueError(
                f"Cannot compute covariance with ddof={ddof} on data sets of size {n}"
            )

        mean_x = self.mean(x)
        mean_y = self.mean(y)

        return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - ddof)

    def pearson_correlation(self, x: Sequence[float], y: Sequence[float]) -> float:
        """Return the Pearson correlation coefficient between two data sets.

        The coefficient ranges from -1 (perfect negative correlation) through
        0 (no correlation) to +1 (perfect positive correlation).

        Raises:
            ValueError: If x and y have different lengths or fewer than 2 elements.
            ValueError: If either data set has zero variance.
        """
        if len(x) != len(y):
            raise ValueError("Cannot compute correlation of data sets with different lengths")
        if len(x) < 2:
            raise ValueError("Cannot compute correlation with fewer than 2 data points")

        std_x = self.standard_deviation(x, ddof=0)
        std_y = self.standard_deviation(y, ddof=0)

        if std_x == 0 or std_y == 0:
            raise ValueError("Cannot compute correlation when one or both data sets have zero variance")

        cov = self.covariance(x, y, ddof=0)
        return cov / (std_x * std_y)

    def spearman_correlation(self, x: Sequence[float], y: Sequence[float]) -> float:
        """Return the Spearman rank correlation coefficient between two data sets.

        This non-parametric measure assesses monotonic relationships using
        ranked data. The coefficient ranges from -1 to +1.

        Raises:
            ValueError: If x and y have different lengths or fewer than 2 elements.
        """
        if len(x) != len(y):
            raise ValueError("Cannot compute correlation of data sets with different lengths")
        if len(x) < 2:
            raise ValueError("Cannot compute correlation with fewer than 2 data points")

        def rank(data: Sequence[float]) -> list[float]:
            """Assign ranks to data, handling ties with average rank."""
            sorted_data = sorted(enumerate(data), key=lambda t: t[1])
            n = len(data)
            ranks = [0.0] * n

            i = 0
            while i < n:
                j = i
                # Find all elements with the same value (ties)
                while j < n and sorted_data[j][1] == sorted_data[i][1]:
                    j += 1
                # Assign average rank to tied positions
                avg_rank = (i + j - 1) / 2.0 + 1  # 1-based ranking
                for k in range(i, j):
                    idx = sorted_data[k][0]
                    ranks[idx] = avg_rank
                i = j

            return ranks

        rank_x = rank(x)
        rank_y = rank(y)

        # Compute Pearson on ranks = Spearman
        return self.pearson_correlation(rank_x, rank_y)

    def linear_regression(self, x: Sequence[float], y: Sequence[float]) -> dict[str, float]:
        """Perform linear regression on two data sets.

        Returns a dict with:
            - slope: The slope of the regression line
            - intercept: The y-intercept of the regression line
            - r_squared: The coefficient of determination (R-squared)
            - r: The Pearson correlation coefficient

        Raises:
            ValueError: If x and y have different lengths or fewer than 2 elements.
            ValueError: If x has zero variance.
        """
        if len(x) != len(y):
            raise ValueError("Cannot perform regression on data sets with different lengths")
        if len(x) < 2:
            raise ValueError("Cannot perform regression with fewer than 2 data points")

        std_x = self.standard_deviation(x, ddof=0)
        if std_x == 0:
            raise ValueError("Cannot perform regression when the independent variable has zero variance")

        mean_x = self.mean(x)
        mean_y = self.mean(y)

        # slope = covariance(x, y, ddof=0) / variance(x, ddof=0)
        # But we need population terms so use ddof=0
        cov = self.covariance(x, y, ddof=0)
        var_x = self.variance(x, ddof=0)
        slope = cov / var_x

        intercept = mean_y - slope * mean_x

        # R-squared from Pearson correlation
        r = self.pearson_correlation(x, y)
        r_squared = r ** 2

        return {
            "slope": slope,
            "intercept": intercept,
            "r_squared": r_squared,
            "r": r,
        }
