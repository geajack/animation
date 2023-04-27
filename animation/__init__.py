import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import pygame.gfxdraw as gfxdraw
import cv2


class StopAnimation(Exception):
    pass


def animate(render, fps, window_width, window_height, silent=None, preview=True, filename=None):
    pygame.init()

    if filename is not None:
        video_writer = cv2.VideoWriter(
            filename,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (window_width, window_height),
        )

    if preview:
        flags = pygame.SHOWN
        clock = pygame.time.Clock()
    else:
        flags = pygame.HIDDEN

    if silent is None:
        silent = preview

    surface = pygame.display.set_mode((window_width, window_height), flags)
    running = True
    rendering = True
    n_frames = 0
    try:
        while running:
            if preview:
                clock.tick(fps)

            if rendering:
                try:
                    render(surface)
                except StopAnimation:
                    rendering = False
                    if not preview:
                        running = False
                pygame.display.flip()
            
            if filename is not None:
                buffer = pygame.surfarray.array3d(surface)
                video_writer.write(cv2.transpose(buffer[:, :, ::-1]))

            n_frames += 1
            seconds = n_frames / fps
            if not silent:
                print(f"\rframe {n_frames} - {seconds:.2f}s", end=" " * 20 + "\r")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    finally:
        if filename is not None:   
            video_writer.release()