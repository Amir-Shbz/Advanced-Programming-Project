# Amir Shahbazi - 9812033

Bus_names = []
Bus_list = []

# ---------------------------------------------------------------------------------------


class Bus:
    def __init__(self, Driver, bus, ar_time, de_time, Destination, seats_num, seat_list=[]):
        self.Driver = Driver
        self.bus = bus
        self.ar_time = ar_time
        self.de_time = de_time
        self.Destination = Destination
        self.seats_num = seats_num
        self.seat_list = seat_list
        for i in range(seats_num):
            self.seat_list.append(i+1)

    @property
    def Driver(self):
        return self.__Driver

    @Driver.setter
    def Driver(self, Driver):
        if isinstance(Driver, str):
            self.__Driver = Driver

    @property
    def bus(self):
        return self.__bus

    @bus.setter
    def bus(self, bus):
        if isinstance(bus, str):
            if bus not in Bus_names:
                self.__bus = bus
                Bus_names.append(bus)
            else:
                print("Your bus is not availible")

    @property
    def ar_time(self):
        return self.__ar_time

    @ar_time.setter
    def ar_time(self, ar_time):
        if isinstance(ar_time, str):
            self.__ar_time = ar_time

    @property
    def de_time(self):
        return self.__de_time

    @de_time.setter
    def de_time(self, de_time):
        if isinstance(de_time, str):
            self.__de_time = de_time

    @property
    def Destination(self):
        return self.__Destination

    @Destination.setter
    def Destination(self, Destination):
        if isinstance(Destination, str):
            self.__Destination = Destination

    @property
    def seats_num(self):
        return self.__seats_num

    @seats_num.setter
    def seats_num(self, seats_num):
        if isinstance(seats_num, int):
            self.__seats_num = seats_num

    def printbus(self):
        print("Driver :", self.Driver)
        print("Terminal Entry Time :", self.ar_time)
        print("Terminal Exit Time :", self.de_time)
        print("Destination :", self.Destination)
        print("Number of Seats :", self.seats_num)

    def bus_av(self):
        Bus_list.append(self)

    def passenger(self):
        print("Enter your name :")
        name = input()
        print("This is the list of availible seatnumbers:")
        print(self.seat_list)
        print("Enter your seat number :")
        seatnumber = int(input())
        if seatnumber in self.seat_list:
            self.seat_list[seatnumber-1] = "*"
            print("Your reservation was successful!\n")
            print("Passenger :", name)
            print("Bus :", self.bus)
            print("Driver :", self.Driver)
            print("Terminal Entry Time :", self.ar_time)
            print("Terminal Exit Time :", self.de_time)
            print("Destination :", self.Destination)
            print("Number of Seats :", self.seats_num)
            print("Reserved Seat :", seatnumber)
        else:
            print("Your seat is not availible!")
            self.passenger()
# --------------------------------------------------------------------------


def add_bus():
    print("Enter the Driver name:")
    a = input()
    print("\n")
    print("Enter the Bus name:")
    b = input()
    print("\n")
    print("Enter the arrival time:")
    c = input()
    print("\n")
    print("Enter the departure time:")
    d = input()
    print("\n")
    print("Enter the Destination:")
    e = input()
    print("\n")
    print("Enter the number of seats:")
    f = int(input())
    print("\n")
    y = Bus(a, b, c, d, e, f)
    Bus_list.append(y)


# --------------------------------------------------------------------------
def busavailible(Bus_list):
    shomarandeh = len(Bus_list)
    for i in range(shomarandeh):
        print(i+1, ':')
        Bus_list[i].printbus()
        shomarandeh += 1
        print(3*"\n")
