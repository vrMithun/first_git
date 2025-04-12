#include<iostream>
#include<vector>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    struct ListNode* result=new ListNode();
    struct ListNode* last=new ListNode();
    while(list1 && list2){
        if(list1->val<=list2->val){
            if(result==nullptr){
                result=list1;
                last=list1;

            }
            else{
                last->next=list1;
                last=last->next;
            }
            list1=list1->next;
        }
        else{
            if(result==nullptr){
                result=list2;
                last=list2;

            }
            else{
                last->next=list2;
                last=last->next;
            }
            list2=list2->next;
        }
    }
    if(list1!=nullptr){
        last->next=list1;
    }
    if(list2!=nullptr){
        last->next=list2;
    }
    return result;
}

 int main(){
     struct ListNode* mylist=new ListNode(0);
     cout<<mylist->val;
}
