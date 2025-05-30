# less
# Autogenerated from man page /data/data/com.termux/files/usr/share/man/man1/less.1.gz
complete -c less -s '?' -l help -d 'This option displays a summary of the commands accepted by  less (the same as…'
complete -c less -s a -l search-skip-screen -d 'By default, forward searches start at the top of the displayed screen and bac…'
complete -c less -s A -l SEARCH-SKIP-SCREEN -d 'Causes all forward searches (not just non-repeated searches) to start just af…'
complete -c less -o bn -l buffers -d 'Specifies the amount of buffer space  less will use for each file, in units o…'
complete -c less -s B -l auto-buffers -d 'By default, when data is read from a pipe, buffers are allocated automaticall…'
complete -c less -s c -l clear-screen -d 'Causes full screen repaints to be painted from the top line down'
complete -c less -s C -l CLEAR-SCREEN -d 'Same as -c, for compatibility with older versions of  less '
complete -c less -s d -l dumb -d 'The -d option suppresses the error message normally displayed if the terminal…'
complete -c less -o Dxcolor -l color -d 'Changes the color of different parts of the displayed text'
complete -c less -s e -l quit-at-eof -d 'Causes  less to automatically exit the second time it reaches end-of-file'
complete -c less -s E -l QUIT-AT-EOF -d 'Causes  less to automatically exit the first time it reaches end-of-file'
complete -c less -s f -l force -d 'Forces non-regular files to be opened'
complete -c less -s F -l quit-if-one-screen -d 'Causes  less to automatically exit if the entire file can be displayed on the…'
complete -c less -s g -l hilite-search -d 'Normally,  less will highlight ALL strings which match the last search command'
complete -c less -s G -l HILITE-SEARCH -d 'The -G option suppresses all highlighting of strings found by search commands'
complete -c less -o hn -l max-back-scroll -d 'Specifies a maximum number of lines to scroll backward'
complete -c less -s i -l ignore-case -d 'Causes searches to ignore case; that is, uppercase and lowercase are consider…'
complete -c less -s I -l IGNORE-CASE -d 'Like -i, but searches ignore case even if the pattern contains uppercase lett…'
complete -c less -o jn -l jump-target -d 'Specifies a line on the screen where the "target" line is to be positioned'
complete -c less -s J -l status-column -d 'Displays a status column at the left edge of the screen'
complete -c less -o kfilename -l lesskey-file -d 'Causes  less to open and interpret the named file as a  lesskey (1) binary fi…'
complete -c less -l lesskey-src -d 'Causes  less to open and interpret the named file as a   lesskey (1) source f…'
complete -c less -l lesskey-content -d 'Causes less to interpret the specified text as the contents of a  lesskey (1)…'
complete -c less -s K -l quit-on-intr -d 'Causes  less to exit immediately (with status 2) when an interrupt character …'
complete -c less -s L -l no-lessopen -d 'Ignore the LESSOPEN environment variable (see the INPUT PREPROCESSOR section …'
complete -c less -s m -l long-prompt -d 'Causes  less to prompt verbosely (like   more (1)), with the percent into the…'
complete -c less -s M -l LONG-PROMPT -d 'Causes  less to prompt even more verbosely than  more (1)'
complete -c less -s n -l line-numbers -d 'Suppresses line numbers'
complete -c less -s N -l LINE-NUMBERS -d 'Causes a line number to be displayed at the beginning of each line in the dis…'
complete -c less -o ofilename -l log-file -d 'Causes  less to copy its input to the named file as it is being viewed'
complete -c less -o Ofilename -l LOG-FILE -d 'The -O option is like -o, but it will overwrite an existing file without aski…'
complete -c less -o ppattern -l pattern -d 'The -p option on the command line is equivalent to specifying +/pattern; that…'
complete -c less -o Pprompt -l prompt -d 'Provides a way to tailor the three prompt styles to your own preference'
complete -c less -s q -l quiet -l silent -d 'Causes moderately "quiet" operation: the terminal bell is not rung if an atte…'
complete -c less -s Q -l QUIET -l SILENT -d 'Causes totally "quiet" operation: the terminal bell is never rung'
complete -c less -s r -l raw-control-chars -d 'Causes "raw" control characters to be displayed'
complete -c less -s R -l RAW-CONTROL-CHARS -d 'Like -r, but only ANSI "color" escape sequences and OSC 8 hyperlink sequences…'
complete -c less -s s -l squeeze-blank-lines -d 'Causes consecutive blank lines to be squeezed into a single blank line'
complete -c less -s S -l chop-long-lines -d 'Causes lines longer than the screen width to be chopped (truncated) rather th…'
complete -c less -o ttag -l tag -d 'The -t option, followed immediately by a TAG, will edit the file containing t…'
complete -c less -o Ttagsfile -l tag-file -d 'Specifies a tags file to be used instead of "tags"'
complete -c less -s u -l underline-special -d 'Causes backspaces and carriage returns to be treated as printable characters;…'
complete -c less -s U -l UNDERLINE-SPECIAL -d 'Causes backspaces, tabs, carriage returns and "formatting characters" (as def…'
complete -c less -s V -l version -d 'Displays the version number of  less '
complete -c less -s w -l hilite-unread -d 'Temporarily highlights the first "new" line after a forward movement of a ful…'
complete -c less -s W -l HILITE-UNREAD -d 'Like -w, but temporarily highlights the first new line after any forward move…'
complete -c less -o xn -l tabs -d 'Sets tab stops'
complete -c less -s X -l no-init -d 'Disables sending the termcap initialization and deinitialization strings to t…'
complete -c less -o yn -l max-forw-scroll -d 'Specifies a maximum number of lines to scroll forward'
complete -c less -o zn -l window -d 'Changes the default scrolling window size to n lines'
complete -c less -l tilde -d 'Normally lines after end of file are displayed as a single tilde (\\(ti)'
complete -c less -s '#' -l shift -d 'Specifies the default number of positions to scroll horizontally in the RIGHT…'
complete -c less -l exit-follow-on-close -d 'When using the "F" command on a pipe,  less will automatically stop waiting f…'
complete -c less -l file-size -d 'If --file-size is specified,  less will determine the size of the file  immed…'
complete -c less -l follow-name -d 'Normally, if the input file is renamed while an F command is executing,  less…'
complete -c less -l header -d 'RS Sets the number of header lines and columns displayed on the screen'
complete -c less -l incsearch -d 'Subsequent search commands will be "incremental"; that is,  less will advance…'
complete -c less -l intr -d 'Use the character c instead of \\(haX to interrupt a read when the "Waiting fo…'
complete -c less -l line-num-width -d 'Sets the minimum width of the line number field when the -N option is in effe…'
complete -c less -l match-shift -d 'When -S is in effect, if a search match is not visible because it is shifted …'
complete -c less -l modelines -d 'RS Before displaying a file,  less  will read the first n lines to try to fin…'
complete -c less -l mouse -d 'Enables mouse input: scrolling the mouse wheel down moves forward in the file…'
complete -c less -l MOUSE -d 'Like --mouse, except the direction scrolled on mouse wheel movement is revers…'
complete -c less -l no-keypad -d 'Disables sending the keypad initialization and deinitialization strings to th…'
complete -c less -l no-histdups -d 'This option changes the behavior so that if a search string or file name is t…'
complete -c less -l no-number-headers -d 'Header lines (defined via the --header option) are not assigned line numbers'
complete -c less -l no-search-header-lines -d 'Searches do not include header lines, but still include header columns'
complete -c less -l no-search-header-columns -d 'Searches do not include header columns, but still include header lines'
complete -c less -l no-search-headers -d 'Searches do not include header lines or header columns'
complete -c less -l no-vbell -d 'Disables the terminal\'s visual bell'
complete -c less -l proc-backspace -d 'If set, backspaces are handled as if neither the -u option  nor the -U option…'
complete -c less -l PROC-BACKSPACE -d 'If set, backspaces are handled as if the -U option were set; that is backspac…'
complete -c less -l proc-return -d 'If set, carriage returns are handled as if neither the -u option  nor the -U …'
complete -c less -l PROC-RETURN -d 'If set, carriage returns are handled as if the -U option were set; that is ca…'
complete -c less -l proc-tab -d 'If set, tabs are handled as if the -U option were not set'
complete -c less -l PROC-TAB -d 'If set, tabs are handled as if the -U option were set; that is tabs are treat…'
complete -c less -l redraw-on-quit -d 'When quitting, after sending the terminal deinitialization string, redraws th…'
complete -c less -l rscroll -d 'This option changes the character used to mark truncated lines'
complete -c less -l save-marks -d 'Save marks in the history file, so marks are retained across different invoca…'
complete -c less -l search-options -d 'Sets default search modifiers'
complete -c less -l show-preproc-errors -d 'If a preprocessor produces data,  then exits with a non-zero exit code,  less…'
complete -c less -l status-col-width -d 'Sets the width of the status column when the -J option is in effect'
complete -c less -l status-line -d 'If a line is marked, the entire line (rather than just the status column) is …'
complete -c less -l use-backslash -d 'This option changes the interpretations of options which follow this one'
complete -c less -l use-color -d 'Enables colored text in various places'
complete -c less -l wheel-lines -d 'Set the number of lines to scroll when the mouse wheel is scrolled and the --…'
complete -c less -l wordwrap -d 'When the -S option is not in use, wrap each line at a space or tab if possibl…'
complete -c less -s + -d 'Followed by one of the command line option letters this will reset the option…'
complete -c less -l + -d 'Like the -+ command, but takes a long option name rather than a single option…'
complete -c less -l qui -l qui -d 'Some long option names are in uppercase, such as --QUIT-AT-EOF, as distinct f…'
complete -c less -l quotes -d 'Changes the filename quoting character'
complete -c less -s ~ -d 'Normally lines after end of file are displayed as a single tilde (~)'

