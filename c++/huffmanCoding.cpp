#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>

using namespace std;

struct Node {
    char data;
    int freq;
    Node *left, *right;

    Node(char data, int freq) {
        this->data = data;
        this->freq = freq;
        left = right = nullptr;
    }
};

struct Compare {
    bool operator()(Node* l, Node* r) {
        return l->freq > r->freq;
    }
};

void printCodes(Node* root, string code, unordered_map<char, string>& huffmanMap) {
    if (!root) return;
    if (!root->left && !root->right) {
        cout << root->data << ": " << code << endl;
        huffmanMap[root->data] = code;
    }

    printCodes(root->left, code + "0", huffmanMap);
    printCodes(root->right, code + "1", huffmanMap);
}
void huffmanCoding(vector<char> chars, vector<int> freq) {
    priority_queue<Node*, vector<Node*>, Compare> minHeap;

    for (size_t i = 0; i < chars.size(); i++) {
        minHeap.push(new Node(chars[i], freq[i]));
    }

    while (minHeap.size() > 1) {
        Node *left = minHeap.top(); minHeap.pop();
        Node *right = minHeap.top(); minHeap.pop();

        Node *merged = new Node('$', left->freq + right->freq);
        merged->left = left;
        merged->right = right;

        minHeap.push(merged);
    }

    unordered_map<char, string> huffmanMap;
    cout << "Huffman Codes:\n";
    printCodes(minHeap.top(), "", huffmanMap);
}

int main() {
    vector<char> chars = {'a', 'b', 'c', 'd', 'e', 'f'};
    vector<int> freq = {5, 9, 12, 13, 16, 45};

    huffmanCoding(chars, freq);
    return 0;
}

