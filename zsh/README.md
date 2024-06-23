# Please
## Please read before cloning into your `~/.config`

## About the files here:

### zshrc
Please make sure you have the environment variable:\
`export ZDOTDIR="~/.config/zsh"`\
Otherwise your zshrc won't get sourced.\
Then make sure you have a `.zshrc` file inside the `.config/zsh` dir that sources the already existing `zshrc`

### zsh-functions
This file contains a script that drastically speeds up the tedious process of\
managing plugins in zsh.\
\
Syntax goes like this:
- `zsh-add-file`: sources a file from the zsh config dir
    - `zsh-add-file "zsh-exports"`
    - `zsh-add-file "zsh-aliases"`
- `zsh-add-plugin`: clones a plugin from the repo name to the `plugins` dir and sources it
    - `zsh-plugin-add "zsh-users/zsh-autosuggestions"`
- `zsh-add-completion`: adds a completion plugin. you only need it for `zsh-completions`

### zsh-exports
Contains needed exports and environment variables, needed for programs like zoxide to work
### zsh-aliases
Contains custom aliases, feel free to change
### zsh-prompt
Contains a custom prompt, with a script to display Git status\
The prompt can be changed accordingly.
