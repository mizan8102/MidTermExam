class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        tup = (id, movie_name, time)
        self.__show_list.append(tup)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id, li):
        if id in self.seats:
            for ll in li:
                if self.seats[id][ll[0]][ll[1]] == 0:
                    self.seats[id][ll[0]][ll[1]] = 1
                    print(f"Successfully booked = {ll}")
                else:
                    print(f"{ll} already booked")

        else:
            print("Show id isnot exits")

    def view_show_list(self):
        for mv in self.__show_list:
            print(f"Show Id = {mv[0]},Movie Name ={mv[1]} and Time= {mv[2]}")

    def view_available_seats(self, id):
        if id in self.seats:
            for i in self.seats[id]:
                print(i)
            print()


stc = Star_Cinema()
hall = Hall(6, 6, 10)
stc.entry_hall(hall)

hall.entry_show(23, "Spider man", "15-09-2023 10:30 PM")
hall.entry_show(100, "Avatar", "12-09-2023 4:30 PM")

while True:
    print(f"--------------------------")
    n = int(
        input(
            "1.View all \n2.View Available seats \n3.Book Ticker \n4.Exit \nEnter Option: "
        )
    )
    print(f"--------------------------")
    if n == 1:
        hall.view_show_list()

    elif n == 2:
        idd = int(input("Enter Show Id:"))
        hall.view_available_seats(idd)

    elif n == 3:
        showId = int(input("Enter Show id:"))
        tickets = int(input("Number of Tickets:"))
        tt = []
        for i in range(1, tickets + 1, 1):
            row = int(input("Enter row:"))
            col = int(input("Enter col: "))
            tt.append((row, col))
        hall.book_seats(showId, tt)

    elif n == 4:
        break
