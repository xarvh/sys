/*
 PLAY.C

 Command-line wrapper for mpg321 and ogg123
*/



#include <sys/select.h>
#include <sys/types.h>
#include <signal.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <termio.h>
#include <unistd.h>

#define COMMAND	"%s \"%s\""

#define NONE	0
#define QUIT	1
#define NEXT	2
#define NEXTF	3	//Next Finished: il Brano e' finito, non terminarlo
#define PREV	4
#define RESTART	5
#define RNEXT	6



char Bf[1024];		//chiamate a system() e lettura dal terminale
int Brano = 0;
int Cmd = NONE;

char* Lista[50*1000];
short ListaCnt;




/*=============================================================================
 * MOVE
 *
 * £%&/ non riesco a far funzionare la funzione rename()
 */
void move(char* n, char* dest)
{
 sprintf(Bf, "mv \"%s\" \"%s/Musica/%s/\"", n, getenv("HOME"), dest);
 int __r_system =  system(Bf);

// sprintf(bf, "%s/Musica/%s", getenv("HOME"), dest);
// rename(n, bf);

 printf("moved to %s\n", dest);
}



/*=============================================================================
 * MAIN LOOP
 */
int loop()
{
 switch(Cmd) {
    case NONE: break;
    case QUIT: return 0;
    case PREV: if(Brano > 0) Brano--; break;
    case NEXT:
    case NEXTF: if(++Brano == ListaCnt) return 0; break;
    case RNEXT: Brano = (int)((random()/(double)RAND_MAX)*ListaCnt); break;
    case RESTART: break;
 }

 Cmd = NONE;

 // Scegli il decodificatore
 char* dec = "mplayer -noconsolecontrols";
 char* e = strrchr(Lista[Brano], '.');
      if(e && !strcasecmp(e, ".mp3")) dec = "mplayer -really-quiet -noconsolecontrols";
 else if(e && !strcasecmp(e, ".ogg")) dec = "ogg123 -q";
 else
 {
    printf("%4d# ? %s\n", Brano, Lista[Brano]);
    Cmd = NEXT;
    return 1;
 }



 int pi[2];
 int __repipe = pipe(pi);


 // fork
 pid_t child_pid = fork();


 // child process
 if(!child_pid)
 {
    close(0); close(pi[0]);
    sprintf(Bf, COMMAND, dec, Lista[Brano]);
    int __r_system = system(Bf);
    close(pi[1]);
    exit(0);
 }


 //parent process
 close(pi[1]);

 printf("%4d# ", Brano+1);

 char* c = strrchr(Lista[Brano], '/');
 if(c) c++;
 else c = Lista[Brano];

 for( ; c < e; c++)
    if(*c == '\\');
    else if(*c == '_') printf(" ");
    else printf("%c", *c);

 printf("\n");

 do {
    // check for incoming keys
    static fd_set read_fds[1];
    FD_ZERO(read_fds);
    FD_SET(0, read_fds);
    FD_SET(pi[0], read_fds);
    select(pi[0]+1, read_fds, NULL, NULL, NULL);

    // broken pipe, child dead, go to next process
    if(FD_ISSET(pi[0], read_fds)) Cmd = NEXTF;

    // an actual key
    if(FD_ISSET(0, read_fds))
    {
	int __r_read = read(0, Bf, 100);
	switch(Bf[0]) {
	    case '?': printf("decoder: %s\n%s\n", dec, Lista[Brano]); break;
	    case 'p': Cmd = PREV; break;
	    case 'q': Cmd = QUIT; break;
	    case 'r': Cmd = RESTART; break;
	    case ' ':
	    case 'n': Cmd = NEXT; break;
	    case 'N': Cmd = RNEXT; break;

	    case 'K': move(Lista[Brano], "new/trash"); Cmd = NEXT; break;
	    case '_': move(Lista[Brano], "pacco/"); Cmd = NEXT; break;
	    case '!': move(Lista[Brano], "new/good"); break;
	    case 'G': move(Lista[Brano], "categories/uncategorized"); break;

	    case 'T': move(Lista[Brano], "categories/tango"); break;
	    case 'S': move(Lista[Brano], "categories/tango/slow"); break;
	    case 'P': move(Lista[Brano], "categories/party"); break;
	    case 'R': move(Lista[Brano], "categories/rock"); break;
	    case 'O': move(Lista[Brano], "categories/oldies"); break;
	    case 'M': move(Lista[Brano], "categories/metal"); break;
	    case '$': move(Lista[Brano], "categories/commercial"); break;
	    case 'C': move(Lista[Brano], "categories/chill"); break;
	    case 'L': move(Lista[Brano], "categories/latin"); break;

	    default: break;
	    }
	}
 } while(Cmd == NONE);


 // close the pipe
 close(pi[0]);
 if(Cmd != NEXTF)
 {
    //kill(child_pid, SIGTERM);
    //sprintf(Bf, "kill `pidof %s`", dec);
    sprintf(Bf, "killall mplayer ogg123", dec);
    int __r_system = system(Bf);
 }

 return 1;
}





/*=============================================================================
 * MAIN LOOP
 */
int loadLista(char* fn)
{
 ListaCnt = 0;

 FILE* f = fopen(fn, "rt");
 if(!f) return -1;

 while(fgets(Bf, sizeof(Bf), f))
 {
    char* n = strrchr(Bf, '\n');
    if(n) *n = '\0';

    Lista[ListaCnt++] = strdup(Bf);

    if(ListaCnt > sizeof(Lista)/sizeof(Lista[0]))
    {
	printf("Too many tracks. Increase the buffers. Yeah, I'm a lazy bastard.\n");
	break;
    }
 }


 fclose(f);
 return !ListaCnt;
}





/*=============================================================================
 *
 */
static struct termios _old;
static struct termios cooked;



static void restore_terminal()
{
 tcsetattr(0, TCSANOW, &_old);
}



int main(int argc, char *argv[])
{
 srandom(time(0));
 if(loadLista(argv[1])) return -1;


 //Inizializza il terminale
 tcgetattr(0, &cooked);
 _old = cooked;

 cooked.c_lflag &= ~(ICANON | ECHO);
 cooked.c_cc[VEOL] = 1;
 cooked.c_cc[VEOF] = 2;
 tcsetattr(0, TCSANOW, &cooked);
 atexit(restore_terminal);



 //Loop principale
 while(loop());
 exit(1);
}

//EOF =========================================================================
