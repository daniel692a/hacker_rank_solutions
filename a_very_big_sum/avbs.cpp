# include <iostream>
# include <vector>
using namespace std;

long a_very_big_sum(vector<long> ar) {
    long result = 0;
    for (long i = 0; i < ar.size(); i++) {
        result += ar[i];
    }
    return result;
}

int main() {
    vector<long> ar = {1000000001, 1000000002, 1000000003, 1000000004, 1000000005};
    long result = a_very_big_sum(ar);
    return 0;
}