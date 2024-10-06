#include <stdio.h>

int main(){
    int m,n;
    printf("Inserire numero righe e colonne -> ");
    scanf("%d%d",&m,&n);
    int matrix[m][n];

    //inizializzazione array
    for (int i=0;i<m;i++){
        printf("inserire riga %d",i);
        for(int j=0;j<n;j++){
            scanf("%d",&matrix[i][j]);
        }
    }

    

    //stampa array
    for (int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}