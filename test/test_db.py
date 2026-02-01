from db.session import SessionLocal
from db.models.driver import Driver
from db.models.team import Team
from game.race import run_race

db = SessionLocal()

# Create Driver and Teams
driver = Driver(name="Aaron Planas")
team1 = Team(name="Team A", signing_bonus=300, min_level=2)
team2 = Team(name="Team B", signing_bonus=500, min_level=3)


# Add teams to the database
db.add_all([team1, team2])
db.commit()

# Refresh driver
db.refresh(driver)

teams = [team1, team2]


# Run a race for driver
driver = run_race(
    driver,
    race = type('Race', (), {'entry_fee': 100, 'max_reward':500})(),
    position = 2,
    incidents = [50],
    available_teams = teams
)

# Commit changes to the database
db.commit()

print(driver.name, driver.money, driver.team.name if driver.team else None)