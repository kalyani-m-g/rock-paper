import random

choices = {
    'fire': '🔥',
    'grass': '🌾',
    'water': '💧'
}

rules = {
    'fire': 'grass',   # fire beats grass
    'grass': 'water',  # grass beats water
    'water': 'fire'    # water beats fire
}

player = input("Choose fire, grass, or water: ").lower()
if player not in choices:
    print("Invalid choice.")
else:
    comp = random.choice(list(choices.keys()))
    print(f"You: {player} {choices[player]}")
    print(f"Computer: {comp} {choices[comp]}")
    if player == comp:
        print("→ It's a tie!")
    elif rules[player] == comp:
        print("🎉 You win!")
    else:
        print("😞 You lose.")

