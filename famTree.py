class FamilyTree:
    def leshakTree():
        print('Welcome to Leshak Family Tree!','\n','SAMUILA LUNG AND YOSI\n')
        children = ('Esther', 'Laitu', 'Rifkatu', 'Arenious', 
                    'Tabitha', 'Huldah', 'Nehemiah', 'Emmanuel', 'Patience\n')
        print('Children of Samuila Lung and Yosi are:')
        print(children)
        #to select between Leshaks children or grandchildren
        option1 = input('''
                        Which do you wan to check?\n
                        [Children] or [Grandchildren] or [Great-Grandchildren]\n
                        type 'Children' for list of Leshak's Children and their Children
                        type 'Grandchildren' for list of Grand childrens
                        type 'GGC' for list of Great-Grand childrens\n
                        Enter Valid Keyword: ''')
        
        #to get list of children
        if (option1.upper()) == 'CHILDREN':
            print('You select {}, follow the next procedure to continue'.format(option1))
            FamilyTree.leshakTree2()
            
        #FOR Grandchildren
        elif (option1.upper()) == 'GRANDCHILDREN':
            print(f'You Select {option1}, and Leshak list of Grandchildren is: \n')
            grd = ('Comfort', 'Onu', 'Agbene', 'Inikpi', 'Nanchin', 'Attah', 'Nankling',
                   'Simi', 'Noro', 'Yeipeng', 'Rhoda', 'Phoebe', 'Grace', 'Domkat', 
                   'Felicity', 'Favor', 'Sattong', 'Sekyen', 'Collins', 'Blessing',
                   'Melchizedek', 'Longkat', 'Mathew','Annah', 'Josepher','Benevolence',
                   'Goshen', 'Gretchen', 'Gadiela','Raphael', 'Khirnaan', 'Kyenret',
                   'Nanmet', 'Lawson\n')  
            for i in grd:
                print(i)
            print('The total number of grandChildren is: ', len(grd))
            
        #for grrat grand children
        elif (option1.upper()) == 'GGC':
            print('You Select {}, and Leshak list of Great-Grand children is: '.format(option1))
            ggc = ('Caroline', 'mafeng', 'njere', 'Weng', 'Nekenlis', 'Fwaniken', 'Jerushadai',
                   'Ojoma', 'Onu3', 'Liskwopnan', 'Nanmet', 'Nanshang', 'Nan\'aken', 'Shupel', 
                   'Miracle', 'Emmanuella', 'Melody', 'Inikp1', 'Inikpi2', 'Treasure', 'Rose', 'Emmanuella'
                   'Weng', 'Kaweng', 'feli1','feli2\n')  
            for i in ggc:
                print(i)
            print('The total number of great-grandChildren is: ', len(ggc))    
            #to restart from welcome page
            print('\nDo you want start from the begining?\n'.upper()) 
            FamilyTree.grdTry()
            
        else:
            print('Your input not valid, please check your spelling and try again!')
            FamilyTree.grdTry()
            
        FamilyTree.grdTry()       
        Option = input('''
                        Whose family from the Leshaks do you want to check?\n
                        INPUT:
                        Esther for her list of children
                        Laitu for her list of chidren
                        Rifkatu for her list of children
                        Arenious for his list of children
                        Tabitha for her list of children
                        Huldah for her list of children
                        Nehemiah for his list of children
                        Emmanuel for his list of chidren
                        Patience for her list of children\n
                        Enter Valid Keyword: ''')
        #For Esther's Children
        if Option.upper() == 'ESTHER':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Comfort', 'Onu', 'Agbene', 'Inikpi', 'Nanchin', 'Attah', 'Nankling')
            for i in a:
                print(i)
                
        #For Laitu's Children
        elif Option.upper() == 'LAITU':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Simi', 'Noro', 'Yeipeng', 'Rhoda', 'Phoebe', 'Grace')
            for i in a:
                print(i)
                
        #For Rifkatu's Children
        elif Option.upper() == 'RIFKATU':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Domkat', 'Felicity', 'Favor')
            for i in a:
                print(i)
                
        #For Arenious's Children
        elif Option.upper() == 'ARENIOUS':
            print('you select {} and his children are: \n'.format(Option))
            a = ('Sattong', 'Sekyen', 'Collins', 'Blessing', 'Melchizedek')
            for i in a:
                print(i)
                
        #For Tabitha's Children
        elif Option.upper() == 'TABITHA':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Longkat', 'Mathew')
            for i in a:
                print(i)
                
        #For Huldah's Children
        elif Option.upper() == 'HULDAH':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Annah', 'Josepher')
            for i in a:
                print(i)
                
        #For Nehemiah's Children
        elif Option.upper() == 'NEHEMIAH':
            print('you select {} and his child is: \n'.format(Option))
            print('Benevolence')
            
        #For Emmanuel's Children
        elif Option.upper() == 'EMMANUEL':
            print('you select {} and his children are: \n'.format(Option))
            a = ('Goshen', 'Gretchen', 'Gadiela')
            for i in a:
                print(i)
                
        #For Patience's Children
        elif Option.upper() == 'PATIENCE':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Raphael', 'Khirnaan', 'Kyenret', 'Nanmet', 'Lawson')
            for i in a:
                print(i)
        #to collect error inace user input other words other than the one they should        
        else:
            print('\ninput not valid, kindly input any of the children name!')
            FamilyTree.leshakTree2()
                
            
        #to start again if user want to know other family members    
        FamilyTree.tryAgain()
        
    def leshakTree2():
        Option = input('''
                        Whose family from the Leshaks do you want to check?\n
                        INPUT:
                        Esther for her list of children
                        Laitu for her list of chidren
                        Rifkatu for her list of children
                        Arenious for his list of children
                        Tabitha for her list of children
                        Huldah for her list of children
                        Nehemiah for his list of children
                        Emmanuel for his list of chidren
                        Patience for her list of children\n
                        Enter Valid Keyword: ''')
        #For Esther's Children
        if Option.upper() == 'ESTHER':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Comfort', 'Onu', 'Agbene', 'Inikpi', 'Nanchin', 'Attah', 'Nankling')
            for i in a:
                print(i)
                
        #For Laitu's Children
        elif Option.upper() == 'LAITU':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Simi', 'Noro', 'Yeipeng', 'Rhoda', 'Phoebe', 'Grace')
            for i in a:
                print(i)
                
        #For Rifkatu's Children
        elif Option.upper() == 'RIFKATU':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Domkat', 'Felicity', 'Favor')
            for i in a:
                print(i)
                
        #For Arenious's Children
        elif Option.upper() == 'ARENIOUS':
            print('you select {} and his children are: \n'.format(Option))
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
            print('you select {} and her children are: \n'.format(Option))
            a = ('Annah', 'Josepher')
            for i in a:
                print(i)
                
        #For Nehemiah's Children
        elif Option.upper() == 'NEHEMIAH':
            print('you select {} and his child is: '.format(Option))
            print('Benevolence')
            
        #For Emmanuel's Children
        elif Option.upper() == 'EMMANUEL':
            print('you select {} and his children are: \n'.format(Option))
            a = ('Goshen', 'Gretchen', 'Gadiela')
            for i in a:
                print(i)
                
        #For Patience's Children
        elif Option.upper() == 'PATIENCE':
            print('you select {} and her children are: \n'.format(Option))
            a = ('Raphael', 'Khirnaan', 'Kyenret', 'Nanmet', 'Lawson')
            for i in a:
                print(i)
        #to collect error inace user input other words other than the one they should        
        else:
            print('\ninput not valid, kindly input any of the children name!')
            FamilyTree.leshakTree2()    
        FamilyTree.tryAgain()
        
    def tryAgain():
        again = input('''\n
                    Do you want to check other family?
                    INPUT:
                    y for YES
                    n for NO
                    ''')
        if again.upper() == 'Y':
            FamilyTree.leshakTree2()
        elif again.upper() == 'N':
            print('Thank you! have a great time')
            exit()
        else:
            print('not a valid input, use Y or N')
            FamilyTree.tryAgain()
            
    #for grandchildren's error collection        
    def grdTry():
        again = input('''
                        Input:
                        Y for Yes
                        N for No\n
                        Enter valid Keyword: ''')
        if again.upper() == 'Y':
            FamilyTree.leshakTree()
        elif again.upper() == 'N':
            print('Thanks! reamin blessed')
            exit()
        else:
            print('invalid input!') 
            FamilyTree.grdTry()           
            
FamilyTree.leshakTree()