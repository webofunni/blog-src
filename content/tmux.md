Title: My tmux settings explained
Author: Unni
Date: 2014-09-03
Tags: tmux, dotfiles
Category: tmux
Summary: Tmux settings making my tmux aowesome

I am using tmux for almost 2 years now. I was using and was a big fan of screen before that. But screen was replaced by tmux from the moment one of my colleague introduced me to a more actively developed tmux.

Here I am documenting my Tmux configuration. Full configuration file is stored at [Github](https://github.com/webofunni/dotfiles/blob/master/tmux/tmux.conf)

	::text
	#Use screen key combination
	unbind C-b
	set -g prefix C-a
	bind C-a send-prefix

Above settings will replace default prefix for tmux from Ctrl+b or CMD+b to Ctrl+a or CMD+a. It also binds Ctrl+a+Ctrl+a or CMD+a+CMD+a to send prefix to multiplexer running under tmux such as screen.

	::text
	#Some easy key combination to Split window
	bind | split-window -h
	bind - split-window -v

Now its time to change the keyboard short cut to Prefix + | for vertical split and Prefix + - for horizontal split.

	::text
	#Easily reload configuration
	bind r source-file ~/.tmux.conf \; display "Reloaded!!!"

Easily reload the configuration file using Prefix+r

	::text
	#Change starting window index to 1 from 0
	set -g base-index 1

	#Monitor activity in windows
	setw -g monitor-activity on 
	set -g visual-activity on

Change the window index from 0 to 1 and keep monitor activity on each window.

	::text
	# status bar colors
	set -g status-fg white 
	set -g status-bg black

	set -g status-left-length 40
	set -g status-left "#[fg=green][#[fg=yellow]#S #[bg=black,fg=cyan]Win: #[fg=yellow]#I #[fg=cyan]Pane: #[fg=yellow]#P#[fg=green]]"

	set -g status-right "#[fg=green][#[fg=cyan]%d %b %R#[fg=green]]"

	## window list options
	setw -g window-status-fg cyan 
	setw -g window-status-bg default 
	setw -g window-status-attr dim
	setw -g window-status-current-fg white 
	setw -g window-status-current-bg red
	setw -g window-status-current-attr bright
	setw -g automatic-rename on
	set-window-option -g window-status-format '#[fg=green][#[fg=cyan,dim]#I#[fg=blue]:#[default]#W#[fg=grey,dim]#F#[fg=green]]'
	set-window-option -g window-status-current-format '#[bg=red,fg=cyan,bold][#I#[bg=red,fg=cyan]:#[fg=colour230]#W#[fg=dim]#F#[bg=red,fg=cyan]]'

Above settings will format the status bar at bottom. Below screenshot shows the left side of statusbar.

![Alt text](/blog/theme/images/tmux-left.png)

Above status bar is from a tmux session with name dev. 

	::bash
	tmux new -s dev

As you can see left side of status bar shows tmux session name, number of windows, number of panes and window list. You can see that window index start from 1 instead of default zero and active window background is red.

Right side of the statusbar is set to show the the date. 

	::text
	set -g status-right "#[fg=green][#[fg=cyan]%d %b %R#[fg=green]]"

Result will look like : 

![Alt status bar right](/blog/theme/images/tmux-right.png)

Thats all about my Tmux settings :)
