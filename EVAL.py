import os
import subprocess
import sys
import time


class EvalManager:
    def __init__(self, LANG, TIM_LIMIT=1000, MEM_LIMIT=256):
        self.language = LANG
        self.limits = (TIM_LIMIT, MEM_LIMIT)

    def compile(self, FNAME, ENV_PATH):
        FPATH = os.path.join(ENV_PATH, f"{FNAME}.{self.language}")
        CPATH = os.path.join(ENV_PATH, "a.out")
        if self.language == "cpp":
            try:
                subprocess.call(["g++", FPATH, "-o", CPATH])
                return True
            except:
                print(" compilation failed !!")
                print(" executed from : ", os.curdir)
                print(f" g++ {FPATH} -o a.out")
                return False

    def run(self,INP_NAME,ENV_PATH):
        inp = os.path.join(ENV_PATH,INP_NAME)
        out = os.path.join(ENV_PATH,"output.txt")
        exec_dir = os.path.join(ENV_PATH,"a.out")
        print("")
        time1 = time.time()
        # subprocess.run("./a.out",input=inp,stdout=out)
        with open(inp, 'r') as inpt:
            with open(out, 'w') as ofile:
                proc = subprocess.Popen(exec_dir, stdin=inpt, stdout=ofile, shell=True)
                maxmemused = 0
                while proc.poll() is None:
                    meminf = os.popen("sudo ps aux | grep " + str(proc.pid)).read().split(" ")
                    for num in meminf:
                        if num.isdecimal():
                            maxmemused = max(maxmemused, int(num))
                    if maxmemused > self.limits[1]*1000:
                        print()
                        print("Memory limit exceeded..!")
                        proc.kill()
                        return False
                    print("Max Memory Usage : ", maxmemused, "KB", end='\r')

                    sys.stdout.flush()

                    # check time limit...
                    if time.time() - time1 > self.limits[0]:
                        print()
                        print("Time Limit Exceeded .. !")
                        proc.kill()
                        return False
                    # time.sleep(0.001)
        print()
        #        with open(inp,"rb") as ifile:
        #            with open(out,"wb") as ofile:
        #                ofile.write(subprocess.run("./a.out",input=ifile.read(),capture_output=True).stdout)
        time2 = time.time()
        print(f"Execution time : {time2 - time1}")
        print()
        return True