# plex-structure-gen

Plex Structure Generator builds a file structure to meet Plex suggested formatting. Built with Qt (Pyside2).

## Plex Formatting rules
[Movies](https://support.plex.tv/articles/naming-and-organizing-your-movie-media-files/)
[TV Shows](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/)
[Media Assets](https://support.plex.tv/articles/200220677-local-media-assets-movies/)

## Data Providers

Create a JSON file named `credentials.json` in the project root with the following structure:
```json
{
    "tmdb": {
        "key": ""
    },
    "imdb": {
        "key": ""
    },
    "tvdb": {
        "key": ""
    }
}
```

### TMDB

Uses [tmdbsimple](https://github.com/celiao/tmdbsimple).

### IMDB

Not implemented.

### TVDB

Not implemented.

## Notes

Use `pyside2-uic.exe` to convert `.ui` files to Python classes.