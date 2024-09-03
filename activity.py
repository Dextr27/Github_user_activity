import requests
import click

def fetch_github_username(username) :
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    
    #successful request 
    if response.status_code == 200:
        return response.json()
    
    else:
        return None
    
@click.command()
@click.argument('username')

def main(username) :
    activities = fetch_github_username(username)
    if activities:
        for activity in activities[:5]:  # Display only the 5 most recent activities
            print(f"Type: {activity['type']}")
            print(f"Repo: {activity['repo']['name']}")
            print(f"Created at: {activity['created_at']}")
            print("---")
    else:
        print(f"Failed to fetch activities for user {username}")

if __name__ == "__main__":
    main()
    