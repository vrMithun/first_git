#include <iostream>
#include <vector>
using namespace std;
int ShiftVac(vector<int>& myvect,int index,int value);
void InsersionSort(vector<int>& myvect,int length){
    int current;
    int loc;
    for(int i=1;i<length;i++){
        current=myvect.at(i);
        loc=ShiftVac(myvect,i,current);
        myvect.at(loc)=current;
    }
}

int ShiftVac(vector<int>& myvect, int index, int value) {
    int vacant = index;
    while (vacant > 0 && myvect.at(vacant - 1) > value) {
        myvect.at(vacant) = myvect.at(vacant - 1);
        vacant = vacant - 1;

        for (int j = 0; j < myvect.size(); j++) {
            cout << myvect.at(j) << " ";
        }
        cout << "\n";
    }
    return vacant;
}

int main(){
    vector<int> myvect={1,2,3,4,5,6,7,8,9};
    int length=myvect.size();
    InsersionSort(myvect,length);

}
