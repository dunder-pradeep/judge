from colorama import Fore,Back,Style

def print_color_coded_text(string,color,end="",sp = 0):
    sps = sp*" "
    if color == "r":
        print(f"{sps}{Fore.RED}{string}",end=end)
    elif color == "g":
        print(f"{sps}{Fore.GREEN}{string}",end=end)
    elif color == "y":
        print(f"{sps}{Fore.YELLOW}{string}",end=end)
    print(Style.RESET_ALL,end="")

class UIManager:
    def __init__(self):
        self.status = "[judge] : "
        self.cur_code = 1

    def show_status(self):
        print( (Fore.GREEN if self.cur_code == 1 else Fore.RED) + self.status,end = "")
        print(Style.RESET_ALL,end = "")

    def man(self):
        print("PYJUDGE 1.0")
        print("1. 'help/man' wil open up this menu. ")
        print("2. single letter cmd is used to create a file from template. ")
        print("3. 'quit/qq/q/exit' will exit the judge. ")
        print("4. 'clear/clr' to clear screen.")
        print("5. 'in' is used to take input.(NOTE:if input.txt is not empty then multiple tests will not run..!)")
        print("6. 'clear input' deletes the input file so multi tests can run.")

    def badcmd(self):
        print("bad command refer man")

    def draw_line(self):
        print()
        print_color_coded_text("#"*60,"y")
        print()