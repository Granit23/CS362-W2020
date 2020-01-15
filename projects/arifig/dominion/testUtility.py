import Dominion
import random
from collections import defaultdict

def getBoxes(nV, numCards):
  box = {}
  box["Woodcutter"]=[Dominion.Woodcutter()]*numCards
  box["Smithy"]=[Dominion.Smithy()]*numCards
  box["Laboratory"]=[Dominion.Laboratory()]*numCards
  box["Village"]=[Dominion.Village()]*numCards
  box["Festival"]=[Dominion.Festival()]*numCards
  box["Market"]=[Dominion.Market()]*numCards
  box["Chancellor"]=[Dominion.Chancellor()]*numCards
  box["Workshop"]=[Dominion.Workshop()]*numCards
  box["Moneylender"]=[Dominion.Moneylender()]*numCards
  box["Chapel"]=[Dominion.Chapel()]*numCards
  box["Cellar"]=[Dominion.Cellar()]*numCards
  box["Remodel"]=[Dominion.Remodel()]*numCards
  box["Adventurer"]=[Dominion.Adventurer()]*numCards
  box["Feast"]=[Dominion.Feast()]*numCards
  box["Mine"]=[Dominion.Mine()]*numCards
  box["Library"]=[Dominion.Library()]*numCards
  box["Gardens"]=[Dominion.Gardens()]*nV
  box["Moat"]=[Dominion.Moat()]*numCards
  box["Council Room"]=[Dominion.Council_Room()]*numCards
  box["Witch"]=[Dominion.Witch()]*numCards
  box["Bureaucrat"]=[Dominion.Bureaucrat()]*numCards
  box["Militia"]=[Dominion.Militia()]*numCards
  box["Spy"]=[Dominion.Spy()]*numCards
  box["Thief"]=[Dominion.Thief()]*numCards
  box["Throne Room"]=[Dominion.Throne_Room()]*numCards
  return box


def getSupply(player_names, box, nV, nC, numSupply):
  #Pick 10 cards from box to be in the supply.
  boxlist = [k for k in box]
  random.shuffle(boxlist)
  random10 = boxlist[:numSupply]
  
  supply = defaultdict(list,[(k,box[k]) for k in random10])
  #The supply always has these cards
  supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
  supply["Silver"]=[Dominion.Silver()]*40
  supply["Gold"]=[Dominion.Gold()]*30
  supply["Estate"]=[Dominion.Estate()]*nV
  supply["Duchy"]=[Dominion.Duchy()]*nV
  supply["Province"]=[Dominion.Province()]*nV
  supply["Curse"]=[Dominion.Curse()]*nC
  return supply