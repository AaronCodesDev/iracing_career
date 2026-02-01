from core.rules import (RACE_REWARD_PER_POSITION, LEVEL_UP_THRESHOLD, POLE_POSITION_BONUS, INCIDENT_PENALTIES, INCIDENT_PENALTY_MULTIPLIER)

def run_race(driver, race, position, incidents=None, available_teams=None, pole_position=False):
    if incidents is None:
        incidents = []
    if available_teams is None:
        available_teams = []

    # 🔹 Bonus for pole position in qualifying
    if pole_position:
        driver.money += POLE_POSITION_BONUS
        print(f"🏎️ {driver.name} earned a pole position bonus +${POLE_POSITION_BONUS}")

    # 🔹 Subtract entry fee
    driver.money -= race.entry_fee

    # 🔹 Reward based on finishing position
    reward = max(race.max_reward - (position - 1) * RACE_REWARD_PER_POSITION, 0)
    driver.money += reward
    print(f"💰 {driver.name} earned ${reward} for finishing position {position}")

    # 🔹 Subtract penalties for incidents
    total_penalty = sum(INCIDENT_PENALTIES.get(i, 0) for i in incidents) * INCIDENT_PENALTY_MULTIPLIER
    driver.money -= total_penalty
    if total_penalty > 0:
        print(f"💥 {driver.name} penalized ${total_penalty} for incidents: {incidents}")

    # 🔹 Level up if money exceeds threshold
    if driver.money > LEVEL_UP_THRESHOLD:
        driver.level += 1
        print(f"⬆️ {driver.name} leveled up to {driver.level}")

    # 🔹 Try signing with a team
    for team in available_teams:
        if driver.level >= team.min_level and driver.team_id is None:
            driver.team_id = team.id
            driver.money += team.signing_bonus
            print(f"🎉 {driver.name} has been signed by {team.name} +${team.signing_bonus}")
            break

    return driver
