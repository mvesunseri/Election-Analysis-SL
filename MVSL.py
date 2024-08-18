import os.path

while True:
    try:
        while True:
            try:
                year = input("\nEnter the year of this election: ")    #Takes user input to determine file names
                country = input("Enter the country name: ")
                electiontype = input("Enter the type of election: ")
                filenames = year+" "+country+" "+electiontype
                outcome = " Election Outcome.txt"
                analysis = " Election Analysis.txt"
                if os.path.exists(filenames+outcome) == False:         #Raises error if file does not exist in directory
                    verror = ValueError("Invalid file name.")
                    raise verror
                else:
                    break
            except:
                print('''\nThis file does not exist. See README.txt.''')    #Catch exception and prompt user to re-try
                
            repeat = input("\nWould you like to run again? (yes or no): ")
            if repeat == "yes":
                continue
            else:
                print("\nGoodbye!\n")
                break

        totalseats = int(input("Enter the number of seats to be determined: "))

        votes = {}
        quotient = {}    #Defines four dictionaries that keep track of votes, quotients, and seats for parties
        seatsa = {}
        seatsp = {}
        
        def pdict(txt):
            """    Splits input text at double newline, newline, and then again at ": "   """
            vs = txt.split("\n\n")
            votedict = vs[0].split("\n")
            seatdict = vs[1].split("\n")
            for line in votedict:
                v = line.split(": ")
                votes[v[0]] = v[1]    #Defines each party as a key and their votes and actual seats as values for dict votes and seatsa
            for line in seatdict:
                s = line.split(": ")
                seatsa[s[0]] = s[1]
            return list(votes)

        def quot(parties):
            """    Calculates the quotient for each party based on Sainte-Lague Formula   """
            for party in parties:
                seatsp[party] = 0
                quotient[party] = int(votes[party])    #Initialize both seatsp and quotient dicts
            while sum(seatsp.values()) < totalseats:    #Ensures that it stops at total Parliament size
                for party in parties:
                    if sum(seatsp.values()) >= totalseats:    #Interrupts for loop if it passes maximum
                        break
                    else:
                        quotient[party] = int(votes[party])/(2*seat(party)+1)    #Quotient in terms of seat function
            print(seatsp)    #Optional print messages to check that all works as intended
            print(quotient)    
            return list(votes)    #Returns list of parties

        def seat(party):
            """    Increments seatsp value of party with the most votes    """
            if(max(quotient.values()) == quotient[party]):    #If a party has the largest quotient, += 1
                seatsp[party] += 1                             #Cumulative
            else:
                seatsp[party] += 0
            return seatsp[party]

        def slindex(dicts):
            """    Determines total votes and seats and calculates SLI    """
            sli = 0
            v = list(votes.values())    #Lists values (each party's votes)
            s = list(dicts.values())    #Lists values (each party's actual or proportional seats, depending on input
            for i in v:
                v[v.index(i)] = int(i)  #Change from dict value to int
            for i in s:
                s[s.index(i)] = int(i)
            v = sum(v)                  #Total votes and seats
            s = sum(s)
            for i in votes:
                vts = int(votes[i])/v   #Relative difference between actual and ideal proportional ratios
                sts = int(dicts[i])/s
                sli += ((sts-vts)**2)/vts    #Sum to calculate election SLI
            sli = round(sli, 10)
            print(sli)
            return sli
        
        def saintelague(otcm, anls):    #Opens txt docs
            """    Opens text documents, calls functions with extracted text, formats result, and writes to new file.    """
            o = open(otcm)
            a = open(anls, "w")
            while True:
                text = o.read()
                if len(text) == 0:
                    break
                sl = quot(pdict(text))    #Sends full text to pdict, then pdict to quot
                seat_totals = ""    #Initialize formatting
                for party in sl:
                    seat_totals += "{0:<30} {1:<30} {2:<30} {3}\n".format(party,votes[party],seatsa[party],seatsp[party])
                n0 = "Actual SLI: {0}".format(slindex(seatsa))    #Run slindex with actual seat values
                n1 = "Proportional SLI: {0}".format(slindex(seatsp))    #Run slindex with Sainte-Lague seat values
                n2 = "Party"
                n3 = "Votes"
                n4 = "Actual Seats"
                n5 = "Proportional Seats"
                n6 = ""
                for i in range(111):
                    n6 += "="
                a.write("{0}\n{1}\n\n{2:<30} {3:<30} {4:<30} {5}\n{6}\n{7}".format(n0,n1,n2,n3,n4,n5,n6,seat_totals))
            o.close()
            a.close()

        saintelague(filenames+outcome, filenames+analysis)

    except:
        print("\nInvalid input file. See README.txt.")    #Catch exception and prompt user to re-try

    repeat = input("\nWould you like to run again? (yes or no): ")
    if repeat == "yes":
        continue
    else:
        print("\nGoodbye!\n")
        break
