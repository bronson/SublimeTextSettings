# DELETED

Now using ST3 here: https://github.com/bronson/Sublime-3-Settings


# Sharing Sublime Text 2 Settings via Git

This keeps [Sublime Text 2's](http://www.sublimetext.com/)
settings consistent across multiple computers.
(I've only tried Mac so far but Linux will come soon)

These settings are mostly for editing JavaScript, Ruby/Rails, and C/C++.
The list of installed packages is in the [Package Control settings](https://github.com/bronson/SublimeTextSettings/blob/master/Packages/User/Package%20Control.sublime-settings).
I also [use vim](https://github.com/bronson/dotfiles/blob/master/.vimrc).


## Installation

### Mac

(untested, something like this...)

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/
    git clone git://github.com/bronson/SublimeTextSettings.git
    mv SublimeTextSettings/.git .
    rm -rf SublimeTextSettings
    git status                  # shows changes that we're about to make
    git reset --hard HEAD       # start using upstream settings

Running `ln -s '~/Library/Application Support/Sublime Text 2' ~/.sublimetext`
makes it easier to access your settings directory.

### Linux

(todo)

~/.config/SublimeTextSettings on Linux or "~/Library/Application Support/Sublime Text 2" on Mac

## Usage

Use Package Control as usual to add and remove packages.  After making
changes, commit the results.  On your other machines, just
`(cd ~/.sublimetext; git pull)` to bring them in sync.  Easy!


## Key Bindings

All stock with Vintage mode enabled.  Here are Notable bindings
from installed plugins:

#### Testing

- Command-Shift-R: run single ruby test under cursor
- Command-Control-Shift-R: run all Ruby tests in current file
- Command-Shift-E: run last ruby test   (is this useful?)
- Command-Shift-X: show test panel (would be nice if this toggled the test panel)
- Command-Period: switch between code and test (add ctrl to open in new split)

No need for verify keybinding -- SublimeLint does that.

#### Misc

- Command-K Command-F: reeveal current file in sidebar (like Cmd-K Cmd-B toggles sidebar)


## Notes/Guesses

Only the `Packages` directory is versioned.  `Settings` shouldn't be shared
since it tracks settings local to this computer (recent files, window
layouts, etc), `Installed Packages` doesn't seem to be used,
and `Pristine Packages` doesn't seem to be worth versioning (?).

## Living with Sublime

#### Don't memeorize keyboard shortcuts

That's a big time sink, locks you in, and exposes you to oddball
platform and package author choices.  Instead, learn the
bare minimum to navigate and edit quickly, then use the Command Palette
(command-shift-P) for everything else.  For example, don't learn whatever
random press the Markdown Preview package uses, just hit "Cmd-Shift-P
md".  Markdown Preview will be the top command, then you just hit return.

If you do something all the time (like switching between tabs), the
quickest way to find the keyboard shortcut is to go Preferences ->

