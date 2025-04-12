
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Activity {
    int start, finish;
};

bool compare(Activity a1, Activity a2) {
    return a1.finish < a2.finish;
}

void activitySelection(vector<Activity> activities) {
    sort(activities.begin(), activities.end(), compare);

    cout << "Selected activities: \n";

    int lastFinishTime = 0;
    for (const auto& act : activities) {
        if (act.start >= lastFinishTime) {
            cout << "(" << act.start << ", " << act.finish << ") ";
            lastFinishTime = act.finish;
        }
    }
    cout << endl;
}

int main() {
    vector<Activity> activities = {{1, 3}, {2, 5}, {3, 9}, {6, 8}, {5, 7}, {8, 9}};

    activitySelection(activities);
    return 0;
}
