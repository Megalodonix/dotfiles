function fish_prompt

	echo -e "╭─($(whoami)@$(hostnamectl hostname))──[ $(prompt_pwd) ] $(fish_git_prompt)"
	echo -e "╰─λ "
end
