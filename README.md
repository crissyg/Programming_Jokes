# Programming Jokes Fetcher

A simple Python script that fetches and displays 3 programming jokes from the JokeAPI.

---

## 🎯 Features

- **Fetches jokes from the [JokeAPI Programming category](https://v2.jokeapi.dev/)**
- **Supports filtering out jokes containing specific keywords**
- **Displays up to 3 jokes before stopping**
- **Easy to customize for different joke types or categories**

---

## 🛠️ Requirements

- **Python 3.x**
- **requests** library (`pip install requests`)

---

## 🚀 How to Use

1. **Clone or download this repository.**
2. **Open a terminal and navigate to the project directory.**
3. **Run the script:**
   ```
   python jokes.py
   ```
4. **Enjoy your programming jokes!**

---

## 📝 Customization

- **Change the joke category:**  
  Edit the `url` in `fetch_joke()` to use a different category (e.g., `"https://v2.jokeapi.dev/joke/Any"`).
- **Filter out keywords:**  
  Add keywords to the `exclude_keywords` list in the main loop (e.g., `['sql', 'python']`).
- **Change the joke type:**  
  Set `joke_type` to `'twopart'` for two-part jokes.

---

## 📄 Example Output

```
Joke #1:
Category: Programming
Type: single
Joke: Why do programmers prefer dark mode? Because light attracts bugs.

Joke #2:
Category: Programming
Type: single
Joke: Why do Java developers wear glasses? Because they can't C#.

Joke #3:
Category: Programming
Type: single
Joke: How many programmers does it take to change a light bulb? None, that's a hardware problem.

Finished fetching 3 programming jokes!
```

## 🤝 Contributing

Feel free to fork, modify, or submit pull requests!

---

**Enjoy the jokes!**

---


