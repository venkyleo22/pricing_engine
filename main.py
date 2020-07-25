from models import wheel, handle, chain, seating, frame, cycle
import json


print("Welcome to pricing engine for cycle")
fp =open("input.json","r")

data = json.load(fp)
#print(data)

def calculate_date_factor(time):
    ##
    return 1.5


for cycle_id, params in data.items():
    frame_details = params.get("frame")
    frame_tfactor = calculate_date_factor(frame_details.get("date"))
    frame_price = frame_details.get("frame")
    fg = frame_details.get("fguard")
    bg = frame_details.get("bguard")
    frame_obj = frame(frame_tfactor,frame_price,fg,bg)
    
    handle_details = params.get("handle")
    handle_tfactor = calculate_date_factor(handle_details.get("date"))
    hbar = handle_details.get("handle_bar")
    bwire = handle_details.get("break_wire") 
    bshoe = handle_details.get("break_shoe")
    h_obj = handle(handle_tfactor, hbar, bwire, bshoe)
    
    seating_details = params.get("seating")
    seating_tfactor = calculate_date_factor(seating_details.get("date"))
    seat_price = seating_details.get("seat")
    bottle = seating_details.get("bottel")
    s_obj = seating(seating_tfactor,seat_price, bottle)
    
    wheel_details = params.get("wheel")
    wheel_tfactor = calculate_date_factor(wheel_details.get("date"))
    spoke = wheel_details.get("spokes")
    rim = wheel_details.get("rim")
    tube = wheel_details.get("tube")
    tyre = wheel_details.get("tyre")
    wheel_obj = wheel(wheel_tfactor,spoke,rim,tube,tyre)
    
    chain_details = params.get("chain")
    chain_tfactor = calculate_date_factor(chain_details.get("date"))
    pedal = chain_details.get("pedal")
    chain_price = chain_details.get("chain")
    rim = chain_details.get("rim")
    chain_obj = chain(chain_tfactor,pedal,chain_price,rim)
    
    cycle_obj = cycle(cycle_id,frame_obj,h_obj,s_obj,wheel_obj,chain_obj)
    cycle_obj.display()
    
    
    
