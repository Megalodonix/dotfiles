[ -f /etc/xprofile ] && source /etc/xprofile
[ -f ~/.xprofile ] && source ~/.xprofile

dwmblocks &
play ~/SoundFiles/Synchedit.mp3 &
exec dwm
