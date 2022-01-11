print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_01 = input('\nYou\'ve left your ship and after ten minutes of walking, you\'re at a crossroad.\nWhere do you want to go? Type "Left" or "Right". ').lower()

if choice_01 == "left":
  choice_02 = input("\nThe path you chose is a narrow trail among the palm trees. Aside from the chirping of birds you seem to be alone.\nThe long walk takes you to a small lake, with an island in its middle. Do you want to swim across, or look for a way to sail towards the island?\nType \"Swim\" or \"Look\". ").lower()
    
  if choice_02 == "look":
    choice_03 = input("\nLooking around, you find a small boat hidden behind some bushes.\nIt's not particularly sturdy, but it seems enough to get to the island.\nOnce you get onto the small patch of land, a temple stands in front of you.\nYou can enter by choosing one of three doors: the red one, the blue one, or the yellow one.\nType \"Red\", \"Blue\" or \"Yellow\" to pick a door. ").lower()
  
    if choice_03 == "red":
      print("\nYou walk towards the red door and open it, getting into a wide wood chamber.\nThe door immediately closes behind you, while the room becomes hotter and hotter, soon engulfed by flames.\nGame Over.")
    elif choice_03 == "blue":
      print("\nYou walk towards the blue door and open it, getting into a wide rock chamber.\nThe door immediately closes behind you, while from the shadows at the other side of the room a huge beast shows itself, attacking you and ripping you to pieces.\nGame Over.")
    elif choice_03 == "yellow":
      print("\nYou walk towards the red door and open it, getting into a wide golden chamber.\nIn the middle of it, you can see a big chest full of gold and precious stones.\nGood job, you found the treasure!")
    else:
      print("\nBeing indecisive is never a good choice. You sit down in front of the temple, not sure about what to do.\nYou find yourself unable to pick a door and you just keep staring at them till you grow weaker and weaker, losing consciousness.\nGame Over.") 
  
  else:
      print("\nYou jump into the water without a second thought.\nSadly, you're soon surrounded by menacing shark fins. Trying to cross the lake this recklessly wasn't a good choice.\nGame Over.")  
else: 
  print("\nNot long after taking the path on the right, the ground beneath you starts to crumble. You fall into a hole and end up trapped, unable to proceed.\nGame Over.")
