'''
------------------------------------------------------------------------------------------------------------------------------------------------------------
Program Description:

The molar mass of a susbtance is a physical property defined by the mass of the chemicals that the substance is made of (in grams), realtive to the amount of
susbtance in moles (mol). Therefore, the molar mass of a given substance is measured as grams/mol. This physical property is widely used in chemistry-realted
and Stoichiometric applications, as well as an array of STEM fields such Biochemistry, Forensic sciences, Envrionmental Sciences and many others.

The molar mass of a given susbstance when calculated manually, using the 'Periodic Table of Elements', can be repetitive, time-consuming, and bound to errors

With this program, 'Molar Mass Calculator', one can simply type-in the chemical formula of the substance, and obtain its molar mass.

Refer to "Molar Mass Calculator_Offline_Documentations.txt" for offline documentations and more information about the program

------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
import sys
import easygui

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
p_table ={
'H': 1.00794,     'He': 4.002602,  'Li': 6.941,       'Be': 9.012182,    'B': 10.811,     'C': 12.0107,         'N': 14.0067,
'O': 15.9994,     'F': 18.9984032, 'Ne': 20.1797,     'Na': 22.98976928, 'Mg': 24.305,    'Al': 26.9815386,
'Si': 28.0855,    'P': 30.973762,  'S': 32.065,       'Cl': 35.453,      'Ar': 39.948,    'K': 39.0983,         'Ca': 40.078,
'Sc': 44.955912,  'Ti': 47.867,    'V': 50.9415,      'Cr': 51.9961,     'Mn': 54.938045,
'Fe': 55.845,     'Co': 58.933195, 'Ni': 58.6934,     'Cu': 63.546,      'Zn': 65.409,    'Ga': 69.723,         'Ge': 72.64,
'As': 74.9216,    'Se': 78.96,     'Br': 79.904,      'Kr': 83.798,      'Rb': 85.4678,   'Sr': 87.62,          'Y': 88.90585,
'Zr': 91.224,     'Nb': 92.90638,  'Mo': 95.94,       'Tc': 98.9063,     'Ru': 101.07,    'Rh': 102.9055,       'Pd': 106.42,
'Ag': 107.8682,   'Cd': 112.411,   'In': 114.818,     'Sn': 118.71,      'Sb': 121.760,   'Te': 127.6,
'I': 126.90447,   'Xe': 131.293,   'Cs': 132.9054519, 'Ba': 137.327,     'La': 138.90547, 'Ce': 140.116,
'Pr': 140.90465,  'Nd': 144.242,   'Pm': 146.9151,    'Sm': 150.36,      'Eu': 151.964,   'Gd': 157.25,
'Tb': 158.92535,  'Dy': 162.5,     'Ho': 164.93032,   'Er': 167.259,     'Tm': 168.93421, 'Yb': 173.04,
'Lu': 174.967,    'Hf': 178.49,    'Ta': 180.9479,    'W': 183.84,       'Re': 186.207,   'Os': 190.23,         'Ir': 192.217,
'Pt': 195.084,    'Au': 196.966569,'Hg': 200.59,      'Tl': 204.3833,    'Pb': 207.2,     'Bi': 208.9804,
'Po': 208.9824,   'At': 209.9871,  'Rn': 222.0176,    'Fr': 223.0197,    'Ra': 226.0254,  'Ac': 227.0278,
'Th': 232.03806,  'Pa': 231.03588, 'U': 238.02891,    'Np': 237.0482,    'Pu': 244.0642,  'Am': 243.0614,
'Cm': 247.0703,   'Bk': 247.0703,  'Cf': 251.0796,    'Es': 252.0829,    'Fm': 257.0951,  'Md': 258.0951,
'No': 259.1009,   'Lr': 262,       'Rf': 267,         'Db': 268,         'Sg': 271,       'Bh': 270, 'Hs': 269, 'Mt': 278,
'Ds': 281,        'Rg': 281,       'Cn': 285,         'Nh': 284,         'Fl': 289,       'Mc': 289, 'Lv': 292,
'Ts': 294,        'Og': 294,

'POLY': 0 #this key and value 'POLY' is a placeholder, and will be used when the user enters a polyatomic compound
}

#The dictionary above consists of the 102 different elements on the periodic table, along with their Molar Masses.
#The data was extracted from: https://www.lenntech.com/periodic/mass/atomic-mass.htm
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Following are lists of options of buttons that the user will be able to pick from. They will be used in the easyguiboxes

button_choices = ['Continue to Program', 'Exit Program', 'Description and Instructions']
reconfirm_choices = ['YES', 'NO']

while True:#forever loop
       user_choice = easygui.buttonbox('Molar Mass Calculator \nAuthors: Shreshth N. \nVersion 1.0 \nMade with Python 3.7', choices = button_choices)
       while user_choice == 'Description and Instructions': #if the user selects the 'Description and Instructions' button, the following easygui message box is called:
              easygui.msgbox(
'''-------------------------------------------------------------------------------
Program Description:
-------------------------------------------------------------------------------
The Molar Mass of a susbtance is a physical property defined by its mass in grams (of the chemicals that the substance is made of) realtive to the amount of susbtance in moles (a chemical SI unit). Therefore, the molar mass of a given substance is measured as g/mol.

This physical property is widely used in chemistry-realted and Stoichiometric applications, as well as an array of STEM fields such Biochemistry, Forensic sciences, Envrionmental sciences and many others.

The molar mass of susbtances can be calculated using the Periodic Table of Elements, but can be very repetitive and tiresome. This program allows you to simply type in the chemical chemical of the substance, and obtain its molar mass
-------------------------------------------------------------------------------
Instructions:
-------------------------------------------------------------------------------
To run the porgram, click on the button "Continue to Program." Once prompted, input the chemical formula of the susbtance, and the 'Molar Mass Calculator' will instantly display the molar mass. Please note that the chemical formula is case-sensitive. If an incorrect
chemical formula is provided, the 'Molar Mass Claculator' will ask the user to re-enter the chemical formula.

If you wish to exit, please click on "Exit Program". A reconformation menu will appear, and you can chose whether you want to exit the program or go back and keep using it.
''')
              break
       while user_choice == 'Continue to Program':

              formula = easygui.enterbox('Enter Chemical Formula of the desired chemical below. \nExample: "Al2(SO4)3", not "aL2(sO4)3"')


              while (formula is not None) and (formula.isupper()) and (('A' in formula) or ('D' in formula) or ('E' in formula) or ('G' in formula) or ('J' in formula) or ('L' in formula) or ('M' in formula) or ('Q' in formula) or ('R' in formula) or ('T' in formula) or ('X' in formula) or ('Z' in formula)):
                     easygui.msgbox('The chemical compound "' + str(formula) + '" is invalid. \nEnsure that you have used elements from the periodic table \nNote that the interpreted information is case-sensitive') #the user is notified that the input is invalid
                     formula = easygui.enterbox('Enter Chemical Formula of the desired formula below. \nExample: "MgCl2", not "mgcl2"') #the user is asked to enter the formula of their element or compound again

              while formula == '': #if nothing is typed, meaning a blank character is entered, the following is executed:
                     formula = easygui.enterbox('You must enter an element or formula \nEnter Chemical Formula of the desired compound below. \nExample: "MgCl2", not "mgcl2"')
                     #the user will be prompted to enter the chemical formula of desired compound again

              if formula is None: #This prompt will be executed when the user clicks 'Cancel' as one of the default options when using the easygui enterbox
                     #when 'Cancel' is clicked, a NoneType value is returned to the variable 'formula'. Note that a NoneType variable does not register as
                     #a blank character, so the while loop above must compare this returned value with python's built-in prompt, 'None'.
                     #If the retruned value is None, the while loop is discontinued using 'break', and the while True loop is re-executed
                     break


              #the variables below are declared as booleans
              poly = False
              Last = False
              multiply = False
              #-------------

              poly_mass = 0 #this variable will store the molar mass of polyatomic compounds - those that have brackets. Example: Al2(SO4)3 [Aluminum Sulfate]
              final_mass = 0 #this variable will store the final molar mass of the given compound
              subscript = 1 #this variable will change depending on the numbers that are in the typed compound. It will multiply the poly_mass or final_mass values accordingly

              Element = 'POLY' #the variable Element will hold the key value 'POLY', which has a value of 0 in the dictionary. This value will be used when the user has entered a polyatomic compounds - those that have parentheses

              for i in range(0,len(formula) + 1): #this for loop will run for the total number of characters in the variable 'formula', or the chemical compound that is entered by the user

                     char = formula[i:i + 1] #This prompt will slice each character of the string 'formula'. The sliced value is held by the variable 'char', and will change to the next character of the variable 'formula' with every iteration of the for loop
                     if len(Element) >= 2: #if the length of the variable 'Element' is greater than or equal to 2, the following is executed:
                            if Element not in p_table: #the KeyValue will change from 'POLY' to some other character on the second iteration of the while loop. If this character is not found in the p_table dictionary, the following will be executed:
                                   #the user is notified that the entered chemcial formula is invalid
                                   easygui.msgbox('The chemical compound "' + str(formula) + '" is invalid. \nEnsure that you have used elements from the periodic table \nNote that the interpreted information is case-sensitive')
                                   break #the for loop is discontinued, and the while loop is iterated again, in which the user is asked to enter the chemical formula again


                     if poly: #this conditional statement is executed when the boolean variable 'poly' is True. It will only be declared true when the user has entered a polyatomic compound that has parantheses, i.e. when the variable 'char' == '('

                         if Last: #this conditional statement is executed when the boolean variable 'Last' is True. It will only be declared true when the parantheses are closed, i.e. 'char' == ')'
                             poly = False #when the boolean variable 'Last' is True, it means that the polyatomic compound has been read, and therefore, the variable boolean poly is declared False
                             try:
                                    final_mass += int(char) * poly_mass #the variable char is read as 1 if there is no numerical character present after parantheses. If there is a numerical character present, it must be converted from
                             #type String to type Integer. Then, this integer value is multiplied by the 'poly-mass', or the mass of the polyatomic compound which will be calculated later in the code below
                             #the product of the integer and 'poly_mass' is added to the value of the variable 'final_mass' which will store the total molar mass of the chemical formula entered
                             except:
                                    easygui.msgbox('The chemical compound "' + str(formula) + '" is invalid. \nEnsure that you have used elements from the periodic table \nNote that the interpreted information is case-sensitive')
                                    break #the for loop is discontinued, and the while loop is iterated again, in which the user is asked to enter the chemical formula again

                         elif char.isdigit(): #if the character is a numerical number, the following is executed:
                             if multiply: #if the boolean variable multiply is True, the following is executed (the boolean will be True on the second iteration):
                                    subscript = int(str(subscript) + char) # the variable subscript is added to char as a string value, and then converted to an integer value. The new value is then stored by the same variable 'subscript'
                             else: #if the boolean variable is False, the variable susbcript is given the integer value of the variable char, which is a numeric digit
                                    subscript = int(char)
                             multiply = True #the boolean variable multiiply is declared True

                         elif char.islower(): #if the sliced character is lower case, it will be added to the variable Element (i.e. 'POLY') on the first iteration, or an uppercase character before it in the second iteration or a higher iteration.
                                Element += char

                         elif char.isupper(): #if the sliced character is upper case, the following executions are made:
                                poly_mass += subscript * p_table[Element] #on the first iteration, the value of 'Element' will be that of the Key, 'POLY', which has a value of 1 in the p_table dicitonary
                                #on the second iteration, the value of Element will change to the sliced character as seen in the code below...
                                #The value of the susbcript is multplied by the KeyValue of the sliced character fethced from the p_table dictionary. The multiplied value is now held by the variable poly_mass

                                Element = char #as mentioned above, the value of Element will now be changed to the value of the uppercase sliced character, 'char'
                                subscript = 1 #the subscript value is reset back to 1
                                multiply = False #the boolean variable multiply is changed to False


                         elif char == ')': #once the sliced character is a closed parantheses, the following is executed
                                poly_mass += subscript * p_table[Element] #The value of the susbcript is multplied by the KeyValue of the sliced character fethced from the p_table dictionary. The multiplied value is now held by the variable poly_mass
                                Element = 'POLY' #the Element value is reset to 'POLY'
                                subscript = 1 #the subscript value is reset to 1
                                Last = True #the boolean variable Last is declared True, meaning that the program interpreter is now done reading the polyatomic compound that was entered as the chemical formula by the user
                                multiply = False #the boolean variable multiply is reset to False

                     elif char == '(': #once the sliced character is an open parantheses, the following is executed
                            final_mass += subscript * p_table[Element] #The value of the susbcript is multplied by the KeyValue of the sliced character fetched from the p_table dictionary. The multiplied value is now held by the variable final_mass
                            Element = 'POLY'
                            subscript = 1
                            poly = True #since a parantheses is recognized as the sliced character, it means that the user has entered a polyatomic compound
                            multiply = False #the boolean variable 'multiply' is reset to False

                     elif char.isdigit(): #if the sliced character is a digit, and not a polyatomic compound (because the boolean variable poly is preset as False)
                            if multiply: # if the boolean variable multiply is True, the following is executed (it will be declared True on the second iteration)
                                   subscript = int(str(subscript) + char) # the variable subscript is added to char as a string value, and then converted to an integer value
                            else: #if the boolean variable is False, the variable susbcript is given the integer value of the variable char, which is a numeric digit
                                   subscript = int(char)
                            multiply = True #the boolean variable multiiply is declared True

                     elif char.islower(): #if the sliced character is lower case, it will be added to the variable Element (i.e. 'POLY') on the first iteration, or an uppercase character before it in the second iteration or a higher iteration.
                            Element += char

                     elif char.isupper():  #if the sliced character is upper case, the following executions are made:

                            #easygui.msgbox('The chemical compound "' + str(formula) + '" is invalid. \nEnsure that you have used elements from the periodic table \nNote that the interpreted information is case-sensitive')
                            #break #the for loop is discontinued, and the while loop is iterated again, in which the user is asked to enter the chemical formula again

                            try: #the following will be executed if there are no KeyErrors:
                                   final_mass += subscript * p_table[Element] #on the first iteration, the value of 'Element' will be that of the Key, 'POLY', which has a value of 1 in the p_table dicitonary
                                   #on the second iteration, the value of Element will change to the sliced character as seen in the code below...
                                   #The value of the susbcript is multplied by the KeyValue of the sliced character fethced from the p_table dictionary. The multiplied value is now held by the variable final_mass

                                   Element = char #as mentioned above, the value of Element will now be changed to the value of the uppercase sliced character, 'char'
                                   subscript = 1 #the subscript value is reset back to 1
                                   multiply = False #the boolean variable multiply is changed to False

                            except: #if there are any KeyErrors in the code above, python will make it an exception, and execute the following:

                                   easygui.msgbox('The chemical compound "' + str(formula) + '" is invalid. \nEnsure that you have used elements from the periodic table \nNote that the interpreted information is case-sensitive')
                                   break #the for loop is discontinued, and the while loop is iterated again, in which the user is asked to enter the chemical formula again


                     while i == len(formula): #the following code is executed on the last iteration where i (a numerical value that increses by 1 with each for loop iteration) is equal to the length of the total number of characters present in the checmial formula
                            final_mass += subscript * p_table[Element] #since this is the last iteration, the value of the variable Element will be that of the the last sliced character which is an alphabet
                            #The 'Element' value is used as the Key to fetch its respective value from the dictionary p_table. The returned value is then multiplied by the subscript, which will be 1 if nothing no numerical number is subsequnt to it.
                            #the multiplied value is then held by the variable 'final_mass'

                            Element = char #the value of 'Element' will now be changed to the value of the uppercase sliced character, 'char'
                            subscript = 1 #the subscript value is reset back to 1
                            multiply = False #the boolean variable multiply is reset to False

                            #an output message is created as a string, where the final_mass value is rounded to 2 decimal places using the function round(x,2)
                            output_msg =  ' \nThe Molar mass of "' + formula + '" is ' + str(round(final_mass,2)) + ' g/mol'
                            easygui.msgbox(output_msg) #easygui messagebox is used to output the message above
                            break #this while loop is discontinued, and the exterior while loop is executed, in which the user is asked for the chemcial formula of another compound
#-----------------------------------------------------------------------------------
       while user_choice == 'Exit Program': #if the user chose the "Exit Program" button by selecting that choice in the button_box, the following will be executed
              reconfirm = easygui.buttonbox('Are you sure that you want to exit the program?', choices = reconfirm_choices)
              if reconfirm == 'NO': #if the user selects 'NO', this while loop will be discontinued and the while True loop will be re-executed
                     break
              else: #the following is executed if the user selects 'YES', meaning they want to exit the program
                     sys.exit() #the program is exited by using python's sys library's sys.exit() function which terminates the program
