<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Fire‑Grass‑Water Game</title>
  <style>
    body { text-align: center; font-family: sans-serif; padding: 50px; }
    button { font-size: 2rem; margin: 0 10px; padding: 10px 20px; cursor: pointer; }
    #result { margin-top: 30px; font-size: 1.5rem; }
  </style>
</head>
<body>
  <h1>Fire 🌾 Water Element Battle</h1>
  <div>
    <button data-choice="fire">🔥 Fire</button>
    <button data-choice="grass">🌾 Grass</button>
    <button data-choice="water">💧 Water</button>
  </div>
  <div id="result"></div>
  <script>
    const choices = ['fire','grass','water'];
    const emoji = { fire:'🔥', grass:'🌾', water:'💧' };
    const rules = {
      fire: 'grass',
      grass: 'water',
      water: 'fire'
    };

    function decide(player, comp) {
      if (player === comp) return "It's a tie!";
      if (rules[player] === comp) return "🎉 You win!";
      return "😞 You lose.";
    }

    document.querySelectorAll('button').forEach(btn =>
      btn.addEventListener('click', () => {
        const player = btn.dataset.choice;
        const comp = choices[Math.floor(Math.random() * choices.length)];
        const msg = `You: ${emoji[player]} vs Comp: ${emoji[comp]}. ${decide(player, comp)}`;
        document.getElementById('result').textContent = msg;
      })
    );
  </script>
</body>
</html>
