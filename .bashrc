#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Huge prompt
PS1="\`LAST_COMMAND=\$?; "										# Save last command return value for line 3 of PS1
PS1+="IFS=';' read -sdR -p $'\E[6n' ROW COL; if [ \${COL#*[} -ne 1 ]; then echo -n $'\n'; fi; "		# Print a new line if the last command did not have one
PS1+="if [ \$LAST_COMMAND -eq 0 ]; then echo \[\e[1\;33m\]^_^; else echo \[\e[1\;31m\]O_O; fi\`"	# Print a different smiley face depending on last command success
PS1+="\[\e[0m\]["											# Reset colors and opening brace
PS1+="`if [ $EUID -eq 0 ]; then echo $'\e[31m'; fi`"							# Print username red if running as root
PS1+="`getent passwd $LOGNAME | cut -d: -f5 | cut -d, -f1`"						# Print pretty username
PS1+="\[\e[0m\]@"											# Reset colors and at symbol
PS1+="`awk -F= '/PRETTY/ {gsub(/"/,"");print $2}' /etc/machine-info` "					# Print pretty machine name
PS1+="\[\e[1;36m\]\w\[\e[0m\]]\\$ "									# The rest of the fucking owl

# Aliases, features and environment variables
alias su='sudo su'											# Make su work when root login is disabled
alias ls='ls --color -A'										# Colors and hidden files by default in ls
alias grep='grep --color'										# Colors in grep
alias shutdown='sudo shutdown'										# Handy alias
alias poweroff='sudo shutdown -h now'									# ^
alias reboot='sudo shutdown -r now'									# ^
shopt -s autocd												# Automatically CD to a folder if we enter it directly to the prompt
source /usr/share/doc/pkgfile/command-not-found.bash							# Show if a missing command can be found in a package
export PKGFILE_PROMPT_INSTALL_MISSING=1									# Prompt to install said package
export HASTE_SERVER=https://haste.charlesmilette.net							# Custom server for hastebin uploader script
export PROMPT_DIRTRIM=4											# Trim directory in prompt if too long
shopt -s cdspell											# Fix those fucking typos
shopt -s dirspell											# ^
eval "$(SHELL=bash thefuck --alias)"									# FUCK
eval "$(hub alias -s)"											# Hub as git
