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


## Usage

Use Package Control as usual.  After making changes, commit the results.
On your other machines, just `(cd ~/.sublimetext; git pull)` to bring them
in sync.  Easy!

## Notes/Guesses

Only the `Packages` directory is versioned.  `Settings` shouldn't be shared
since it tracks settings local to this computer (recent files, window
layouts, etc), `Installed Packages` doesn't seem to be used,
and `Pristine Packages` doesn't seem to be worth versioning (?).

