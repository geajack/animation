# Animation

This is a CLI tool for creating animations in Python and saving them as video files.

## API

Create a Python file with a function in it called which accepts as an argument a PyGame Surface object and draw a single frame to that surface:

```
import pygame.draw

def render(surface):
    pygame.draw.rect(canvas, (255, 255, 255), (0, 0, 800, 800))
    # see https://www.pygame.org/docs/ref/draw.html
    # and https://www.pygame.org/docs/ref/gfxdraw.html
    # for the full API
```

The render function can be any Callable, so it can be e.g. a class method if you like. Your render function can optionally raise a `animation.StopAnimation` exception to signal the animation is over. Note that the frame during which the `StopAnimation` was raised will still be rendered (e.g. it will still be part of the video file if you generate a video).

To actually display the animation, use the library programmatically or use the CLI (see below). To use the library directly in your script, just call `animate`:

```
animate(render, fps, window_width, window_height, silent=None, preview=True, filename=None)
```

Where `render` is your render function, `fps` is your target FPS, and `window_width`/`height` are the video dimensions in pixels. If `filename` is set, a video will be saved as an MP4. If `preview` is True, a window will also show up displaying your animation. Note that the preview windwo might not achieve your target framerate if the animation is compute-heavy, but the saved video file will always be at the right framerate. If `silent` is False, a log will be displayed in the console showing the current frame and elapsed time. By default `silent` is False if and only if `preview` is False.

## CLI

Where `my_animation.py` is the file containing your render function called `render`, simply run `animate my_animation` to show a preview of the animation. The animation module can also be in a subpackage, called as `animate my_package.my_animation`, and the render function can be called something else, specified with a colon as in `animation my_package.my_animation:draw_frame`.

Pass a filename with `--o` to save the animation as an mp4. Pass `--np` to hide the preview and encode the video in the background - rendering will stop and the script will exit when your render function raises a `StopAnimation` or any other exception. You can also set the width, height, and FPS - just run `animate --help` to learn more.

# Installation

```
pip install git+https://github.com/geajack/animation
```
