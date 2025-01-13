#include <iostream>
#include <vector>
using namespace std;

void SelectionSort(vector<int>& myvect, int length) {
    int left = 0, right = length - 1;

    while (left < right) {
        // Initialize mini and maxi for the current range
        int mini = left, maxi = right;

        // Find the minimum and maximum in the range [left, right]
        for (int i = left; i <= right; i++) {
            if (myvect[i] < myvect[mini]) {
                mini = i;
            }
            if (myvect[i] > myvect[maxi]) {
                maxi = i;
            }
        }

        // Swap the minimum element with the left-most element
        swap(myvect[left], myvect[mini]);

        // If the maximum element was swapped with the left-most element,
        // update its index to reflect the new position
        if (maxi == left) {
            maxi = mini;
        }

        // Swap the maximum element with the right-most element
        swap(myvect[right], myvect[maxi]);

        // Move the bounds inward
        left++;
        right--;
    }
}

int main() {
    vector<int> myvect = {9, 8, 7, 6, 5, 4};
    int length = myvect.size();
    SelectionSort(myvect, length);

    // Print the sorted array
    for (int i = 0; i < length; i++) {
        cout << myvect[i] << " ";
    }
    return 0;
}
