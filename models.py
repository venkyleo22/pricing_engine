class wheel:
    def __init__(self, time_factor, spokes, rim, tube ,tyre):
        self.time_factor = time_factor
        self.spokes = spokes
        self.rim = rim
        self. tube = tube
        self.tyre = tyre
    
    def price(self):
        return (self.spokes+self.rim+self.tube+self.tyre) * self.time_factor

class handle:
    def __init__(self, time_factor, handle_bar, break_wire, break_shoe):
        self.time_factor = time_factor
        self.handle_bar = handle_bar
        self.break_wire = break_wire
        self.break_shoe = break_shoe
        
    def price(self):
        return (self.handle_bar+self.break_shoe+self.break_wire)*self.time_factor

class chain:
    def __init__(self, time_factor, pedal, chain, rim):
        self.time_factor = time_factor
        self.pedal = pedal
        self.chain = chain
        self.rim = rim
    
    def price(self):
        return (self.pedal+self.chain+self.rim) * self.time_factor

class seating:
    def __init__(self, time_factor, seat, bottle):
        self.time_factor = time_factor
        self.seat_p = seat
        self.bottle = bottle
    
    def price(self):
        return (self.seat_p + seat.bottle) * self.time_factor

class frame:
    def __init__(self, time_factor, frame, front_guard, back_guard):
        self.time_factor = time_factor
        self.frame = frame
        self.fg = front_guard
        self.bg = back_guard
    
    def price(self):
        return (self.frame+self.fg+self.bg)*self.time_factor
      
class cycle:
    def __init__(self, cycle_id, frame, handle, seating, wheel, chain):
        self.cycle_id = cycle_id
        self.frame = frame
        self.handle = handle
        self.seating = seating
        self.wheel = wheel
        self.chain = chain
        
    def price(self):
        frame_price = self.frame.price()
        handle_price = self.handle.price()
        seat_price = self.seating.price()
        wheel_price = self.wheel.price()
        chain_price = self.chain.price()
        
        self.total_price = frame_price + handle_price + seat_price +\
                            wheel_price + chain_price
    
    def __str__(self):
        self.price()
        print("The price of the cycle %s is %s " %(self.cycle_id, self.total_price))
