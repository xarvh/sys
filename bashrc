export HISTCONTROL=ignoreboth
export PYTHONSTARTUP=$HOME/dati/sys/pythonstartup.py

DRed="\[\033[00;31m\]"
LRed="\[\033[01;31m\]"
Blue="\[\033[01;34m\]"
Norm="\[\033[00m\]"

PS1=$LRed"\u"$DRed"@"$LRed"\h"$DRed":"$Blue"\w"$DRed"\$"$Norm" "
unset DRed LRed Blue Norm

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias me='vim'
alias yd='youtube-dl -t'
alias t='less -Q $HOME/dati/tel/telefoni'

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

alias ack='ack-grep -a'
alias v='vim'
alias b='bundle exec'
alias 192='rvm use 1.9.2'


PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
