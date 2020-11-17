# Foxmote

Yet another XBMC remote for firefox os,
built using [AngularJS](http://angularjs.org/), [Node](http://nodejs.org/) and [Grunt](http://gruntjs.com/).

***

## Purpose

Foxmote is an XBMC remote that let you control XBMC with your firefox os phone. It is powered with some of the most trendy, popular frameworks around.

## Stack

* [AngularJS](http://www.angularjs.org/) power the application
* Beautiful styles using [LESS css](http://lesscss.org/) and [Font-Awesome](http://fortawesome.github.io/Font-Awesome/)

### Build

Build system focused on AngularJS apps and tightly integrated with other tools commonly used in the AngularJS community:
* powered by [Grunt.js](http://gruntjs.com/)
* build supporting JS, CSS and AngularJS templates minification

## Installation
### Platform & tools

You need to install Node.js and then the development tools. Node.js comes with a package manager called [npm](http://npmjs.org) for installing NodeJS applications and libraries.
* [Install node.js](http://nodejs.org/download/) (requires node.js version >= 0.8.4)
* Install Grunt-CLI as global npm modules:

    ```
    npm install -g grunt-cli
    ```

### Application Server

When testing with your browser (Chrome, Firefox) you will need to use our backend application server (using nodejs).  Please follow the below steps :

* Install local dependencies:

    ```
    cd server
    npm install
    cd ..
    ```

### Client Application

Our client application is a straight HTML/Javascript application but our development process uses a Node.js build tool
[Grunt.js](gruntjs.com) and [Bower](https://github.com/bower/bower) to retrieve 3rd party dependencies. Grunt relies upon some 3rd party libraries that we need to install as local dependencies using npm.

* Install local dependencies:

    ```
    cd client
    npm install
    cd ..
    ```

## Building

The application made up of a number of javascript, css and html files that need to be merged into a final distribution for running.  We use the Grunt build tool to do this.
Build client application with:

    ```
    cd client
    grunt build
    ```

*Note : It is important to build again if you change files in under client directory.
 You can avoid this painful process by using continuous building see dedicated section.*

## Running
### Start the Server
Run the server with :

    ```
    cd server
    node server.js
    ```

Your browser should automatically open at the following URL [http://localhost:8082] letting you use the application. Of course you can manually navigate to this URL at any time.*

## Development
### Folders structure
At the top level, the repository is split into a client folder and a server folder.  The client folder contains all the client-side AngularJS application.  The server folder contains a very basic webserver that delivers and supports the application while using a desktop browse (not needed when app is added to the firefox os emulator).
Within the client folder you have the following structure:
* `dist` contains build results
* `src` contains application's sources
* `vendor` contains external dependencies for the application

### Default Build
The default grunt task will build the application.

    ```
    cd client
    grunt
    ```

### Continuous Building
The watch grunt task will monitor the source files and run the default build task every time a file changes.

    ```
    cd client
    grunt watch
    ```

### Building release code, aka create a zip file ready for firefox os marketplace upload
You can build a zipped release version of the app, with minified files using a dedicated grunt task.

    ```
    cd client
    grunt marketplace
    ```

### Using Firefox OS Simulator

Once application is build you can add it to firefox os simulator. To do so :
* Be sure firefox os simulator is installed. Instruction [here](https://addons.mozilla.org/en/firefox/addon/firefox-os-simulator/)
* Open firefox and navigate to Firefox > Web Developer >  Firefox os Simulator
* On the Firefox os Simulator page click on add directory
* Navigate to the dist folder under client directory
* Select manifest.webapp
* Emulator should start and application run
