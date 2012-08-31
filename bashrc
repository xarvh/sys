export HISTCONTROL=ignoreboth
export PYTHONSTARTUP=$HOME/dati/sys/pythonstartup.py

DRed="\[\033[00;31m\]"
LRed="\[\033[01;31m\]"
Blue="\[\033[01;34m\]"
Norm="\[\033[00m\]"

PS1=$LRed"\u"$DRed"@"$LRed"\h"$DRed":"$Blue"\w"$DRed"\$"$Norm" "
unset DRed LRed Blue Norm

alias ls='ls --color=auto'
alias yd='youtube-dl -t'
alias grep='grep --color=auto'

alias mp='m_playlist.sh'
alias md='m_playlist.sh --sort'
alias mr='m_playlist.sh --new'
alias ml='playlist.player $HOME/.playlist'

alias pinstall='sudo apt-get install'
alias psearch='apt-cache search'
alias premove='sudo apt-get --purge remove'

alias rmrm="rm -r"
alias dd="du -sh"
alias pp="python -B"

alias ga='git add'
alias gst='git status'
alias gbr='git branch'
alias gco='git checkout'
alias gcm='git commit -m'

alias ack='ack-grep'
alias ff='find * |grep --ignore-case'
alias v='vim'
alias b='bundle exec'


PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
