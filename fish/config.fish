if status is-interactive
    # Commands to run in interactive sessions can go here
    #and not set -q TMUX
#    exec tmux
end

source ~/.config/fish/functions/zoxide.fish

function def_prompt
    #colors (TokyoNight)
    set -l foreground c8d3f5
    set -l selection 2d3f76
    set -l comment 636da6
    set -l red ff757f
    set -l orange ff966c
    set -l yellow ffc777
    set -l green c3e88d
    set -l purple fca7ea
    set -l cyan 86e1fc
    set -l pink c099ff

    # Prompt
    set_color -d
	echo -ne "╭─"
    set_color reset
    #set_color white
    echo -ne "("
    set_color reset
    #set_color fff
    echo -ne "$(whoami)"
    #set_color fff -d
    echo -ne "@"
    set_color reset
    #set_color fff
    echo -ne "$(hostnamectl hostname)"
    #set_color white
    echo -ne ")"
    set_color -d
    echo -ne "──"
    set_color reset
    echo -ne "["
    set_color reset
    #set_color fff
    echo -ne "   "
    #set_color white
    echo -ne "]"
    set_color -d
    echo -ne "──"
    set_color reset
    echo -ne "[ "
    #set_color fff
    echo -ne "$(prompt_pwd)"
    #set_color white
    echo -ne " ]"
    set_color $pink -oi
    echo -e "$(fish_git_prompt)"
    set_color reset
    set_color -d
	echo -ne "╰─"
    set_color reset
    echo -ne "λ "
end

function minimal_prompt
    set_color -o 81a1c1
    echo -ne "$(prompt_pwd)"
    set_color a3be8c
    #❱❱❱
    echo -ne " ❱ "
    set_color reset
end

function fish_prompt
    def_prompt
end

function fish_greeting
	echo "" && neofetch
end

thefuck --alias | source

alias ls="eza --icons=always --color=auto"
alias please="sudo"
alias cat="bat"
alias vicecity="cd ~/.reVC && reVC"
alias vim="nvim"
alias pamcan='echo "You misspelled it, silly :P"'

set -Ux EDITOR nvim
set -Ux QT_QPA_PLATFORMTHEME qt5ct
set -Ux GEM_HOME $(ruby -e 'puts Gem.user_dir')
set -Ux PATH $PATH:$GEM_HOME/bin

function colorscheme
    source ~/.config/fish/themes/nord.fish
end

colorscheme
