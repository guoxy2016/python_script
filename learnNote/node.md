# SQLAlchemy
[数据库sql`cascade`的使用](https://docs.sqlalchemy.org/en/13/orm/cascades.html#unitofwork-cascades)

# crontab
打开日志记录\
sudo vim /etc/rsyslog.d/50-default.conf\
取消对`cron.*`的注释, 然后重启rsyslog和cron服务\
sudo service rsyslog restart\
sudo service cron restart

设定格式
分钟 小时 日 月 星期 命令          \
 /  /   /  /   |   |           \
|  /   /  |   /     \          \
m h  dom mon dow   command

`*` 任意
`/` 每隔  例子 `*/2` 每隔两小时
`-` 
`,`

# shell中的最强的几个强大的命令

## ls
```
用法：ls [选项]... [文件]...
输出文件的信息 (默认输出当前目录).
如果没有使用 -cftuvSUX 或 --sort 指定, 将按照字母顺序输出
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

必选参数对长短选项同时适用。
  -a, --all                  不隐藏任何以. 开始的项目
  -A, --almost-all           列出除. 及.. 以外的任何项目
      --author               与-l 同时使用时列出每个文件的作者
  -b, --escape               以八进制溢出序列表示不可打印的字符
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                               e.g., '--block-size=M'; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         类似-l，但不列出所有者
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                               (default if omitted), 'auto', or 'never'
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage;
                               used only with -s and per directory totals
  -l                         使用较长格式列出信息
  -L, --dereference          当显示符号链接的文件信息时，显示符号链接所指示
                             的对象而并非符号链接本身的信息
  -m                         所有项目以逗号分隔，并填满整行行宽
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print entry names without quoting
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
                               (overrides QUOTING_STYLE environment variable)
  -r, --reverse              逆序排列
  -R, --recursive            递归显示子目录
  -s, --size                 以块数形式显示每个文件分配的尺寸
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help                 显示此帮助信息并退出
      --version              显示版本信息并退出

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
Also the TIME_STYLE environment variable sets the default style to use.

使用色彩来区分文件类型的功能已被禁用，默认设置和 --color=never 同时禁用了它。
使用 --color=auto 选项，ls 只在标准输出被连至终端时才生成颜色代码。
LS_COLORS 环境变量可改变此设置，可使用 dircolors 命令来设置。

退出状态：
 0  正常
 1  一般问题 (例如：无法访问子文件夹)
 2  严重问题 (例如：无法使用命令行参数)

GNU coreutils 在线帮助：<https://www.gnu.org/software/coreutils/>
请向 <http://translationproject.org/team/zh_CN.html> 报告 ls 的翻译错误
完整文档请见：<https://www.gnu.org/software/coreutils/ls>
或者在本地使用：info '(coreutils) ls invocation'
```
---

## find
```
Usage: find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]

默认路径为当前目录；默认表达式为 -print
表达式可能由下列成份组成：操作符、选项、测试表达式以及动作：
操作符 (优先级递减；未做任何指定时默认使用 -and):
      ( EXPR )   ! EXPR   -not EXPR   EXPR1 -a EXPR2   EXPR1 -and EXPR2
      EXPR1 -o EXPR2   EXPR1 -or EXPR2   EXPR1 , EXPR2
位置选项 (总是真): -daystart -follow -regextype

普通选项 (总是真，在其它表达式前指定):
      -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf
      --version -xdev -ignore_readdir_race -noignore_readdir_race
测试(N可以是 +N 或-N 或 N):-amin N -anewer FILE -atime N -cmin  
      -cnewer 文件 -ctime N -empty -false -fstype 类型 -gid N -group 名称
      -ilname 匹配模式 -iname 匹配模式 -inum N -ipath 匹配模式 -iregex 匹配模式
      -links N -lname 匹配模式 -mmin N -mtime N -name 匹配模式 -newer 文件
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN
      -readable -writable -executable
      -wholename PATTERN -size N[bcwkMG] -true -type [bcdpflsD] -uid N
      -used N -user NAME -xtype [bcdpfls]      -context 文本

actions: -delete -print0 -printf FORMAT -fprintf FILE FORMAT -print 
      -fprint0 FILE -fprint FILE -ls -fls FILE -prune -quit
      -exec COMMAND ; -exec COMMAND {} + -ok COMMAND ;
      -execdir COMMAND ; -execdir COMMAND {} + -okdir COMMAND ;

Valid arguments for -D:
exec, opt, rates, search, stat, time, tree, all, help
Use '-D help' for a description of the options, or see find(1)

Please see also the documentation at http://www.gnu.org/software/findutils/.
You can report (and track progress on fixing) bugs in the "find"
program via the GNU findutils bug-reporting page at
https://savannah.gnu.org/bugs/?group=findutils or, if
you have no web access, by sending email to <bug-findutils@gnu.org>.
```
---

## grep
```
Usage: grep [OPTION]... PATTERNS [FILE]...
Search for PATTERNS in each FILE.
Example: grep -i 'hello world' menu.h main.c
PATTERNS can contain multiple patterns separated by newlines.

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERNS are extended regular expressions
  -F, --fixed-strings       PATTERNS are strings
  -G, --basic-regexp        PATTERNS are basic regular expressions
  -P, --perl-regexp         PATTERNS are Perl regular expressions
  -e, --regexp=PATTERNS     use PATTERNS for matching
  -f, --file=FILE           take PATTERNS from FILE
  -i, --ignore-case         ignore case distinctions
  -w, --word-regexp         match only whole words
  -x, --line-regexp         match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline

杂项:
  -s, --no-messages         不显示错误信息
  -v, --invert-match        选中不匹配的行
  -V, --version             显示版本信息并退出
      --help                显示此帮助并退出

输出控制：
  -m, --max-count=<次数>    得到给定<次数>次匹配后停止
  -b, --byte-offset         输出的同时打印字节偏移
  -n, --line-number         输出的同时打印行号
      --line-buffered       每行输出后刷新输出缓冲区
  -H, --with-filename       为输出行打印文件名
  -h, --no-filename         输出时不显示文件名前缀
      --label=<标签>        将给定<标签>作为标准输入文件名前缀
  -o, --only-matching       show only nonempty parts of lines that match
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        等同于 --binary-files=without-match
  -d, --directories=ACTION  读取目录的方式；
                            ACTION 可以是`read', `recurse',或`skip'
  -D, --devices=ACTION      读取设备、先入先出队列、套接字的方式；
                            ACTION 可以是`read'或`skip'
  -r, --recursive           等同于--directories=recurse
  -R, --dereference-recursive       同上，但遍历所有符号链接
      --include=GLOB        search only files that match GLOB (a file pattern)
      --exclude=GLOB        skip files and directories matching GLOB
      --exclude-from=FILE   skip files matching any file pattern from FILE
      --exclude-dir=GLOB    skip directories that match GLOB
  -L, --files-without-match  只打印没有匹配上的<文件>的名称
  -l, --files-with-matches  只打印有匹配的<文件>的名称
  -c, --count               只打印每个<文件>中的匹配行数目
  -T, --initial-tab         行首制表符对齐（如有必要）
  -Z, --null                在<文件>名最后打印空字符

文件控制:
  -B, --before-context=NUM  打印文本及其前面NUM 行
  -A, --after-context=NUM   打印文本及其后面NUM 行
  -C, --context=NUM         打印NUM 行输出文本
  -NUM                      等同于 --context=NUM
      --color[=WHEN],
      --colour[=WHEN]       使用标记高亮匹配字串；
                            WHEN 可以是“always”、“never”或“auto”
  -U, --binary              不要清除行尾的 CR 字符（MSDOS/Windows）

When FILE is '-', read standard input.  With no FILE, read '.' if
recursive, '-' otherwise.  With fewer than two FILEs, assume -h.
Exit status is 0 if any line (or file if -L) is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.

请将错误报告给: bug-grep@gnu.org。翻译问题请报告至:Chinese (simplified) <i18n-zh@googlegroups.com>。
GNU grep 主页: <http://www.gnu.org/software/grep/>
General help using GNU software: <https://www.gnu.org/gethelp/>
```
---

## ps
```
Usage:
 ps [options]

Basic options:
 -A, -e               all processes
 -a                   all with tty, except session leaders
  a                   all with tty, including other users
 -d                   all except session leaders
 -N, --deselect       negate selection
  r                   only running processes
  T                   all processes on this terminal
  x                   processes without controlling ttys

Selection by list:
 -C <command>         command name
 -G, --Group <GID>    real group id or name
 -g, --group <group>  session or effective group name
 -p, p, --pid <PID>   process id
        --ppid <PID>  parent process id
 -q, q, --quick-pid <PID>
                      process id (quick mode)
 -s, --sid <session>  session id
 -t, t, --tty <tty>   terminal
 -u, U, --user <UID>  effective user id or name
 -U, --User <UID>     real user id or name

  The selection options take as their argument either:
    a comma-separated list e.g. '-u root,nobody' or
    a blank-separated list e.g. '-p 123 4567'

Output formats:
 -F                   extra full
 -f                   full-format, including command lines
  f, --forest         ascii art process tree
 -H                   show process hierarchy
 -j                   jobs format
  j                   BSD job control format
 -l                   long format
  l                   BSD long format
 -M, Z                add security data (for SELinux)
 -O <format>          preloaded with default columns
  O <format>          as -O, with BSD personality
 -o, o, --format <format>
                      user-defined format
  s                   signal format
  u                   user-oriented format
  v                   virtual memory format
  X                   register format
 -y                   do not show flags, show rss vs. addr (used with -l)
     --context        display security context (for SELinux)
     --headers        repeat header lines, one per page
     --no-headers     do not print header at all
     --cols, --columns, --width <num>
                      set screen width
     --rows, --lines <num>
                      set screen height

Show threads:
  H                   as if they were processes
 -L                   possibly with LWP and NLWP columns
 -m, m                after processes
 -T                   possibly with SPID column

Miscellaneous options:
 -c                   show scheduling class with -l option
  c                   show true command name
  e                   show the environment after command
  k,    --sort        specify sort order as: [+|-]key[,[+|-]key[,...]]
  L                   show format specifiers
  n                   display numeric uid and wchan
  S,    --cumulative  include some dead child process data
 -y                   do not show flags, show rss (only with -l)
 -V, V, --version     display version information and exit
 -w, w                unlimited output width

        --help <simple|list|output|threads|misc|all>
                      display help and exit

For more details see ps(1).
```
## 其他命令
### tail
```
用法：tail [选项]... [文件]...
Print the last 10 lines of each FILE to standard output.
With more than one FILE, precede each with a header giving the file name.

如果没有指定文件，或者文件为"-"，则从标准输入读取。

必选参数对长短选项同时适用。
  -c, --bytes=[+]NUM       output the last NUM bytes; or use -c +NUM to
                             output starting with byte NUM of each file
  -f, --follow[={name|descriptor}]
                           output appended data as the file grows;
                             an absent option argument means 'descriptor'
  -F                       same as --follow=name --retry
  -n, --lines=[+]NUM       output the last NUM lines, instead of the last 10;
                             or use -n +NUM to output starting with line NUM
      --max-unchanged-stats=N
                           with --follow=name, reopen a FILE which has not
                             changed size after N (default 5) iterations
                             to see if it has been unlinked or renamed
                             (this is the usual case of rotated log files);
                             with inotify, this option is rarely useful
      --pid=PID            with -f, terminate after process ID, PID dies
  -q, --quiet, --silent    never output headers giving file names
      --retry              keep trying to open a file if it is inaccessible
  -s, --sleep-interval=N   with -f, sleep for approximately N seconds
                             (default 1.0) between iterations;
                             with inotify and --pid=P, check process P at
                             least once every N seconds
  -v, --verbose            always output headers giving file names
  -z, --zero-terminated    以 NUL 字符而非换行符作为行尾分隔符
      --help		显示此帮助信息并退出
      --version		显示版本信息并退出

NUM may have a multiplier suffix:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.

如果您希望即时追查一个文件的有效名称而非描述内容(例如循环日志)，默认
的程序动作并不如您所愿。在这种场合可以使用--follow=name 选项，它会使
tail 定期追踪打开给定名称的文件，以确认它是否被删除或被其它某些程序重新创建过。

GNU coreutils 在线帮助：<https://www.gnu.org/software/coreutils/>
请向 <http://translationproject.org/team/zh_CN.html> 报告 tail 的翻译错误
完整文档请见：<https://www.gnu.org/software/coreutils/tail>
或者在本地使用：info '(coreutils) tail invocation'
```
