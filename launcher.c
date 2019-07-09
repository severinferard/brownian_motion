#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
int main(int argc, char **argv)
{
    char *finalslash,cwd[250];
printf("ici = %s\n",argv[0]);
strcpy(cwd,argv[0]);
finalslash=strrchr(cwd,'/');
printf("la = %s\n",finalslash);


*finalslash=0;
printf("la = %s\n",cwd);

    char cwd2[200];
    int k,k2;
    for (k=0,k2=0; k<strlen(cwd); k++)
    {
        if (cwd[k]!=' ')
            cwd2[k2++]=cwd[k];
        else
        {
            cwd2[k2++]='\\';
            cwd2[k2++]=' ';
        }
    }
    cwd2[k2]=0;
    printf("cwd2=%s\n",cwd2);
   char prog[200];
   strcpy(prog,"python3 ");
   strcat(prog,cwd2);
   strcat(prog,"/");
    printf("prog=%s\n",prog);
   strcat(prog,"ball_tracker.py");
   printf("prog=%s\n",prog);
    int status = system(prog);

    return 0;
}
