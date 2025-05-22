// tim gcd cuar moi phan tu trong mang (gcd: UCLN)
 
 // tim so lon nhat ma moi so trong mang deu chia het cho so do
 
#include<stdio.h>

#define ll long long

ll gcd(ll a, ll b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

int main() {
    int n;
    scanf("%d", &n);

    ll a[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }

    ll uc = a[0];
    for (int i = 1; i < n; i++) {
        uc = gcd(uc, a[i]);
    }

    printf("%lld\n", uc);

    return 0;
}

