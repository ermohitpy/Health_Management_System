#
#
# print("what you want to do:\n"
#       "1 for add data \n2 for retrieve data\n")
#
# inp = int(input())
#
#
# print("For which client:\n"
#       "1 for Harry\n2 for Rohan\n3 for Hammad\n")
#
# client = int(input())
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# def add(client):
#     print("What you want to feed:\n"
#           "1 for Diet\n2 forExercise\n")
#     feed = int(input())
#
#     if feed == 1:
#         f=open("diet.txt","w")
#         f.write(input())
#         f.close()
#     elif feed == 2:
#         f=open("exercise.txt",'w')
#         f.write(input())
#         f.close()
#
#
# if inp == 1:
#     add()


print("*************************another program*****************************")

 # Health Managment System

client_list = {1:"Manoj",2:"Pritesh",3:"Rushi"}

log_list = {1:"Exercise", 2:"Diet"}



def getdate():

    import datetime

    return datetime.datetime.now()



try:

    print("Select Client Name:")

    for key,value in client_list.items():

        print("Press",key,"For",value,"\n",end="")

    client_name = int(input())



    print("Press 1 for log")

    print("Press 2 for Retrieve")

    op = int(input())



    if op is 1:

        for key,value in log_list.items():

            print("Press",key,"For",value,"\n",end="")

        log_name = int(input())

        print("Selected Job:",log_list[log_name])

        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")

        k = 'y'

        while(k is not "n"):

            print("Enter", log_list[log_name],"\n", end="")

            mytext = input()

            f.write("["+str(getdate())+"]:"+mytext+"\n")

            k = input("Add More ? y/n:")

            continue

        f.close()

    elif op is 2:

        for key,value in log_list.items():

            print("Press",key,"to retrieve",value,"\n",end="")

        log_Name = int(input())

        print(client_list[client_name],"-",log_list[log_Name],"Report:","\n", end="")

        f = open(client_list[client_name]+"_"+log_list[log_Name]+".txt")

        contents = f.readline()

        for line in contents:

            print(line,end="")

        f.close()

    else:

        print("Invalid Input !!!")

except Exception as e:

    print("Wrong Input !!!",e)




