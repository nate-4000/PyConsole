import random

ver = "v1.1 release"
whatsnew = """Added motd command
Better support for cd; no funky error messages"""
motd = [
    "Also avaliable on pastebin!",
    "Type whatsnew to get latest changelog!",
    "When do we get a color update?",
    "WSL is still better!",
    "type cd \"%%\" i dare you",
    "Don't forget: $0 | $0 is a virus!",
    "hehe command go brrr",
    "hehe \"format c: /P:0 /FS:ntfs\" go brrr",
    "Is it just me or did the code get longer when I added these?",
    "String indice out of range",
    "Replying to motd[2]: We did! You just don't see color often in a terminal"
    ]

print("PyConsole " + ver)
print(random.choice(motd))
print()

import os

exit = False
while not exit:
    try:
        path = os.getcwd()
        comm = input("PyCon " + path + "> ")
        if comm == "exit":
            exit = True
            print("Exiting")
        elif comm.startswith("cd "):
            comm = comm.removeprefix("cd ")
            try:
                os.chdir(comm)
            except BaseException:
                os.system('cd ' + comm)
            print()
        elif comm == "whatsnew":
            print("\n" + ver)
            print(whatsnew)
        elif comm.startswith("format ") and (comm.__contains__('c:') or comm.__contains__('C:')) and os.name == 'nt':
            print("""Were you really trying to kill this computer?
You know I won't let you do that.""")
        elif comm.startswith("motd "):
            comm = comm.removeprefix("motd ")
            try:
                print(motd[int(comm)])
            except IndexError:
                print("That isn't a valid motd.")
            except BaseException:
                print("That isn't a number.")
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
