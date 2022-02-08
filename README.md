# python-logger
a simple python logger

# how to use

* ### downloading the logger and installing required libraries

1. install the colorama library
2. download the logger and add ikt to your project
3. import the logger using `import logger`
* ## personalizing the logger

1. to toggle the logging of levels you can change the `logLevel` from true to false
2. to color the level identifier you can switch the `colorLevelText` variable from false to true
3. if you wish to change the default color of a level you can do that by altering the colour variables(warnColor, infoColor, debugColor, ect.) in the file
4. the logger executes the quit() function when a fatal is logged if you wish to switch that off you can switch the **quitWhenLogFatal** variable from true to false
* ## adding additional levels

1. to add custom levels create an instance of the `CustomLogLevel` class, for this you need to provide a name, a color(optional), and is the level used for fatal errors(optional)
2. e.g. `CustomLevel = logger.CustomLogLevel("CUSTOM", Fore.GREEN, False)` NOTE: if you don't provide the `color` parameter it will be set to the default color of your IDE or console, if you don't provide the `isFatal` parameter it will be set to false
3. to log the custom level you can use the `log` method of the class e.g. `CustomLevel.log("custom message")`

