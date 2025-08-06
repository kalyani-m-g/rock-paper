<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Rock Paper Scissors</title>
  <style>
    body { font-family: sans-serif; text-align: center; padding: 50px; }
    button { font-size: 2rem; padding: 10px 20px; margin: 5px; cursor: pointer; }
    #result { margin-top: 20px; font-size: 1.5rem; }
  </style>
</head>
<body>
  <h1>Rock Paper Scissors</h1>
  <div>
    <button data-choice="rock">✊ Rock</button>
    <button data-choice="paper">✋ Paper</button>
    <button data-choice="scissors">✌️ Scissors</button>
  </div>
  <div id="result"></div>

  <script>
    const choices = ['rock','paper','scissors'];
    const emoji = {rock:'✊', paper:'✋', scissors:'✌️'};
    function decide(player, comp) {
      if (player === comp) return "It's a tie!";
      if (
        (player === 'rock' && comp === 'scissors') ||
        (player === 'paper' && comp === 'rock') ||
        (player === 'scissors' && comp === 'paper')
      ) return "🎉 You win!";
      return "😞 You lose.";
    }
    document.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', () => {
        const player = btn.getAttribute('data-choice');
        const comp = choices[Math.floor(Math.random() * choices.length)];
        document.getElementById('result').textContent =
          `You: ${emoji[player]} vs Computer: ${emoji[comp]}. ${decide(player, comp)}`;
      });
    });
  </script>
</body>
</html>

