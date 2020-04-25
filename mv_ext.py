import os
import sys
import shutil




def main(argv):

    if len(argv)!=3 or not os.path.isdir(argv[0]) or  not os.path.isdir(argv[1]):
        print("mv_ext.py dirin dirout <type to match>")
        return -1


    total = 0
    for root,dirs,names in os.walk(argv[0]):
        for filename in names:

            if filename.endswith(argv[2]):
                total += 1
    


    for root,dirs,names in os.walk(argv[0]):
        for filename in names:

            if filename.endswith(argv[2]):

                dest = filename
                attempts = 0
                success = False
                while not success and attempts < 20:
                    try:
                        shutil.copyfile(os.path.join(root, filename), os.path.join(argv[1], dest))
                        success = True
                        print("copied "+ os.path.join(root, filename) +" to "+ os.path.join(argv[1], dest))


                    except shutil.Error:
                        attempts += 1
                        dest =  str(attempts) + filename





    return







if __name__ == "__main__":
    main(sys.argv[1:])

