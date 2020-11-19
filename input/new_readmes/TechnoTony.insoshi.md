# Insoshi social software

NOTE: If you downloaded a zipped archive of Insoshi, we strongly encourage you to clone the Insoshi Git repository instead.  See the instructions below, and also see

http://sites.google.com/a/insoshi.com/insoshi-guides/Installation

for more details.

To follow our progress, join the Insoshi developer community site at 

http://dogfood.insoshi.com/signup

and join the Insoshi Google group at

http://groups.google.com/group/insoshi/subscribe


## Get Git

The source code to Insoshi is managed via Git, a version control system developed by Linus Torvalds to host the Linux kernel.  

The first step is to install it from here:

http://git.or.cz/

Linux and Mac users should have no problems; Windows users might have to install Cygwin (http://cygwin.com/) first.

For more detailed information, check out our guide for Installing Git under Git Guides at

http://docs.insoshi.com

## Install libraries and gems

### Libraries

You'll need to install FreeImage or some other image processor (such as ImageMagick/RMagick), SQLite, and (optionally) MySQL.  Install instructions for all three are easy to find using Google.

### Gems

You probably have Rails already, but might not have the others.

$ sudo gem install rails
$ sudo gem install ferret
$ sudo gem install sqlite3-ruby
$ sudo gem install mysql

If you're using FreeImage/ImageScience, you'll also need the image_science gem:

$ sudo gem install image_science


## Installing the app

Here are the steps to get up and running with the Insoshi Rails app.

### Git steps

Our public Git repository is hosted on GitHub and can be viewed at

http://github.com/insoshi/insoshi

You can clone the the repository with the command

$ git clone git://github.com/insoshi/insoshi.git

The clone make take a moment to complete (mainly due to the frozen Rails gems).

Then make a local Git branch for yourself:

$ git checkout -b <local_branch>

where you should replace <local_branch> with the name of your choice (without angle brackets!).  

For more information on configuring your local clone of our repository, check out our Git Guides at

http://docs.insoshi.com

which also includes a scripted Quick Local Repository Setup.

### Config files and tests

You will to set up your database configuration.  If you're using SQLite, you can just copy the example file

$ cp config/database.example config/database.yml

If you're using MySQL, you'll need to create a configure the database.yml manually.  The easiest way is to copy and modify one from an existing Rails application or from a new Rails project that explicitly uses MySQL (rails -d mysql <mysql project>).

Run the following custom rake task

$ rake install

The install rake task runs the database migration and performs some additional setup tasks (generate an encryption keypair for password management, creating an admin account, etc.)

If the install step fails, you may not have properly set up the configuration files.

Then prepare the test database and run the tests (which are actually RSpec examples in the spec/ directory):

$ rake db:test:prepare
$ rake spec

If the tests fail in the Photos controller test, double-check that an image processor is properly installed.

### Loading sample data

Now load the sample data and start the server:

$ rake db:sample_data:reload
$ script/server

The rake task loads sample data to make developing easier.  All the sample users have email logins <name>@example.com, with password foobar.  

Go to http://localhost:3000 and log in as follows:

email: michael@example.com
password: foobar

### Admin user

To sign in as the pre-configured admin user, use

email: admin@example.com
password: admin

You should update the email address and password.  Insoshi will display warning messages to remind you to do that.

To see site preferences such as email settings, click on the "Admin view" and the click on "Prefs" in the menu.  Click the "Edit" link to customize the preferences for your particular site.

### Start hacking

Now open the source code with your favorite editor and start hacking!

Check out our Git Guides for information on how to manage your local development and how you can contribute your updates back to us:

http://docs.insoshi.com

## Stat tracker

Note that there is a minimalist stat tracker that lets us keep track of how many different installs of Isoshi are out there.  We don't collect any personal information, but if you don't want to be tracked just open application.html.erb and comment out the line after this one:

<%# A tracker to tell us about the activity of Insoshi installs %>

## License

See the file LICENSE.