import requests
import time


def fetch_joke(exclude_keywords=None, joke_type='single'):
    """
    Fetches 3 programming joke from JokeAPI, with optional keyword filtering.

    Args:
        exclude_keywords: List of keywords to exclude (e.g., ['sql', 'python'])
        joke_type: 'single' or 'twopart' (default: 'single')
    Returns:
        dict: Joke data (category, type, joke) or None if filtered out
    """
    # Define the API endpoint for programming jokes
    url = "https://v2.jokeapi.dev/joke/Programming"
    # Set the joke type parameter
    params = {'type': joke_type}

    # Make the API request
    response = requests.get(url, params=params)
    # If the request fails, return None
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # If it's a two-part joke, combine setup and delivery
    if data.get('type') == 'twopart':
        joke_text = f"{data['setup']} {data['delivery']}"
    else:
        joke_text = data.get('joke', '')

    # Filter out jokes containing any of the excluded keywords
    if exclude_keywords and any(keyword.lower() in joke_text.lower() for keyword in exclude_keywords):
        return None

    # Return the joke data if not filtered out
    return {
        'category': data.get('category', 'Programming'),
        'type': data.get('type', 'single'),
        'joke': joke_text
    }


# Main execution block
if __name__ == '__main__':
    # Initialize joke counter and set the maximum number of jokes to fetch
    joke_count = 0
    max_jokes = 3

    # Loop until we have fetched the desired number of jokes
    while joke_count < max_jokes:
        # Fetch a joke (no keywords excluded in this example)
        joke_data = fetch_joke(
            exclude_keywords=[],  # Add keywords to exclude here, e.g., ['sql', 'python']
            joke_type='single'
        )
        # If a valid joke was returned, print it and increment the counter
        if joke_data:
            joke_count += 1
            print(f"\nJoke #{joke_count}:")
            print(f"Category: {joke_data['category']}")
            print(f"Type: {joke_data['type']}")
            print(f"Joke: {joke_data['joke']}")
        else:
            # If no joke was returned (filtered out or API error), notify the user
            print("No suitable joke found this round.")

        # Wait a second to be polite to the API and avoid spamming
        time.sleep(1)

    # Print a completion message
    print(f"\nFinished fetching {joke_count} programming jokes!")