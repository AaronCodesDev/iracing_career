from core.rules import RACE_REWARD_PER_POSITION, INCIDENT_PENALTY_MULTIPLIER, LEVEL_UP_THRESHOLD, POLE_POSITION_BONUS

def run_race(driver, race, position, incidents, available_teams, pole_position=False):
    
    if pole_position:
        driver.money += POLE_POSITION_BONUS
        print(f"🏆 {driver.name} received a pole position bonus of +${POLE_POSITION_BONUS}")
    
    # Deduct entry fee
    driver.money -= race.entry_fee
    
    reward = max(race.max_reward - (position - 1) * RACE_REWARD_PER_POSITION, 0)
    driver.money += reward
    
    driver.money -= sum(incidents)  * INCIDENT_PENALTY_MULTIPLIER # Each incident has a cost equal to its severity
    
    if driver.money > LEVEL_UP_THRESHOLD:
        driver.level += 1
        
    for team in available_teams:
        if driver.level>=team.min_level and driver.team_id is None:
            driver.team.id = team.id
            driver.money += team.signing_bonus
            print(f"🎉 {driver.name} has been signed by {team.name} +${team.signing_bonus}")
            break
        
    return driver