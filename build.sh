#!/usr/bin/bash
aaa=$1
cat ./uploads/$aaa.c >> ./uploads/$aaa.c.c
/usr/bin/clang -c -m32 -nostdlib ./uploads/$aaa.c.c -o /tmp/$aaa.o
