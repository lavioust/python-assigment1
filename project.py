import projectoptions 
projectoptions.menu()
option="go"
while option!="Q":
    option=raw_input("select an option from the menu:")
    if option=="1" or option=="O":
        projectoptions.openfile()
    elif option=="2" or option=="A":
        projectoptions.alignmentinfo()
        s=raw_input("Press [enter] to display the menu again:")
        if s=="":
            projectoptions.menu()
    elif option=="3" or option=="E":
        projectoptions.alignmentexplorer()
        s=raw_input("Press [enter] to display the menu again or E to select other segment:")
        if s=="E":
            projectoptions.alignmentexplorer()
        else:
            projectoptions.menu()
    elif option=="4" or option=="I":
        projectoptions.infopersequence()
        s=raw_input("Press [enter] to display the menu again or I to select other sequence:")
        if s=="I":
            projectoptions.infopersequence()
        else:
            projectoptions.menu()
    elif option=="5" or option=="S":
        projectoptions.glycosylation()
        s=raw_input("Press [enter] to display the menu again:")
        if s=="":
            projectoptions.menu()
    elif option=="6" or option=="X":
        projectoptions.export2fasta()
        s=raw_input("Press [enter] to display the menu again:")
        if s=="":
            projectoptions.menu() 
    else:
        print "press Q to Exit"
            
            
      