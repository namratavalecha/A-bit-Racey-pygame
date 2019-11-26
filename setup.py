from cx_Freeze import setup, Executable

base = None

executables = [Executable("basic_pygame.py", base = base)]

packages = ["pygame"]

options = {
        'build_exe': {
            'packages':packages,
            'include_files':['/home/namrata/A bit Racey/racecar.png',
                            '/home/namrata/A bit Racey/crash.wav',
                            '/home/namrata/A bit Racey/jazzpiano.wav'],
            },
        }

setup(
        name = "basic_pygame.exe",
        option = options,
        version = "0.1",
        description = "A car game",
        executables = executables
        )
