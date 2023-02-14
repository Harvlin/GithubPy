def class_1():
    class Contest:
        def __init__(self, cn, cd, cf, cp):
            self.Contest_name = cn
            self.Contest_date = cd
            self.Contest_fee = cf
            self.Contest_participant = cp

        def prcontest(self):
            print(self.Contest_fee,
                  self.Contest_date,
                  self.Contest_fee,
                  self.Contest_participant)

    class ContestData(Contest):
        def __init__(self, cn, cd, cf, cp, cl):
            super().__init__(cn, cd, cf, cp)
            self.Contest_location = cl
        def prcontest(self):
            print(self.Contest_location)

    class ContestFinal(ContestData):
        def __init__(self, cn, cd, cf, cp, cl, cg):
            super().__init__(cn, cd, cf, cp, cl)
            self.Contest_gift = cg

    x = ContestFinal("Code", "27 December 2022", 10000, "John", "Jambi", 20000)
    print(x.Contest_name, "Contest", x.Contest_date, x.Contest_location, "\n", "Contest fee:", x.Contest_fee, "\n", "Contest gift:", x.Contest_gift, "\n", "Participant:", x.Contest_participant)
class_1()