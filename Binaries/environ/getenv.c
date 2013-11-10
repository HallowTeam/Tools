#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>

int     exists(char *name)
{
	return open(name, O_RDONLY);
}

int     main(int argc, char **argv)
{
	int   offset;
	char  *addr;

	if (argc < 3)
	{
		printf("Usage: %s <VAR_NAME> <PROC_NAME>\n", argv[0]);
		return 0;
	}

	if ((addr = getenv(argv[1])) == NULL)
	{
		printf("%s is not defined\n", argv[1]);
		return 0;
	}

	if (exists(argv[2]) == -1)
	{
		printf("%s doesn't exist or is not readable\n", argv[2]);
		return 0;
	}

	offset  = 0;
	offset  = strlen(realpath(argv[0], NULL)) - strlen(realpath(argv[2], NULL));
	offset *= 2;
	addr   += offset;

	printf("Address: \\x%02lx\\x%02lx\\x%02lx\\x%02lx (%08lx)",
				 (0x000000FF & (long)addr) >> 0,
				 (0x0000FF00 & (long)addr) >> 8,
				 (0x00FF0000 & (long)addr) >> 16,
				 (0xFF000000 & (long)addr) >> 24,
				 (long)addr);

	return 0;
}
