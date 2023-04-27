# Animation

This is a CLI tool for creating animations in Python and saving them as video files.

## API

Create a Python file with a function in it called `render`. This function should accept as an argument a PyGame Surface object and draw a single frame to that surface. The function will have to keep track itself of what frame it's on using global variables, or you can make it a method of a class like this:

```python
class Renderer:

    def render(surface):
        ...

render = Renderer().render
```

The function does not necessarily have to be called `render` as long as you tell the tool the name of the function using the CLI.

Your render function can optionally raise a `animation.StopAnimation` exception to signal the animation is over.

## CLI

Where `my_animation.py` is the file containing your render function, simply run `animate my_animation` to show a preview of the animation. The animation module can also be in a subpackage, called like `animate my_package.my_animation`, and the render function can be called something else, specified with a colon as in `animation my_package.my_animation:draw_frame`.

Pass a filename with `--o` to save the animation as an mp4. Pass `--np` to hide the preview and encode the video in the background - rendering will stop and the script will exit when your render function raises a `StopAnimation` or any other exception.

# Installation

```
pip install git+https://github.com/geajack/animation
```