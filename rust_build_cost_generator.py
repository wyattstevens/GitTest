def main():

    #implement this in a web browser so i dont have to ask about each
    #piece individually and allow people to backtrack and change
    #their awnsers if they mess up. Could be a very simple clean ui pretty
    #easily

    #Think about how to simplify and break down this problem so it doesnt
    #feel like im typing so much.

    calculate_wood_cost()

def inputPrompt(piece):

    if piece.lower() == "wall":
        return input("How many walls?")

    elif piece.lower() == "door frame":
        print("How many door frames?")
        number = input()
        return number

    elif piece.lower() == "foundation":
        print("How many square foundations?")
        number = input()
        return number

    elif piece.lower() == "triangle_foundation":
        print("How many triangle foundations?")
        number = input()
        return number

    elif piece.lower() == "ceiling":
        print("How many square ceilings?")
        number = input()
        return number

    elif piece.lower() == "triangle_ceiling":
        print("How many triangle ceilings?")
        number = input()
        return number

    elif piece.lower() == "wooden doors":
        print("How many wooden doors?")
        number = input()
        return number

    elif piece.lower() == "sheet metal doors":
        print("How many sheet metal doors?")
        number = input()
        return number

    else:
        print("Error  building piece unknown")


def calculate_wood_cost():

    # cost of each piece to upgrade from twig
    wall_cost = 200
    foundation_cost = 200
    triangle_foundation_cost = 100
    door_frame_cost = 140
    ceiling_cost = 100
    triangle_ceiling_cost = 50
    wooden_door_cost = 300
    sheet_door_cost = 150
    tc_cost = 1000

    # number of each building piece
    wall = int(inputPrompt("wall"))
    door_frame = int(inputPrompt("door frame"))
    foundation = int(inputPrompt("foundation"))
    triangle_foundation = int(inputPrompt("triangle_foundation"))
    ceiling = int(inputPrompt("ceiling"))
    triangle_ceiling = int(inputPrompt("triangle_ceiling"))
    wooden_door = int(inputPrompt("wooden doors"))
    sheet_door = int(inputPrompt("sheet metal doors"))

    #totals
    twig_cost = (wall + door_frame + foundation + ceiling) * 50

    wood_cost = (
                   (wall * wall_cost)
                 + (door_frame * door_frame_cost)
                 + (foundation * foundation_cost)
                 + (ceiling * ceiling_cost)
                 + (triangle_foundation * triangle_foundation_cost)
                 + (triangle_ceiling * triangle_ceiling_cost)
                 + (wooden_door * wooden_door_cost)
                 + twig_cost
                 + tc_cost

                   )

    metal_cost = sheet_door * sheet_door_cost

    print("It will cost " + str(wood_cost) + " total wood and " + str(metal_cost)
          + " total metal frags to build your base!")



main()


#potential data structures

wooden_dict = {
    "wall": 200,
    "square-foundation": 200,
    "triangle-foundation": 100,
    "half-wall": 200,
    "doorway": 140,
    "square-roof": 200,
    "triangle-roof": 50,
    "door": 300,
    "double-door:": 350
}
