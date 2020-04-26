import os
import sys
import shutil
import argparse

def check_path(i, o):

    if not os.path.isdir(i) or not os.path.isdir(o):
        return False
    else:
        return True

def print_matches(i, suf, verbose):
    total = 0
    
    for root, dirs, names in os.walk(i):
        for filename in names:
            if filename.endswith(suf):
                if verbose:
                    print(os.path.join(root, filename))
                total += 1
    
    return total

def copy_matches(i, suf, o, total, remove, trials=20):


    count = 0
    for root, dirs, names in os.walk(i):
        for filename in names:
            if filename.endswith(suf):
                dest = filename
                attempts = 0
                success = False
                if not remove:
                    while not success and attempts < trials:
                        try:
                            shutil.copyfile(os.path.join(root, filename), os.path.join(o, dest))
                            success = True
                            count += 1
                            print("(" + str(count) + "/" + str(total) + \
                                    ") "+ os.path.join(root, filename) + \
                                    " copied to "+ os.path.join(o, dest))

                        except shutil.Error:
                            attempts += 1
                            dest =  str(attempts) + filename
                
                else:
                    while not success and attempts < trials:
                        try:
                            shutil.move(os.path.join(root, filename), os.path.join(o, dest))
                            success = True
                            count += 1
                            print("(" + str(count) + "/" + str(total) + \
                                    ") "+ os.path.join(root, filename) + \
                                    " moved to "+ os.path.join(o, dest))

                        except shutil.Error:
                            attempts += 1
                            dest =  str(attempts) + filename

    
    return 0

def main(argv):



    parser = argparse.ArgumentParser(description='print/move/copy files recursively')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--copy',action='store_true', dest='copy')
    group.add_argument('-p', '--print',action='store_true', dest='print')
    group.add_argument('-m', '--move',action='store_true', dest='move')
    
    parser.add_argument('-o', '--output_dir', nargs=1, type=str, default="." ,dest='output_dir')
    parser.add_argument('i', type=str, nargs=1)
    parser.add_argument('suffix', type=str, nargs=1)

    args = parser.parse_args(argv[1:])
    '''
    print(args.copy)
    print(args.o)
    print(args.i)
    print(args.suffix)
    '''

    if not check_path(args.i[0], args.output_dir[0]):
        print("invalid path")
        return -1
    if args.print:
        total = print_matches(args.i[0], args.suffix[0], True)
        print(str(total) + " files matched within " + args.i[0])

    elif args.copy:
        total = print_matches(args.i[0], args.suffix[0], False)
        print(str(total) + " files matched within " + args.i[0])

        copy_matches(args.i[0], args.suffix[0], args.output_dir[0], total ,False, trials=10)
    elif args.move:
        total = print_matches(args.i[0], args.suffix[0], False)
        print(str(total) + " files matched within " + args.i[0])

        copy_matches(args.i[0], args.suffix[0], args.output_dir[0], total, True, trials=10)

    else:
        print("[-c | -p | -m]")


    return 0







if __name__ == "__main__":
    #main(sys.argv[1:])
    main(sys.argv)
