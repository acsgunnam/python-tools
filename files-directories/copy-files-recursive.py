# import required module
import os
 
# assign directory keep forward slash
directory = 'E:/Test'
 
# iterate over files in
# that directory

try: 
    for root, dirs, files in os.walk(directory):
        print(root)
        print(dirs)
        print(files)
        for filename in files:
            print(os.path.join(root, filename))

except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")