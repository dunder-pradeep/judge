import os
import shutil


# IO helpers ..

class IOManager:
    def __init__(self):
        pass

    def parse_config(self):
        pass

    def create_config(self):
        pass

    def start(self, ENV_PATH):
        if os.path.exists(ENV_PATH):
            print("Are you sure (y/n) : ")
            if input() in {"n","no"}:
                return
            shutil.rmtree(ENV_PATH)
        os.mkdir(ENV_PATH)

    def setup(self):
        print("WELCOME TO JUDGEPY  .. UWU")
        print("Enter the path to env (0 -- > default): ")
        env_path = input()
        print("Enter language choice : ")
        lang = input()
        print("Enter path to templates : ")
        temp_path = input()
        return env_path, lang, temp_path

    def make_from_template(self,FNAME,ENV_PATH,TEMP_PATH):
        if os.path.exists(os.path.join(ENV_PATH,FNAME)):
            print("Similar file exists Do you want to delete it(y/n) : ")
            if input() in {"n","no"}:
                return
            os.remove(os.path.join(ENV_PATH,FNAME))
        shutil.copy2(TEMP_PATH,os.path.join(ENV_PATH,FNAME))

    def get_input(self,ENV_PATH):
        instr = ""
        while True:
            inp = input()
            if inp == "\'":
                break
            instr += inp + '\n'
        with open(os.path.join(ENV_PATH,"input.txt"),"w+") as f:
            f.write(instr)

    def clear_in(self,ENV_PATH):
        if os.path.exists(os.path.join(ENV_PATH,"input.txt")):
            os.remove(os.path.join(ENV_PATH, 'input.txt'))

    def get_mult_input(self,FNAME,ENV_PATH):
        pass
