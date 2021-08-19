import os
import subprocess
import sys

from IO import IOManager
from UI import UIManager,print_color_coded_text
from EVAL import EvalManager

# defaults ..
ENV_PATH = os.path.join(os.curdir, "env")
LANGUAGE = "cpp"
TEMPLATES_PATH = os.path.join(os.curdir, "template.cpp")

# initialising objects..
IO = IOManager()
UI = UIManager()
Eval = EvalManager(LANGUAGE)


# setup
def setup():
    return IO.setup


def print_output():
    with open(os.path.join(ENV_PATH, "output.txt"), "r") as f:
        print("output : ")
        print(f.read())
        UI.draw_line()

def print_input(inp):
    with open(os.path.join(ENV_PATH,inp),"r") as f:
        print_color_coded_text("Input : ","r")
        print()
        print_color_coded_text(f.read(),"r")

# main loop
while True:
    UI.show_status()

    raw_args = input()
    args = raw_args.split(" ")

    # length 1 args ..
    if len(args) == 1:
        if args[0] == "setup":
            ENV_PATH, LANGUAGE, TEMPLATES_PATH = setup()
            print(ENV_PATH, LANGUAGE)

        elif args[0] == "start":
            IO.start(ENV_PATH)

        elif args[0] in {"a", "b", "c", "d", "e", "f", "g"}:
            IO.make_from_template(f"{args[0]}.{LANGUAGE}", ENV_PATH, TEMPLATES_PATH)

        elif args[0] == "in":
            IO.get_input(ENV_PATH)

        elif len(args[0].split("in")) == 2 and args[0].split("in")[1].isnumeric():
            IO.get_mult_input(args[0], ENV_PATH)

        elif args[0] in {"quit", "q", "qq", "exit"}:
            sys.exit(0)

        elif args[0] in {"clear", "clr"}:
            subprocess.call('clear')

        elif args[0] in {"man", "help", "h"}:
            subprocess.call('clear')
            UI.man()

        else:
            UI.badcmd()

    elif len(args) == 2:
        if args[0] in {"clear", "clr"}:
            if args[1] in {"input", "in"}:
                IO.clear_in(ENV_PATH)

        if args[0] == "run":
            if Eval.compile(args[1], ENV_PATH):
                UI.draw_line()
                if Eval.run("input.txt", ENV_PATH):
                    print_input("input.txt")
                    print_output()

    elif len(args) == 3:
        if args[0] in {"run"}:
            if not Eval.compile(args[1], ENV_PATH):
                break
            if args[2] == "all":
                UI.draw_line()
                for f in os.listdir(ENV_PATH):
                    if f.startswith("in") and Eval.run(f, ENV_PATH):
                        print_input(f)
                        print_output()
            else:
                UI.draw_line()
                if Eval.run(args[2] + ".txt", ENV_PATH):
                    print_input("input.txt")
                    print_output()
