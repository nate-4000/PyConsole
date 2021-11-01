import random

ver = "v1.0 release"
whatsnew = """Added support for formatting drives
Added this feature and the greeting messages
Added version numbers"""
motd = [
    "Also avaliable on pastebin!",
    "Type whatsnew to get latest changelog!",
    "When do we get a color update?",
    "WSL is still better!",
    "type cd \"%%\" i dare you",
    "Don't forget: $0 | $0 is a virus!",
    "hehe command go brrr",
    "hehe \"format c: /P:0 /FS:ntfs\" go brrr"
    "Is it just me or did the code get longer when I added these?"
    ]

print("PyConsole " + ver)
print(random.choice(motd))
print()

import os

exit = False
while not exit:
    try:
        path = os.getcwd()
        comm = input(path + "> ")
        if comm == "exit":
            exit = True
            print("Exiting")
        elif comm.startswith("cd "):
            comm = comm.removeprefix("cd ")
            try:
                os.chdir(comm)
            except FileNotFoundError:
                print("That file or directory doesn't exist here.")
            except OSError:
                print("Are you sure that's a folder?")
            print()
        elif comm == "whatsnew":
            print("\n" + ver)
            print(whatsnew)
        elif comm.startswith("format c:"):
            print("""Were you really trying to kill this computer?
You know I won't let you do that.""")
        else:
            os.system(comm)
            print()
    except KeyboardInterrupt:
        print("^C")
    except EOFError:
        pass
    except BaseException as err:
        try:
            print(f"Could not execute command\n{err=}\n{type(err)=}")
        except BaseException:
            print("Failed generating error message")