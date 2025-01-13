#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void InsertionSort(vector<float>& bucket) {
    for (int i = 1; i < bucket.size(); i++) {
        float key = bucket[i];
        int j = i - 1;
        while (j >= 0 && bucket[j] > key) {
            bucket[j + 1] = bucket[j];
            j--;
        }
        bucket[j + 1] = key;
    }
}

void BucketSort(vector<float>& arr) {
    int n = arr.size();
    if (n <= 1) return;

    float minValue = arr[0], maxValue = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < minValue) minValue = arr[i];
        if (arr[i] > maxValue) maxValue = arr[i];
    }

    float range = maxValue - minValue;
    int k = floor(sqrt(n));
    vector<vector<float>> buckets(k);

    for (int i = 0; i < n; i++) {
        int index = floor((arr[i] - minValue) * k / range);
        if (index == k) index = k - 1;
        buckets[index].push_back(arr[i]);
    }

    for (int i = 0; i < k; i++) {
        InsertionSort(buckets[i]);
    }

    int idx = 0;
    for (int i = 0; i < k; i++) {
        for (float val : buckets[i]) {
            arr[idx++] = val;
        }
    }
}

int main() {
    vector<float> arr = {214,32,122,111};
    BucketSort(arr);
    for (float val : arr) {
        cout << val << " ";
    }
    return 0;
}
