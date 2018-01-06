if test $TERMINOLOGY -eq 1 ^ /dev/null
    set -g theme_nerd_fonts yes
    set -g theme_color_scheme gruvbox
else
    set -g theme_color_scheme terminal2-light-black
end

set -g theme_display_date no
set -g theme_display_cmd_duration no
set -g theme_title_display_process yes
set -g theme_show_exit_status yes
set -g fish_prompt_pwd_dir_length 5
set -x HASTE_SERVER "https://haste.charlesmilette.net"
set -x THEFUCK_OVERRIDDEN_ALIASES "git"

alias su="sudo su"
alias ls="ls --color -A"
alias grep="grep --color"


eval (hub alias -s)
