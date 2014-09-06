Title: My tmux settings explained
Author: Unni
Date: 2014-09-03
Tags: tmux, dotfiles
Category: tmux
Status: draft
Summary: Tmux settings making my tmux aowesome

I am using tmux for almost 2 years now. I was using and a big fan of screen before that. But screen was replaced by tmux from the moment one of my colleages introduced me to a more actively deleoped tmux.

Here I am documenting my Tmux configuration. Full configuration file is stored at [Github](https://github.com/webofunni/dotfiles/blob/master/tmux/tmux.conf)

	::text
	#Use screen key combination
	unbind C-b
	set -g prefix C-a
	bind C-a send-prefix

Above settings will replace defualt prefix for tmux from Ctrl+b or CMD+b to Ctrl+a or CMD+a. It also binds Ctrl+a+Ctrl+a or CMD+a+CMD+a to send prefix to multiplexer running under tmux such as screen.
