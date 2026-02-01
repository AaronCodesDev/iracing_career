from db.session import SessionLocal
from db.models.driver import Driver
from db.models.team import Team
from game.race import run_race

db = SessionLocal()

driver = Driver(name="Aaron Planas")
team1 = Team(name="Team A", signing_bonus=300, min_level=2)
team2 = Team(name="Team B", signing_bonus=500, min_level=3)

db.add_all([team1, team2])
db.commit()
db.refresh(driver)

teams = [team1, team2]
race = type('Race', (), {'entry_fee': 100, 'max_reward': 500})()

driver = run_race(
    driver,
    race=race,
    position=2,
    incidents=["minor", "major"],
    available_teams=teams,
    pole_position=True
)

db.commit()
print(driver.name, driver.money, driver.level, driver.team.name if driver.team else None)
