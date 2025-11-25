# src/algorithms.py
# Contains Binary Search (Best-Fit) and Backtracking loader

from src.storage_bin import StorageBin

# ------------------------------
# Binary Search: Best-Fit Bin
# ------------------------------
def find_best_fit_bin(sorted_bins, package_size):
    """
    Finds the smallest bin with capacity >= package_size using binary search.
    Returns the bin object or None.
    """
    left, right = 0, len(sorted_bins) - 1
    best_bin = None

    while left <= right:
        mid = (left + right) // 2
        if sorted_bins[mid].capacity >= package_size:
            best_bin = sorted_bins[mid]  # candidate
            right = mid - 1              # search smaller
        else:
            left = mid + 1

    return best_bin


# ------------------------------
# Backtracking: Shipment Planner
# ------------------------------
def can_fit_packages(packages, remaining_space):
    """
    Returns True/False depending on whether packages can fit into 'remaining_space'.
    Uses backtracking.
    """
    return _backtrack(packages, 0, remaining_space)


def _backtrack(packages, index, remaining_space):
    if remaining_space < 0:
        return False
    if index == len(packages):
        return True

    # Option 1: Include current package
    include = _backtrack(packages, index + 1, remaining_space - packages[index].size)

    # Option 2: Exclude current package
    exclude = _backtrack(packages, index + 1, remaining_space)

    return include or exclude
