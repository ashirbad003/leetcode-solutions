#define MOD 1000000007LL
int* sumAndMultiply(char* s,int** queries,int queriesSize,int* queriesColSize,int* returnSize){
    int n=strlen(s);
    long long* pow10=(long long*)malloc((n+1)*sizeof(long long));
    long long* prefVal=(long long*)malloc((n+1)*sizeof(long long));
    long long* prefSum=(long long*)malloc((n+1)*sizeof(long long));
    int* cnt=(int*)malloc((n+1)*sizeof(int));
    pow10[0]=1;
    for(int i=1;i<=n;i++)
        pow10[i]=(pow10[i-1]*10)%MOD;
    prefVal[0]=0;
    prefSum[0]=0;
    cnt[0]=0;
    for(int i=1;i<=n;i++){
        int d=s[i-1]-'0';
        prefSum[i]=prefSum[i-1]+d;
        if(d!=0){
            prefVal[i]=(prefVal[i-1]*10+d)%MOD;
            cnt[i]=cnt[i-1]+1;
        }else{
            prefVal[i]=prefVal[i-1];
            cnt[i]=cnt[i-1];
        }
    }
    int* ans=(int*)malloc(sizeof(int)*queriesSize);
    for(int i=0;i<queriesSize;i++){
        int l=queries[i][0];
        int r=queries[i][1];
        long long sum=prefSum[r+1]-prefSum[l];
        int k=cnt[r+1]-cnt[l];
        long long x=(prefVal[r+1]-(prefVal[l]*pow10[k])%MOD+MOD)%MOD;
        ans[i]=(int)((x*(sum%MOD))%MOD);
    }
    free(pow10);
    free(prefVal);
    free(prefSum);
    free(cnt);
    *returnSize=queriesSize;
    return ans;
}