import time , math
from termcolor import colored
from data import JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_FOOD_HORSE_COPPER_PER_DAY ,COST_TENT_GOLD_PER_WEEK ,COST_HORSE_SILVER_PER_DAY,AANTAL_OP_PAARD,AANTAL_IN_TENT,COST_INN_HUMAN_SILVER_PER_NIGHT ,COST_INN_HORSE_COPPER_PER_NIGHT 

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount: int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    silver_amount = copper2silver(amount)
    gold_amount = silver2gold(silver_amount)
    return gold_amount

def platinum2gold(amount: int) -> float:
    return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    total_gold = 0
    if 'copper' in personCash:
        total_gold += copper2gold(personCash['copper'])
    if 'silver' in personCash:
        total_gold += silver2gold(personCash['silver'])
    if 'gold' in personCash:
        total_gold += personCash['gold']
    if 'platinum' in personCash:
        total_gold += platinum2gold(personCash['platinum'])
    return round(total_gold,2)


##################### O05 #####################
def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    kosten_perdag_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    hele_reis_kosten = kosten_perdag_copper * JOURNEY_IN_DAYS
    totaal_in_goud = copper2gold(hele_reis_kosten)
    
    
    return round(totaal_in_goud,2)

##################### O06 #####################
def getFromListByKeyIs(list_: list, key: str, value: any) -> list:
    filtered_list = []
    for item in list_:
        if item.get(key) == value:
            filtered_list.append(item)
    return filtered_list

def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends: list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(adventuring_people)
    return share_with_friends


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends: list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(adventuring_people)
    return share_with_friends


##################### O07 #####################


def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / AANTAL_OP_PAARD)

def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / AANTAL_IN_TENT)

def getTotalRentalCost(horses: int, tents: int) -> float:
    horse_cost = (horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    tent_cost = (tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7))

    return silver2gold(horse_cost) + tent_cost


##################### O08 #####################
def getItemsAsText(items: list) -> str:
    item_texts = []
    for item in items:
        item_text = f"{item['amount']}{item['unit']} {item['name']}"
        item_texts.append(item_text)
    if len(item_texts) > 1:
        return ", ".join(item_texts[:-1]) + f" & {item_texts[-1]}"
    else:
        return item_texts[0] if item_texts else ""
def getItemsValueInGold(items: list) -> float:
    total_value = 0.0
    for item in items:
        item_value = item['price']['amount']*item['amount']
        if item['price']['type'] == 'copper':
            item_value = copper2gold(item_value)
        elif item['price']['type'] == 'silver':  
            item_value = silver2gold(item_value)
        elif item['price']['type'] == 'gold':  
            item_value = item_value
        elif item['price']['type'] == 'platinum':  
            item_value = platinum2gold(item_value)
        total_value += item_value
    return total_value



##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_gold = 0.0
    for person in people:
        total_gold += person['cash']['gold']
        total_gold += copper2gold(person['cash']['copper'])
        total_gold += silver2gold(person['cash']['silver'])
        total_gold += platinum2gold(person['cash']['platinum'])
    return round(total_gold,2)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    return list(filter(lambda investor: investor['profitReturn'] <= 10, investors))

    

def getAdventuringInvestors(investors:list) -> list:
    return getAdventuringPeople(getInterestingInvestors(investors))



def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_cost = 0.0
    for investor in investors:
        if investor['adventuring'] and investor['profitReturn'] <= 10:  
            total_cost += getTotalRentalCost(1,1) + getItemsValueInGold(gear) + getJourneyFoodCostsInGold(1,1)
    return total_cost

##################### O11 #####################
def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    nightly_cost = getJourneyInnCostsInGold(1 , people, horses) 
    if leftoverGold >0 and nightly_cost > 0:
        nights = int(leftoverGold // nightly_cost)
    else:
        nights = 0
    return nights

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    people_cost = people * COST_INN_HUMAN_SILVER_PER_NIGHT * nightsInInn
    horse_cost = horses * COST_INN_HORSE_COPPER_PER_NIGHT * nightsInInn
    
    total_cost = silver2gold(people_cost) + copper2gold(horse_cost) 
    
    return round(total_cost,2)
##################### O13 #####################
def getInvestorsCuts(profitGold: float, investors: list) -> list:
    investor_cuts = []
    for investor in getInterestingInvestors(investors):
        investor_cut = round(profitGold * (investor['profitReturn'] / 100), 2)
        investor_cuts.append(investor_cut)
    
    return investor_cuts


def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    total_investor_cut = sum(investorsCuts)
    
    if total_investor_cut > profitGold:
        return 0.0
    
    remaining_gold = profitGold - total_investor_cut
    
    adventurer_cut = round(remaining_gold / fellowship, 2)
    
    return adventurer_cut
##################### O14 #####################
def getEarnigs(profitGold, mainCharacter, friends, investors):
    people = [mainCharacter] + friends + investors
    earnings = []

    adventuringFriends = getAdventuringFriends(friends)
    interestinginvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(adventuringFriends) + 1 +len(adventuringInvestors))

    aantal_vrienden=len(adventuringFriends)
    winst_vrienden=aantal_vrienden*10
    for person in people:
        start_gold = getPersonCashInGold(person['cash'])
        end_gold = start_gold

        if person == mainCharacter:
            end_gold += goldCut + winst_vrienden
        elif person in adventuringFriends:
            end_gold += goldCut - 10
        elif person in investors:
            if person in adventuringInvestors:
                end_gold += goldCut
            if person in interestinginvestors:
                end_gold += investorsCuts.pop(0)

        earnings.append({
            'name': person['name'],
            'start': start_gold,
            'end': round(end_gold, 2)
        })

    return earnings



##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()