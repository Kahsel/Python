class FamilyTree:
    def leshakTree():
        print('Welcome to Leshak Family Tree!','\n','SAMUILA LUNG AND YOSI')
        children = ('Esther', 'Laitu', 'Rifkatu', 'Arenious', 'Tabitha', 'Huldah', 'Nehemiah', 'Emmanuel', 'Patience')
        print('Children of Samuila Lung and Yosi are:')
        print(children)
        Option = input('''
                        Whose family from the Leshaks do you want to check?
                        INPUT:
                        Esther for her list of children
                        Laitu for her list of chidren
                        Rifkatu for her list of children
                        Arenious for his list of children
                        Tabitha for her list of children
                        Huldah for her list of children
                        Nehemiah for his list of children
                        Emmanuel for his list of chidren
                        Patience for her list of children
                        ''')
        #For Esther's Children
        if Option.upper() == 'ESTHER':
            print('you select {} and her children are: '.format(Option))
            a = ('Comfort', 'Onu', 'Agbene', 'Inikpi', 'Nanchin', 'Attah', 'Nankling')
            for i in a:
                print(i)
                
        #For Laitu's Children
        elif Option.upper() == 'LAITU':
            print('you select {} and her children are: '.format(Option))
            a = ('Simi', 'Noro', 'Yeipeng', 'Rhoda', 'Phoebe', 'Grace')
            for i in a:
                print(i)
                
        #For Rifkatu's Children
        elif Option.upper() == 'RIFKATU':
            print('you select {} and her children are: '.format(Option))
            a = ('Domkat', 'Felicity', 'Favor')
            for i in a:
                print(i)
                
        #For Arenious's Children
        elif Option.upper() == 'ARENIOUS':
            print('you select {} and his children are: '.format(Option))
            a = ('Sattong', 'Sekyen', 'Collins', 'Blessing', 'Melchizedek')
            for i in a:
                print(i)
                
        #For Tabitha's Children
        elif Option.upper() == 'TABITHA':
            print('you select {} and her children are: '.format(Option))
            a = ('Longkat', 'Mathew')
            for i in a:
                print(i)
                
        #For Huldah's Children
        elif Option.upper() == 'HULDAH':
            print('you select {} and her children are: '.format(Option))
            a = ('Annah', 'Josepher')
            for i in a:
                print(i)
                
        #For Nehemiah's Children
        elif Option.upper() == 'NEHEMIAH':
            print('you select {} and his child is: '.format(Option))
            print('Benevolence')
            
        #For Emmanuel's Children
        elif Option.upper() == 'EMMANUEL':
            print('you select {} and his children are: '.format(Option))
            a = ('Goshen', 'Gretchen', 'Gadiela')
            for i in a:
                print(i)
                
        #For Patience's Children
        elif Option.upper() == 'PATIENCE':
            print('you select {} and her children are: '.format(Option))
            a = ('Raphael', 'Khirnaan', 'Kyenret', 'Nanmet', 'Lawson')
            for i in a:
                print(i)
        #to collect error inace user input other words other than the one they should        
        else:
            print('input not valid, kindly input valid keyword')
        #to start again if user want to know other family members    
        FamilyTree.tryAgain()
        
    def tryAgain():
        again = input('''
                    Do you want check other family?
                    INPUT:
                    y for YES
                    n for NO
                    ''')
        if again.upper() == 'Y':
            FamilyTree.leshakTree()
        elif again.upper() == 'N':
            print('Thank you! have a great time')
        else:
            print('not a valid input, use Y or N')
                 
            
FamilyTree.leshakTree()