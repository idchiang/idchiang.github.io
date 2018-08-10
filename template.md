### Python templates
I will keep some python templates that might be useful for scientific usage here.

## Click and examine!
[clicking]: https://github.com/idchiang/templates/raw/master/clicking/example.png

Sometimes, we are interested in examine the properties of our object in some specific regions, i.e., plotting the fit results versus original observation, and/or plotting the probability distribution function at that pixel. This template offers an interactive clicking system: it can read the coordinate user clicks on the first axis, and use that coordinate to do other things.

Here is an example: when the user clicks somewhere in the left panel (makred by the cyan star), the code reads the x-y coordinates, and uses them to plot a sine function. I am sure you can come up with something more useful than a sine function!

![Example for ][clicking]

<a href="https://github.com/idchiang/templates/blob/master/clicking/clicking.py" target="_blank">[Link to the template]</a>
