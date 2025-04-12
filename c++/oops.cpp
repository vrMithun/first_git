#include<iostream>
#include<vector>
#include<set>
using namespace std;

class Rectangle{
private:
    int length;
    int width;

public:
    Rectangle(int l,int w){
        length=l;
        width=w;
    }
    int area(){
        return length*width;
    }
    int perimeter(){
        return 2*(length+width);
    }
};

int main(){
    Rectangle myobj(2,3);
    cout<<myobj.area();
}
