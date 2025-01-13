#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void radixsort(vector<int>& arr) {
    int maxval = *max_element(arr.begin(), arr.end());
    int exp = 1;

    while (maxval / exp > 0) {
        vector<vector<int>> bucket(10);

        for (int val : arr) {
            int radixindex = (val / exp) % 10;
            bucket[radixindex].push_back(val);
        }

        int i = 0;
        for (auto& buckets : bucket) {
            for (auto& val : buckets) {
                arr[i++] = val;
            }
        }

        exp *= 10;
    }
}

int main() {
    vector<int> arr = {489, 987, 456, 3456, 2343, 7777, 123, 311};
    radixsort(arr);
    for (int i : arr) {
        cout << i << " ";
    }
}
