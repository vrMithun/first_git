#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

// Custom comparator for the priority queue (min-heap)
struct Compare
{
    bool operator()(pair<int, int> &a, pair<int, int> &b)
    {
        return a.second > b.second; // Min-heap based on frequency
    }
};

int kthMostFrequentElement(vector<int> &nums, int k)
{
    // Step 1: Count the frequency of each element
    unordered_map<int, int> freqMap;
    for (int num : nums)
    {
        freqMap[num]++;
    }

    // Step 2: Use a min-heap to keep track of the k most frequent elements
    priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> minHeap;

    for (auto &entry : freqMap)
    {
        minHeap.push(entry);
        // If the heap has more than k elements, pop the least frequent
        if (minHeap.size() > k)
        {
            minHeap.pop();
        }
    }

    // Step 3: The top of the heap is the k-th most frequent element
    return minHeap.top().first;
}

int main()
{
    vector<int> nums = {1, 1, 1, 2, 2, 3, 4, 4, 4, 4}; // Example input
    int k = 2;                                         // Example k

    int result = kthMostFrequentElement(nums, k);
    cout << "The " << k << "-th most frequent element is: " << result << endl;

    return 0;
}
