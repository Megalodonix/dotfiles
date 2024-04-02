# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

rofi = os.path.expanduser("~/.config/rofi/launchers/type-6/launcher.sh")
printscr = os.path.expanduser("~/.config/rofi/applets/bin/screenshot.sh"),

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "mod1"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "mod1"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.group.setlayout("max"), desc="Switch to max layout"),
    Key([mod], "c", lazy.group.setlayout("columns"), desc="Switch to columns layout"),
    Key([mod], "z", lazy.group.setlayout("zoomy"), desc="Switch to zoomy layout"),
    Key([mod], "p", lazy.spawn(rofi), desc="Run Rofi"),
    Key([], "Print", lazy.spawn(printscr), desc="Print screen"),
    Key([mod], "e", lazy.spawn("pcmanfm-qt"), desc="File Manager")

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=["#c0caf5"],
        border_normal=["#414868"],
        margin=10,
        border_width=1),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    layout.MonadTall(),
    #layout.MonadWide(),
    layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font="Minerva Modern",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

powerline = {
        "decorations": [
        PowerLineDecoration(path="forward_slash")
                        ],
        "padding": 10,
        }

rectdeco = {
        "decorations": [
        RectDecoration(padding_y=1, filled=True, radius=10, extrawidth=6, colour="#72ffff", group=False)
        ],
        "padding": 10,
        "foreground": "#03163e"
}

rectdecoAlter = {
        "decorations": [
        RectDecoration(padding_y=1, filled=True, radius=10, extrawidth=6, colour="#168ce6", group=False)
        ],
        "padding": 10,
}

powerlineAlter = {
        "decorations": [
        PowerLineDecoration(path="back_slash")
                        ],
        "padding": 10,
        }

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(background="#000000", **powerline),
                widget.GroupBox(background="#0316b0", **powerline, active="#fefefe", inactive="#70fffa", highlight_method="line", fontsize=14, this_current_screen_border="#0850bc"),
                widget.Prompt(background="#81ffff", **powerline, prompt="Summon: ", foreground="#0316b0"),
                widget.WindowName(background="#ffffff",
                                  foreground="#084bbc",
                                  scroll=True,
                                  max_chars=0,
                                  width=350,
                                  scroll_clear=False,
                                  scroll_delay=1,
                                  scroll_step=2,
                                  **powerline),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.TextBox(**powerlineAlter),
                widget.Cmus(**powerlineAlter, play_color="#fefefe", background="#0850bc", format="󰝚   {title}", fontsize=16),
                widget.Systray(**powerlineAlter, background="#fefefe"), 
                widget.Clock(format="󰞌  %b %d %a %I:%M %p",**powerlineAlter, background="#0316b0", fontsize=16, foreground="#fefefe"),
                widget.Volume(fmt='  󰕾    {}  ', volume_app="pavucontrol", background="#000", fontsize=14, foreground="#fefefe"),
                ],
            22,
            background = "#1da0fb",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=["#c0caf5"],
    border_normal=["#414868"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Gimp-2.10"),
        Match(wm_class="Gthumb"),
        Match(wm_class="Lutris"),
        Match(wm_class="mpv"),
        Match(wm_class="TelegramDesktop"),
        Match(title="QtAppLol")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "UltraBasedWM"

"""
Custom config yayyyyyy
I'm so retarded
"""

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostartONCE.sh')
    subprocess.Popen([home])
