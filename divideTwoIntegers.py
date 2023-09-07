class Solution {
public:
    int divide(int A, int B) {
        //Consider the edge case INT_MIN=-2^31 whose change sign is not INT
        if (A==INT_MIN && B==-1) 
            return INT_MAX;
        if (A==INT_MIN && B==1)
            return INT_MIN;
        if (B==INT_MIN && A!=INT_MIN) return 0;

        //Edge cases can lead to TLE
        if (A==B) return 1;
        if ( (0<=A && A<B)||(A<0 && B<A)) return 0;

        int ch_sgn=0;
        if (A>0){//A!=INT_MIN
            A=-A;
            ch_sgn++;
        }
        if (B<0){//quarantee B!=INT_MIN
            B=-B;
            ch_sgn++;
        }
        int sgn=(ch_sgn&1)?1:-1;
        int q=0;
        while(-B>=A){//TLE can happen when -A/B is large if only performing A+=B
            int b=B;
            int k=0;//Performing A+=b where b=B*(2^k)<=INT_MAX
            while(A<=-b && b<=INT_MAX){
                A+=b;
                q+=(1<<k);
                if (b<(1<<30)){
                    b<<=1;
                    k++;
                } 
            } 
        }
        return (sgn==1)?q:-q;
    }
};